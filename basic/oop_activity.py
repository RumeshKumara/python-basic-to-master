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

# ============================================================================
# 5. ABSTRACTION
# ============================================================================
print("=" * 60)
print("5. ABSTRACTION")
print("=" * 60)

class Vehicle(ABC):
    """Abstract base class - cannot be instantiated"""
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    @abstractmethod
    def start_engine(self):
        """Abstract method - must be implemented by child classes"""
        pass
    
    @abstractmethod
    def stop_engine(self):
        """Abstract method - must be implemented by child classes"""
        pass
    
    def display_info(self):
        """Concrete method - can be used by all child classes"""
        return f"{self.brand} {self.model}"

class Car(Vehicle):
    """Concrete class implementing abstract methods"""
    
    def start_engine(self):
        return f"{self.display_info()}: Engine started with key"
    
    def stop_engine(self):
        return f"{self.display_info()}: Engine stopped"

class Motorcycle(Vehicle):
    """Another concrete class"""
    
    def start_engine(self):
        return f"{self.display_info()}: Engine started with kick/button"
    
    def stop_engine(self):
        return f"{self.display_info()}: Engine stopped"

# Using abstraction
car = Car("Toyota", "Camry")
motorcycle = Motorcycle("Harley-Davidson", "Street 750")

print(car.start_engine())
print(car.stop_engine())
print()
print(motorcycle.start_engine())
print(motorcycle.stop_engine())
print()

# ============================================================================
# 6. CLASS VARIABLES VS INSTANCE VARIABLES
# ============================================================================
print("=" * 60)
print("6. CLASS VARIABLES VS INSTANCE VARIABLES")
print("=" * 60)

class Employee:
    """Demonstrates class vs instance variables"""
    
    company_name = "TechCorp"  # Class variable (shared by all instances)
    employee_count = 0          # Class variable
    
    def __init__(self, name, salary):
        self.name = name        # Instance variable (unique to each instance)
        self.salary = salary    # Instance variable
        Employee.employee_count += 1
    
    @classmethod
    def get_employee_count(cls):
        """Class method - works with class variables"""
        return cls.employee_count
    
    @staticmethod
    def is_workday(day):
        """Static method - doesn't access instance or class variables"""
        return day not in ['Saturday', 'Sunday']

emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)
emp3 = Employee("Charlie", 55000)

print(f"Company: {Employee.company_name}")
print(f"Total Employees: {Employee.get_employee_count()}")
print(f"Employee 1: {emp1.name}, Salary: ${emp1.salary}")
print(f"Employee 2: {emp2.name}, Salary: ${emp2.salary}")
print(f"Is Monday a workday? {Employee.is_workday('Monday')}")
print(f"Is Saturday a workday? {Employee.is_workday('Saturday')}")
print()

# ============================================================================
# 7. PROPERTY DECORATORS (GETTERS AND SETTERS)
# ============================================================================
print("=" * 60)
print("7. PROPERTY DECORATORS")
print("=" * 60)

class Temperature:
    """Demonstrates property decorators for controlled attribute access"""
    
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Getter for celsius"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Setter for celsius with validation"""
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero (-273.15°C)")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Convert celsius to fahrenheit"""
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """Set temperature using fahrenheit"""
        self._celsius = (value - 32) * 5/9

temp = Temperature(25)
print(f"Temperature: {temp.celsius}°C = {temp.fahrenheit}°F")

temp.celsius = 30
print(f"After setting celsius to 30: {temp.celsius}°C = {temp.fahrenheit}°F")

temp.fahrenheit = 68
print(f"After setting fahrenheit to 68: {temp.celsius}°C = {temp.fahrenheit}°F")
print()

# ============================================================================
# 8. COMPOSITION (HAS-A RELATIONSHIP)
# ============================================================================
print("=" * 60)
print("8. COMPOSITION (Has-A Relationship)")
print("=" * 60)

class Engine:
    """Component class"""
    
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def start(self):
        return f"Engine with {self.horsepower}hp started"

class Wheel:
    """Component class"""
    
    def __init__(self, size):
        self.size = size
    
    def rotate(self):
        return f"{self.size}-inch wheel rotating"

class CarComposition:
    """Composition - Car HAS-A Engine and Wheels"""
    
    def __init__(self, brand, engine_hp, wheel_size):
        self.brand = brand
        self.engine = Engine(engine_hp)  # Composition
        self.wheels = [Wheel(wheel_size) for _ in range(4)]  # Composition
    
    def start_car(self):
        print(f"{self.brand} car starting:")
        print(f"  {self.engine.start()}")
        for i, wheel in enumerate(self.wheels, 1):
            print(f"  Wheel {i}: {wheel.rotate()}")

my_car = CarComposition("Honda", 200, 17)
my_car.start_car()
print()


# ============================================================================
# 9. SPECIAL/MAGIC METHODS (DUNDER METHODS)
# ============================================================================
print("=" * 60)
print("9. SPECIAL/MAGIC METHODS")
print("=" * 60)

