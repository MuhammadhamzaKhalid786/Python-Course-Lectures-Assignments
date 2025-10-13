# =====================================
# Inheritance in Python (Syntax)
# =====================================
# class ParentClass:
#     def __init__(self, attributes):
#         self.attributes = attributes
#     def method1(self):
#         pass
#
# class ChildClass(ParentClass):
#     def method2(self):
#         pass

# =====================================
# Example 1: Simple Inheritance
# =====================================
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking")


dog1 = Dog("Tommy")
dog1.speak()
dog1.bark()


# =====================================
# Example 2: Method Overriding
# =====================================
class Animal:
    def speak(self):
        print("This is an animal")

class Cat(Animal):
    def speak(self):
        print("Meow Meow")

cat1 = Cat()
cat1.speak()


# =====================================
# Example 3: Adding New Methods in Child
# =====================================
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def drive(self):
        print(f"{self.brand} is driving on the road")

mycar = Car("Toyota")
mycar.drive()


# =====================================
# Example 4: Using super() to Call Parent
# =====================================
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def show(self):
        print(f"{self.name}, {self.age} years old, Grade: {self.grade}")

s1 = Student("Arooj", 23, "16th")
s1.show()


# =====================================
# Example 5: Multilevel Inheritance
# =====================================
class Animal:
    def eat(self):
        print("This animal eats food")

class Mammal(Animal):
    def walk(self):
        print("This mammal walks")

class Human(Mammal):
    def speak(self):
        print("Human can speak")

h = Human()
h.eat()
h.walk()
h.speak()


# =====================================
# Example 6: Multiple Inheritance
# =====================================
class Father:
    def skill(self):
        print("Father knows driving")

class Mother:
    def skill(self):
        print("Mother knows cooking")

class Child(Father, Mother):
    def show(self):
        print("Child inherits from both Father and Mother")

c = Child()
c.skill()
c.show()


# =====================================
# Example 7: Inheriting and Adding Methods
# =====================================
class Shape:
    def area(self):
        print("Shape has no area")

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        print(self.side * self.side)

sq = Square(5)
sq.area()


# =====================================
# Example 8: super() with Method Overriding
# =====================================
class Parent:
    def show(self):
        print("This is parent method")

class Child(Parent):
    def show(self):
        super().show()
        print("This is child method")

c1 = Child()
c1.show()


# =====================================
# Example 9: Inheritance with Input
# =====================================
class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def teach(self, subject):
        print(f"{self.name} teaches {subject}")

t1 = Teacher(input("Enter teacher name: "))
t1.teach("Math")


# =====================================
# Example 10: Inheriting Constructor
# =====================================
class Device:
    def __init__(self, brand):
        self.brand = brand

class Laptop(Device):
    def __init__(self, brand, ram):
        super().__init__(brand)
        self.ram = ram

    def details(self):
        print(f"Laptop Brand: {self.brand}, RAM: {self.ram}GB")

lap1 = Laptop("Dell", 16)
lap1.details()


# =====================================
# Example 11: Polymorphism via Inheritance
# =====================================
class Bird:
    def fly(self):
        print("Some birds can fly")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow flies high")

class Penguin(Bird):
    def fly(self):
        print("Penguins cannot fly")

birds = [Sparrow(), Penguin()]
for b in birds:
    b.fly()


# =====================================
# Example 12: Employee and Manager

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def bonus(self):
        print(f"{self.name} gets bonus of {self.salary * 0.1}")

m = Manager("Khalid", 50000)
m.bonus()
