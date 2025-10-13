# ==============================
# Encapsulation Simple Examples
# ==============================

# 1. Simple private variable + getter
class Student:
    def __init__(self, name):
        self.__name = name   # private

    def get_name(self):
        return self.__name

s1 = Student("Arooj")
print(s1.get_name())


# 2. Private variable + setter
class Employee:
    def __init__(self):
        self.__salary = 0

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

e1 = Employee()
e1.set_salary(50000)
print(e1.get_salary())


# 3. Bank balance with deposit only
class Bank:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

b1 = Bank()
b1.deposit(1000)
print(b1.get_balance())


# 4. Library book title
class Book:
    def __init__(self, title):
        self.__title = title

    def get_title(self):
        return self.__title

book = Book("Python Basics")
print(book.get_title())


# 5. Car model
class Car:
    def __init__(self, model):
        self.__model = model

    def show_model(self):
        return self.__model

c = Car("Toyota Corolla")
print(c.show_model())


# 6. School name
class School:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

s = School("Hawk Vision")
print(s.get_name())


# 7. Encapsulation with age
class Person:
    def __init__(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

p = Person(20)
print(p.get_age())


# 8. Laptop brand
class Laptop:
    def __init__(self, brand):
        self.__brand = brand

    def get_brand(self):
        return self.__brand

l = Laptop("Dell")
print(l.get_brand())


# 9. Simple subject class
class Subject:
    def __init__(self, name):
        self.__name = name

    def get_subject(self):
        return self.__name

sub = Subject("Mathematics")
print(sub.get_subject())


# 10. Teacher name
class Teacher:
    def __init__(self, name):
        self.__name = name

    def get_teacher(self):
        return self.__name

t = Teacher("Khalid Bashir")
print(t.get_teacher())


# 11. Mobile price
class Mobile:
    def __init__(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

m = Mobile(30000)
print(m.get_price())


# 12. Marks with setter
class Marks:
    def __init__(self):
        self.__marks = 0

    def set_marks(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

mk = Marks()
mk.set_marks(90)
print(mk.get_marks())


# 13. Employee ID
class Worker:
    def __init__(self, eid):
        self.__eid = eid

    def get_eid(self):
        return self.__eid

w = Worker(12345)
print(w.get_eid())


# 14. ATM Pin
class ATM:
    def __init__(self, pin):
        self.__pin = pin

    def check_pin(self, pin):
        return self.__pin == pin

atm = ATM(1234)
print(atm.check_pin(1234))


# 15. Advanced Example (Rectangle area)
class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def set_width(self, w):
        if w > 0:
            self.__width = w

    def set_height(self, h):
        if h > 0:
            self.__height = h

    def area(self):
        return self.__width * self.__height

r = Rectangle(10, 5)
r.set_width(20)
r.set_height(10)
print(r.area())
