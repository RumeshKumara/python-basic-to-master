"""
Python String Examples - Comprehensive Guide
All string operations with detailed explanations
"""

# =============================================================================
# 1. STRING CREATION
# =============================================================================

print("=" * 60)
print("1. STRING CREATION")
print("=" * 60)

# Single quotes
string1 = 'Hello, World!'
print(f"Single quotes: {string1}")

# Double quotes
string2 = "Python Programming"
print(f"Double quotes: {string2}")

# Triple quotes (multi-line strings)
string3 = '''This is a
multi-line
string'''
print(f"Triple quotes:\n{string3}")

# Triple double quotes
string4 = """Another way to
create multi-line
strings"""
print(f"Triple double quotes:\n{string4}")

# Empty string
empty_string = ""
print(f"Empty string: '{empty_string}'")

# =============================================================================
# 2. STRING CONCATENATION
# =============================================================================

print("\n" + "=" * 60)
print("2. STRING CONCATENATION")
print("=" * 60)

# Using + operator
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(f"Using +: {full_name}")

# Using join() method
words = ["Python", "is", "awesome"]
sentence = " ".join(words)
print(f"Using join(): {sentence}")

# Using f-strings (Python 3.6+)
age = 25
message = f"My name is {full_name} and I am {age} years old"
print(f"Using f-strings: {message}")

# Using format() method
message2 = "My name is {} and I am {} years old".format(full_name, age)
print(f"Using format(): {message2}")

# =============================================================================
# 3. STRING INDEXING AND SLICING
# =============================================================================

print("\n" + "=" * 60)
print("3. STRING INDEXING AND SLICING")
print("=" * 60)

text = "Python Programming"

# Indexing (accessing individual characters)
print(f"First character: {text[0]}")
print(f"Last character: {text[-1]}")
print(f"5th character: {text[4]}")

# Slicing [start:end:step]
print(f"First 6 characters: {text[0:6]}")
print(f"From index 7 to end: {text[7:]}")
print(f"From start to index 6: {text[:6]}")
print(f"Every 2nd character: {text[::2]}")
print(f"Reverse string: {text[::-1]}")
print(f"Characters from index 2 to 8: {text[2:9]}")

# =============================================================================
# 4. STRING LENGTH
# =============================================================================

print("\n" + "=" * 60)
print("4. STRING LENGTH")
print("=" * 60)

sample = "Hello, Python!"
length = len(sample)
print(f"String: '{sample}'")
print(f"Length: {length}")

# =============================================================================
# 5. STRING METHODS - CASE CONVERSION
# =============================================================================

print("\n" + "=" * 60)
print("5. CASE CONVERSION METHODS")
print("=" * 60)

text = "Python Programming"

print(f"Original: {text}")
print(f"upper(): {text.upper()}")           # Convert to uppercase
print(f"lower(): {text.lower()}")           # Convert to lowercase
print(f"capitalize(): {text.capitalize()}") # First char uppercase
print(f"title(): {text.title()}")           # Title case
print(f"swapcase(): {text.swapcase()}")     # Swap case

# =============================================================================
# 6. STRING METHODS - SEARCHING AND CHECKING
# =============================================================================

print("\n" + "=" * 60)
print("6. SEARCHING AND CHECKING METHODS")
print("=" * 60)

text = "Python Programming is fun and Python is powerful"

# find() - returns index or -1 if not found
print(f"find('Python'): {text.find('Python')}")
print(f"find('Java'): {text.find('Java')}")

# index() - returns index or raises ValueError if not found
print(f"index('Programming'): {text.index('Programming')}")

# count() - count occurrences
print(f"count('Python'): {text.count('Python')}")
print(f"count('is'): {text.count('is')}")

# startswith() and endswith()
print(f"startswith('Python'): {text.startswith('Python')}")
print(f"endswith('powerful'): {text.endswith('powerful')}")

# in operator
print(f"'fun' in text: {'fun' in text}")
print(f"'Java' in text: {'Java' in text}")

