"""
Python Lists (Arrays) - Comprehensive Guide

In Python, lists are ordered, mutable collections of items that can hold elements of different types.
They are one of the most versatile and commonly used data structures in Python.
"""

# 1. Creating Lists
print("1. Creating Lists")
print("-" * 40)

# Empty list
empty_list = []
print(f"Empty list: {empty_list}")

# List with elements of the same type
numbers = [1, 2, 3, 4, 5]
print(f"Numbers list: {numbers}")

# List with elements of different types
mixed_list = [1, "Hello", 3.14, True]
print(f"Mixed list: {mixed_list}")

# Creating a list using the list() constructor
list_from_string = list("Python")
print(f"List from string: {list_from_string}")

# Creating a list using list comprehension
squares = [x**2 for x in range(1, 6)]
print(f"Squares using list comprehension: {squares}")
print("\n")

# 2. Accessing List Elements
print("2. Accessing List Elements")
print("-" * 40)

fruits = ["apple", "banana", "cherry", "orange", "kiwi"]
print(f"Fruits list: {fruits}")

# Accessing by index (indexing starts at 0)
print(f"First fruit: {fruits[0]}")
print(f"Third fruit: {fruits[2]}")

# Negative indexing (counts from the end)
print(f"Last fruit: {fruits[-1]}")
print(f"Second last fruit: {fruits[-2]}")

# Slicing a list [start:end:step]
print(f"First two fruits: {fruits[0:2]}")
print(f"All fruits except first: {fruits[1:]}")
print(f"Last three fruits: {fruits[-3:]}")
print(f"Every second fruit: {fruits[::2]}")
print("\n")

# 3. Modifying Lists
print("3. Modifying Lists")
print("-" * 40)

# Lists are mutable - we can change their content
colors = ["red", "green", "blue"]
print(f"Original colors: {colors}")

# Changing an item
colors[1] = "yellow"
print(f"After changing second item: {colors}")

# Adding items to a list
colors.append("purple")  # Add at the end
print(f"After appending 'purple': {colors}")

colors.insert(2, "orange")  # Insert at specific position
print(f"After inserting 'orange' at position 2: {colors}")

# Extending a list
more_colors = ["pink", "black"]
colors.extend(more_colors)
print(f"After extending with more colors: {colors}")

# Removing items
colors.remove("yellow")  # Remove by value
print(f"After removing 'yellow': {colors}")

popped_color = colors.pop()  # Remove and return the last item
print(f"Popped color: {popped_color}")
print(f"After popping: {colors}")

popped_at_index = colors.pop(1)  # Remove at index
print(f"Popped at index 1: {popped_at_index}")
print(f"After popping at index 1: {colors}")

# Clear a list
colors_copy = colors.copy()
colors_copy.clear()
print(f"After clearing colors_copy: {colors_copy}")
print("\n")

# 4. List Operations and Methods
print("4. List Operations and Methods")
print("-" * 40)

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenation
combined = list1 + list2
print(f"Concatenated lists: {combined}")

# Repetition
repeated = list1 * 3
print(f"List1 repeated 3 times: {repeated}")

# Length of a list
print(f"Length of combined list: {len(combined)}")

# Count occurrences of an element
digits = [1, 2, 2, 3, 2, 4, 5, 2]
print(f"Count of 2 in digits: {digits.count(2)}")

# Find index of an element (first occurrence)
print(f"Index of 4 in digits: {digits.index(4)}")

# Sorting
unsorted = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Unsorted list: {unsorted}")

# Sort the list in-place
unsorted.sort()
print(f"After sorting: {unsorted}")

# Sort in descending order
unsorted.sort(reverse=True)
print(f"After sorting in descending order: {unsorted}")

# Sorting without modifying the original list
original = [3, 1, 4, 1, 5, 9]
sorted_list = sorted(original)
print(f"Original list: {original}")
print(f"Sorted list: {sorted_list}")

# Reversing a list
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(f"Reversed list: {numbers}")
print("\n")

# 5. Nested Lists (Multi-dimensional arrays)
print("5. Nested Lists (Multi-dimensional arrays)")
print("-" * 40)

# 2D list (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"Matrix: {matrix}")

# Accessing elements in a 2D list
print(f"First row: {matrix[0]}")
print(f"Element at row 1, column 2: {matrix[1][2]}")

