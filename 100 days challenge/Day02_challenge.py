# Day 2: Variables aur data types
# Variable = naam wala dabba jisme value rakhte hain.

name = "khushiyadav-Dev"     # str   -> text
age = 21                     # int   -> poora number
height = 5.4                 # float -> decimal
is_learning = True           # bool  -> True / False
skills = ["Python", "Git"]   # list  -> kai values
nothing = None               # None  -> "koi value nahi"

print("Naam:", name, "| type:", type(name))
print("Age:", age, "| type:", type(age))
print("Height:", height, "| type:", type(height))
print("Learning:", is_learning, "| type:", type(is_learning))
print("Skills:", skills, "| type:", type(skills))
print("Nothing:", nothing, "| type:", type(nothing))

# Value baad mein badal sakti hai (type bhi badal sakta hai)
age = age + 1
print("Agle saal:", age)

# Ek line mein do variables
city, country = "Jaipur", "India"
print(city, country)

# Type badalna (casting) — abhi sirf ek jhalak
marks = "88"
print("String jodne par:", marks + "1")      # "881"
print("Number jodne par:", int(marks) + 1)   # 89
