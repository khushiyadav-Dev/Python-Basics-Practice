friends = ["apple","orange",5,345.06,false,"aakash","rohan"]

print(friends)

friends.append("khushi") #append ek method h jo ki end of the list insertion karta h 

#append = at the end 

**Common List Methods:
append(x) → List ke end me element add karta hai
extend(iterable) → Multiple elements add karta hai (list merge jaisa)
insert(i, x) → Specific index par element add karta hai
remove(x) → First occurrence delete karta hai
pop([i]) → Index se element remove karke return karta hai
clear() → Puri list empty kar deta hai
index(x) → Element ka index batata hai
count(x) → Kitni baar element aaya hai count karta hai
sort() → List ko sort karta hai
reverse() → List ko reverse karta hai
copy() → List ki copy banata hai

lst = [1, 2, 3]

lst.append(4)        # [1, 2, 3, 4]
lst.insert(1, 10)    # [1, 10, 2, 3, 4]
lst.remove(2)        # [1, 10, 3, 4]
lst.sort()           # [1, 3, 4, 10]

#pop([i]) delete karke return kar deta h 
lst = [1, 2, 3]
x = lst.pop()
print(x)     # 3
print(lst)   # [1, 2]

#count() count karta h 
lst = [1, 2, 2, 3]
print(lst.count(2))    # 2

#clear()
lst = [1, 2, 3]
lst.clear()
print(lst)   # []

#index()
lst = [10, 20, 30]
print(lst.index(20))   # 1

#reverse()
lst = [1, 2, 3]
lst.reverse()
print(lst)   # [3, 2, 1]

#copy()
lst = [1, 2, 3]
new_lst = lst.copy()
print(new_lst)   # [1, 2, 3]