class Book:
    """Demonstrates various special methods"""
    
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        """Called by str() and print()"""
        return f"'{self.title}' by {self.author}"
    
    def __repr__(self):
        """Called by repr() - should be unambiguous"""
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    def __len__(self):
        """Called by len()"""
        return self.pages
    
    def __eq__(self, other):
        """Called by == operator"""
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):
        """Called by < operator"""
        return self.pages < other.pages
    
    def __add__(self, other):
        """Called by + operator"""
        return f"Book Series: {self.title} & {other.title}"

book1 = Book("Python Programming", "John Smith", 350)
book2 = Book("Data Science Handbook", "Jane Doe", 420)
book3 = Book("Python Programming", "John Smith", 350)

print(f"String representation: {book1}")
print(f"Repr representation: {repr(book1)}")
print(f"Length (pages): {len(book1)}")
print(f"book1 == book2: {book1 == book2}")
print(f"book1 == book3: {book1 == book3}")
print(f"book1 < book2: {book1 < book2}")
print(f"book1 + book2: {book1 + book2}")
print()


# ============================================================================
# 10. METHOD RESOLUTION ORDER (MRO)
# ============================================================================
print("=" * 60)
print("10. METHOD RESOLUTION ORDER (MRO)")
print("=" * 60)

class A:
    def process(self):
        return "Process from A"

class B(A):
    def process(self):
        return "Process from B"

class C(A):
    def process(self):
        return "Process from C"

class D(B, C):
    pass

obj = D()
print(f"Method Resolution Order for class D: {D.__mro__}")
print(f"Calling process(): {obj.process()}")
print()


# ============================================================================
# 11. REAL-WORLD EXAMPLE: LIBRARY MANAGEMENT SYSTEM
# ============================================================================
print("=" * 60)
print("11. REAL-WORLD EXAMPLE: LIBRARY MANAGEMENT SYSTEM")
print("=" * 60)

class LibraryItem(ABC):
    """Abstract base class for library items"""
    
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self.is_borrowed = False
    
    @abstractmethod
    def get_late_fee(self, days_late):
        pass
    
    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return f"{self.title} has been borrowed"
        return f"{self.title} is already borrowed"
    
    def return_item(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return f"{self.title} has been returned"
        return f"{self.title} was not borrowed"

class LibraryBook(LibraryItem):
    """Book in library"""
    
    def __init__(self, title, item_id, author, isbn):
        super().__init__(title, item_id)
        self.author = author
        self.isbn = isbn
    
    def get_late_fee(self, days_late):
        return days_late * 0.50  # $0.50 per day
    
    def __str__(self):
        return f"Book: '{self.title}' by {self.author}"

class LibraryDVD(LibraryItem):
    """DVD in library"""
    
    def __init__(self, title, item_id, director, duration):
        super().__init__(title, item_id)
        self.director = director
        self.duration = duration
    
    def get_late_fee(self, days_late):
        return days_late * 1.00  # $1.00 per day
    
    def __str__(self):
        return f"DVD: '{self.title}' directed by {self.director}"

class Member:
    """Library member"""
    
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_items = []
    
    def borrow_item(self, item):
        result = item.borrow()
        if "has been borrowed" in result:
            self.borrowed_items.append(item)
        return result
    
    def return_item(self, item):
        result = item.return_item()
        if "has been returned" in result and item in self.borrowed_items:
            self.borrowed_items.remove(item)
        return result
    
    def list_borrowed_items(self):
        if not self.borrowed_items:
            return f"{self.name} has no borrowed items"
        items = ", ".join([item.title for item in self.borrowed_items])
        return f"{self.name}'s borrowed items: {items}"

# Using the library system
book1 = LibraryBook("1984", "B001", "George Orwell", "978-0451524935")
dvd1 = LibraryDVD("Inception", "D001", "Christopher Nolan", 148)
member1 = Member("Alice Johnson", "M001")

print(book1)
print(dvd1)
print()
print(member1.borrow_item(book1))
print(member1.borrow_item(dvd1))
print(member1.list_borrowed_items())
print()
print(f"Late fee for book (5 days): ${book1.get_late_fee(5)}")
print(f"Late fee for DVD (5 days): ${dvd1.get_late_fee(5)}")
print()
print(member1.return_item(book1))
print(member1.list_borrowed_items())
print()


# ============================================================================
# SUMMARY OF OOP PRINCIPLES
# ============================================================================
print("=" * 60)
print("SUMMARY OF OOP PRINCIPLES")
print("=" * 60)
print("""
1. ENCAPSULATION: Bundle data and methods, hide internal details
2. INHERITANCE: Reuse code by creating parent-child relationships
3. POLYMORPHISM: Same interface, different implementations
4. ABSTRACTION: Hide complexity, show only essential features

Additional Concepts:
- Class vs Instance variables
- Static methods and Class methods
- Property decorators (getters/setters)
- Composition (has-a relationship)
- Special/Magic methods
- Method Resolution Order (MRO)

SOLID Principles:
- Single Responsibility Principle
- Open/Closed Principle
- Liskov Substitution Principle
- Interface Segregation Principle
- Dependency Inversion Principle
""")
print("=" * 60)