# =============================================================================
# 7. STRING METHODS - CHECKING STRING TYPES
# =============================================================================

print("\n" + "=" * 60)
print("7. STRING TYPE CHECKING METHODS")
print("=" * 60)

# isalpha() - all alphabetic
print(f"'Hello'.isalpha(): {'Hello'.isalpha()}")
print(f"'Hello123'.isalpha(): {'Hello123'.isalpha()}")

# isdigit() - all digits
print(f"'12345'.isdigit(): {'12345'.isdigit()}")
print(f"'123abc'.isdigit(): {'123abc'.isdigit()}")

# isalnum() - alphanumeric
print(f"'Hello123'.isalnum(): {'Hello123'.isalnum()}")
print(f"'Hello 123'.isalnum(): {'Hello 123'.isalnum()}")

# isspace() - all whitespace
print(f"'   '.isspace(): {'   '.isspace()}")
print(f"'Hello'.isspace(): {'Hello'.isspace()}")

# isupper() and islower()
print(f"'HELLO'.isupper(): {'HELLO'.isupper()}")
print(f"'hello'.islower(): {'hello'.islower()}")

# istitle()
print(f"'Python Programming'.istitle(): {'Python Programming'.istitle()}")
print(f"'python programming'.istitle(): {'python programming'.istitle()}")

# =============================================================================
# 8. STRING METHODS - TRIMMING AND PADDING
# =============================================================================

print("\n" + "=" * 60)
print("8. TRIMMING AND PADDING METHODS")
print("=" * 60)

text = "   Hello, Python!   "

# strip() - remove leading and trailing whitespace
print(f"strip(): '{text.strip()}'")

# lstrip() - remove leading whitespace
print(f"lstrip(): '{text.lstrip()}'")

# rstrip() - remove trailing whitespace
print(f"rstrip(): '{text.rstrip()}'")

# Remove specific characters
text2 = "###Python###"
print(f"strip('#'): '{text2.strip('#')}'")

# center() - center align
print(f"center(30): '{text.strip().center(30)}'")

# ljust() - left justify
print(f"ljust(30): '{text.strip().ljust(30)}'")

# rjust() - right justify
print(f"rjust(30): '{text.strip().rjust(30)}'")

# zfill() - pad with zeros
number = "42"
print(f"zfill(5): '{number.zfill(5)}'")

# =============================================================================
# 9. STRING METHODS - SPLITTING AND JOINING
# =============================================================================

print("\n" + "=" * 60)
print("9. SPLITTING AND JOINING METHODS")
print("=" * 60)

# split() - split string into list
text = "Python is a powerful programming language"
words = text.split()
print(f"split(): {words}")

# split with delimiter
csv_data = "apple,banana,orange,grape"
fruits = csv_data.split(',')
print(f"split(','): {fruits}")

# splitlines() - split by line breaks
multiline = "Line 1\nLine 2\nLine 3"
lines = multiline.splitlines()
print(f"splitlines(): {lines}")

# join() - join list into string
joined = " ".join(words)
print(f"join(): {joined}")

# partition() - split into 3-tuple
text = "Python:Programming:Language"
result = text.partition(':')
print(f"partition(':'): {result}")

# =============================================================================
# 10. STRING METHODS - REPLACING
# =============================================================================

print("\n" + "=" * 60)
print("10. REPLACING METHODS")
print("=" * 60)

text = "Python is great. Python is easy. Python is powerful."

# replace() - replace substring
new_text = text.replace("Python", "JavaScript")
print(f"replace('Python', 'JavaScript'): {new_text}")

# replace with count limit
new_text2 = text.replace("Python", "Java", 2)
print(f"replace('Python', 'Java', 2): {new_text2}")

# translate() - character mapping
translation_table = str.maketrans("aeiou", "12345")
text2 = "hello world"
print(f"translate(): {text2.translate(translation_table)}")

# =============================================================================
# 11. STRING FORMATTING
# =============================================================================

print("\n" + "=" * 60)
print("11. STRING FORMATTING")
print("=" * 60)

