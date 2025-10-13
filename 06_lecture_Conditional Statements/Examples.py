
# Conditional Statements in Python
# Assignment with Solutions

# Used to make decisions in code
# It's like telling Python:
# "If this happens, do this, otherwise do something else"

# Three types of conditional statements:
# 1) if
# 2) if - else
# 3) if - elif - else


# 1) Only IF

age = 18
if age >= 18:
    print("You are an adult")


age = 20
if age >= 10:
    print("Age is greater than or equal to 10")
    
age = 10
if age == 18:
    print("Age is equal to 18")    


# 2) IF - ELSE

age = 15
if age >= 18:
    print("You are an adult")
else:
    print("You are not an adult")


# 3) IF - ELIF - ELSE

marks = 75
if marks >= 90:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Fail")



# EXTRA PRACTICE EXAMPLES


# Example 1: Check Even or Odd
number = 7
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# Example 2: Temperature Check
temperature = 30
if temperature > 35:
    print("It's very hot outside")
elif temperature > 20:
    print("Weather is pleasant")
else:
    print("It's cold outside")

# Example 3: Find Largest Number
a = 25
b = 40
c = 30
if a >= b and a >= c:
    print("A is the largest")
elif b >= a and b >= c:
    print("B is the largest")
else:
    print("C is the largest")

# Example 4: Voting Eligibility
age = 17
if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")

# Example 5: Login Check (username and password)
username = "admin"
password = "1234"
if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid credentials")

# Example 6: Positive, Negative or Zero
num = -5
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

# Example 7: Simple Calculator (without input)
a = 10
b = 5
operator = "*"
if operator == "+":
    print("Result:", a + b)
elif operator == "-":
    print("Result:", a - b)
elif operator == "*":
    print("Result:", a * b)
elif operator == "/":
    print("Result:", a / b)
else:
    print("Invalid operator")
    
    
#If it’s raining, take an umbrella.

#solution
is_raining = True

if is_raining:
    print("Take an umbrella")    
    
    
#If you’re hungry, eat food. Otherwise, drink water.

#solution
hungry = False

if hungry:
    print("Eat food")
else:
    print("Drink water")    
    
    
# Check age and decide:
# If age < 13 → “You are a child”
# If age is between 13 and 19 → “You are a teenager”
# Else → “You are an adult”

#solution
age = 15

if age < 13:
    print("You are a child")
elif age >= 13 and age <= 19:
    print("You are a teenager")
else:
    print("You are an adult")
    
    
# If the temperature is greater than 30 → “It’s hot”
# Else if it’s between 15 and 30 → “It’s warm”
# Else → “It’s cold”

#solution
temperature = 28

if temperature > 30:
    print("It's hot")
elif temperature >= 15:
    print("It's warm")
else:
    print("It's cold")
    
# If color is:
# “red” → print “You like passion!”
# “blue” → print “You like calmness!”
# “green” → print “You love nature!”
# Else → print “Nice choice!”

#solution
color = input("Enter your favorite color: ")

if color == "red":
    print("You like passion!")
elif color == "blue":
    print("You like calmness!")
elif color == "green":print("You love nature!")
else:
    print("Nice choice!")    