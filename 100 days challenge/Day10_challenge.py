# Day 10: List methods + slicing

nums = [3, 1, 4, 1, 5]

# ---- Methods (list ko badalte hain, in-place) ----
nums.append(9)
print("append:", nums)

nums.insert(0, 100)
print("insert:", nums)

nums.remove(1)             # pehli baar jo 1 mile
print("remove:", nums)

last = nums.pop()          # aakhri item nikal ke deta hai
print("pop:", last, "| list:", nums)

first = nums.pop(0)
print("pop(0):", first, "| list:", nums)

nums.extend([7, 8])
print("extend:", nums)

nums.sort()
print("sort:", nums)

nums.sort(reverse=True)
print("sort reverse:", nums)

nums.reverse()
print("reverse:", nums)

print("\ncount of 4:", nums.count(4))
print("index of 7:", nums.index(7))

# copy — bina .copy() ke dono ek hi list ko point karte hain
copy_list = nums.copy()
copy_list.append(999)
print("\noriginal:", nums)
print("copy    :", copy_list)

# ---- sorted() vs sort() ----
marks = [78, 92, 65]
new_list = sorted(marks)          # nayi list deta hai, original safe
print("\nsorted():", new_list, "| original:", marks)

marks.sort()                      # original hi badal jaata hai
print("sort():  ", marks)

# ================= SLICING =================
data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("\ndata          :", data)
print("[:3]          :", data[:3])       # pehle 3
print("[3:]          :", data[3:])       # index 3 se end
print("[2:6]         :", data[2:6])      # 2..5 (6 include nahi)
print("[-3:]         :", data[-3:])      # aakhri 3
print("[::2]         :", data[::2])      # har doosra
print("[::-1]        :", data[::-1])     # ulta
print("[8:2:-2]      :", data[8:2:-2])

# slice se nayi copy banti hai
part = data[2:5]
part[0] = 999
print("\nslice:", part, "| original:", data)

# slice assignment (length badal sakti hai)
letters = ["a", "b", "c", "d"]
letters[1:3] = ["B", "C", "D"]
print("slice assign:", letters)

# string par bhi same rules
word = "programming"
print("\nword[:7]:", word[:7], "| word[-4:]:", word[-4:], "| reverse:", word[::-1])
