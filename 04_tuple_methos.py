Tuple ke sirf 2 methods hote hain:
count()  #kitni baar value aayi
index () #value kaha pe hai


#count()
t = (1, 2, 3, 2, 2, 4)
print(t.count(2))   # Output: 3

#index()
t = (10, 20, 30, 20)
print(t.index(20))   # Output: 1

a= (1,45,342,3424,False,"aRohan","shivam")
print(a)

no = a.count(45)
print(no)

t = tuple([1, 2, 3])   # list ko tuple me convert kiya
print(t)

# length
t = (10, 20, 30, 40, 50)

print(len(t))   # Output: 5
