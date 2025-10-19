"""
PYTHON FUNCTIONS - COMPLETE GUIDE WITH EXAMPLES AND THEORY

THEORY:
========
A function is a reusable block of code that performs a specific task.
Functions help in:
- Code reusability
- Better organization
- Easier debugging
- Modularity

SYNTAX:
def function_name(parameters):
    '''docstring'''
    statement(s)
    return value
"""

# ============================================================================
# 1. BASIC FUNCTION - Without Parameters and Return
# ============================================================================
print("=" * 70)
print("1. BASIC FUNCTION - Without Parameters and Return")
print("=" * 70)

def greet():
    """Simple function that prints a greeting"""
    print("Hello, Welcome to Python Functions!")

# Call the function
greet()
print()


# ============================================================================
# 2. FUNCTION WITH PARAMETERS
# ============================================================================
print("=" * 70)
print("2. FUNCTION WITH PARAMETERS")
print("=" * 70)

def greet_person(name):
    """Function with one parameter"""
    print(f"Hello, {name}! Welcome to Python!")

def greet_full(first_name, last_name):
    """Function with multiple parameters"""
    print(f"Hello, {first_name} {last_name}!")

# Call functions with parameters
greet_person("Alice")
greet_full("John", "Doe")
print()


# ============================================================================
# 3. FUNCTION WITH RETURN VALUE
# ============================================================================
print("=" * 70)
print("3. FUNCTION WITH RETURN VALUE")
print("=" * 70)

def add_numbers(a, b):
    """Returns the sum of two numbers"""
    return a + b

def multiply(x, y):
    """Returns the product of two numbers"""
    result = x * y
    return result

# Call and use return values
sum_result = add_numbers(5, 3)
print(f"5 + 3 = {sum_result}")

product = multiply(4, 6)
print(f"4 * 6 = {product}")
print()


# ============================================================================
# 4. FUNCTION WITH DEFAULT PARAMETERS
# ============================================================================
print("=" * 70)
print("4. FUNCTION WITH DEFAULT PARAMETERS")
print("=" * 70)

def greet_with_title(name, title="Mr."):
    """Function with default parameter value"""
    print(f"Hello, {title} {name}")

def calculate_power(base, exponent=2):
    """Calculate power with default exponent of 2"""
    return base ** exponent

# Call with and without default parameters
greet_with_title("Smith")           # Uses default "Mr."
greet_with_title("Johnson", "Dr.")  # Overrides default

print(f"3^2 = {calculate_power(3)}")        # Uses default exponent
print(f"3^3 = {calculate_power(3, 3)}")     # Custom exponent
print()


# ============================================================================
# 5. FUNCTION WITH KEYWORD ARGUMENTS
# ============================================================================
print("=" * 70)
print("5. FUNCTION WITH KEYWORD ARGUMENTS")
print("=" * 70)

def describe_person(name, age, city):
    """Function demonstrating keyword arguments"""
    print(f"{name} is {age} years old and lives in {city}")

# Call with positional arguments
describe_person("Alice", 25, "New York")

# Call with keyword arguments (any order)
describe_person(city="London", name="Bob", age=30)
describe_person(age=28, city="Paris", name="Charlie")
print()


# ============================================================================
# 6. FUNCTION WITH *args (Variable Length Arguments)
# ============================================================================
print("=" * 70)
print("6. FUNCTION WITH *args (Variable Length Arguments)")
print("=" * 70)

def sum_all(*numbers):
    """Sum any number of arguments"""
    total = 0
    for num in numbers:
        total += num
    return total

def print_names(*names):
    """Print all names passed"""
    print("Names:")
    for name in names:
        print(f"  - {name}")

# Call with different numbers of arguments
print(f"Sum of 1, 2, 3: {sum_all(1, 2, 3)}")
print(f"Sum of 1, 2, 3, 4, 5: {sum_all(1, 2, 3, 4, 5)}")
print(f"Sum of 10, 20: {sum_all(10, 20)}")
print()
print_names("Alice", "Bob", "Charlie", "David")
print()


# ============================================================================
# 7. FUNCTION WITH **kwargs (Keyword Variable Arguments)
# ============================================================================
print("=" * 70)
print("7. FUNCTION WITH **kwargs (Keyword Variable Arguments)")
print("=" * 70)

def display_info(**info):
    """Display information from keyword arguments"""
    print("Information:")
    for key, value in info.items():
        print(f"  {key}: {value}")

def create_profile(**details):
    """Create a profile with any number of details"""
    return details

# Call with various keyword arguments
display_info(name="Alice", age=25, city="Boston", occupation="Engineer")
print()
profile = create_profile(name="Bob", age=30, country="USA", hobby="Reading")
print(f"Profile: {profile}")
print()


