CHAPTER 13 – PRACTICE SET

# Question 1: Create two virtual environments, install few packages in the first one. How do you create a similar environment in the second one?
"""
Solution:
1. Create first virtual environment:
   python -m venv env1
   
2. Activate env1 and install packages:
   (On Windows) env1\Scripts\activate
   (On macOS/Linux) source env1/bin/activate
   pip install requests numpy pandas
   
3. Create requirements.txt from first environment:
   pip freeze > requirements.txt
   
4. Create second virtual environment:
   python -m venv env2
   
5. Activate env2 and install packages from requirements.txt:
   (On Windows) env2\Scripts\activate
   (On macOS/Linux) source env2/bin/activate
   pip install -r requirements.txt

This way, env2 will have the same packages as env1.
"""

print("="*60)
print("QUESTION 1: Virtual Environment Setup")
print("="*60)
print(__doc__)

# Question 2: Write a program to input name, marks and phone number of a student and format it using the format function
print("\n" + "="*60)
print("QUESTION 2: Student Information Formatting")
print("="*60)

name = input("Enter student name: ")
marks = input("Enter marks: ")
phone = input("Enter phone number: ")

# Using format() function
formatted_string = "The name of the student is {}, his marks are {} and phone number is {}".format(name, marks, phone)
print(formatted_string)

# Alternative using f-string (Python 3.6+)
print(f"(Alternative f-string format): The name of the student is {name}, his marks are {marks} and phone number is {phone}")

# Question 3: A list contains the multiplication table of 7. Convert it to vertical string
print("\n" + "="*60)
print("QUESTION 3: Multiplication Table as Vertical String")
print("="*60)

# Create multiplication table of 7
multiplication_table = [7*i for i in range(1, 11)]
print(f"Multiplication table of 7: {multiplication_table}")

# Convert to vertical string
vertical_string = "\n".join(map(str, multiplication_table))
print("\nVertical representation:")
print(vertical_string)

# Alternative method
vertical_string_alt = ""
for num in multiplication_table:
    vertical_string_alt += str(num) + "\n"
print("\nAlternative vertical representation:")
print(vertical_string_alt)
