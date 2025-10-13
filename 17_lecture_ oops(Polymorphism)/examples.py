# ============================
# Polymorphism Examples
# ============================

# 1. Same function name in two classes
class Dog:
    def sound(self):
        return "Bark"

class Cat:
    def sound(self):
        return "Meow"

d = Dog()
c = Cat()
print(d.sound())
print(c.sound())


# 2. Animal speak with same method
class Cow:
    def speak(self):
        return "Moo"

class Goat:
    def speak(self):
        return "Baa"

a = Cow()
b = Goat()
print(a.speak())
print(b.speak())


# 3. Vehicle move
class Car:
    def move(self):
        return "Car is driving"

class Bike:
    def move(self):
        return "Bike is running"

c = Car()
b = Bike()
print(c.move())
print(b.move())


# 4. Bird fly
class Sparrow:
    def fly(self):
        return "Sparrow is flying"

class Pigeon:
    def fly(self):
        return "Pigeon is flying"

s = Sparrow()
p = Pigeon()
print(s.fly())
print(p.fly())


# 5. Shape area (different formula)
class Square:
    def area(self, side):
        return side * side

class Circle:
    def area(self, radius):
        return 3.14 * radius * radius

sq = Square()
ci = Circle()
print(sq.area(4))
print(ci.area(3))


# 6. Teacher and Student introduce
class Teacher:
    def introduce(self):
        return "I teach students."

class Student:
    def introduce(self):
        return "I learn from teachers."

t = Teacher()
s = Student()
print(t.introduce())
print(s.introduce())


# 7. Laptop and Mobile device info
class Laptop:
    def info(self):
        return "This is a laptop."

class Mobile:
    def info(self):
        return "This is a mobile."

l = Laptop()
m = Mobile()
print(l.info())
print(m.info())


# 8. Different sports play
class Football:
    def play(self):
        return "Playing football"

class Cricket:
    def play(self):
        return "Playing cricket"

f = Football()
c = Cricket()
print(f.play())
print(c.play())


# 9. Different languages say hello
class English:
    def say_hello(self):
        return "Hello"

class Urdu:
    def say_hello(self):
        return "Assalam o Alaikum"

e = English()
u = Urdu()
print(e.say_hello())
print(u.say_hello())


# 10. Different instruments sound
class Guitar:
    def sound(self):
        return "Strum"

class Drum:
    def sound(self):
        return "Boom Boom"

g = Guitar()
d = Drum()
print(g.sound())
print(d.sound())


# 11. Employee roles
class Manager:
    def role(self):
        return "I manage the team."

class Developer:
    def role(self):
        return "I write code."

m = Manager()
d = Developer()
print(m.role())
print(d.role())


# 12. Transport example
class Bus:
    def capacity(self):
        return "Bus carries 40 people."

class Van:
    def capacity(self):
        return "Van carries 8 people."

b = Bus()
v = Van()
print(b.capacity())
print(v.capacity())


# 13. Drinks
class Tea:
    def serve(self):
        return "Serving Tea"

class Coffee:
    def serve(self):
        return "Serving Coffee"

t = Tea()
c = Coffee()
print(t.serve())
print(c.serve())


# 14. Polymorphism with a loop (same method different class)
class Dog:
    def speak(self):
        return "Woof"

class Cat:
    def speak(self):
        return "Meow"

animals = [Dog(), Cat()]
for a in animals:
    print(a.speak())


# 15. Advanced Example → Shape area polymorphism
class Shape:
    def area(self):
        pass   # method left empty

class Rectangle(Shape):
    def area(self):
        return 10 * 5

class Triangle(Shape):
    def area(self):
        return 0.5 * 10 * 5

shapes = [Rectangle(), Triangle()]
for s in shapes:
    print(s.area())
