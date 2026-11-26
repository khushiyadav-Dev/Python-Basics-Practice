# Day 12: dict methods, nested data, aur ab tak ka revision

# ---- Counting pattern (sabse zyada use hone wala) ----
text = "python is easy and python is powerful"
words = text.split()

counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
print("Word counts:", counts)

# ---- setdefault: group karna ----
by_length = {}
for w in words:
    by_length.setdefault(len(w), []).append(w)
print("By length:", by_length)

# ---- update / merge ----
student = {"name": "khushiyadav-Dev", "age": 21}
student.update({"age": 22, "city": "Jaipur"})
print("\nAfter update:", student)

a, b = {"x": 1}, {"y": 2}
print("Merge (|):", a | b)      # Python 3.9+

# ---- pop / popitem / clear ----
removed = student.pop("city")
print("pop('city'):", removed)
print("pop with default:", student.pop("salary", 0))
last = student.popitem()
print("popitem:", last, "| ab bacha:", student)

# ---- Dict comprehension (kal detail mein) ----
squares = {n: n * n for n in range(1, 6)}
print("\nSquares dict:", squares)

marks = {"Aarav": 88, "Diya": 34, "Kabir": 71, "Meera": 45}
passed = {name: m for name, m in marks.items() if m >= 40}
print("Passed:", passed)

# ---- Nested data: list of dicts (API ka format) ----
students = [
    {"name": "Aarav", "age": 20, "skills": ["Python", "SQL"], "marks": {"math": 88, "python": 92}},
    {"name": "Diya", "age": 22, "skills": ["Python", "Git"], "marks": {"math": 71, "python": 79}},
]

for s in students:
    avg = sum(s["marks"].values()) / len(s["marks"])
    print(f'{s["name"]:<6} age={s["age"]} avg={avg:.1f} skills={", ".join(s["skills"])}')

# nested access
print("\nAarav ka python score:", students[0]["marks"]["python"])
print("Diya ki pehli skill:", students[1]["skills"][0])

# nested modify
students[1]["skills"].append("Pandas")
print("Diya ki skills:", students[1]["skills"])

# ---- Dict ko sort karna ----
print("\nMarks se sort (desc):")
for name, m in sorted(marks.items(), key=lambda kv: -kv[1]):
    print(f"  {name:<6} {m}")

# ---- REVISION: days 1-11 ka ek chhota mix ----
print("\n--- Revision ---")
name = "khushiyadav-Dev"
age = 21
skills = ["Python", "Git", "AWS"]
scores = {"python": 88, "git": 75, "aws": 62}

# f-string + loop + dict + condition
for skill in skills:
    score = scores.get(skill.lower(), 0)
    level = "strong" if score >= 80 else "improving" if score >= 60 else "start"
    print(f"{skill:<7} {score:>3} -> {level}")

# function + tuple return + unpacking
def stats(numbers):
    return min(numbers), max(numbers), round(sum(numbers) / len(numbers), 1)

low, high, avg = stats(list(scores.values()))
print(f"\nmin={low} max={high} avg={avg}")

# set se unique + sorted
print("Unique first letters:", sorted({s[0] for s in skills}))

# slicing + join
print("Initials:", "".join(s[0] for s in name.split("-")))
