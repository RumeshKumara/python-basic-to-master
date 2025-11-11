"""
Object-Oriented Programming (OOP) Concepts in Python
=====================================================
This file demonstrates all major OOP concepts with practical examples.
"""

from abc import ABC, abstractmethod


# ============================================================================
# 1. CLASSES AND OBJECTS
# ============================================================================
print("=" * 60)
print("1. CLASSES AND OBJECTS")
print("=" * 60)

class Person:
    """Basic class demonstrating class and object creation"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

# Creating objects
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

print(person1.introduce())
print(person2.introduce())
print()

# ============================================================================
# 2. ENCAPSULATION
# ============================================================================
print("=" * 60)
print("2. ENCAPSULATION (Data Hiding)")
print("=" * 60)

class BankAccount:
    """Demonstrates encapsulation with private attributes"""
    
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder  # Public
        self._account_number = "ACC123456"     # Protected (convention)
        self.__balance = balance                # Private (name mangling)
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited ${amount}. New balance: ${self.__balance}"
        return "Invalid amount"
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew ${amount}. Remaining balance: ${self.__balance}"
        return "Insufficient funds or invalid amount"
    
    def get_balance(self):
        """Getter method to access private attribute"""
        return self.__balance
    
    def set_balance(self, balance):
        """Setter method with validation"""
        if balance >= 0:
            self.__balance = balance
        else:
            print("Balance cannot be negative")

# Using encapsulation
account = BankAccount("John Doe", 1000)
print(f"Account holder: {account.account_holder}")
print(account.deposit(500))
print(account.withdraw(200))
print(f"Current balance: ${account.get_balance()}")
# print(account.__balance)  # This would raise AttributeError
print()

# ============================================================================
# 3. INHERITANCE
# ============================================================================
print("=" * 60)
print("3. INHERITANCE")
print("=" * 60)

# A. Single Inheritance
class Animal:
    """Parent/Base class"""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        return "Some generic animal sound"
    
    def info(self):
        return f"{self.name} is a {self.species}"

class Dog(Animal):
    """Child/Derived class - Single Inheritance"""
    
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed
    
    def make_sound(self):
        return "Woof! Woof!"
    
    def fetch(self):
        return f"{self.name} is fetching the ball!"

class Cat(Animal):
    """Another child class"""
    
    def __init__(self, name, color):
        super().__init__(name, "Cat")
        self.color = color
    
    def make_sound(self):
        return "Meow! Meow!"

# Using inheritance
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Orange")

print(dog.info())
print(dog.make_sound())
print(dog.fetch())
print()
print(cat.info())
print(cat.make_sound())
print()

# B. Multiple Inheritance
class Flyer:
    """Mixin class for flying capability"""
    
    def fly(self):
        return "Flying in the sky!"

class Swimmer:
    """Mixin class for swimming capability"""
    
    def swim(self):
        return "Swimming in the water!"

class Duck(Animal, Flyer, Swimmer):
    """Multiple Inheritance - inherits from multiple classes"""
    
    def __init__(self, name):
        super().__init__(name, "Duck")
    
    def make_sound(self):
        return "Quack! Quack!"

duck = Duck("Donald")
print(f"\n{duck.info()}")
print(duck.make_sound())
print(duck.fly())
print(duck.swim())
print()

# C. Multilevel Inheritance
class LivingBeing:
    """Grandparent class"""
    
    def breathe(self):
        return "Breathing..."

class Mammal(LivingBeing):
    """Parent class"""
    
    def give_birth(self):
        return "Giving birth to live young"

class Human(Mammal):
    """Child class - Multilevel Inheritance"""
    
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} is speaking"

human = Human("Sarah")
print(f"Multilevel Inheritance:")
print(human.speak())
print(human.give_birth())
print(human.breathe())
print()

# ============================================================================
# 4. POLYMORPHISM
# ============================================================================
print("=" * 60)
print("4. POLYMORPHISM")
print("=" * 60)

# A. Method Overriding (Runtime Polymorphism)
class Shape:
    """Base class for shapes"""
    
    def area(self):
        return 0
    
    def perimeter(self):
        return 0

class Circle(Shape):
    """Circle with overridden methods"""
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius

class Rectangle(Shape):
    """Rectangle with overridden methods"""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Triangle(Shape):
    """Triangle with overridden methods"""
    
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def area(self):
        return 0.5 * self.base * self.height
    
    def perimeter(self):
        return self.side1 + self.side2 + self.side3

# Polymorphism in action
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 4, 3, 4, 5)
]

print("Polymorphism - Different shapes, same interface:")
for shape in shapes:
    print(f"{shape.__class__.__name__}: Area = {shape.area():.2f}, Perimeter = {shape.perimeter():.2f}")
print()

# B. Operator Overloading (Special Methods)
class Vector:
    """Demonstrates operator overloading"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        """Overload + operator"""
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """Overload - operator"""
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        """Overload * operator for scalar multiplication"""
        return Vector(self.x * scalar, self.y * scalar)
    
    def __str__(self):
        """Overload str() function"""
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        """Overload repr() function"""
        return f"Vector({self.x}, {self.y})"
    
    def __eq__(self, other):
        """Overload == operator"""
        return self.x == other.x and self.y == other.y

v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2
v4 = v2 - v1
v5 = v1 * 3

print("Operator Overloading:")
print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v1 + v2 = {v3}")
print(f"v2 - v1 = {v4}")
print(f"v1 * 3 = {v5}")
print(f"v1 == v2: {v1 == v2}")
print()