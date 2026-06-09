CHAPTER 8 – PRACTICE SET
1)Write a program using functions to find greatest of three numbers.
2)Write a python program using function to convert Celsius to Fahrenheit.
3)How do you prevent a python print() function to print a new line at the end?
4)Write a recursive function to calculate the sum of first n natural numbers.
5)Write a python function to print first n lines of the following pattern:

***
**
*
(for n = 3)
6)Write a python function which converts inches to cms.
7)Write a python function to remove a given word from a list and strip it at the same time.
8)Write a python function to print multiplication table of a given number.

q1
  def greatest_of_three(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

print(greatest_of_three(10, 25, 15))


q2
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print(celsius_to_fahrenheit(37))

q3)
print("Hello", end=" ")
print("World")
# आउटपुट: Hello World (एक ही लाइन में)

q4
def sum_recursive(n):
    if n == 0:
        return 0
    return n + sum_recursive(n - 1)

print(sum_recursive(5)) # 1+2+3+4+5 = 15


q5

def print_pattern(n):
    for i in range(n, 0, -1):
        print("*" * i)

print_pattern(3)

q6

def inches_to_cms(inches):
    return inches * 2.54

print(inches_to_cms(10))

q7
def remove_and_strip(word_list, word_to_remove):
    new_list = [word.strip() for word in word_list if word.strip() != word_to_remove]
    return new_list

list_data = ["apple", " banana ", "cherry"]
print(remove_and_strip(list_data, "banana"))

q8

def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} X {i} = {n * i}")

multiplication_table(5)




























  
