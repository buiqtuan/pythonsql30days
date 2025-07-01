"""
Day 2 Solution: Calculator Program
=================================

SOLUTION with detailed explanations and enhanced features

This solution demonstrates:
- User input handling and validation
- Type conversion and error handling
- Mathematical operations
- String formatting for output
- Advanced calculator features
"""

# =============================================================================
# BASIC SOLUTION
# =============================================================================

print("=== BASIC CALCULATOR SOLUTION ===")

# Get input from user
print("Enter two numbers to perform calculations:")

try:
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

except ValueError:
    print("Error: Please enter valid numbers!")

print(f"\n🎉 Basic calculator complete!")

# =============================================================================
# ENHANCED SOLUTION WITH ADVANCED FEATURES
# =============================================================================

import math

def enhanced_calculator():
    """Enhanced calculator with multiple operations and better error handling"""
    
    print("\n" + "="*60)
    print("              ENHANCED CALCULATOR SOLUTION")
    print("="*60)
    
    def get_number(prompt):
        """Get a valid number from user with error handling"""
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("❌ Invalid input! Please enter a valid number.")

    def safe_divide(a, b):
        """Safely divide two numbers"""
        if b == 0:
            return None, "Cannot divide by zero!"
        return a / b, None

    def safe_root(a, n=2):
        """Safely calculate nth root"""
        if a < 0 and n % 2 == 0:
            return None, "Cannot calculate even root of negative number!"
        if n == 0:
            return None, "Root index cannot be zero!"
        return a ** (1/n), None

    # Get numbers from user
    print("🔢 Enter two numbers for calculations:")
    num1 = get_number("Enter first number: ")
    num2 = get_number("Enter second number: ")
    
    print(f"\n📊 CALCULATION RESULTS FOR {num1} AND {num2}")
    print("="*50)
    
    # Basic arithmetic operations
    print("\n🧮 BASIC OPERATIONS:")
    print(f"Addition:       {num1} + {num2} = {num1 + num2}")
    print(f"Subtraction:    {num1} - {num2} = {num1 - num2}")
    print(f"Multiplication: {num1} × {num2} = {num1 * num2}")
    
    # Safe division
    division_result, division_error = safe_divide(num1, num2)
    if division_error:
        print(f"Division:       {num1} ÷ {num2} = {division_error}")
    else:
        print(f"Division:       {num1} ÷ {num2} = {division_result}")
    
    # Modulus (remainder)
    if num2 != 0:
        print(f"Modulus:        {num1} % {num2} = {num1 % num2}")
    
    # Power operations
    print(f"\n⚡ POWER OPERATIONS:")
    print(f"Power:          {num1} ^ {num2} = {num1 ** num2}")
    print(f"Square of num1: {num1}² = {num1 ** 2}")
    print(f"Square of num2: {num2}² = {num2 ** 2}")
    
    # Root operations
    sqrt1_result, sqrt1_error = safe_root(num1, 2)
    sqrt2_result, sqrt2_error = safe_root(num2, 2)
    
    print(f"\n🌱 ROOT OPERATIONS:")
    if sqrt1_error:
        print(f"Square root of {num1}: {sqrt1_error}")
    else:
        print(f"Square root of {num1}: √{num1} = {sqrt1_result}")
    
    if sqrt2_error:
        print(f"Square root of {num2}: {sqrt2_error}")
    else:
        print(f"Square root of {num2}: √{num2} = {sqrt2_result}")
    
    # Advanced mathematical functions
    print(f"\n🔬 ADVANCED OPERATIONS:")
    print(f"Absolute values: |{num1}| = {abs(num1)}, |{num2}| = {abs(num2)}")
    print(f"Maximum:        max({num1}, {num2}) = {max(num1, num2)}")
    print(f"Minimum:        min({num1}, {num2}) = {min(num1, num2)}")
    
    # Statistical calculations
    print(f"\n📈 STATISTICAL CALCULATIONS:")
    average = (num1 + num2) / 2
    print(f"Average (mean): ({num1} + {num2}) ÷ 2 = {average}")
    print(f"Range:          |{num1} - {num2}| = {abs(num1 - num2)}")
    
    # Geometric mean (if both numbers are positive)
    if num1 > 0 and num2 > 0:
        geometric_mean = math.sqrt(num1 * num2)
        print(f"Geometric mean: √({num1} × {num2}) = {geometric_mean}")
    else:
        print("Geometric mean: Not applicable (requires positive numbers)")
    
    # Trigonometric functions (treating numbers as radians)
    print(f"\n📐 TRIGONOMETRIC FUNCTIONS (in radians):")
    print(f"sin({num1}) = {math.sin(num1):.4f}")
    print(f"cos({num1}) = {math.cos(num1):.4f}")
    print(f"tan({num1}) = {math.tan(num1):.4f}")
    
    # Logarithmic functions
    print(f"\n📊 LOGARITHMIC FUNCTIONS:")
    if num1 > 0:
        print(f"ln({num1}) = {math.log(num1):.4f}")
        print(f"log₁₀({num1}) = {math.log10(num1):.4f}")
    else:
        print(f"ln({num1}) = Undefined (requires positive number)")
        print(f"log₁₀({num1}) = Undefined (requires positive number)")
    
    if num2 > 0:
        print(f"ln({num2}) = {math.log(num2):.4f}")
        print(f"log₁₀({num2}) = {math.log10(num2):.4f}")
    else:
        print(f"ln({num2}) = Undefined (requires positive number)")
        print(f"log₁₀({num2}) = Undefined (requires positive number)")

