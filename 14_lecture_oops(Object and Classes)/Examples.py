# Oops (Classes and Objects)
# 1. Basic Class Syntax
# ==============================
# class ClassName:
#     def __init__(self, attributes):
#         self.attribute = value
#     def method(self):
#         pass

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Arooj", 20)
print(student1.name)   
print(student1.age)    



# 2. Class with a Simple Method

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} is barking!")

dog1 = Dog("Tommy")
dog1.bark()    


# 3. Multiple Objects from Same Class

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

print(car1.brand, car1.model)
print(car2.brand, car2.model)  



# 4. Object Method with Parameters

class Calculator:
    def add(self, x, y):
        return x + y

calc = Calculator()
print(calc.add(5, 3)) 


# 5. Using f-string in Class

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}")

p1 = Person("Sara")
p1.greet()   



# 6. Boolean Attribute

class Light:
    def __init__(self, status):
        self.status = status

lamp = Light(True)
print(lamp.status)   



# 7. Class with Default Values

class Book:
    def __init__(self, title="Unknown", author="Unknown"):
        self.title = title
        self.author = author

book1 = Book()
book2 = Book("Python Basics", "John")

print(book1.title, book1.author)  
print(book2.title, book2.author)  


# 8. Method that Changes Attribute

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

account = BankAccount()
account.deposit(500)
print(account.balance) 


# 9. Object Containing Another Object

class Engine:
    def __init__(self, hp):
        self.hp = hp

class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine

engine1 = Engine(1500)
car1 = Car("Suzuki", engine1)
print(car1.brand, car1.engine.hp)   



# 10. Returning Values from Method

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rect = Rectangle(5, 3)
print(rect.area())  



# 11. Class with __str__ Method

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __str__(self):
        return f"{self.name} is in grade {self.grade}"

s = Student("Sara", 10)
print(s)  


# 12. Changing Object Attribute After Creation

class Phone:
    def __init__(self, brand):
        self.brand = brand

my_phone = Phone("Samsung")
print(my_phone.brand)    
my_phone.brand = "iPhone"
print(my_phone.brand)    



# 13. Counter Example

class Counter:
    def __init__(self):
        self.count = 0

    def increase(self):
        self.count += 1

c = Counter()
c.increase()
c.increase()
print(c.count)   



# 14. Using Input with Class

class Student:
    def __init__(self, name):
        self.name = name

name = input("Enter your name: ")
s1 = Student(name)
print(f"Student name is {s1.name}")



# 15. Class with Multiple Methods

class Laptop:
    def __init__(self, brand, ram):
        self.brand = brand
        self.ram = ram

    def upgrade_ram(self, new_ram):
        self.ram = new_ram

    def display(self):
        print(f"Laptop Brand: {self.brand}, RAM: {self.ram}GB")

lap = Laptop("Dell", 8)
lap.display()         
lap.upgrade_ram(16)
lap.display()          
