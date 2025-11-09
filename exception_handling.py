"""
Exception Handling in Python
============================
Comprehensive examples demonstrating exception handling concepts
"""

# ============================================
# 1. BASIC TRY-EXCEPT
# ============================================
print("=" * 50)
print("1. Basic Try-Except")
print("=" * 50)

try:
    result = 10 / 0  # This will raise ZeroDivisionError
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
print()


# ============================================
# 2. MULTIPLE EXCEPT BLOCKS
# ============================================
print("=" * 50)
print("2. Multiple Except Blocks")
print("=" * 50)

def divide_numbers(a, b):
    try:
        result = a / b
        print(f"Result: {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed!")
    except TypeError:
        print("Error: Please provide numeric values!")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")

# Test cases
divide_numbers(10, 2)      # Works fine
divide_numbers(10, 0)      # ZeroDivisionError
divide_numbers(10, "a")    # TypeError
print()


# ============================================
# 3. TRY-EXCEPT-ELSE-FINALLY
# ============================================
print("=" * 50)
print("3. Try-Except-Else-Finally")
print("=" * 50)

def read_file(filename):
    try:
        file = open(filename, 'r')
        content = file.read()
        print(f"File content: {content}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
    except PermissionError:
        print(f"Error: Permission denied to read '{filename}'!")
    else:
        print("File read successfully!")
    finally:
        print("Execution completed (finally block always runs)")
        try:
            file.close()
            print("File closed successfully")
        except:
            pass

# Test with non-existent file
read_file("nonexistent.txt")
print()


# ============================================
# 4. CATCHING EXCEPTION OBJECT
# ============================================
print("=" * 50)
print("4. Catching Exception Object")
print("=" * 50)

try:
    numbers = [1, 2, 3]
    print(numbers[10])  # IndexError
except IndexError as e:
    print(f"Error occurred: {e}")
    print(f"Error type: {type(e).__name__}")
print()


# ============================================
# 5. RAISING EXCEPTIONS
# ============================================
print("=" * 50)
print("5. Raising Exceptions")
print("=" * 50)

def validate_age(age):
    """Validate age and raise exception if invalid"""
    if age < 0:
        raise ValueError("Age cannot be negative!")
    elif age > 150:
        raise ValueError("Age seems unrealistic!")
    elif not isinstance(age, (int, float)):
        raise TypeError("Age must be a number!")
    else:
        print(f"Valid age: {age}")

# Test cases
try:
    validate_age(25)      # Valid
    validate_age(-5)      # ValueError
except ValueError as e:
    print(f"Validation Error: {e}")

try:
    validate_age("twenty")  # TypeError
except TypeError as e:
    print(f"Type Error: {e}")
print()


# ============================================
# 6. CUSTOM EXCEPTIONS
# ============================================
print("=" * 50)
print("6. Custom Exceptions")
print("=" * 50)

class InsufficientBalanceError(Exception):
    """Custom exception for insufficient balance"""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.message = f"Insufficient balance! Available: ${balance}, Required: ${amount}"
        super().__init__(self.message)

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError(self.balance, amount)
        self.balance -= amount
        print(f"Withdrawn ${amount}. New balance: ${self.balance}")
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive!")
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

# Test custom exception
account = BankAccount(100)
try:
    account.deposit(50)
    account.withdraw(80)
    account.withdraw(100)  # This will raise InsufficientBalanceError
except InsufficientBalanceError as e:
    print(f"Transaction Failed: {e.message}")
except ValueError as e:
    print(f"Invalid Operation: {e}")
print()


# ============================================
# 7. NESTED TRY-EXCEPT
# ============================================
print("=" * 50)
print("7. Nested Try-Except")
print("=" * 50)

def process_data(data):
    try:
        print(f"Processing data: {data}")
        
        # Outer try block
        try:
            # Convert to integer
            number = int(data)
            
            # Inner try block
            try:
                result = 100 / number
                print(f"Result: 100 / {number} = {result}")
            except ZeroDivisionError:
                print("Inner exception: Cannot divide by zero!")
        
        except ValueError:
            print("Middle exception: Invalid number format!")
    
    except Exception as e:
        print(f"Outer exception: {e}")

# Test cases
process_data("10")    # Works fine
process_data("0")     # ZeroDivisionError
process_data("abc")   # ValueError
print()


# ============================================
# 8. EXCEPTION CHAINING
# ============================================
print("=" * 50)
print("8. Exception Chaining")
print("=" * 50)

def calculate_average(numbers):
    try:
        if not numbers:
            raise ValueError("List cannot be empty!")
        total = sum(numbers)
        average = total / len(numbers)
        return average
    except TypeError as e:
        # Chain exceptions using 'from'
        raise ValueError("Invalid data type in list") from e

try:
    result = calculate_average([1, 2, "three", 4])
except ValueError as e:
    print(f"Error: {e}")
    print(f"Original cause: {e.__cause__}")
print()


# ============================================
# 9. CONTEXT MANAGER (WITH STATEMENT)
# ============================================
print("=" * 50)
print("9. Context Manager (Better Exception Handling)")
print("=" * 50)

# Using 'with' statement for automatic resource management
def safe_file_operation():
    try:
        with open("test_file.txt", "w") as file:
            file.write("Hello, World!")
            print("File written successfully")
        # File is automatically closed here, even if exception occurs
    except IOError as e:
        print(f"File operation failed: {e}")

safe_file_operation()
print()


# ============================================
# 10. PRACTICAL EXAMPLE: USER INPUT VALIDATION
# ============================================
print("=" * 50)
print("10. Practical Example: User Input Validation")
print("=" * 50)

def get_valid_number(prompt, min_value=None, max_value=None):
    """Get and validate numeric input from user"""
    while True:
        try:
            # For demonstration, we'll use predefined values
            # In real scenario, use: value = input(prompt)
            value = "25"  # Simulated input
            number = float(value)
            
            if min_value is not None and number < min_value:
                raise ValueError(f"Number must be at least {min_value}")
            
            if max_value is not None and number > max_value:
                raise ValueError(f"Number must be at most {max_value}")
            
            print(f"Valid input received: {number}")
            return number
        
        except ValueError as e:
            print(f"Invalid input: {e}")
            break  # In real scenario, continue the loop
        except KeyboardInterrupt:
            print("\nOperation cancelled by user")
            break

# Example usage
get_valid_number("Enter age: ", min_value=0, max_value=120)
print()


# ============================================
# SUMMARY
# ============================================
print("=" * 50)
print("EXCEPTION HANDLING BEST PRACTICES")
print("=" * 50)
print("""
1. Catch specific exceptions rather than generic Exception
2. Use finally block for cleanup operations
3. Don't use exceptions for flow control
4. Log exceptions for debugging
5. Create custom exceptions for domain-specific errors
6. Use context managers (with statement) for resources
7. Don't catch exceptions silently (empty except)
8. Re-raise exceptions when you can't handle them properly
9. Use else block for code that should run only if no exception
10. Keep try blocks small and focused
""")
