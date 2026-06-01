#Question: modify this program to find the average of two numbers instead of the sum.

# Program to find the average of two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

average = (num1 + num2) / 2

print(f"\n--- Output ---")
print(f"First number: {num1}")
print(f"Second number: {num2}")
print(f"Average of two numbers: {average}")

"""
--- Example Output ---
Enter first number: 10
Enter second number: 20

--- Output ---
First number: 10.0
Second number: 20.0
Average of two numbers: 15.0
"""
