"""
╔═══════════════════════════════════════════════════════════╗
║     PYTHON SET METHODS - COMPLETE GUIDE                   ║
║     All important set operations with examples             ║
╚═══════════════════════════════════════════════════════════╝
"""

# ═══════════════════════════════════════════════════════════
# 1. UNION ( .union() or | )
# ═══════════════════════════════════════════════════════════
print("=" * 60)
print("1. UNION - Combines all unique elements from both sets")
print("=" * 60)

s1 = {1, 45, 6}
s2 = {7, 8, 1, 78}

print(f"Set 1: {s1}")
print(f"Set 2: {s2}")
print(f"Union using .union(): {s1.union(s2)}")  # Output: {1, 6, 7, 8, 45, 78}
print(f"Union using | operator: {s1 | s2}")      # Output: {1, 6, 7, 8, 45, 78}

A = {1, 2, 3}
B = {3, 4, 5}
result = A.union(B)
print(f"\nExample: A.union(B) where A={A}, B={B}")
print(f"Result: {result}")  # Output: {1, 2, 3, 4, 5}

# ═══════════════════════════════════════════════════════════
# 2. INTERSECTION ( .intersection() or & )
# ═══════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("2. INTERSECTION - Only common elements from both sets")
print("=" * 60)

A = {1, 2, 3}
B = {2, 3, 4}

print(f"Set A: {A}")
print(f"Set B: {B}")
result = A.intersection(B)
print(f"Intersection using .intersection(): {result}")  # Output: {2, 3}
print(f"Intersection using & operator: {A & B}")        # Output: {2, 3}

# Shortcut operator
result = A & B
print(f"\nUsing & operator: {result}")

# ═══════════════════════════════════════════════════════════
# 3. DIFFERENCE ( .difference() or - )
# ═══════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("3. DIFFERENCE - Elements in first set but NOT in second")
print("=" * 60)

A = {1, 2, 3, 4}
B = {3, 4, 5}

print(f"Set A: {A}")
print(f"Set B: {B}")
result = A.difference(B)
print(f"Difference using .difference(): {result}")  # Output: {1, 2}
print(f"Difference using - operator: {A - B}")      # Output: {1, 2}

# ═══════════════════════════════════════════════════════════
# 4. SYMMETRIC DIFFERENCE ( .symmetric_difference() or ^ )
# ═══════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("4. SYMMETRIC DIFFERENCE - Elements in either but NOT both")
print("=" * 60)

A = {1, 2, 3}
B = {2, 3, 4}

print(f"Set A: {A}")
print(f"Set B: {B}")
result = A.symmetric_difference(B)
print(f"Symmetric Difference using .symmetric_difference(): {result}")  # Output: {1, 4}
print(f"Symmetric Difference using ^ operator: {A ^ B}")                # Output: {1, 4}

# ═══════════════════════════════════════════════════════════
# 5. ADD ( .add() )
# ═══════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("5. ADD - Adds a single element to the set")
print("=" * 60)

my_set = {1, 2, 3}
print(f"Original set: {my_set}")
my_set.add(4)
print(f"After adding 4: {my_set}")  # Output: {1, 2, 3, 4}

my_set.add(2)  # Won't add duplicate
print(f"After adding 2 again: {my_set}")  # Output: {1, 2, 3, 4}

# ═══════════════════════════════════════════════════════════
# 6. REMOVE ( .remove() )
# ═══════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("6. REMOVE - Removes element (raises error if not found)")
print("=" * 60)

my_set = {1, 2, 3, 4}
print(f"Original set: {my_set}")
my_set.remove(2)
print(f"After removing 2: {my_set}")  # Output: {1, 3, 4}

# Uncomment to see error:
# my_set.remove(5)  # ❌ KeyError: 5

# ═══════════════════════════════════════════════════════════
# 7. DISCARD ( .discard() )
# ═══════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("7. DISCARD - Removes element (NO error if not found)")
print("=" * 60)

my_set = {1, 2, 3, 4}
print(f"Original set: {my_set}")
my_set.discard(2)
print(f"After discarding 2: {my_set}")  # Output: {1, 3, 4}

my_set.discard(5)  # ✅ No error!
print(f"After discarding 5 (not in set): {my_set}")  # Output: {1, 3, 4}

# ═══════════════════════════════════════════════════════════
# 8. POP ( .pop() )
# ═══════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("8. POP - Removes and returns an arbitrary element")
print("=" * 60)

my_set = {1, 2, 3, 4}
print(f"Original set: {my_set}")
removed_element = my_set.pop()
print(f"Removed element: {removed_element}")
print(f"Set after pop: {my_set}")

# ═══════════════════════════════════════════════════════════
# 9. CLEAR ( .clear() )
# ═══════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("9. CLEAR - Removes ALL elements from the set")
print("=" * 60)

my_set = {1, 2, 3, 4}
print(f"Original set: {my_set}")
my_set.clear()
print(f"After clear(): {my_set}")  # Output: set()

# ═══════════════════════════════════════════════════════════
# 10. COPY ( .copy() )
# ═══════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("10. COPY - Creates a shallow copy of the set")
print("=" * 60)

my_set = {1, 2, 3}
my_set_copy = my_set.copy()
print(f"Original set: {my_set}")
print(f"Copied set: {my_set_copy}")

my_set_copy.add(4)
print(f"\nAfter adding 4 to copy:")
print(f"Original set: {my_set}")      # Output: {1, 2, 3}
print(f"Copied set: {my_set_copy}")   # Output: {1, 2, 3, 4}

