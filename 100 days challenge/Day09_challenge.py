# Day 9: break, continue, pass + lists basics

# ---- break: loop se turant bahar ----
print("break:")
for i in range(1, 10):
    if i == 4:
        break
    print(i, end=" ")
print()

# ---- continue: sirf current round skip ----
print("continue (even skip):")
for i in range(1, 8):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print()

# ---- pass: placeholder, kuch nahi karta ----
for i in range(3):
    if i == 1:
        pass          # baad mein yahan logic aayega
    else:
        print("pass demo i =", i)

# ---- for...else: break na ho to else chalta hai ----
numbers = [3, 8, -2, 9]
for num in numbers:
    if num < 0:
        print("Pehla negative:", num)
        break
else:
    print("Koi negative nahi mila")

# ================= LISTS =================
marks = [78, 92, 65, 88, 50]

print("\nPoori list:", marks)
print("Length:", len(marks))
print("Pehla:", marks[0], "| Aakhri:", marks[-1])

# List mutable hai — index se badal sakte hain
marks[4] = 55
print("Update ke baad:", marks)

# Mixed types bhi chalte hain
mixed = ["khushiyadav-Dev", 21, 5.4, True, None]
print("Mixed:", mixed)

# Nested list (matrix)
matrix = [[1, 2, 3], [4, 5, 6]]
print("\nMatrix:", matrix)
print("Row 2, Col 3:", matrix[1][2])

# Loop se access
print("\nLoop:")
for m in marks:
    print(m, end=" ")
print()

# List par built-ins
print("\nTotal:", sum(marks))
print("Average:", round(sum(marks) / len(marks), 2))
print("Highest:", max(marks), "| Lowest:", min(marks))

# Ek list banao loop se (accumulator pattern)
squares = []
for n in range(1, 6):
    squares.append(n * n)
print("\nSquares:", squares)

# membership check
print("92 list mein hai?", 92 in marks)
print("100 list mein hai?", 100 in marks)

# IndexError ka example (safe check ke saath)
index = 10
if -len(marks) <= index < len(marks):
    print("Index", index, "->", marks[index])
else:
    print(f"Index {index} list ke bahar hai (length {len(marks)})")
