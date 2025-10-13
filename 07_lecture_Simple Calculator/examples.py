
# Assignment: Simple Calculator & Practice Programs


# Q1: Basic Calculator
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Choose an operation: +  -  *  /")
operation = input("Enter operation: ")

if operation == "+":
    result = num1 + num2
    print("The result is:", result)

elif operation == "-":
    result = num1 - num2
    print("The result is:", result)

elif operation == "*":
    result = num1 * num2
    print("The result is:", result)

elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print("The result is:", result)
    else:
        print("Error: Cannot divide by zero")
else:
    print("Invalid operation selected.")


# Q2: Square Calculator

num = float(input("\nEnter a number to find its square: "))
print("Square is:", num * num)


# Q3: Average of Two Numbers

a = float(input("\nEnter first number: "))
b = float(input("Enter second number: "))

average = (a + b) / 2
print("Average is:", average)


# Q4: Area of Rectangle

length = float(input("\nEnter length of rectangle: "))
width = float(input("Enter width of rectangle: "))

area = length * width
print("Area of rectangle is:", area)



# Q5: Mini Calculator with Power Operation

num1 = float(input("\nEnter first number: "))
num2 = float(input("Enter second number: "))

print("Choose an operation: +  -  *  /  ^")
operation = input("Enter operation: ")

if operation == "+":
    print("Result:", num1 + num2)
elif operation == "-":
    print("Result:", num1 - num2)
elif operation == "*":
    print("Result:", num1 * num2)
elif operation == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Cannot divide by zero")
elif operation == "^":
    print("Result:", num1 ** num2)
else:
    print("Invalid operation")