"""
OBJECT-ORIENTED PROGRAMMING (OOP) - Complete Tutorial
=====================================================

Theory: OOP is a programming paradigm based on the concept of "objects"
which contain data (attributes) and code (methods).

The Four Pillars of OOP:
1. ENCAPSULATION - Bundling data and methods, hiding internal details
2. INHERITANCE - Creating new classes from existing ones
3. POLYMORPHISM - Same interface, different implementations
4. ABSTRACTION - Hiding complexity, showing only essentials
"""

# =============================================================================
# 1. BASIC CLASS AND OBJECT
# =============================================================================

print("\n" + "="*60)
print("1. BASIC CLASS AND OBJECT")
print("="*60)

# Class: Blueprint for creating objects
# Object: Instance of a class

class Dog:
    """A simple Dog class"""
    
    # Constructor - initializes object
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age    # Instance variable
    
    # Instance method
    def bark(self):
        return f"{self.name} says Woof!"
    
    def get_info(self):
        return f"{self.name} is {self.age} years old"

# Creating objects (instances)
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(dog1.bark())
print(dog1.get_info())
print(dog2.bark())
print(dog2.get_info())


# =============================================================================
# 2. ENCAPSULATION - Data Hiding and Protection
# =============================================================================

print("\n" + "="*60)
print("2. ENCAPSULATION")
print("="*60)

class BankAccount:
    """Demonstrates encapsulation with public, protected, and private members"""
    
    def __init__(self, account_number, balance):
        self.account_number = account_number    # Public
        self._branch = "Main Branch"            # Protected (convention: single _)
        self.__balance = balance                # Private (name mangling: double __)
    
    # Public method to access private data
    def get_balance(self):
        return self.__balance
    
    # Public method to modify private data with validation
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited ${amount}. New balance: ${self.__balance}"
        return "Invalid amount"
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.__balance}"
        return "Insufficient funds or invalid amount"

account = BankAccount("ACC001", 1000)
print(f"Account Number: {account.account_number}")
print(f"Initial Balance: ${account.get_balance()}")
print(account.deposit(500))
print(account.withdraw(200))
# print(account.__balance)  # This would cause an error - private variable
print(f"Protected Branch: {account._branch}")  # Accessible but not recommended


# =============================================================================
# 3. INHERITANCE - Code Reusability
# =============================================================================

print("\n" + "="*60)
print("3. INHERITANCE")
print("="*60)

# Parent/Base/Super Class
class Animal:
    """Base class for all animals"""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        return "Some generic sound"
    
    def info(self):
        return f"{self.name} is a {self.species}"

# Child/Derived/Sub Class
class Cat(Animal):
    """Cat inherits from Animal"""
    
    def __init__(self, name, color):
        super().__init__(name, "Cat")  # Call parent constructor
        self.color = color
    
    # Method Overriding
    def make_sound(self):
        return "Meow!"
    
    # Additional method specific to Cat
    def purr(self):
        return f"{self.name} is purring"

class Bird(Animal):
    """Bird inherits from Animal"""
    
    def __init__(self, name, can_fly):
        super().__init__(name, "Bird")
        self.can_fly = can_fly
    
    def make_sound(self):
        return "Chirp!"
    
    def fly(self):
        return f"{self.name} is flying" if self.can_fly else f"{self.name} cannot fly"

cat = Cat("Whiskers", "Orange")
print(cat.info())           # Inherited method
print(cat.make_sound())     # Overridden method
print(cat.purr())           # Cat-specific method

bird = Bird("Tweety", True)
print(bird.info())
print(bird.make_sound())
print(bird.fly())


# =============================================================================
# 4. POLYMORPHISM - Many Forms
# =============================================================================

print("\n" + "="*60)
print("4. POLYMORPHISM")
print("="*60)

# A. Method Overriding (Runtime Polymorphism)
class Shape:
    """Base class for shapes"""
    
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

# Polymorphism in action
shapes = [
    Rectangle(5, 10),
    Circle(7),
    Triangle(6, 8)
]

print("\nCalculating areas (Polymorphism):")
for shape in shapes:
    print(f"{shape.__class__.__name__} area: {shape.area():.2f}")


