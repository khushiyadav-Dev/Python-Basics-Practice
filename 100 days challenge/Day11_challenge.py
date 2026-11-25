# Day 11: tuples (fixed), sets (unique), dicts (key-value)

# ================= TUPLES =================
point = (3, 5)
print("Tuple:", point, "| x:", point[0], "| y:", point[1])

# ek element ka tuple — comma zaroori
print("(7,) type:", type((7,)).__name__, "| (7) type:", type((7)).__name__)

# unpacking
x, y = point
print("Unpacked:", x, y)

# function kai values return kare to tuple hi hota hai
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([4, 8, 1, 9])
print("min:", low, "max:", high)

# immutable — badalne ki koshish par error
try:
    point[0] = 10
except TypeError as e:
    print("Tuple error:", e)

# tuple dictionary ki key ban sakta hai (list nahi)
locations = {(28.61, 77.20): "Delhi", (19.07, 72.87): "Mumbai"}
print("Location:", locations[(28.61, 77.20)])

# ================= SETS =================
nums = {1, 2, 2, 3, 4, 4, 5}
print("\nSet (duplicates hate):", nums)
print("Khali set:", set(), "| type:", type(set()).__name__)

# list se duplicates hatao
marks = [78, 92, 78, 65, 92]
print("Unique marks:", set(marks), "| sorted:", sorted(set(marks)))

# add / discard
s = {"apple", "banana"}
s.add("mango")
s.discard("banana")       # discard safe hai, remove() error deta hai
print("Set:", s, "| 'mango' in s:", "mango" in s)

# set operations
a, b = {1, 2, 3, 4}, {3, 4, 5, 6}
print("\nunion (|)        :", a | b)
print("intersection (&) :", a & b)
print("difference (-)   :", a - b)
print("symmetric (^)    :", a ^ b)

# ================= DICTIONARIES =================
student = {
    "name": "khushiyadav-Dev",
    "age": 21,
    "course": "Python",
    "marks": [78, 92, 65],
}

print("\nDict:", student)
print("Naam:", student["name"])
print("Marks:", student["marks"])

# safe access — get() (na mile to None ya default)
print("City:", student.get("city"))
print("City:", student.get("city", "Jaipur"))

# add / update
student["city"] = "Jaipur"
student["age"] = 22
print("\nUpdate ke baad:", student)

# delete
removed = student.pop("course")
print("Removed:", removed)

# loop
print("\nItems:")
for key, value in student.items():
    print(f"  {key:<7} -> {value}")

print("\nKeys:", list(student.keys()))
print("Values:", list(student.values()))

# membership key par check hota hai (value par nahi)
print("\n'name' in student:", "name" in student)
print("'Khushi' in student:", "khushiyadav-Dev" in student)

# nested dict
config = {"aws": {"region": "ap-south-1", "bucket": "demo"}, "app
