"""
Day 1 Solution: Data Types Exploration
======================================

SOLUTION with detailed explanations and comprehensive examples

This solution demonstrates:
- All basic Python data types
- Type checking and introspection
- Type conversion methods
- Advanced data type concepts
- Best practices for working with different types
"""

# =============================================================================
# BASIC SOLUTION - CORE DATA TYPES
# =============================================================================

print("=== BASIC DATA TYPES SOLUTION ===\n")

# Integer - whole numbers
age = 25
print(f"Age: {age}, Type: {type(age)}")

# Float - decimal numbers
height = 5.8
print(f"Height: {height}, Type: {type(height)}")

# String - text data
name = "Python Learner"
print(f"Name: {name}, Type: {type(name)}")

# Boolean - True/False values
is_learning = True
print(f"Is Learning: {is_learning}, Type: {type(is_learning)}")

# =============================================================================
# ENHANCED SOLUTION - COMPREHENSIVE DATA TYPE EXPLORATION
# =============================================================================

print("\n" + "="*70)
print("              COMPREHENSIVE DATA TYPE EXPLORATION")
print("="*70)

# =============================================================================
# 1. NUMERIC TYPES
# =============================================================================

print("\n🔢 NUMERIC TYPES:")
print("-" * 30)

# Integer examples
whole_number = 42
negative_number = -17
big_number = 1_000_000  # Underscores for readability
print(f"Whole Number: {whole_number} ({type(whole_number).__name__})")
print(f"Negative Number: {negative_number} ({type(negative_number).__name__})")
print(f"Big Number: {big_number} ({type(big_number).__name__})")

# Float examples
decimal_number = 3.14159
scientific_notation = 1.5e6  # 1.5 × 10^6 = 1,500,000
print(f"Decimal Number: {decimal_number} ({type(decimal_number).__name__})")
print(f"Scientific Notation: {scientific_notation} ({type(scientific_notation).__name__})")

# Complex numbers (advanced)
complex_number = 3 + 4j
print(f"Complex Number: {complex_number} ({type(complex_number).__name__})")

# =============================================================================
# 2. STRING TYPES
# =============================================================================

print("\n📝 STRING TYPES:")
print("-" * 30)

# Different string creation methods
greeting = "Hello, World!"
single_quote_string = 'Python is great!'
multiline_string = """This is a
multiline string
spanning multiple lines!"""

# String with escape characters
escaped_string = "Line 1\nLine 2\tTabbed content"

# Raw string (useful for file paths, regex patterns)
raw_string = r"C:\Users\Documents\file.txt"

# Unicode string
unicode_string = "Python supports Unicode: café, naïve, 北京"

print(f"Greeting: '{greeting}' ({type(greeting).__name__})")
print(f"Single quotes: '{single_quote_string}' ({type(single_quote_string).__name__})")
print(f"Multiline: {repr(multiline_string)} ({type(multiline_string).__name__})")
print(f"Escaped: {repr(escaped_string)} ({type(escaped_string).__name__})")
print(f"Raw string: {raw_string} ({type(raw_string).__name__})")
print(f"Unicode: {unicode_string} ({type(unicode_string).__name__})")

# =============================================================================
# 3. BOOLEAN TYPES
# =============================================================================

print("\n✅ BOOLEAN TYPES:")
print("-" * 30)

# Boolean values
is_python_fun = True
is_difficult = False
print(f"Is Python fun? {is_python_fun} ({type(is_python_fun).__name__})")
print(f"Is it difficult? {is_difficult} ({type(is_difficult).__name__})")

# Boolean from comparisons
is_greater = 10 > 5
is_equal = 10 == 10
print(f"10 > 5: {is_greater} ({type(is_greater).__name__})")
print(f"10 == 10: {is_equal} ({type(is_equal).__name__})")

# =============================================================================
# 4. NONE TYPE
# =============================================================================

print("\n⚪ NONE TYPE:")
print("-" * 30)

# None represents absence of a value
nothing = None
empty_var = None
print(f"Nothing: {nothing} ({type(nothing).__name__})")
print(f"Empty variable: {empty_var} ({type(empty_var).__name__})")

# =============================================================================
# 5. COLLECTION TYPES (Preview for later days)
# =============================================================================

print("\n📦 COLLECTION TYPES (Preview):")
print("-" * 30)

# List - ordered, mutable collection
numbers_list = [1, 2, 3, 4, 5]
print(f"List: {numbers_list} ({type(numbers_list).__name__})")

# Tuple - ordered, immutable collection
coordinates = (10, 20)
print(f"Tuple: {coordinates} ({type(coordinates).__name__})")

# Dictionary - key-value pairs
person_info = {"name": "Alice", "age": 30, "city": "New York"}
print(f"Dictionary: {person_info} ({type(person_info).__name__})")