# ═══════════════════════════════════════════════════════════
# 11. ISSUBSET ( .issubset() )
# ═══════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("11. ISSUBSET - Checks if all elements are in another set")
print("=" * 60)

A = {1, 2}
B = {1, 2, 3, 4}

print(f"Set A: {A}")
print(f"Set B: {B}")
result = A.issubset(B)
print(f"Is A a subset of B? {result}")  # Output: True

C = {1, 5}
result = C.issubset(B)
print(f"\nSet C: {C}")
print(f"Is C a subset of B? {result}")  # Output: False

# ═══════════════════════════════════════════════════════════
# 12. ISSUPERSET ( .issuperset() )
# ═══════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("12. ISSUPERSET - Checks if set contains all elements of another")
print("=" * 60)

A = {1, 2, 3, 4}
B = {1, 2}

print(f"Set A: {A}")
print(f"Set B: {B}")
result = A.issuperset(B)
print(f"Is A a superset of B? {result}")  # Output: True

C = {1, 5}
result = A.issuperset(C)
print(f"\nSet C: {C}")
print(f"Is A a superset of C? {result}")  # Output: False

# ═══════════════════════════════════════════════════════════
# 13. ISDISJOINT ( .isdisjoint() )
# ═══════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("13. ISDISJOINT - Checks if sets have NO common elements")
print("=" * 60)

A = {1, 2, 3}
B = {4, 5, 6}

print(f"Set A: {A}")
print(f"Set B: {B}")
result = A.isdisjoint(B)
print(f"Are A and B disjoint? {result}")  # Output: True (no common)

C = {3, 4, 5}
result = A.isdisjoint(C)
print(f"\nSet C: {C}")
print(f"Are A and C disjoint? {result}")  # Output: False (3 is common)

# ═══════════════════════════════════════════════════════════
# 14. UPDATE ( .update() )
# ═══════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("14. UPDATE - Adds multiple elements to the set")
print("=" * 60)

my_set = {1, 2}
print(f"Original set: {my_set}")
my_set.update([3, 4, 5])
print(f"After update([3, 4, 5]): {my_set}")  # Output: {1, 2, 3, 4, 5}

my_set.update({6, 7})
print(f"After update({{6, 7}}): {my_set}")     # Output: {1, 2, 3, 4, 5, 6, 7}

# ═══════════════════════════════════════════════════════════
# 15. INTERSECTION UPDATE ( .intersection_update() )
# ═══════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("15. INTERSECTION UPDATE - Keeps only common elements")
print("=" * 60)

A = {1, 2, 3, 4}
B = {2, 3, 5}

print(f"Set A: {A}")
print(f"Set B: {B}")
A.intersection_update(B)
print(f"After A.intersection_update(B): {A}")  # Output: {2, 3}

# ═══════════════════════════════════════════════════════════
# 16. DIFFERENCE UPDATE ( .difference_update() )
# ═══════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("16. DIFFERENCE UPDATE - Removes elements present in another")
print("=" * 60)

A = {1, 2, 3, 4}
B = {2, 3}

print(f"Set A: {A}")
print(f"Set B: {B}")
A.difference_update(B)
print(f"After A.difference_update(B): {A}")  # Output: {1, 4}

# ═══════════════════════════════════════════════════════════
# 17. SYMMETRIC DIFFERENCE UPDATE ( .symmetric_difference_update() )
# ═══════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("17. SYMMETRIC DIFFERENCE UPDATE - Keep elements in either but not both")
print("=" * 60)

A = {1, 2, 3}
B = {2, 3, 4}

print(f"Set A: {A}")
print(f"Set B: {B}")
A.symmetric_difference_update(B)
print(f"After A.symmetric_difference_update(B): {A}")  # Output: {1, 4}

# ════════════════════════════════════════════════════════���══
# QUICK REFERENCE TABLE
# ═══════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("QUICK REFERENCE TABLE")
print("=" * 60)

reference = """
╔════════════════════╦════════════╦═══════════════════════════════════════╗
║    Method          ║  Operator  ║       Purpose                         ║
╠════════════════════╬════════════╬═══════════════════════════════════════╣
║ union()            ║     |      ║ All elements from both sets           ║
║ intersection()     ║     &      ║ Common elements only                  ║
║ difference()       ║     -      ║ Elements in first but not second      ║
║ symmetric_diff()   ║     ^      ║ Elements in either but not both       ║
║ add()              ║     —      ║ Add single element                    ║
║ remove()           ║     —      ║ Remove element (error if not found)   ║
║ discard()          ║     —      ║ Remove element (no error)             ║
║ pop()              ║     —      ║ Remove & return random element        ║
║ clear()            ║     —      ║ Remove all elements                   ║
║ copy()             ║     —      ║ Create shallow copy                   ║
║ issubset()         ║     —      ║ Check if subset                       ║
║ issuperset()       ║     —      ║ Check if superset                     ║
║ isdisjoint()       ║     —      ║ Check if no common elements           ║
║ update()           ║     —      ║ Add multiple elements                 ║
║ intersection_upd() ║     —      ║ Keep only common elements             ║
║ difference_upd()   ║     —      ║ Remove elements from another set      ║
║ sym_diff_upd()     ║     —      ║ Keep elements in either but not both  ║
╚════════════════════╩════════════╩═══════════════════════════════════════╝
"""

print(reference)

print("\n" + "=" * 60)
print("✅ All Set Methods Covered!")
print("=" * 60)
