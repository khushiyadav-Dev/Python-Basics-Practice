#problem1: write a program to print multiplication developer using for lopp

n = int(input("enter a number: "))

for i in range(1,11):
    print(f"{n} x {i} = {n * i}")
  
#problem2: write a program to great a all the persons names stored in a list  put in a list which starts with  s.

l = ["khushi","sachin","sonam","rahul"]

 for name in l:
   if(name.startswith("s")):
     print(f"hello{name}")

#problem3: problem no 1 ko while loop se kro 

n = int(input("enter a number: "))

i = 1
while(i<11):

    print(f"{n} x {i} = {n * i}")
  
    i+= 1

#problem4 : write a program to print the following star pattern.
 '''
 for n = 3
  *
 ***
*****
 '''

n = int(input("enter the number: "))
 for i in range(1,n+1):
   
print(" "*(n-1),end="")
print("*"* (2*i-1), end="")
print("\n")



#problem5: write a program to find wheather a given number is prime or not

n = int(input("enter a number: "))

for i in range(2, n):
  if(n%i) ==0:
    print("number is not prime")
    break 

else:
   print("number is prime")

#problem6: write a program to find the sum of first and natural numbers using while loop

n = int(input("enter the number: "))

i = 1
sum = 0

while(i<=n):
  sum += i
  i +=1

print(sum)

#problem7: write a program for factorial of a given number using for loop.

l #5! = 1×2×3×4×5

n = int(input("enter the number: "))

product = 1
for i in range(1,n+1):
  product = product * 1

print(f"the factorial of {n} is {product}")


#problem8: star pattern ko i times print karo 

i = int(input("enter the number of times to print pattern: "))
n = int(input("enter the number for pattern size: "))

for j in range(i):
    for k in range(1, n+1):
        print(" "*(n-k), end="")
        print("*"*(2*k-1))
    print()  # blank line between patterns
