# -------------------------------
#  Lecture: Functions in Python
# -------------------------------

# 1) Simple Function
def say_hello():
    print("Hello! Welcome to Python.")

say_hello()
say_hello()


# 2) Function with Parameter
def greet(name):
    print(f"Hello {name}, nice to meet you!")

greet("Arooj")
greet("Amna")


# 3) Function with Multiple Parameters
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce("Aleena", 20)
introduce("Hamza", 25)


# 4) Function with Return Value
def square(num):
    return num * num

result = square(5)
print("Square of 5 is:", result)


# 5) Function Returning Multiple Values
def math_operations(a, b):
    return a+b, a-b, a*b, a/b

add, sub, mul, div = math_operations(20, 5)
print("Addition:", add)
print("Subtraction:", sub)
print("Multiplication:", mul)
print("Division:", div)


# 6) Default Parameter
def greet_user(name="Guest"):
    print(f"Hello {name}, welcome!")

greet_user()
greet_user("Sara")


# 7) Function with Loop
def print_numbers(n):
    for i in range(1, n+1):
        print(i)

print_numbers(5)


# 8) Function with Condition
def check_even_odd(num):
    if num % 2 == 0:
        print(num, "is Even")
    else:
        print(num, "is Odd")

check_even_odd(7)
check_even_odd(12)


# 9) Calculator Using Function
def calculator(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b != 0:
            return a / b
        else:
            return "Error: Division by Zero!"
    else:
        return "Invalid Operation"

print(calculator(10, 5, "+"))
print(calculator(10, 5, "/"))
print(calculator(10, 0, "/"))


# 10) Nested Function
def outer():
    print("This is the outer function.")

    def inner():
        print("This is the inner function.")

    inner()

outer()


# 11) Function with List
def print_list(items):
    for i in items:
        print(i)

fruits = ["Apple", "Banana", "Mango"]
print_list(fruits)


# 12) Factorial Function
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print("Factorial of 5:", factorial(5))


# 13) Function with Boolean Return
def is_adult(age):
    return age >= 18

print(is_adult(20))
print(is_adult(15))


# 14) Function with Keyword Arguments
def student_info(name, age, grade):
    print(f"Name: {name}, Age: {age}, Grade: {grade}")

student_info(age=18, grade="A", name="Hira")


# 15) Function with *args (Multiple Arguments)
def add_all(*numbers):
    return sum(numbers)

print(add_all(2, 4, 6))
print(add_all(10, 20, 30, 40))


# 16) Function with **kwargs (Dictionary Arguments)
def print_details(**details):
    for key, value in details.items():
        print(key, ":", value)

print_details(name="Sara", age=25, city="Lahore")


# 17) Function Calling Another Function
def add(a, b):
    return a + b

def double_sum(a, b):
    return add(a, b) * 2

print(double_sum(3, 5))


# 18) Recursive Function
def countdown(n):
    if n == 0:
        print("Time up!")
    else:
        print(n)
        countdown(n-1)

countdown(5)


# -------------------------------
#  Assignments for Practice
# -------------------------------

# 1) Function to calculate area of rectangle
def rectangle_area(length, width):
    return length * width

print("Area of Rectangle:", rectangle_area(10, 5))


# 2) Function to check Prime Number
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print("Is 7 Prime?", is_prime(7))
print("Is 12 Prime?", is_prime(12))


# 3) Function to reverse a string
def reverse_string(text):
    return text[::-1]

print(reverse_string("Python"))
print(reverse_string("Arooj"))


# 4) Function that returns max number in list
def find_max(numbers):
    return max(numbers)

print(find_max([10, 25, 3, 99, 45]))


# 5) Calculator program using functions
def calc(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b if b != 0 else "Error: Division by Zero!"
    else:
        return "Invalid Operator"

print(calc(15, 5, "+"))
print(calc(15, 5, "-"))
print(calc(15, 5, "*"))
print(calc(15, 0, "/"))