# ============================================================================
# 8. FUNCTION WITH MIXED ARGUMENTS (*args and **kwargs)
# ============================================================================
print("=" * 70)
print("8. FUNCTION WITH MIXED ARGUMENTS")
print("=" * 70)

def mixed_function(name, *hobbies, **details):
    """Function with regular, *args, and **kwargs parameters"""
    print(f"Name: {name}")
    print("Hobbies:", ", ".join(hobbies))
    print("Details:")
    for key, value in details.items():
        print(f"  {key}: {value}")

mixed_function("Alice", "Reading", "Swimming", "Coding", 
               age=25, city="NYC", occupation="Developer")
print()


# ============================================================================
# 9. LAMBDA FUNCTIONS (Anonymous Functions)
# ============================================================================
print("=" * 70)
print("9. LAMBDA FUNCTIONS (Anonymous Functions)")
print("=" * 70)

# Regular function
def square(x):
    return x ** 2

# Lambda function (same as above)
square_lambda = lambda x: x ** 2

# Lambda with multiple parameters
add = lambda a, b: a + b
multiply = lambda x, y: x * y

print(f"Square of 5: {square(5)}")
print(f"Square (lambda) of 5: {square_lambda(5)}")
print(f"Add (lambda) 3 + 4: {add(3, 4)}")
print(f"Multiply (lambda) 3 * 4: {multiply(3, 4)}")

# Lambda with map, filter, reduce
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))

print(f"Original: {numbers}")
print(f"Squared: {squared}")
print(f"Even numbers: {evens}")
print()


# ============================================================================
# 10. RECURSIVE FUNCTIONS
# ============================================================================
print("=" * 70)
print("10. RECURSIVE FUNCTIONS")
print("=" * 70)

