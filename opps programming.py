# OOPS ke 4 Main Concepts

# 1. Class
# Class ak design / blueprint hota hai.

class Student:
    name = "Shivam"
    age = 20


# 2. Object
# Object class ka real instance hota hai.

s1 = Student()
print(s1.name)
print(s1.age)

# 3. # Method (Function in Class)
# Class ke andar function ko method kehte hain.

class Student:
    def show(self):
        print("This is Student class")

s1 = Student()
s1.show()

##  self ka matlab: current object

# Constructor (__init__)

# Constructor object banate hi automatically call hota hai.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name, self.age)

s1 = Student("Shivam", 21)
s1.show()

# OOPS ke 4 Pillars

# 1. Encapsulation (Data Protection)
# Data ko class ke andar safe rakhna.

class Account:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def show(self):
        print(self.__balance)

a = Account(5000)
a.show()

# 2. Inheritance (Reuse)


class Parent:
    def home(self):
        print("This is Parent home")

class Child(Parent):
    def car(self):
        print("This is Child car")

c = Child()
c.home()
c.car()

# 3. Polymorphism (One name, many forms)
class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

d = Dog()
c = Cat()

d.sound()
c.sound()

# 4. Abstraction (Hide Details)

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def area(self):
        print("Area = side * side")

s = Square()
s.area()


# Method ke andar condition

class Result:
    def check(self, marks):
        if marks >= 40:
            print("Pass")
        else:
            print("Fail")

r = Result()
r.check(55)

# Constructor me condition

class Vote:
    def __init__(self, age):
        if age >= 18:
            print("You can vote")
        else:
            print("You cannot vote")

