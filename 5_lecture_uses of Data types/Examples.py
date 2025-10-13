
# Uses of Data Types — Practice Set


# 1) Use of Integer (whole numbers)
# Counting numbers, score, age, quantity


# Example 1: Age
age = 25
print(age + 5)

# Example 2: Scores
score = 90
bonus = 10
print(score + bonus)

# Example 3: Counting apples
total_apples = 12
eaten = 3
print(total_apples - eaten)

# Example 4: Items in boxes
items_per_box = 24
boxes = 7
print(items_per_box * boxes)

# Example 5: Page counting
pages_read = 30
pages_total = 120
print(pages_total - pages_read)

# Example 6: Convert string digits to int
num_str = "15"
num_int = int(num_str)
print(num_int + 5)


# Example 7: Loop counter sum (1..n)
n = 5
sum_up_to_n = n * (n + 1) // 2
print(sum_up_to_n)

# Example 8: Inventory left
stock = 100
sold = 37
print(stock - sold)

# -------------------------------
# 2) Use of String (text)
# Storing names, messages, address, printing text, taking input strings
# -------------------------------

# Example 1: Greeting (fixed)
name = "Sarah"
greeting = "Hello, " + name + "!"
print(greeting)

# Example 2: Full name
first_name = "Arooj"
last_name = "Fatima"
full_name = first_name + " " + last_name
print(full_name)

# Example 3: Address formatting
house = "H#12"
street = "Main Road"
city = "Lahore"
address = house + ", " + street + ", " + city
print(address)

# Example 4: Length of a message
message = "Welcome to Python class!"
print(len(message))

# Example 5: Case changes
text = "learn PYTHON"
print(text.lower())
print(text.upper())
print(text.title())

# Example 6: Strip spaces
raw = "   hello world   "
print(raw.strip())

# Example 7: Replace words
line = "I love java"
print(line.replace("java", "python"))

# Example 8: Split and join
csv = "apple,banana,orange"
parts = csv.split(",")
print(parts)
print(" | ".join(parts))

# Example 9: Indexing and slicing
g = "Hello"
print(g[0])
print(g[-1])
print(g[1:4])


# -------------------------------
# 3) Use of Float (decimal numbers)
# Temperature, weight, price, percentages
# -------------------------------

# Example 1: Prices
price = 19.99
tax_rate = 0.05
total_price = price + (price * tax_rate)
print(total_price)

# Example 2: Weights
weight = 5.5
extra = 1.25
print(weight + extra)

# Example 3: Percentage marks
obtained = 425.0
total = 500.0
percentage = (obtained / total) * 100
print(percentage)

# Example 4: Temperature conversion (F -> C)
temp_f = 98.6
temp_c = (temp_f - 32) * 5/9
print(temp_c)

# Example 5: Rounding to 2 decimals
value = 12.34567
print(round(value, 2))

# Example 6: Convert string to float
rate_str = "15.75"
rate = float(rate_str)
print(rate * 2)

# -------------------------------
# 4) Combined Example (mini shop)
# Quantity * Price per item with basic formatting
# -------------------------------

# Example 1: Basic bill
quantity = 3
price_per_item = 19.99
item_name = "notebook"
total_cost = quantity * price_per_item
print("You bought", quantity, item_name + "s", "for a total of", total_cost)

# Example 2: Add sales tax
tax_rate = 0.08
bill_with_tax = total_cost * (1 + tax_rate)
print("Bill with tax:", bill_with_tax)

# Example 3: Discount then tax
discount_rate = 0.10
after_discount = total_cost * (1 - discount_rate)
final_bill = after_discount * (1 + tax_rate)
print("Final bill after discount and tax:", final_bill)

# Example 4: Show 2 decimal places
print(f"Payable: Rs {final_bill:.2f}")

# Example 5: Update quantity
quantity += 2
new_total = quantity * price_per_item
print("New total after adding 2 more:", new_total)


#Simple Calculator Example (Add, Subtract, Multiply, Divide)
# Simple Calculator Example

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Basic operations
print("Addition:", num1 + num2)       
print("Subtraction:", num1 - num2)    
print("Multiplication:", num1 * num2) 
print("Division:", num1 / num2)       

#Extra Practice Examples
#1. Area of Rectangle Calculator
# Area of Rectangle = length × width
length = int(input("Enter length: "))
width = int(input("Enter width: "))
area = length * width
print("Area of Rectangle:", area)


#2. Student Marks Percentage Calculator
# Total Marks out of 500
marks_obtained = int(input("Enter marks obtained: "))
total_marks = 500
percentage = (marks_obtained / total_marks) * 100
print("Percentage:", percentage, "%")
