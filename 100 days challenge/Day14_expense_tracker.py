# ---------- report table ----------
HEADER = f"{'ID':>3}  {'DATE':<10}  {'CATEGORY':<10}  {'NOTE':<22}  {'AMOUNT':>9}"

def format_table(expenses: list[Expense]) -> str:
    if not expenses:
        return "Koi expense nahi mila."

    lines = [HEADER, "-" * len(HEADER)]
    for e in sorted(expenses, key=lambda x: (x.date, x.id)):
        note = e.note if len(e.note) <= 22 else e.note[:19] + "..."
        lines.append(f"{e.id:>3}  {e.date:<10}  {e.category:<10}  {note:<22}  {e.amount:>9,.2f}")
    lines.append("-" * len(HEADER))
    lines.append(f"{'':>3}  {'':<10}  {'TOTAL':<10}  {'':<22}  {total(expenses):>9,.2f}")
    return "\n".join(lines)

# ---------- summary + budget ----------
def format_summary(expenses: list[Expense], budget: float | None = None) -> str:
    s = summary(expenses)
    if s["count"] == 0:
        return "Abhi koi expense nahi hai."

    lines = ["=" * 46, "EXPENSE SUMMARY", "=" * 46]
    lines.append(f"total   : Rs {s['total']:,.2f}")
    lines.append(f"biggest : Rs {s['biggest'].amount:,.2f} ({s['biggest'].category})")
    for cat, amt in s["categories"].items():
        pct = amt / s["total"] * 100
        lines.append(f"  {cat:<10} Rs {amt:>8,.2f}  {pct:>5.1f}%  {'#' * int(pct / 4)}")

    if budget is not None:
        left = round(budget - s["total"], 2)
        lines.append(f"left    : Rs {left:,.2f}")
        lines.append("STATUS  : budget cross ho gaya!" if left < 0 else "STATUS  : budget ke andar ho")
    return "\n".join(lines)

# ---------- CLI ----------
def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="expense-tracker", description="Chhota expense tracker")
    common = argparse.ArgumentParser(add_help=False)          # parent parser pattern
    common.add_argument("--data", default=str(DATA_FILE), help="JSON file ka path")
    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", parents=[common], help="naya expense add karo")
    p_add.add_argument("amount")
    p_add.add_argument("category")
    p_add.add_argument("--note", default="")
    p_add.add_argument("--date", default=None)

    p_list = sub.add_parser("list", parents=[common])
    p_list.add_argument("--category", default=None)
    p_list.add_argument("--month", default=None, help="YYYY-MM")

    p_sum = sub.add_parser("summary", parents=[common])
    p_sum.add_argument("--budget", type=float, default=None)
    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    path = Path(args.data)
    expenses = load_expenses(path)

    if args.command == "add":
        try:
            e = add_expense(expenses, args.amount, args.category, args.note, args.date)
        except ValueError as err:
            print(f"Error: {err}")
            return 1                    # exit code 1 = fail
        save_expenses(expenses, path)
        print(f"added #{e.id}  Rs {e.amount:,.2f}  {e.category}")
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
