"""
Day 2 Exercise: Calculator Program
=================================

Build calc.py that takes two numbers and displays sum, product, and average

Instructions:
1. Get two numbers from user input
2. Calculate sum, product, and average
3. Display results with proper formatting
"""

# Get input from user
print("=== Simple Calculator ===")
print("Enter two numbers to perform calculations:")

# Input and convert to float for decimal support
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform calculations
sum_result = num1 + num2
product_result = num1 * num2
average_result = (num1 + num2) / 2

# Display results using f-strings
print(f"\n=== Results ===")
print(f"Number 1: {num1}")
print(f"Number 2: {num2}")
print(f"Sum: {num1} + {num2} = {sum_result}")
print(f"Product: {num1} × {num2} = {product_result}")
print(f"Average: ({num1} + {num2}) ÷ 2 = {average_result}")

# Additional calculations
difference = num1 - num2
print(f"Difference: {num1} - {num2} = {difference}")

# Division with error handling
if num2 != 0:
    division_result = num1 / num2
    print(f"Division: {num1} ÷ {num2} = {division_result}")
else:
    print("Division: Cannot divide by zero!")

print(f"\n🎉 Calculator complete!")
