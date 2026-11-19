# Day 5: input() — user se value lena, aur type conversion (casting)

# input() HAMESHA string deta hai, chahe user number likhe.
# Neeche wale 3 lines uncomment karke terminal mein try karo (GitHub par nahi chalenge):
# name = input("Apna naam likho: ")
# age = int(input("Umar likho: "))
# print(f"Namaste {name}, agle saal tum {age + 1} saal ki ho jaogi")

# ---- Demo: bina rukey chalne ke liye fixed values ----
def parse_age(raw):
    """input() se aayi string ko safely int banata hai."""
    raw = raw.strip()
    if not raw.isdigit():
        return None
    age = int(raw)
    return age if 0 < age < 120 else None

for raw in ["21", "  19 ", "abc", "-5", "150"]:
    result = parse_age(raw)
    print(f"{raw!r:<8} -> {result}")

# ---- Type conversion ke rules ----
print("\nint('42')      =", int("42"))          # str -> int
print("float('3.7')   =", float("3.7"))        # str -> float
print("str(21)        =", str(21) + " (string)")  # int -> str
print("int(9.99)      =", int(9.99))           # decimal part KAT jaata hai (round nahi)
print("round(9.99)    =", round(9.99))
print("int('7') + 1   =", int("7") + 1)
# print("7" + 1)   -> TypeError: str + int allowed nahi

# ---- bool() conversions: khali cheez = False ----
print("\nbool(0):", bool(0), "| bool(1):", bool(1))
print("bool(''):", bool(""), "| bool('hi'):", bool("hi"))
print("bool([]):", bool([]), "| bool([1]):", bool([1]))

# ---- String <-> list ----
data = "10 20 30"
nums = list(map(int, data.split()))
print("\nnums:", nums, "| sum:", sum(nums))
print("join:", "-".join(["a", "b", "c"]))

# ---- Safe calculator (input wala hissa upar comment mein hai) ----
def calculator(a_raw, b_raw, op):
    try:
        a, b = float(a_raw), float(b_raw)
    except ValueError:
        return "number galat hai"

    if op == "+":  return round(a + b, 2)
    if op == "-":  return round(a - b, 2)
    if op == "*":  return round(a * b, 2)
    if op == "/":  return round(a / b, 2) if b != 0 else "zero se bhaag nahi"
    return "operator galat hai"

print("\nCalculator:")
for args in [("12", "4", "+"), ("12", "4", "/"), ("12", "0", "/"), ("abc", "4", "+")]:
    print(f"  {args[0]} {args[2]} {args[1]} = {calculator(*args)}")