name = "Alice"
age = 30
height = 5.6

# Old style (%)
print("Old style: My name is %s, I am %d years old" % (name, age))

# format() method
print("format(): My name is {}, I am {} years old".format(name, age))
print("format() with index: My name is {0}, I am {1} years old, yes {0}!".format(name, age))
print("format() with names: My name is {n}, I am {a} years old".format(n=name, a=age))

# f-strings (Python 3.6+)
print(f"f-string: My name is {name}, I am {age} years old")
print(f"f-string with expression: Next year I'll be {age + 1}")
print(f"f-string with format spec: Height: {height:.1f} feet")

# Format specifications
number = 123.456789
print(f"Float with 2 decimals: {number:.2f}")
print(f"Percentage: {0.85:.1%}")
print(f"Scientific notation: {number:.2e}")
print(f"Padding: {number:10.2f}")

# =============================================================================
# 12. STRING ESCAPE CHARACTERS
# =============================================================================

print("\n" + "=" * 60)
print("12. ESCAPE CHARACTERS")
print("=" * 60)

# Common escape sequences
print("Newline: Hello\\nWorld")
print("Hello\nWorld")

print("\nTab: Hello\\tWorld")
print("Hello\tWorld")

print("\nBackslash: C:\\\\Users\\\\Documents")
print("C:\\Users\\Documents")

print("\nSingle quote: It\\'s a beautiful day")
print("It's a beautiful day")

print("\nDouble quote: She said \\\"Hello\\\"")
print("She said \"Hello\"")

# Raw strings (ignore escape characters)
print("\nRaw string: r'C:\\Users\\Documents'")
print(r'C:\Users\Documents')

# =============================================================================
# 13. STRING ITERATION
# =============================================================================

print("\n" + "=" * 60)
print("13. STRING ITERATION")
print("=" * 60)

text = "Python"

# Iterate through characters
print("Characters in 'Python':")
for char in text:
    print(char, end=' ')
print()

# Iterate with index
print("\nWith index:")
for i, char in enumerate(text):
    print(f"Index {i}: {char}")

# =============================================================================
# 14. STRING COMPARISON
# =============================================================================

print("\n" + "=" * 60)
print("14. STRING COMPARISON")
print("=" * 60)

str1 = "apple"
str2 = "banana"
str3 = "apple"

print(f"'{str1}' == '{str2}': {str1 == str2}")
print(f"'{str1}' == '{str3}': {str1 == str3}")
print(f"'{str1}' < '{str2}': {str1 < str2}")  # Lexicographical comparison
print(f"'{str1}' > '{str2}': {str1 > str2}")

# Case-insensitive comparison
str4 = "APPLE"
print(f"'{str1}' == '{str4}': {str1 == str4}")
print(f"'{str1}'.lower() == '{str4}'.lower(): {str1.lower() == str4.lower()}")

# =============================================================================
# 15. STRING MULTIPLICATION
# =============================================================================

print("\n" + "=" * 60)
print("15. STRING MULTIPLICATION")
print("=" * 60)

# Repeat string
repeat = "Python! "
print(f"'{repeat}' * 3: {repeat * 3}")

# Create patterns
print("=" * 40)
print("*" * 20)
print("-" * 30)

# =============================================================================
# 16. ADVANCED STRING OPERATIONS
# =============================================================================

print("\n" + "=" * 60)
print("16. ADVANCED STRING OPERATIONS")
print("=" * 60)

# String reversal
text = "Python"
reversed_text = text[::-1]
print(f"Reverse '{text}': {reversed_text}")

# Palindrome check
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

word1 = "radar"
word2 = "python"
print(f"Is '{word1}' a palindrome? {is_palindrome(word1)}")
print(f"Is '{word2}' a palindrome? {is_palindrome(word2)}")

# Remove duplicates while preserving order
def remove_duplicates(s):
    seen = set()
    result = []
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)

text = "programming"
print(f"Remove duplicates from '{text}': {remove_duplicates(text)}")

