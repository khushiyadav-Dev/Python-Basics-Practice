# Day 6: Booleans + comparison + if / elif / else

# ---- Comparison operators: result hamesha True/False ----
a, b = 10, 20
print("a == b :", a == b)     # barabar
print("a != b :", a != b)     # barabar nahi
print("a >  b :", a > b)
print("a <= b :", a <= b)
print("type:", type(a < b).__name__)

# Python chained comparison support karta hai
marks = 78
print("60 <= marks < 85 :", 60 <= marks < 85)

# ---- if / elif / else ----
def grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 75:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "Fail"

for m in [95, 78, 62, 45, 30]:
    print(f"marks {m:>3} -> grade {grade(m)}")

# ---- Ternary (ek line wala if-else) ----
status = "Pass" if marks >= 40 else "Fail"
print("\nStatus:", status)

# ---- Truthiness: khali cheez False ----
values = [0, 1, "", "hi", [], [1], None, True]
for v in values:
    print(f"{str(v):<6} -> {bool(v)}")

# ---- if ke saath 'in' aur string methods ----
email = "khushi@gmail.com"
if "@" in email and email.endswith(".com"):
    print("\nEmail theek lagta hai")
else:
    print("\nEmail galat hai")

# ---- Nested if (zaroorat par, warna elif better) ----
age, has_id = 20, False
if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID lao, phir entry")
else:
    print("18 se kam hai — entry nahi")

# ---- Ek chhota validation example ----
password = "khushi1234"
if len(password) < 8:
    print("Password chhota hai")
elif password.isdigit():
    print("Sirf numbers kaafi nahi")
else:
    print("Password theek hai (length + letters)")
