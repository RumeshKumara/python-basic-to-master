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