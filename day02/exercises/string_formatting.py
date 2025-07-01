"""
Day 2 Exercise: String Formatting Practice
==========================================

Practice different ways to format strings with variables

Instructions:
1. Practice f-string formatting
2. Use .format() method
3. Try different formatting options
"""

print("=== String Formatting Practice ===\n")

# Sample data
name = "John Doe"
age = 30
salary = 75000.50
city = "New York"
is_employed = True

print("1. F-String Formatting (Recommended):")
print(f"Hello, {name}!")
print(f"You are {age} years old.")
print(f"Your salary is ${salary:,.2f}")
print(f"You live in {city}.")
print(f"Employment status: {is_employed}")

print(f"\nDetailed info: {name} is {age} years old, earns ${salary:,.2f} per year, and lives in {city}.")

print("\n2. Format Method:")
print("Hello, {}!".format(name))
print("You are {} years old.".format(age))
print("Your salary is ${:,.2f}".format(salary))

# Named placeholders
print("Name: {person_name}, Age: {person_age}".format(person_name=name, person_age=age))

print("\n3. Advanced F-String Formatting:")

# Number formatting
pi = 3.14159265359
large_number = 1234567890

print(f"Pi rounded to 2 decimals: {pi:.2f}")
print(f"Pi rounded to 4 decimals: {pi:.4f}")
print(f"Large number with commas: {large_number:,}")
print(f"Large number in scientific notation: {large_number:.2e}")

# Percentage formatting
growth_rate = 0.1234
print(f"Growth rate: {growth_rate:.2%}")

# String alignment and padding
print(f"Left aligned: '{name:<20}'")
print(f"Right aligned: '{name:>20}'")
print(f"Center aligned: '{name:^20}'")

# Date formatting (bonus)
from datetime import datetime
now = datetime.now()
print(f"Current date and time: {now:%Y-%m-%d %H:%M:%S}")
print(f"Just the date: {now:%B %d, %Y}")

print("\n4. Multi-line F-Strings:")
report = f"""
Employee Report
===============
Name: {name}
Age: {age}
Salary: ${salary:,.2f}
Location: {city}
Status: {'Active' if is_employed else 'Inactive'}
"""
print(report)

print("\n5. Expression in F-Strings:")
x = 10
y = 20
print(f"Sum: {x} + {y} = {x + y}")
print(f"Is x greater than y? {x > y}")
print(f"Square of x: {x}² = {x**2}")

# Mathematical expressions
print(f"Area of circle (r=5): π × 5² = {3.14159 * 5**2:.2f}")

print("\n🎉 String formatting practice complete!")
