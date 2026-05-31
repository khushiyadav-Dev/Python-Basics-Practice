# Question: Take diameter as input to calculate area of circle

# User se diameter input lena (float use kiya hai taaki point wali values bhi kaam karein)
diameter = float(input("Enter the diameter of the circle: "))

# Diameter se radius nikalna (Radius = Diameter / 2)
radius = diameter / 2

# Area calculate karna (Formula: π * r * r) -> π ki value 3.14159 hoti hai
area = 3.14159 * (radius ** 2)

# Result print karna
print("The area of the circle is:", area)