# Creating a 3x3 matrix with all zeros using list comprehension
zeros_matrix = [[0 for _ in range(3)] for _ in range(3)]
print(f"3x3 Zero matrix: {zeros_matrix}")
print("\n")

# 6. List Comprehensions
print("6. List Comprehensions")
print("-" * 40)

# Basic list comprehension
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(f"Numbers: {numbers}")
print(f"Squares: {squares}")

# List comprehension with condition
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(f"Even squares: {even_squares}")

# Nested list comprehension (flattening a 2D list)
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [num for row in matrix for num in row]
print(f"Matrix: {matrix}")
print(f"Flattened: {flattened}")
print("\n")

# 7. Common List Operations
print("7. Common List Operations")
print("-" * 40)

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(f"Numbers: {numbers}")

# Finding min and max
print(f"Minimum value: {min(numbers)}")
print(f"Maximum value: {max(numbers)}")

# Sum of all elements
print(f"Sum of all elements: {sum(numbers)}")

# Check if an element exists in a list
print(f"Is 5 in the list? {'yes' if 5 in numbers else 'no'}")
print(f"Is 7 in the list? {'yes' if 7 in numbers else 'no'}")

# Copying lists
# Simple assignment creates a reference, not a copy
list1 = [1, 2, 3]
list2 = list1  # Both variables refer to the same list

# To create actual copies
shallow_copy = list1.copy()  # or list(list1)
import copy
deep_copy = copy.deepcopy(list1)  # For nested lists

list1[0] = 99  # This will affect list2 but not the copies
print(f"Original list after modification: {list1}")
print(f"Referenced list (affected): {list2}")
print(f"Shallow copy (unaffected): {shallow_copy}")
print(f"Deep copy (unaffected): {deep_copy}")
print("\n")

# 8. Advanced List Techniques
print("8. Advanced List Techniques")
print("-" * 40)

# Using zip to work with multiple lists simultaneously
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
zipped = list(zip(names, ages))
print(f"Zipped lists: {zipped}")

# Unzipping a list of tuples
unzipped_names, unzipped_ages = zip(*zipped)
print(f"Unzipped names: {unzipped_names}")
print(f"Unzipped ages: {unzipped_ages}")

# Using enumerate to get index and value
for i, name in enumerate(names):
    print(f"Index {i}: {name}")

# List as a stack (LIFO - Last In, First Out)
stack = []
stack.append(1)  # Push
stack.append(2)
stack.append(3)
print(f"Stack: {stack}")
print(f"Popped item: {stack.pop()}")  # Pop
print(f"Stack after pop: {stack}")

# List as a queue (FIFO - First In, First Out)
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")  # Add to right side
print(f"Queue: {queue}")
print(f"Dequeued item: {queue.popleft()}")  # Remove from left side
print(f"Queue after dequeue: {queue}")
print("\n")

# 9. Performance Considerations
print("9. Performance Considerations")
print("-" * 40)
print("Lists in Python are implemented as dynamic arrays, which means:")
print("- Accessing an element by index is O(1) - constant time")
print("- Appending to the end is usually O(1), but can be O(n) when resizing is needed")
print("- Inserting or deleting elements in the middle is O(n) - linear time")
print("- Searching for an element is O(n) in the worst case")
print("\n")

# 10. Lists vs Other Data Structures
print("10. Lists vs Other Data Structures")
print("-" * 40)
print("When to use lists vs other data structures:")
print("- Use lists when you need an ordered collection that might change")
print("- Use tuples for immutable ordered collections")
print("- Use sets for unordered collections with no duplicates")
print("- Use dictionaries when you need key-value mapping")
print("\nExample comparison:")

# Example list, tuple, set, and dictionary
example_list = [1, 2, 2, 3]
example_tuple = (1, 2, 2, 3)
example_set = {1, 2, 2, 3}  # Will only store {1, 2, 3}
example_dict = {1: "one", 2: "two", 3: "three"}

print(f"List: {example_list} - Ordered, mutable, allows duplicates")
print(f"Tuple: {example_tuple} - Ordered, immutable, allows duplicates")
print(f"Set: {example_set} - Unordered, mutable, no duplicates")
print(f"Dict: {example_dict} - Ordered (Python 3.7+), mutable, key-value pairs")