🔹 Loop kya hota hai?
Loop ka use same code ko baar-baar run karne ke liye hota hai
Jab tak condition true ho, loop chalta rehta hai

🔸 Types of Loops in Python
for loop
while loop

🔸 1. for Loop
Jab fixed number of times repeat karna ho
Mostly list, tuple, string ke saath use hota hai
Python
for i in range(5):
    print(i)
👉 Output: 0 1 2 3 4
Example (list):
Python
fruits = ["apple", "banana", "mango"]

for f in fruits:
    print(f)

🔸 2. while Loop
Jab tak condition true hai, tab tak loop chalega
Python
i = 1
while i <= 5:
    print(i)
    i += 1


🔸 Loop Control Statements

🔹 break
Loop ko turant stop karta hai
Python
for i in range(5):
    if i == 3:
        break
    print(i)

🔹 continue
Current iteration skip karta hai
Python
for i in range(5):
    if i == 2:
        continue
    print(i)

🔹 pass
Kuch nahi karta (placeholder)
Python
for i in range(5):
    pass


🔸 Nested Loop
Loop ke andar loop
Python
for i in range(2):
    for j in range(3):
        print(i, j)