# Set - unique values
unique_numbers = {1, 2, 3, 4, 5}
print(f"Set: {unique_numbers} ({type(unique_numbers).__name__})")

# =============================================================================
# 6. TYPE CHECKING AND CONVERSION
# =============================================================================

print("\n🔄 TYPE CHECKING AND CONVERSION:")
print("-" * 30)

# Type checking with isinstance()
number = 42
text = "Hello"
print(f"Is {number} an integer? {isinstance(number, int)}")
print(f"Is {text} a string? {isinstance(text, str)}")
print(f"Is {number} a number? {isinstance(number, (int, float))}")

# Type conversion (casting)
string_number = "123"
converted_int = int(string_number)
converted_float = float(string_number)
print(f"String '{string_number}' as int: {converted_int} ({type(converted_int).__name__})")
print(f"String '{string_number}' as float: {converted_float} ({type(converted_float).__name__})")

# Converting numbers to strings
number_to_string = str(42)
float_to_string = str(3.14)
print(f"Number 42 as string: '{number_to_string}' ({type(number_to_string).__name__})")
print(f"Float 3.14 as string: '{float_to_string}' ({type(float_to_string).__name__})")

# Boolean conversions
print(f"bool(1): {bool(1)}")  # True
print(f"bool(0): {bool(0)}")  # False
print(f"bool('hello'): {bool('hello')}")  # True
print(f"bool(''): {bool('')}")  # False

# =============================================================================
# 7. ADVANCED TYPE CONCEPTS
# =============================================================================

print("\n🚀 ADVANCED TYPE CONCEPTS:")
print("-" * 30)

# Check object attributes and methods
sample_string = "Python"
print(f"String methods available: {len(dir(sample_string))} methods")
print(f"Some string methods: {[method for method in dir(sample_string) if not method.startswith('_')][:5]}")

# Memory size and identity
a = 1000
b = 1000
print(f"Variables a and b have same value: {a == b}")
print(f"Variables a and b are same object: {a is b}")  # Might be False for large numbers

# String interning (small strings and numbers are cached)
x = "hello"
y = "hello"
print(f"String variables x and y are same object: {x is y}")  # Usually True

# =============================================================================
# 8. PRACTICAL EXAMPLES
# =============================================================================

print("\n💼 PRACTICAL EXAMPLES:")
print("-" * 30)

# Example 1: User data processing
user_input = "25"  # Simulated user input (always string)
try:
    user_age = int(user_input)
    is_adult = user_age >= 18
    print(f"User age: {user_age}, Is adult: {is_adult}")
except ValueError:
    print("Invalid age entered!")

# Example 2: Data validation
def validate_data(data):
    """Validate and report data types"""
    if isinstance(data, str) and data.strip():
        return f"Valid string: '{data}'"
    elif isinstance(data, (int, float)) and data >= 0:
        return f"Valid number: {data}"
    elif isinstance(data, bool):
        return f"Boolean value: {data}"
    else:
        return f"Invalid or empty data: {data}"

# Test validation
test_data = ["Hello", 42, -5, True, "", None, 3.14]
for item in test_data:
    print(validate_data(item))

# =============================================================================
# EDUCATIONAL NOTES
# =============================================================================

print("\n" + "="*70)
print("                        LEARNING NOTES")
print("="*70)

print("""
📖 KEY CONCEPTS COVERED:

1. BASIC DATA TYPES:
   • int: Whole numbers (42, -17, 1_000_000)
   • float: Decimal numbers (3.14, 1.5e6)
   • str: Text data ("hello", 'world', '''multiline''')
   • bool: True/False values
   • NoneType: Represents absence of value (None)

2. TYPE OPERATIONS:
   • type(): Get the type of an object
   • isinstance(): Check if object is of specific type
   • Type conversion: int(), float(), str(), bool()

3. STRING FEATURES:
   • Single quotes: 'text'
   • Double quotes: "text" 
   • Triple quotes: '''multiline text'''
   • Raw strings: r"C:\path\file.txt"
   • f-strings: f"Hello {name}"

4. BOOLEAN CONTEXT:
   • Truthy values: non-zero numbers, non-empty strings, True
   • Falsy values: 0, 0.0, "", False, None, empty collections

🎯 BEST PRACTICES:
   ✅ Use descriptive variable names
   ✅ Choose appropriate data types for your data
   ✅ Validate user input and handle type errors
   ✅ Use isinstance() for type checking
   ✅ Use f-strings for string formatting
   ✅ Be aware of implicit type conversions

🚫 COMMON MISTAKES:
   ❌ Comparing different types without conversion
   ❌ Not handling ValueError in type conversion
   ❌ Using == instead of is for None comparison
   ❌ Forgetting that user input is always string
""")

print("🎉 Data types exploration complete!")
print("Next: Variables, operators, and string manipulation!")
