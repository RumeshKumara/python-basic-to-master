# ============================================
# 1. EXCEPTION HANDLING - Manage runtime errors safely
# ============================================

def divide_numbers(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except TypeError:
        print("Error: Invalid data type!")
    finally:
        print("Execution completed.\n")

# Usage
divide_numbers(10, 2)   # Success
divide_numbers(10, 0)   # ZeroDivisionError


# ============================================
# 2. FILE HANDLING - Read/write data to files
# ============================================

# Writing to a file
with open('sample.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("Python File Handling\n")

# Reading from a file
with open('sample.txt', 'r') as file:
    content = file.read()
    print("File Content:")
    print(content)

# Appending to a file
with open('sample.txt', 'a') as file:
    file.write("Appended line\n")


# ============================================
# 3. ITERATORS - Step through data manually
# ============================================

# Creating a custom iterator
class CountDown:
    def __init__(self, start):
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

# Usage
counter = CountDown(5)
for num in counter:
    print(f"Countdown: {num}")

# Manual iteration
numbers = iter([1, 2, 3, 4, 5])
print(next(numbers))  # 1
print(next(numbers))  # 2


# ============================================
# 4. GENERATORS - Yield data lazily (one at a time)
# ============================================

# Simple generator function
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Usage
print("\nFibonacci sequence:")
for num in fibonacci(8):
    print(num, end=" ")

# Generator expression
squares = (x**2 for x in range(1, 6))
print("\n\nSquares:", list(squares))


# ============================================
# 5. DECORATORS - Add behavior to functions
# ============================================

# Simple decorator
def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@uppercase_decorator
def greet():
    return "hello, world!"

print("\n" + greet())  # HELLO, WORLD!

# Decorator with arguments
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Python")


# ============================================
# 6. COMPREHENSIONS - Create data structures concisely
# ============================================

# List comprehension
squares = [x**2 for x in range(1, 6)]
print(f"\nSquares: {squares}")

# List comprehension with condition
evens = [x for x in range(10) if x % 2 == 0]
print(f"Even numbers: {evens}")

# Dictionary comprehension
square_dict = {x: x**2 for x in range(1, 6)}
print(f"Square dict: {square_dict}")

# Set comprehension
unique_lengths = {len(word) for word in ["apple", "bat", "cherry", "dog"]}
print(f"Unique lengths: {unique_lengths}")

# Nested list comprehension
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(f"Matrix: {matrix}")


# ============================================
# 7. REGEX - Pattern matching in strings
# ============================================

import re

text = "Contact: john@example.com or call 123-456-7890"

# Find email
email = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
print(f"\nEmail found: {email.group()}")

# Find phone number
phone = re.search(r'\d{3}-\d{3}-\d{4}', text)
print(f"Phone found: {phone.group()}")

# Replace pattern
new_text = re.sub(r'\d', 'X', text)
print(f"Masked: {new_text}")

# Find all matches
numbers = re.findall(r'\d+', "Order: 100 items at $25 each")
print(f"All numbers: {numbers}")

# Split by pattern
words = re.split(r'\s+', "Python   is    awesome")
print(f"Words: {words}")

# Match validation
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

print(f"\nIs 'test@example.com' valid? {is_valid_email('test@example.com')}")
print(f"Is 'invalid-email' valid? {is_valid_email('invalid-email')}")


# ============================================
# BONUS: Combining multiple concepts
# ============================================

# Generator with decorator
def timer_decorator(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"\nExecution time: {end - start:.6f} seconds")
        return result
    return wrapper

@timer_decorator
def process_data(data):
    # Using comprehension and generator
    return [x * 2 for x in data if x > 0]

result = process_data([-1, 2, 3, -4, 5])
print(f"Processed data: {result}")
