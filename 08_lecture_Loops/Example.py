##FOR LOOP IN PYTHON 

# Example 1: Print numbers 1 to 10
for i in range(1, 11):
    print(i)

# Example 2: Print even numbers 2 to 20
for i in range(2, 21, 2):
    print(i)

# Example 3: Print odd numbers 1 to 19
for i in range(1, 20, 2):
    print(i)

# Example 4: Print squares of numbers 1 to 10
for i in range(1, 11):
    print(i**2)

# Example 5: Print multiplication table of 5
for i in range(1, 11):
    print("5 x", i, "=", 5*i)

# Example 6: Print characters of a string
for ch in "HawkVision":
    print(ch)

# Example 7: Reverse counting 10 to 1
for i in range(10, 0, -1):
    print(i)

# Example 8: Sum of first 10 natural numbers
total = 0
for i in range(1, 11):
    total += i
print("Sum =", total)

# Example 9: Factorial of 5
fact = 1
for i in range(1, 6):
    fact *= i
print("Factorial of 5 =", fact)

# Example 10: Print list elements
fruits = ["apple", "banana", "cherry", "mango"]
for fruit in fruits:
    print(fruit)

##WHILE LOOP IN PYTHON 

# Example 1: Print numbers 1 to 10
i = 1
while i <= 10:
    print(i)
    i += 1

# Example 2: Print even numbers
i = 2
while i <= 20:
    print(i)
    i += 2

# Example 3: Reverse counting
i = 10
while i >= 1:
    print(i)
    i -= 1

# Example 4: Sum of numbers 1 to 10
i = 1
total = 0
while i <= 10:
    total += i
    i += 1
print("Sum =", total)

# Example 5: Factorial of 5
i = 1
fact = 1
while i <= 5:
    fact *= i
    i += 1
print("Factorial of 5 =", fact)

# Example 6: Print digits of a number
num = 9876
while num > 0:
    print(num % 10)
    num //= 10

# Example 7: Print squares up to 5
i = 1
while i <= 5:
    print(i**2)
    i += 1

# Example 8: Countdown timer
i = 5
while i > 0:
    print("Time left:", i)
    i -= 1

# Example 9: Ask user until correct password
password = ""
while password != "1234":
    password = input("Enter password: ")
print("Access Granted!")

# Example 10: Multiples of 3 up to 30
i = 3
while i <= 30:
    print(i)
    i += 3

##NESTED LOOP IN PYTHON 
# Example 1: Multiplication tables (1 to 3)
for i in range(1, 4):
    for j in range(1, 11):
        print(i, "x", j, "=", i*j)
    print("---")

# Example 2: Rectangle of stars
for i in range(4):
    for j in range(6):
        print("*", end=" ")
    print()

# Example 3: Right angled triangle
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

# Example 4: Inverted triangle
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

# Example 5: Matrix of numbers
for i in range(1, 4):
    for j in range(1, 4):
        print(j, end=" ")
    print()

# Example 6: Print pairs (i, j)
for i in range(1, 4):
    for j in range(1, 3):
        print(f"({i}, {j})")

# Example 7: Chessboard pattern
for i in range(8):
    for j in range(8):
        if (i+j) % 2 == 0:
            print("W", end=" ")
        else:
            print("B", end=" ")
    print()

# Example 8: Multiplication triangle
for i in range(1, 6):
    for j in range(1, i+1):
        print(i*j, end=" ")
    print()

# Example 9: Pyramid pattern
for i in range(1, 6):
    for j in range(5-i):
        print(" ", end=" ")
    for k in range(2*i-1):
        print("*", end=" ")
    print()

# Example 10: Nested loop with strings
words = ["Hawk", "Vision"]
for w in words:
    for ch in w:
        print(ch, end=" ")
    print()
