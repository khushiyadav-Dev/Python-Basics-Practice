# Day 3: Strings — text ke saath kaam
first = "khushiyadav"
last = "Dev"

full = first + " " + last        # + se jodna (concatenation)
print("Full:", full)
print("Repeat:", "-" * 25)
print("Length:", len(full))

# Indexing (0 se shuru, -1 aakhri)
print("Pehla:", full[0], "| Aakhri:", full[-1])
print("Index 5:", full[5])

# Slicing — [start:stop:step], stop include NAHI hota
print("Pehle 5:", full[:5])
print("Aakhri 3:", full[-3:])
print("Ulta:", full[::-1])
print("Har doosra:", full[::2])

# String immutable hai — change nahi kar sakte
# full[0] = "K"        # yeh TypeError dega

# Methods — nayi string return karte hain, original nahi badalta
messy = "  Python Seekhna Aasan Hai  "
print("strip:", repr(messy.strip()))
print("lower:", messy.strip().lower())
print("title:", messy.strip().title())
print("replace:", messy.strip().replace("Aasan", "Mazedaar"))

words = "main python seekh rahi hoon"
print("split:", words.split())
print("join:", "-".join(words.split()))

print("find 'python':", words.find("python"))
print("count 'a':", words.count("a"))
print("startswith 'main':", words.startswith("main"))
print("'python' in words:", "python" in words)

# Validation methods
print("isdigit:", "12345".isdigit(), "| isalpha:", "Python".isalpha())
print("isalnum:", "abc123".isalnum(), "| isspace:", "   ".isspace())
