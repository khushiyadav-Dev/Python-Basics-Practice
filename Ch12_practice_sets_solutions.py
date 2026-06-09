"""
CHAPTER 12 - PRACTICE SET SOLUTIONS
"""

# ============================================================================
# PROBLEM 1: Open three files and handle FileNotFoundError
# ============================================================================
print("=" * 70)
print("PROBLEM 1: Opening three files with error handling")
print("=" * 70)

def problem_1():
    """Open three files 1.txt, 2.txt and 3.txt with error handling"""
    files = ['1.txt', '2.txt', '3.txt']
    
    for file in files:
        try:
            with open(file, 'r') as f:
                print(f"✓ Successfully opened {file}")
                content = f.read()
                if content:
                    print(f"  Content: {content[:50]}...")  # Print first 50 chars
        except FileNotFoundError:
            print(f"✗ File '{file}' not found. Please ensure the file exists.")
        except Exception as e:
            print(f"✗ Error opening {file}: {e}")

# Uncomment to run problem 1
# problem_1()


# ============================================================================
# PROBLEM 2: Print 3rd, 5th, and 7th element using enumerate
# ============================================================================
print("\n" + "=" * 70)
print("PROBLEM 2: Print 3rd, 5th, and 7th element using enumerate")
print("=" * 70)

def problem_2():
    """Print 3rd, 5th, and 7th element from a list using enumerate"""
    my_list = list(range(1, 20))  # Example list [1, 2, 3, ..., 19]
    print(f"Original list: {my_list}")
    
    target_indices = [2, 4, 6]  # 0-indexed positions for 3rd, 5th, 7th
    
    print("\nUsing enumerate:")
    for index, value in enumerate(my_list):
        if index in target_indices:
            element_number = index + 1  # Convert to 1-indexed for display
            print(f"  {element_number}rd/th element (index {index}): {value}")

problem_2()


# ============================================================================
# PROBLEM 3: List comprehension for multiplication table
# ============================================================================
print("\n" + "=" * 70)
print("PROBLEM 3: Multiplication table using list comprehension")
print("=" * 70)

def problem_3():
    """Generate multiplication table using list comprehension"""
    try:
        number = int(input("Enter a number to generate multiplication table: "))
        
        # List comprehension to generate multiplication table
        multiplication_table = [number * i for i in range(1, 11)]
        
        print(f"\nMultiplication table of {number}:")
        for i, result in enumerate(multiplication_table, 1):
            print(f"  {number} × {i} = {result}")
        
        return multiplication_table
    
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
        return None

# Uncomment to run problem 3 (requires user input)
# table = problem_3()


# ============================================================================
# PROBLEM 4: Display a/b with ZeroDivisionError handling
# ============================================================================
print("\n" + "=" * 70)
print("PROBLEM 4: Division with ZeroDivisionError handling")
print("=" * 70)

def problem_4():
    """Display a/b where a and b are integers. Handle ZeroDivisionError"""
    try:
        a = int(input("Enter first integer (a): "))
        b = int(input("Enter second integer (b): "))
        
        try:
            result = a / b
            print(f"\n{a} / {b} = {result}")
        except ZeroDivisionError:
            print(f"\n{a} / 0 = Infinite")
    
    except ValueError:
        print("Invalid input! Please enter valid integers.")

# Uncomment to run problem 4 (requires user input)
# problem_4()


# ============================================================================
# PROBLEM 5: Store multiplication table in Tables.txt
# ============================================================================
print("\n" + "=" * 70)
print("PROBLEM 5: Store multiplication table in Tables.txt")
print("=" * 70)

def problem_5():
    """Generate multiplication table and store in Tables.txt"""
    try:
        number = int(input("Enter a number to generate multiplication table: "))
        
        # Generate multiplication table using list comprehension
        multiplication_table = [number * i for i in range(1, 11)]
        
        # Write to file
        with open('Tables.txt', 'w') as file:
            file.write(f"Multiplication Table of {number}\n")
            file.write("=" * 40 + "\n")
            for i, result in enumerate(multiplication_table, 1):
                file.write(f"{number} × {i} = {result}\n")
        
        print(f"\n✓ Multiplication table of {number} has been saved to Tables.txt")
        print("\nContent written to file:")
        print("-" * 40)
        with open('Tables.txt', 'r') as file:
            print(file.read())
    
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
    except IOError as e:
        print(f"Error writing to file: {e}")

# Uncomment to run problem 5 (requires user input)
# problem_5()


# ============================================================================
# COMPLETE SOLUTION WITH ALL PROBLEMS
# ============================================================================
print("\n" + "=" * 70)
print("COMPLETE DEMO - ALL PROBLEMS")
print("=" * 70)

print("\n--- Running Problem 2 (No user input needed) ---")
problem_2()

print("\n" + "-" * 70)
print("\nTo run interactive problems (3, 4, 5), uncomment them in the code")
print("and run the script again. They require user input.")
print("\nExample usage:")
print("  - Problem 3: Generates multiplication table from user input")
print("  - Problem 4: Divides two numbers with error handling")
print("  - Problem 5: Saves multiplication table to Tables.txt")
