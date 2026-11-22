# Day 7: and / or / not + nested conditions

# ---- Truth table ----
print("a     b     a and b   a or b")
for a in (True, False):
    for b in (True, False):
        print(f"{str(a):<6}{str(b):<6}{str(a and b):<10}{a or b}")

print("\nnot True :", not True, "| not False :", not False)

# ---- Real conditions ----
age, has_license, is_drunk = 22, True, False

if age >= 18 and has_license and not is_drunk:
    print("\nDrive kar sakte ho")
else:
    print("\nDrive mat karo")

# or — koi ek sach ho jaye
day = "Sunday"
if day == "Saturday" or day == "Sunday":
    print("Weekend hai, extra practice karo")
# same cheez, chhoti:
if day in ("Saturday", "Sunday"):
    print("(in operator se bhi same kaam hota hai)")

# ---- Short-circuit: and pehli False par ruk jaata hai ----
def check(x):
    print(f"  check chala: {x}")
    return x > 0

print("\nand test:")
print("  result:", check(-1) and check(5))   # doosra check nahi chalega

print("\nor test:")
print("  result:", check(5) or check(-1))     # doosra check nahi chalega

# ---- or ka default value pattern ----
name = ""
display = name or "Guest"
print("\nWelcome,", display)

# ---- and ka guard pattern (error se bachne ke liye) ----
user = {"name": "khushiyadav-Dev", "email": ""}
if user.get("email") and "@" in user["email"]:
    print("Email valid:", user["email"])
else:
    print("Email nahi hai ya galat hai — crash nahi hua")

# ---- Nested condition wala real example ----
students = [
    {"name": "Aarav", "marks": 92, "attendance": 88},
    {"name": "Diya", "marks": 67, "attendance": 55},
    {"name": "Kabir", "marks": 38, "attendance": 90},
]

print()
for s in students:
    if s["marks"] >= 40:
        if s["attendance"] >= 60:
            remark = "Pass"
        else:
            remark = "Pass, par attendance sudharo"
    else:
        if s["attendance"] < 60:
            remark = "Fail — marks aur attendance dono kam"
        else:
            remark = "Fail — marks kam"
    print(f'{s["name"]:<6} marks={s["marks"]:>3} att={s["attendance"]:>3} -> {remark}')

# ---- Ek hi line mein multiple conditions (login check) ----
username, password = "khushi", "python1234"
if username and len(password) >= 8 and not password.isdigit():
    print("\nLogin form valid")
else:
    print("\nUsername ya password theek nahi")