# B. Operator Overloading
class Vector:
    """Demonstrates operator overloading"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # Overload + operator
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    # Overload * operator
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    # Overload str() function
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    # Overload len() function
    def __len__(self):
        return int((self.x**2 + self.y**2)**0.5)

v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2
v4 = v1 * 3

print(f"\nv1: {v1}")
print(f"v2: {v2}")
print(f"v1 + v2: {v3}")
print(f"v1 * 3: {v4}")


# =============================================================================
# 5. ABSTRACTION - Hiding Complexity
# =============================================================================

print("\n" + "="*60)
print("5. ABSTRACTION")
print("="*60)

from abc import ABC, abstractmethod

# Abstract Base Class
class Vehicle(ABC):
    """Abstract class - cannot be instantiated"""
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    @abstractmethod
    def start_engine(self):
        """Abstract method - must be implemented by child classes"""
        pass
    
    @abstractmethod
    def stop_engine(self):
        pass
    
    # Concrete method (can be used by child classes)
    def get_info(self):
        return f"{self.brand} {self.model}"

class Car(Vehicle):
    """Concrete class implementing abstract methods"""
    
    def start_engine(self):
        return f"{self.get_info()} - Engine started: Vroom!"
    
    def stop_engine(self):
        return f"{self.get_info()} - Engine stopped"

class Motorcycle(Vehicle):
    def start_engine(self):
        return f"{self.get_info()} - Engine started: Brrr!"
    
    def stop_engine(self):
        return f"{self.get_info()} - Engine stopped"

# vehicle = Vehicle("Generic", "Model")  # Error: Cannot instantiate abstract class
car = Car("Toyota", "Camry")
bike = Motorcycle("Harley", "Davidson")

print(car.start_engine())
print(car.stop_engine())
print(bike.start_engine())


# =============================================================================
# 6. CLASS VS INSTANCE VARIABLES
# =============================================================================

print("\n" + "="*60)
print("6. CLASS VS INSTANCE VARIABLES")
print("="*60)

class Student:
    # Class variable (shared by all instances)
    school_name = "Python High School"
    total_students = 0
    
    def __init__(self, name, grade):
        # Instance variables (unique to each instance)
        self.name = name
        self.grade = grade
        Student.total_students += 1
    
    def display(self):
        return f"{self.name} - Grade {self.grade} at {Student.school_name}"

student1 = Student("Alice", 10)
student2 = Student("Bob", 11)

print(student1.display())
print(student2.display())
print(f"Total students: {Student.total_students}")

# Changing class variable affects all instances
Student.school_name = "Advanced Python Academy"
print(f"\nAfter changing school name:")
print(student1.display())
print(student2.display())


# =============================================================================
# 7. CLASS METHODS AND STATIC METHODS
# =============================================================================

print("\n" + "="*60)
print("7. CLASS METHODS AND STATIC METHODS")
print("="*60)

class MathOperations:
    pi = 3.14159
    
    def __init__(self, value):
        self.value = value
    
    # Regular instance method
    def square(self):
        return self.value ** 2
    
    # Class method - works with class, not instance
    @classmethod
    def circle_area(cls, radius):
        return cls.pi * radius ** 2
    
    # Static method - independent utility function
    @staticmethod
    def is_even(num):
        return num % 2 == 0
    
    @staticmethod
    def add(a, b):
        return a + b

# Instance method requires object
obj = MathOperations(5)
print(f"Square of 5: {obj.square()}")

# Class method can be called on class or instance
print(f"Circle area (r=3): {MathOperations.circle_area(3):.2f}")

# Static method - no need for instance or class reference
print(f"Is 4 even? {MathOperations.is_even(4)}")
print(f"Add 10 + 20: {MathOperations.add(10, 20)}")


# =============================================================================
# 8. PROPERTIES AND DECORATORS
# =============================================================================

print("\n" + "="*60)
print("8. PROPERTIES AND DECORATORS")
print("="*60)

class Person:
    """Demonstrates @property decorator"""
    
    def __init__(self, first_name, last_name, age):
        self._first_name = first_name
        self._last_name = last_name
        self._age = age
    
    # Getter using @property
    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"
    
    @property
    def age(self):
        return self._age
    
    # Setter with validation
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value
    
    @property
    def is_adult(self):
        return self._age >= 18

person = Person("John", "Doe", 25)
print(f"Full name: {person.full_name}")
print(f"Age: {person.age}")
print(f"Is adult: {person.is_adult}")

person.age = 30  # Using setter
print(f"Updated age: {person.age}")

# person.age = -5  # This would raise ValueError


# =============================================================================
# 9. MULTIPLE INHERITANCE
# =============================================================================

print("\n" + "="*60)
print("9. MULTIPLE INHERITANCE")
print("="*60)

class Father:
    def __init__(self):
        self.father_name = "John"
    
    def gardening(self):
        return "Father loves gardening"

class Mother:
    def __init__(self):
        self.mother_name = "Jane"
    
    def cooking(self):
        return "Mother loves cooking"

class Child(Father, Mother):
    def __init__(self, name):
        Father.__init__(self)
        Mother.__init__(self)
        self.name = name
    
    def display(self):
        return f"{self.name}'s father: {self.father_name}, mother: {self.mother_name}"

child = Child("Tommy")
print(child.display())
print(child.gardening())
print(child.cooking())


# =============================================================================
# 10. METHOD RESOLUTION ORDER (MRO)
# =============================================================================

print("\n" + "="*60)
print("10. METHOD RESOLUTION ORDER (MRO)")
print("="*60)

class A:
    def method(self):
        return "Method from A"

class B(A):
    def method(self):
        return "Method from B"

class C(A):
    def method(self):
        return "Method from C"

class D(B, C):
    pass

d = D()
print(f"Method called: {d.method()}")
print(f"MRO: {[cls.__name__ for cls in D.__mro__]}")


# =============================================================================
# 11. SPECIAL/MAGIC METHODS (DUNDER METHODS)
# =============================================================================

print("\n" + "="*60)
print("11. SPECIAL/MAGIC METHODS")
print("="*60)

class Book:
    """Demonstrates various magic methods"""
    
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        """Called by str() and print()"""
        return f"'{self.title}' by {self.author}"
    
    def __repr__(self):
        """Called by repr() - for developers"""
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    def __len__(self):
        """Called by len()"""
        return self.pages
    
    def __eq__(self, other):
        """Called by =="""
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):
        """Called by <"""
        return self.pages < other.pages
    
    def __add__(self, other):
        """Called by +"""
        return self.pages + other.pages

book1 = Book("Python Basics", "John Smith", 300)
book2 = Book("Advanced Python", "Jane Doe", 500)

print(f"str(): {str(book1)}")
print(f"repr(): {repr(book1)}")
print(f"len(): {len(book1)} pages")
print(f"book1 < book2: {book1 < book2}")
print(f"Total pages: {book1 + book2}")


# =============================================================================
# 12. REAL-WORLD EXAMPLE - E-Commerce System
# =============================================================================

print("\n" + "="*60)
print("12. REAL-WORLD EXAMPLE - E-COMMERCE SYSTEM")
print("="*60)

class Product:
    """Base Product class"""
    
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price
    
    def get_details(self):
        return f"{self.name} - ${self.price:.2f}"
    
    def calculate_total(self, quantity):
        return self.price * quantity

class Electronics(Product):
    """Electronics category"""
    
    def __init__(self, product_id, name, price, warranty_years):
        super().__init__(product_id, name, price)
        self.warranty_years = warranty_years
    
    def get_details(self):
        return f"{super().get_details()} [Warranty: {self.warranty_years} years]"

class Clothing(Product):
    """Clothing category"""
    
    def __init__(self, product_id, name, price, size):
        super().__init__(product_id, name, price)
        self.size = size
    
    def get_details(self):
        return f"{super().get_details()} [Size: {self.size}]"

class ShoppingCart:
    """Shopping cart to manage products"""
    
    def __init__(self):
        self.items = []
    
    def add_item(self, product, quantity):
        self.items.append({"product": product, "quantity": quantity})
        return f"Added {quantity}x {product.name}"
    
    def get_total(self):
        return sum(item["product"].calculate_total(item["quantity"]) 
                  for item in self.items)
    
    def display_cart(self):
        print("\nShopping Cart:")
        print("-" * 50)
        for item in self.items:
            product = item["product"]
            quantity = item["quantity"]
            total = product.calculate_total(quantity)
            print(f"{product.get_details()} x {quantity} = ${total:.2f}")
        print("-" * 50)
        print(f"TOTAL: ${self.get_total():.2f}")

# Using the e-commerce system
laptop = Electronics("E001", "Laptop", 999.99, 2)
phone = Electronics("E002", "Smartphone", 699.99, 1)
shirt = Clothing("C001", "T-Shirt", 29.99, "L")

cart = ShoppingCart()
print(cart.add_item(laptop, 1))
print(cart.add_item(phone, 2))
print(cart.add_item(shirt, 3))
cart.display_cart()


# =============================================================================
# 13. COMPOSITION VS INHERITANCE
# =============================================================================

print("\n" + "="*60)
print("13. COMPOSITION VS INHERITANCE")
print("="*60)

# Composition: "Has-a" relationship
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def start(self):
        return f"Engine with {self.horsepower}HP started"

class Wheel:
    def __init__(self, size):
        self.size = size

class AutoCar:
    """Car has an Engine and Wheels (Composition)"""
    
    def __init__(self, brand, engine, wheel_size):
        self.brand = brand
        self.engine = engine  # Composition
        self.wheels = [Wheel(wheel_size) for _ in range(4)]
    
    def start(self):
        return f"{self.brand} car - {self.engine.start()}"

engine = Engine(200)
car = AutoCar("Tesla", engine, 18)
print(car.start())


# =============================================================================
# SUMMARY
# =============================================================================

print("\n" + "="*60)
print("OOP CONCEPTS SUMMARY")
print("="*60)

summary = """
1. CLASS & OBJECT: Blueprint and instances
2. ENCAPSULATION: Data hiding (public, protected, private)
3. INHERITANCE: Code reusability (parent-child relationship)
4. POLYMORPHISM: Same interface, different implementations
5. ABSTRACTION: Hiding complexity, abstract classes
6. CLASS vs INSTANCE: Shared vs unique data
7. CLASS/STATIC METHODS: Different method types
8. PROPERTIES: Getters/setters with @property
9. MULTIPLE INHERITANCE: Inheriting from multiple parents
10. MRO: Method Resolution Order in inheritance
11. MAGIC METHODS: __init__, __str__, __add__, etc.
12. COMPOSITION: "Has-a" relationship
13. REAL-WORLD USAGE: Combining all concepts

KEY PRINCIPLES:
- DRY (Don't Repeat Yourself)
- Single Responsibility Principle
- Open/Closed Principle
- Liskov Substitution Principle
- Interface Segregation Principle
- Dependency Inversion Principle
"""

print(summary)
print("="*60)
