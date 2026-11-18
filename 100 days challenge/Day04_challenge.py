# Day 4: f-strings (formatting) + numbers ke operators

name = "khushiyadav-Dev"
marks = 87.5
price = 1234567.891
total_days = 100

# f-string: {} ke andar variable ya expression
print(f"{name} ne {total_days} din ka challenge liya.")
print(f"Agle saal: {21 + 1} saal")          # expression bhi chalta hai

# Decimal control
print(f"Marks: {marks:.2f}")
print(f"Price: {price:,.2f}")               # comma + 2 decimal
print(f"Percentage: {marks / 100:.1%}")

# Alignment — table banane ke liye
print(f"|{'Subject':<12}|{'Marks':>8}|")
print(f"|{'Python':<12}|{87:>8}|")
print(f"|{'Maths':<12}|{92:>8}|")

# ---- Numbers ke operators ----
a, b = 17, 5
print("\nJod:", a + b, "| Ghata:", a - b, "| Guna:", a * b)
print("Bhaag (/):", a / b)          # hamesha float
print("Floor (//):", a // b)        # poora hissa
print("Remainder (%):", a % b)      # shesh
print("Power (**):", a ** 2)

# Precedence (BODMAS)
print("2 + 3 * 4 =", 2 + 3 * 4)
print("(2 + 3) * 4 =", (2 + 3) * 4)

# Augmented assignment
score = 100
score += 25      # score = score + 25
score -= 5
score *= 2
print("Score:", score)

# Built-ins
nums = [10, 4, 27, 3]
print("min:", min(nums), "max:", max(nums), "sum:", sum(nums))
print("round(3.567, 2):", round(3.567, 2), "| abs(-9):", abs(-9))

# Float ki chhoti dikkat
print(0.1 + 0.2)                 # 0.30000000000000004
print(round(0.1 + 0.2, 2))       # 0.3