def format_demonstration():
    """Demonstrate various number formatting options"""
    
    print("\n" + "="*60)
    print("              NUMBER FORMATTING DEMONSTRATION")
    print("="*60)
    
    # Sample numbers for formatting
    large_number = 1234567.89012
    small_number = 0.00012345
    percentage = 0.1234
    
    print(f"\n🎨 FORMATTING EXAMPLES:")
    print(f"Original number: {large_number}")
    print(f"2 decimal places: {large_number:.2f}")
    print(f"With thousands separator: {large_number:,.2f}")
    print(f"In scientific notation: {large_number:.3e}")
    print(f"As percentage: {percentage:.2%}")
    
    print(f"\n📏 ALIGNMENT AND PADDING:")
    numbers = [1, 12, 123, 1234]
    for num in numbers:
        print(f"Number: {num:>6}")  # Right-aligned, width 6
    
    print(f"\n💰 CURRENCY FORMATTING:")
    prices = [9.99, 149.50, 1299.99]
    for price in prices:
        print(f"Price: ${price:>8.2f}")

def comprehensive_calculator_demo():
    """Run comprehensive calculator demonstrations"""
    
    print("\n" + "="*60)
    print("              COMPREHENSIVE CALCULATOR DEMO")
    print("="*60)
    
    # Predefined test cases
    test_cases = [
        (10, 3),
        (15.5, 4.2),
        (-8, 2),
        (100, 0),  # Division by zero case
        (16, 4),   # Perfect squares
    ]
    
    for i, (a, b) in enumerate(test_cases, 1):
        print(f"\n📋 TEST CASE {i}: a = {a}, b = {b}")
        print("-" * 30)
        
        # Basic operations
        print(f"Addition: {a} + {b} = {a + b}")
        print(f"Subtraction: {a} - {b} = {a - b}")
        print(f"Multiplication: {a} × {b} = {a * b}")
        
        # Safe division
        if b != 0:
            print(f"Division: {a} ÷ {b} = {a / b:.4f}")
            print(f"Floor division: {a} // {b} = {a // b}")
            print(f"Modulus: {a} % {b} = {a % b}")
        else:
            print(f"Division: {a} ÷ {b} = Cannot divide by zero!")
        
        print(f"Power: {a} ^ {b} = {a ** b}")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    # Run the enhanced calculator
    enhanced_calculator()
    
    # Show formatting demonstration
    format_demonstration()
    
    # Show comprehensive demo
    comprehensive_calculator_demo()
    
    print("\n" + "="*60)
    print("                    LEARNING SUMMARY")
    print("="*60)
    
    print("""
📖 KEY CONCEPTS DEMONSTRATED:

1. USER INPUT HANDLING:
   • input() function always returns string
   • Type conversion with int(), float()
   • Error handling with try/except
   • Input validation loops

2. MATHEMATICAL OPERATIONS:
   • Basic arithmetic: +, -, *, /, %, **
   • Floor division: //
   • Built-in functions: abs(), max(), min()
   • Math module: sqrt(), sin(), cos(), log()

3. ERROR HANDLING:
   • Division by zero checks
   • ValueError for invalid input
   • Graceful error messages

4. STRING FORMATTING:
   • f-strings for modern formatting
   • Number formatting: :.2f, :,.2f, :.2e, :.2%
   • Alignment and padding: :>, :<, :^

🎯 BEST PRACTICES:
   ✅ Always validate user input
   ✅ Handle division by zero
   ✅ Use descriptive variable names
   ✅ Provide clear error messages
   ✅ Format numbers appropriately
   ✅ Use functions for reusable code

🚀 NEXT STEPS:
   • Learn conditional statements (if/else)
   • Explore loops for repetitive operations
   • Build more complex calculators
   • Add menu-driven interfaces
""")
    
    print("🎉 Calculator solution complete!")
    print("Next: Control structures and decision making!")
