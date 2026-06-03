#PROGRAM 1: Add two numbers 
# This program takes two numbers from the user and adds them together
print("Program 1: Add Two Numbers")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
sum_result = num1 + num2
print(f"The sum of {num1} and {num2} is: {sum_result}")
print()


# PROGRAM 2: Find remainder when divided by a number 
# This program finds the remainder when one number is divided by another
print("Program 2: Find Remainder")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter number to divide by: "))
remainder = num1 % num2
print(f"The remainder when {num1} is divided by {num2} is: {remainder}")
print()

# PROGRAM 3: Check type of variables from input() 
# This program shows that input() returns string type by default
print("Program 3: Check Type of Variables")
user_input = input("Enter something: ")
print(f"You entered: {user_input}")
print(f"Type of input is: {type(user_input)}")
# Convert to integer and check type
num = int(user_input)
print(f"After converting to integer, type is: {type(num)}")
print()

# PROGRAM 4: Use comparison operator 
# This program uses comparison operators to check if a is greater than b
print("Program 4: Comparison Operator")
a = 34
b = 80
# Check if a is greater than b
if a > b:
    print(f"{a} is greater than {b}")
else:
    print(f"{a} is NOT greater than {b}")
# Check if b is greater than a
if b > a:
    print(f"{b} is greater than {a}")
print()

# PROGRAM 5: Find average of two numbers 
# This program calculates the average of two numbers entered by the user
print("Program 5: Find Average")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
average = (num1 + num2) / 2
print(f"Average of {num1} and {num2} is: {average}")
print()

# ========== PROGRAM 6: Calculate square of a number ==========
# This program calculates the square (multiply number by itself) of a number entered by user
print("Program 6: Calculate Square")
num = float(input("Enter a number: "))
square = num * num
print(f"Square of {num} is: {square}")
