"""Mini Project 1 — CLI Expense Tracker
Day 1: core logic (model, JSON persistence, validation, summary)
Day 2: report table + argparse CLI (add / list / summary)
"""

import argparse
import json
from dataclasses import dataclass, asdict
from datetime import date
from pathlib import Path

BASE = Path(__file__).parent
DATA_FILE = BASE / "expenses.json"

CATEGORIES = {"food", "travel", "shopping", "bills", "education", "other"}
MAX_NOTE_LEN = 60


# ------------------------- data model -------------------------
@dataclass
class Expense:
    id: int
    amount: float
    category: str
    note: str = ""
    date: str = ""

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict) -> "Expense":
        return cls(
            id=int(d["id"]),
            amount=float(d["amount"]),
            category=str(d["category"]),
            note=d.get("note", ""),
            date=d.get("date", ""),
        )


# ------------------------- persistence -------------------------
def load_expenses(path: Path = DATA_FILE) -> list[Expense]:
    if not path.exists():
        return []
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        print(f"Warning: {path.name} kharab hai, khali list se shuru")
        return []
    return [Expense.from_dict(item) for item in raw]


def save_expenses(expenses: list[Expense], path: Path = DATA_FILE) -> None:
    path.write_text(
        json.dumps([e.to_dict() for e in expenses], indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


def next_id(expenses: list[Expense]) -> int:
    return max((e.id for e in expenses), default=0) + 1


# ------------------------- validation + add -------------------------
def add_expense(expenses: list[Expense], amount, category: str,
                note: str = "", when: str | None = None) -> Expense:
    try:
        amount = round(float(amount), 2)
    except (TypeError, ValueError):
        raise ValueError(f"amount number hona chahiye, mila: {amount!r}")
    if amount <= 0:
        raise ValueError("amount 0 se bada hona chahiye")

    category = category.strip().lower()
    if category not in CATEGORIES:
        raise ValueError(f"category galat hai. Allowed: {sorted(CATEGORIES)}")

    if when is None:
        when = date.today().isoformat()
    else:
        try:
            when = date.fromisoformat(when).isoformat()
        except ValueError:
            raise ValueError(f"date YYYY-MM-DD format mein chahiye, mila: {when!r}")

    expense = Expense(
        id=next_id(expenses),
        amount=amount,
        category=category,
        note=note.strip()[:MAX_NOTE_LEN],
        date=when,
    )
    expenses.append(expense)
    return expense


# ------------------------- filters + summary -------------------------
def filter_by_category(expenses: list[Expense], category: str) -> list[Expense]:
    category = category.strip().lower()
    return [e for e in expenses if e.category == category]


def filter_by_month(expenses: list[Expense], month: str) -> list[Expense]:
    """month format: YYYY-MM"""
    return [e for e in expenses if e.date.startswith(month)]


def total(expenses: list[Expense]) -> float:
    return round(sum(e.amount for e in expenses), 2)


def by_category(expenses: list[Expense]) -> dict[str, float]:
    totals: dict[str, float] = {}
    for e in expenses:
        totals[e.category] = round(totals.get(e.category, 0) + e.amount, 2)
    return dict(sorted(totals.items(), key=lambda kv: -kv[1]))


def summary(expenses: list[Expense]) -> dict:
    if not expenses:
        return {"count": 0, "total": 0.0, "average": 0.0, "biggest": None, "categories": {}}
    biggest = max(expenses, key=lambda e: e.amount)
    grand = total(expenses)
    return {
        "count": len(expenses),
        "total": grand,
        "average": round(grand / len(expenses), 2),
        "biggest": biggest,
        "categories": by_category(expenses),
    }


# ------------------------- report table (day 2 ka main kaam) -------------------------
HEADER = f"{'ID':>3}  {'DATE':<10}  {'CATEGORY':<10}  {'NOTE':<22}  {'AMOUNT':>9}"


def format_table(expenses: list[Expense]) -> str:
    """List ko aligned table mein badalta hai. Khali ho to message deta hai."""
    if not expenses:
        return "Koi expense nahi mila."

    lines = [HEADER, "-" * len(HEADER)]
    for e in sorted(expenses, key=lambda x: (x.date, x.id)):
        note = e.note if len(e.note) <= 22 else e.note[:19] + "..."
        lines.append(f"{e.id:>3}  {e.date:<10}  {e.category:<10}  {note:<22}  {e.amount:>9,.2f}")
    lines.append("-" * len(HEADER))
    lines.append(f"{'':>3}  {'':<10}  {'TOTAL':<10}  {'':<22}  {total(expenses):>9,.2f}")
    return "\n".join(lines)


def format_summary(expenses: list[Expense], budget: float | None = None) -> str:
    s = summary(expenses)
    if s["count"] == 0:
        return "Abhi koi expense nahi hai."

    lines = ["=" * 46, "EXPENSE SUMMARY", "=" * 46]
    lines.append(f"entries : {s['count']}")
    lines.append(f"total   : Rs {s['total']:,.2f}")
    lines.append(f"average : Rs {s['average']:,.2f}")
    lines.append(f"biggest : Rs {s['biggest'].amount:,.2f} ({s['biggest'].category}, {s['biggest'].note})")
    lines.append("-" * 46)
    lines.append("by category:")
    for cat, amt in s["categories"].items():
        pct = amt / s["total"] * 100
        bar = "#" * int(pct / 4)
        lines.append(f"  {cat:<10} Rs {amt:>8,.2f}  {pct:>5.1f}%  {bar}")

    if budget is not None:
        left = round(budget - s["total"], 2)
        lines.append("-" * 46)
        lines.append(f"budget  : Rs {budget:,.2f}")
        lines.append(f"left    : Rs {left:,.2f}")
        if left < 0:
            lines.append("STATUS  : budget cross ho gaya!")
        elif left < budget * 0.1:
            lines.append("STATUS  : budget ke bilkul aakhir mein ho")
        else:
            lines.append("STATUS  : budget ke andar ho")
    lines.append("=" * 46)
    return "\n".join(lines)


# ------------------------- CLI -------------------------
def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="expense-tracker",
        description="Chhota expense tracker — add, list, summary",
    )
    # --data har subcommand ke saath chalta hai (parent parser pattern)
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--data", default=str(DATA_FILE), help="JSON file ka path")

    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", parents=[common], help="naya expense add karo")
    p_add.add_argument("amount", help="kitna kharch hua (number)")
    p_add.add_argument("category", help=f"in mein se ek: {', '.join(sorted(CATEGORIES))}")
    p_add.add_argument("--note", default="", help="chhoti note")
    p_add.add_argument("--date", default=None, help="YYYY-MM-DD (default: aaj)")

    p_list = sub.add_parser("list", parents=[common], help="expenses dikhao")
    p_list.add_argument("--category", default=None)
    p_list.add_argument("--month", default=None, help="YYYY-MM")

    p_sum = sub.add_parser("summary", parents=[common], help="summary + budget check")
    p_sum.add_argument("--budget", type=float, default=None)

    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    path = Path(args.data)
    expenses = load_expenses(path)

    if args.command == "add":
        try:
            e = add_expense(expenses, args.amount, args.category, args.note, args.date)
        except ValueError as err:
            print(f"Error: {err}")
            return 1
        save_expenses(expenses, path)
        print(f"added #{e.id}  Rs {e.amount:,.2f}  {e.category}  {e.note}  ({e.date})")
        return 0

    if args.command == "list":
        rows = expenses
        if args.category:
            rows = filter_by_category(rows, args.category)
        if args.month:
            rows = filter_by_month(rows, args.month)
        print(format_table(rows))
        return 0

    if args.command == "summary":
        print(format_summary(expenses, args.budget))
        return 0

    return 1


# ------------------------- demo run -------------------------
if __name__ == "__main__":
    demo_path = BASE / "expenses_demo.json"
    demo_path.unlink(missing_ok=True)          # har run par fresh demo
    demo = ["--data", str(demo_path)]

    print("$ expense-tracker add 250 food --note lunch --date 2026-11-24")
    main(["add", "250", "food", "--note", "lunch", "--date", "2026-11-24"] + demo)

    print("\n$ expense-tracker add 120 travel --note auto")
    main(["add", "120", "travel", "--note", "auto", "--date", "2026-11-25"] + demo)

    print("\n$ expense-tracker add 1499 shopping --note shoes")
    main(["add", "1499", "shopping", "--note", "running shoes", "--date", "2026-11-26"] + demo)

    print("\n$ expense-tracker add 700 bills --note electricity")
    main(["add", "700", "bills", "--note", "electricity", "--date", "2026-11-26"] + demo)

    print("\n$ expense-tracker add -50 food   (galat amount)")
    main(["add", "-50", "food"] + demo)

    print("\n$ expense-tracker list")
    main(["list"] + demo)

    print("\n$ expense-tracker list --category food")
    main(["list", "--category", "food"] + demo)

    print("\n$ expense-tracker summary --budget 2000")
    main(["summary", "--budget", "2000"] + demo)

    print("\nReal usage (apne terminal mein):")
    print("  python day14/main.py add 250 food --note lunch")
    print("  python day14/main.py list --month 2026-11")
    print("  python day14/main.py summary --budget 5000")
    print("  python day14/main.py -h")

    demo_path.unlink(missing_ok=True)