# Count vowels and consonants
def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    v_count = sum(1 for char in s if char in vowels)
    c_count = sum(1 for char in s if char.isalpha() and char not in vowels)
    return v_count, c_count

text = "Python Programming"
v, c = count_vowels_consonants(text)
print(f"In '{text}': Vowels = {v}, Consonants = {c}")

# =============================================================================
# 17. STRING ENCODING AND DECODING
# =============================================================================

print("\n" + "=" * 60)
print("17. STRING ENCODING AND DECODING")
print("=" * 60)

text = "Python Programming"

# Encode to bytes
encoded = text.encode('utf-8')
print(f"Encoded (UTF-8): {encoded}")

# Decode back to string
decoded = encoded.decode('utf-8')
print(f"Decoded: {decoded}")

# Different encodings
encoded_ascii = text.encode('ascii')
print(f"Encoded (ASCII): {encoded_ascii}")

# =============================================================================
# 18. STRING IMMUTABILITY
# =============================================================================

print("\n" + "=" * 60)
print("18. STRING IMMUTABILITY")
print("=" * 60)

original = "Python"
print(f"Original string: {original}")
print(f"ID of original: {id(original)}")

# Strings are immutable - this creates a new string
modified = original.upper()
print(f"Modified string: {modified}")
print(f"ID of modified: {id(modified)}")
print(f"Original unchanged: {original}")

# Attempting to modify raises an error (uncomment to see)
# original[0] = 'J'  # TypeError: 'str' object does not support item assignment

# =============================================================================
# 19. COMMON STRING USE CASES
# =============================================================================

print("\n" + "=" * 60)
print("19. COMMON STRING USE CASES")
print("=" * 60)

# Email validation (simple)
email = "user@example.com"
is_valid_email = "@" in email and "." in email.split("@")[1]
print(f"Is '{email}' a valid email? {is_valid_email}")

# Extract file extension
filename = "document.pdf"
extension = filename.split('.')[-1]
print(f"File extension of '{filename}': {extension}")

# Title formatting
title = "the great python programming tutorial"
formatted_title = title.title()
print(f"Formatted title: {formatted_title}")

# URL slug creation
title = "Python Programming Tutorial 2024"
slug = title.lower().replace(" ", "-")
print(f"URL slug: {slug}")

# Phone number formatting
phone = "1234567890"
formatted_phone = f"({phone[:3]}) {phone[3:6]}-{phone[6:]}"
print(f"Formatted phone: {formatted_phone}")

# =============================================================================
# 20. STRING METHODS SUMMARY TABLE
# =============================================================================

print("\n" + "=" * 60)
print("20. STRING METHODS SUMMARY")
print("=" * 60)

print("""
CASE CONVERSION:
- upper()        : Convert to uppercase
- lower()        : Convert to lowercase
- capitalize()   : First character uppercase
- title()        : Title case
- swapcase()     : Swap case

SEARCHING:
- find()         : Find substring (returns index or -1)
- index()        : Find substring (raises error if not found)
- count()        : Count occurrences
- startswith()   : Check if starts with substring
- endswith()     : Check if ends with substring

CHECKING:
- isalpha()      : All alphabetic
- isdigit()      : All digits
- isalnum()      : Alphanumeric
- isspace()      : All whitespace
- isupper()      : All uppercase
- islower()      : All lowercase

TRIMMING:
- strip()        : Remove leading/trailing whitespace
- lstrip()       : Remove leading whitespace
- rstrip()       : Remove trailing whitespace

SPLITTING:
- split()        : Split into list
- splitlines()   : Split by line breaks
- partition()    : Split into 3-tuple

REPLACING:
- replace()      : Replace substring
- translate()    : Character mapping

FORMATTING:
- center()       : Center align
- ljust()        : Left justify
- rjust()        : Right justify
- zfill()        : Pad with zeros
- format()       : Format string
""")

print("\n" + "=" * 60)
print("STRING EXAMPLES COMPLETE!")
print("=" * 60)
