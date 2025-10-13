
# #Assignment: Python Modules (os, math)

# # Part 1: OS Module
import os

# Question 1: Create a new folder
os.mkdir("Practice_Folder 1")
print("Folder 'Practice_Folder' created.")

# Question 2: Check current working directory
print("Current directory:", os.getcwd())

# Question 3: Create multiple folders
for i in range(1, 4):
    os.mkdir(f"Folder{i}")
print("Folders Folder1, Folder2, Folder3 created.")


# Question 4: Rename a folder
os.rename("Practice_Folder", "My_New_Folder")
print("Folder renamed to 'My_New_Folder'.")

# Question 5: Remove a folder
os.rmdir("My_New_Folder")
print("Folder 'My_New_Folder' removed.")


# Part 2: Math Module
import math

# Question 6: Square roots
print("Square root of 16 is:", math.sqrt(16))
print("Square root of 81 is:", math.sqrt(81))

import math

number = 25
square_root = math.sqrt(number)
print(f"The square root of {number} is: {square_root}")

# Question 7: Area of a circle
radius = 10
area = math.pi * radius**2
print("Area of circle:", area)

# Question 8: Factorial
print("Factorial of 5 is:", math.factorial(5))


# Question 9: Ceil and Floor
print("Ceil of 5.8:", math.ceil(5.8))
print("Floor of 5.8:", math.floor(5.8))

# Question 10: Power
print("2 raised to power 5 is:", math.pow(2, 5))

# Example 11: Greatest Common Divisor (GCD)
print("GCD of 48 and 18 is:", math.gcd(48, 18))   

# Example 12: Absolute value
print("Absolute value of -15 is:", math.fabs(-15))

# Example 13: Trigonometric functions (Angles in Radians)
angle = math.pi / 2   # 90 degrees
print("Sine of 90 degrees is:", math.sin(angle))  

# Example 14: Logarithm (base e)
print("Natural log of 10 is:", math.log(10))   

# Example 15: Logarithm (custom base)
print("Log base 10 of 1000 is:", math.log10(1000))

# Example 16: Constants (pi and e)
print("Value of pi:", math.pi)
print("Value of e:", math.e)


# Example 17: Radians and Degrees Conversion
print("180 degrees in radians is:", math.radians(180))
print("π radians in degrees is:", math.degrees(math.pi))

# Example 18: Hypotenuse (Pythagoras theorem)
a = 3
b = 4
print("Hypotenuse is:", math.hypot(a, b))

# Example 19: Modf (separate fractional and integer part)
num = 5.75
fraction, integer = math.modf(num)
print("Fractional part:", fraction)
print("Integer part:", integer)

# Example 120: Copysign
print("Copy sign of -3 to 7:", math.copysign(7, -3))


 #Example 21: Product of sequence
numbers = [2, 3, 4]
print("Product of [2, 3, 4] is:", math.prod(numbers)) 