def factorial(n):
    """Calculate factorial using recursion"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    """Calculate nth Fibonacci number using recursion"""
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def countdown(n):
    """Countdown from n to 1"""
    if n <= 0:
        print("Blast off!")
    else:
        print(n)
        countdown(n - 1)

print(f"Factorial of 5: {factorial(5)}")
print(f"Fibonacci of 7: {fibonacci(7)}")
print("Countdown from 5:")
countdown(5)
print()


# ============================================================================
# 11. NESTED FUNCTIONS
# ============================================================================
print("=" * 70)
print("11. NESTED FUNCTIONS")
print("=" * 70)

def outer_function(text):
    """Outer function containing inner function"""
    
    def inner_function():
        """Inner function"""
        print(f"Inner: {text}")
    
    print("Outer function")
    inner_function()

outer_function("Hello from nested function!")
print()


# ============================================================================
# 12. FUNCTION RETURNING MULTIPLE VALUES
# ============================================================================
print("=" * 70)
print("12. FUNCTION RETURNING MULTIPLE VALUES")
print("=" * 70)

def arithmetic_operations(a, b):
    """Return multiple values as tuple"""
    add = a + b
    sub = a - b
    mul = a * b
    div = a / b if b != 0 else None
    return add, sub, mul, div

def get_user_info():
    """Return multiple values"""
    return "Alice", 25, "Engineer"

# Unpack multiple return values
addition, subtraction, multiplication, division = arithmetic_operations(10, 5)
print(f"10 + 5 = {addition}")
print(f"10 - 5 = {subtraction}")
print(f"10 * 5 = {multiplication}")
print(f"10 / 5 = {division}")
print()

name, age, job = get_user_info()
print(f"Name: {name}, Age: {age}, Job: {job}")
print()


# ============================================================================
# 13. HIGHER-ORDER FUNCTIONS
# ============================================================================
print("=" * 70)
print("13. HIGHER-ORDER FUNCTIONS")
print("=" * 70)

def apply_operation(func, x, y):
    """Function that takes another function as parameter"""
    return func(x, y)

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

# Pass functions as arguments
result1 = apply_operation(add, 5, 3)
result2 = apply_operation(multiply, 5, 3)

print(f"Apply add function: {result1}")
print(f"Apply multiply function: {result2}")
print()


# ============================================================================
# 14. FUNCTION WITH TYPE HINTS (Python 3.5+)
# ============================================================================
print("=" * 70)
print("14. FUNCTION WITH TYPE HINTS")
print("=" * 70)

def greet_typed(name: str) -> str:
    """Function with type hints"""
    return f"Hello, {name}!"

def calculate_area(length: float, width: float) -> float:
    """Calculate rectangle area with type hints"""
    return length * width

def process_numbers(numbers: list[int]) -> int:
    """Sum a list of numbers with type hints"""
    return sum(numbers)

print(greet_typed("Alice"))
print(f"Area: {calculate_area(5.5, 3.2)}")
print(f"Sum: {process_numbers([1, 2, 3, 4, 5])}")
print()


# ============================================================================
# 15. DOCSTRING EXAMPLES
# ============================================================================
print("=" * 70)
print("15. DOCSTRING EXAMPLES")
print("=" * 70)

def well_documented_function(param1, param2):
    """
    This is a well-documented function.
    
    Parameters:
    param1 (int): The first parameter
    param2 (str): The second parameter
    
    Returns:
    str: A formatted string with both parameters
    
    Example:
    >>> well_documented_function(42, "test")
    'Parameter 1: 42, Parameter 2: test'
    """
    return f"Parameter 1: {param1}, Parameter 2: {param2}"

result = well_documented_function(42, "Hello")
print(result)

# Access docstring
print(f"\nDocstring:\n{well_documented_function.__doc__}")
print()


# ============================================================================
# 16. SCOPE AND GLOBAL/LOCAL VARIABLES
# ============================================================================
print("=" * 70)
print("16. SCOPE AND GLOBAL/LOCAL VARIABLES")
print("=" * 70)

global_var = "I am global"

def scope_demo():
    """Demonstrate local and global scope"""
    local_var = "I am local"
    print(f"Inside function - Local: {local_var}")
    print(f"Inside function - Global: {global_var}")

def modify_global():
    """Modify global variable"""
    global global_var
    global_var = "Modified global"

scope_demo()
print(f"Outside function - Global: {global_var}")
modify_global()
print(f"After modification - Global: {global_var}")
print()


# ============================================================================
# 17. CLOSURES
# ============================================================================
print("=" * 70)
print("17. CLOSURES")
print("=" * 70)

def multiplier(n):
    """Returns a function that multiplies by n"""
    def multiply(x):
        return x * n
    return multiply

# Create closures
times2 = multiplier(2)
times3 = multiplier(3)
times5 = multiplier(5)

print(f"5 * 2 = {times2(5)}")
print(f"5 * 3 = {times3(5)}")
print(f"5 * 5 = {times5(5)}")
print()


# ============================================================================
# 18. DECORATORS (BASIC)
# ============================================================================
print("=" * 70)
print("18. DECORATORS (Basic)")
print("=" * 70)

def my_decorator(func):
    """Simple decorator"""
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    """Function with decorator"""
    print("Hello!")

say_hello()
print()


# ============================================================================
# 19. PRACTICAL EXAMPLES
# ============================================================================
print("=" * 70)
print("19. PRACTICAL EXAMPLES")
print("=" * 70)

def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

def find_max(numbers):
    """Find maximum in a list"""
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

def reverse_string(text):
    """Reverse a string"""
    return text[::-1]

# Test practical functions
print(f"Is 17 prime? {is_prime(17)}")
print(f"Is 18 prime? {is_prime(18)}")
print(f"25°C = {celsius_to_fahrenheit(25)}°F")
print(f"Max of [3, 7, 2, 9, 1]: {find_max([3, 7, 2, 9, 1])}")
print(f"Reverse 'Python': {reverse_string('Python')}")
print()


# ============================================================================
# 20. FUNCTION ANNOTATIONS AND METADATA
# ============================================================================
print("=" * 70)
print("20. FUNCTION ANNOTATIONS AND METADATA")
print("=" * 70)

def annotated_function(x: int, y: int = 10) -> int:
    """Function with annotations"""
    return x + y

# Access function metadata
print(f"Function name: {annotated_function.__name__}")
print(f"Annotations: {annotated_function.__annotations__}")
print(f"Defaults: {annotated_function.__defaults__}")
print(f"Result: {annotated_function(5)}")
print()


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 70)
print("SUMMARY - KEY CONCEPTS")
print("=" * 70)
print("""
1. Basic Functions: def function_name(): ...
2. Parameters: Pass data to functions
3. Return Values: Get results from functions
4. Default Parameters: Optional parameters with default values
5. Keyword Arguments: Call functions with named arguments
6. *args: Variable number of positional arguments
7. **kwargs: Variable number of keyword arguments
8. Lambda Functions: Anonymous one-line functions
9. Recursive Functions: Functions that call themselves
10. Nested Functions: Functions inside functions
11. Multiple Returns: Return multiple values as tuple
12. Higher-Order Functions: Functions as parameters/return values
13. Type Hints: Specify parameter and return types
14. Docstrings: Document your functions
15. Scope: Local vs Global variables
16. Closures: Inner functions with access to outer variables
17. Decorators: Modify function behavior
18. Function Metadata: Access function properties

BEST PRACTICES:
- Use descriptive function names
- Write clear docstrings
- Keep functions focused on one task
- Use type hints for clarity
- Handle edge cases
- Return early when possible
- Avoid side effects when possible
""")