"""
Day 2 Exercise: Type Practice
============================

Use type() to check data types and perform arithmetic operations

Instructions:
1. Create variables of different types
2. Check their types using type()
3. Practice type casting
4. Handle type conversion errors
"""

print("=== Type Practice and Casting ===\n")

# Create variables of different types
name = "Alice"
age = 28
height = 5.7
is_student = True
account_balance = 1500.50

# Check types
print("1. Checking Data Types:")
print(f"name = '{name}' → type: {type(name).__name__}")
print(f"age = {age} → type: {type(age).__name__}")
print(f"height = {height} → type: {type(height).__name__}")
print(f"is_student = {is_student} → type: {type(is_student).__name__}")
print(f"account_balance = {account_balance} → type: {type(account_balance).__name__}")

print("\n2. Type Casting Examples:")

# String to number conversions
str_number = "42"
str_float = "3.14"
print(f"'{str_number}' → int: {int(str_number)}")
print(f"'{str_float}' → float: {float(str_float)}")

# Number to string conversions
print(f"{age} → string: '{str(age)}'")
print(f"{height} → string: '{str(height)}'")

# Boolean conversions
print(f"True → int: {int(True)}")
print(f"False → int: {int(False)}")
print(f"0 → bool: {bool(0)}")
print(f"1 → bool: {bool(1)}")
print(f"'' → bool: {bool('')}")
print(f"'hello' → bool: {bool('hello')}")

print("\n3. Arithmetic with Different Types:")

# Mixed arithmetic
result1 = age + int(True)  # int + bool
result2 = height * 2       # float * int
result3 = account_balance / age  # float / int

print(f"age + True = {age} + {int(True)} = {result1}")
print(f"height * 2 = {height} * 2 = {result2}")
print(f"account_balance / age = {account_balance} / {age} = {result3:.2f}")

print("\n4. Error Handling in Type Conversion:")

# Safe type conversion with error handling
test_strings = ["123", "45.67", "hello", ""]

for test_str in test_strings:
    try:
        as_int = int(test_str)
        print(f"'{test_str}' → int: {as_int}")
    except ValueError:
        print(f"'{test_str}' → int: Cannot convert to integer")
    
    try:
        as_float = float(test_str)
        print(f"'{test_str}' → float: {as_float}")
    except ValueError:
        print(f"'{test_str}' → float: Cannot convert to float")
    print()

print("🎉 Type practice complete!")
