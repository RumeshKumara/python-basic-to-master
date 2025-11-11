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