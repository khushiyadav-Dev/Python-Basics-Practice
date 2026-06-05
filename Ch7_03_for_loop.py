# ===== FOR LOOP IN PYTHON =====
# A for loop is used to iterate through a sequence (list, tuple, string, range)
# and execute a block of code for each item in the sequence

# ===== BASIC SYNTAX =====
# for variable in sequence:
#     code to execute

print("===== FOR LOOP EXAMPLES =====\n")

# ===== Example 1: For Loop with List =====
print("Example 1: For Loop with List")
fruits = ["apple", "banana", "cherry", "orange"]
for fruit in fruits:
    print(fruit)
print()

# ===== Example 2: For Loop with String =====
print("Example 2: For Loop with String")
word = "Python"
for letter in word:
    print(letter)
print()

# ===== Example 3: For Loop with Range =====
print("Example 3: For Loop with Range (0 to 4)")
for i in range(5):
    print(i)
print()

# ===== Example 4: Range with Start and End =====
print("Example 4: Range from 1 to 5")
for i in range(1, 6):
    print(i)
print()

# ===== Example 5: Range with Step =====
print("Example 5: Range with Step (0 to 10, step 2)")
for i in range(0, 10, 2):
    print(i)
print()

# ===== Example 6: Print Multiplication Table =====
print("Example 6: Multiplication Table of 5")
num = 5
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
print()

# ===== Example 7: Sum of Numbers =====
print("Example 7: Sum of Numbers in a List")
numbers = [10, 20, 30, 40, 50]
total = 0
for number in numbers:
    total += number
print(f"Total sum: {total}")
print()

# ===== Example 8: Count Items =====
print("Example 8: Count Items in a List")
items = ["pen", "pencil", "eraser", "sharpener"]
count = 0
for item in items:
    count += 1
print(f"Total items: {count}")
print()

# ===== Example 9: Find Maximum Number =====
print("Example 9: Find Maximum Number")
numbers = [45, 23, 78, 12, 99, 34]
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print(f"Maximum number: {max_num}")
print()

# ===== Example 10: Nested For Loop (Pattern) =====
print("Example 10: Nested For Loop (Star Pattern)")
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()
print()

# ===== Example 11: Loop with Index using enumerate() =====
print("Example 11: Loop with Index using enumerate()")
colors = ["red", "green", "blue", "yellow"]
for index, color in enumerate(colors):
    print(f"Index {index}: {color}")
print()

# ===== Example 12: Print Even Numbers =====
print("Example 12: Print Even Numbers from 1 to 20")
for i in range(1, 21):
    if i % 2 == 0:
        print(i)
print()

# ===== Example 13: For Loop with Dictionary =====
print("Example 13: For Loop with Dictionary")
student = {"name": "John", "age": 20, "grade": "A"}
for key, value in student.items():
    print(f"{key}: {value}")
print()

# ===== Example 14: For Loop with Break =====
print("Example 14: For Loop with Break (Exit loop early)")
for i in range(1, 10):
    if i == 5:
        break
    print(i)
print()

# ===== Example 15: For Loop with Continue =====
print("Example 15: For Loop with Continue (Skip iteration)")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
print()

# ===== KEY POINTS =====
# 1. For loop iterates through each item in a sequence
# 2. Sequence can be: list, tuple, string, range, dictionary
# 3. range(n) generates numbers from 0 to n-1
# 4. range(start, end) generates numbers from start to end-1
# 5. range(start, end, step) generates numbers with specific step
# 6. break statement exits the loop
# 7. continue statement skips the current iteration
# 8. enumerate() gives both index and value
# 9. Nested loops can create complex patterns
# 10. For loops are faster and easier than while loops for sequences
