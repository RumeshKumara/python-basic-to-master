"""
Python Loop Examples: For Loops and While Loops
"""

# -------------------------
# FOR LOOP EXAMPLES
# -------------------------

print("FOR LOOP EXAMPLES")
print("-" * 30)

# Example 1: Basic for loop with a range
print("\n1. Basic for loop with range:")
for i in range(5):
    print(f"Count: {i}")

# Example 2: For loop with start, stop, and step parameters
print("\n2. For loop with start, stop, and step:")
for i in range(2, 10, 2):
    print(f"Even number: {i}")

# Example 3: For loop iterating through a list
print("\n3. For loop with a list:")
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
for fruit in fruits:
    print(f"Fruit: {fruit}")

# Example 4: For loop with index using enumerate()
print("\n4. For loop with enumerate():")
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# Example 5: For loop with dictionary
print("\n5. For loop with a dictionary:")
person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "job": "Developer"
}

# Iterating over keys
print("Dictionary keys:")
for key in person:
    print(key)

# Iterating over values
print("\nDictionary values:")
for value in person.values():
    print(value)

# Iterating over key-value pairs
print("\nDictionary items:")
for key, value in person.items():
    print(f"{key}: {value}")

# Example 6: Nested for loops
print("\n6. Nested for loops:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i}, {j})", end=" ")
    print()  # New line after each row

# Example 7: For loop with break statement
print("\n7. For loop with break:")
for i in range(10):
    if i == 5:
        print("Breaking the loop at i =", i)
        break
    print(i, end=" ")
print()  # New line

# Example 8: For loop with continue statement
print("\n8. For loop with continue:")
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i, end=" ")  # Print only odd numbers
print()  # New line

# Example 9: For loop with else clause
print("\n9. For loop with else clause:")
for i in range(5):
    print(i, end=" ")
else:
    print("\nLoop completed successfully!")

# Example 10: List comprehension (compact for loop)
print("\n10. List comprehension:")
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

# -------------------------
# WHILE LOOP EXAMPLES
# -------------------------

print("\n\nWHILE LOOP EXAMPLES")
print("-" * 30)

# Example 1: Basic while loop
print("\n1. Basic while loop:")
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

# Example 2: While loop with break statement
print("\n2. While loop with break:")
count = 0
while True:
    print(f"Count: {count}")
    count += 1
    if count >= 5:
        print("Breaking infinite loop")
        break

# Example 3: While loop with continue statement
print("\n3. While loop with continue:")
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue  # Skip even numbers
    print(f"Odd number: {count}")

# Example 4: While loop with else clause
print("\n4. While loop with else clause:")
count = 0
while count < 5:
    print(count, end=" ")
    count += 1
else:
    print("\nWhile loop completed!")

# Example 5: Using while to process user input
print("\n5. While loop for user input (commented out):")
"""
while True:
    user_input = input("Enter a number (or 'quit' to exit): ")
    if user_input.lower() == 'quit':
        break
    try:
        number = float(user_input)
        print(f"You entered: {number}")
    except ValueError:
        print("That's not a valid number!")
"""
print("Example code for user input (see comments)")

# Example 6: Using while to validate input
print("\n6. While loop for input validation (commented out):")
"""
valid_input = False
while not valid_input:
    age = input("Enter your age (18-100): ")
    try:
        age = int(age)
        if 18 <= age <= 100:
            valid_input = True
            print(f"Age {age} accepted!")
        else:
            print("Age must be between 18 and 100")
    except ValueError:
        print("Please enter a valid number")
"""
print("Example code for input validation (see comments)")

# Example 7: Using while to iterate over a list
print("\n7. While loop to iterate over a list:")
fruits = ["apple", "banana", "cherry", "date"]
index = 0
while index < len(fruits):
    print(f"Fruit at index {index}: {fruits[index]}")
    index += 1

# Example 8: Nested while loops
print("\n8. Nested while loops:")
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(f"({i}, {j})", end=" ")
        j += 1
    print()  # New line
    i += 1

# Example 9: Do-while emulation (Python doesn't have do-while)
print("\n9. Do-while loop emulation:")
count = 5
while True:
    print(f"This will execute at least once: {count}")
    count -= 1
    if count < 0:
        break

# Example 10: While loop with complex condition
print("\n10. While loop with complex condition:")
a, b = 0, 10
while a < 5 and b > 5:
    print(f"a = {a}, b = {b}")
    a += 1
    b -= 1

print("\nEnd of loop examples.")