"""
Day 3 Solution: Even/Odd Number Checker
=======================================

SOLUTION with comprehensive number analysis and enhanced features

This solution demonstrates:
- Conditional statements (if/elif/else)
- Modulus operator for even/odd checking
- Mathematical calculations and analysis
- Input validation and error handling
- Advanced number properties checking
"""

# =============================================================================
# BASIC SOLUTION
# =============================================================================

print("=== BASIC EVEN/ODD CHECKER SOLUTION ===")

try:
    number = int(input("Enter an integer: "))
    
    # Check if even or odd using modulus operator
    if number % 2 == 0:
        print(f"{number} is EVEN")
        print("📊 Even numbers are divisible by 2!")
    else:
        print(f"{number} is ODD")
        print("🔢 Odd numbers leave a remainder when divided by 2!")
    
    # Additional checks
    print(f"\nAdditional info about {number}:")
    
    # Positive, negative, or zero
    if number > 0:
        print("- This is a positive number")
    elif number < 0:
        print("- This is a negative number")
    else:
        print("- This is zero (neither positive nor negative)")
    
    # Check if it's a multiple of common numbers
    multiples = []
    for divisor in [3, 5, 10]:
        if number != 0 and number % divisor == 0:
            multiples.append(divisor)
    
    if multiples:
        print(f"- Multiple of: {', '.join(map(str, multiples))}")
    
    # Check if it's a perfect square
    import math
    sqrt_val = math.sqrt(abs(number))
    if sqrt_val == int(sqrt_val):
        print(f"- This is a perfect square! ({int(sqrt_val)}² = {abs(number)})")

except ValueError:
    print("Error: Please enter a valid integer!")

print("\n=== Basic Check Complete ===")

# Bonus: Batch checking multiple numbers
print("\n=== Bonus: Batch Even/Odd Checker ===")
test_numbers = [1, 2, 3, 4, 5, 10, 15, 20, 25, 100]

print("Number | Even/Odd | Multiples")
print("-" * 35)

for num in test_numbers:
    even_odd = "Even" if num % 2 == 0 else "Odd"
    multiples = [str(d) for d in [3, 5, 10] if num % d == 0]
    multiples_str = ", ".join(multiples) if multiples else "None"
    print(f"{num:6} | {even_odd:8} | {multiples_str}")

print("\n🎉 Basic even/odd checker complete!")

# =============================================================================
# ENHANCED SOLUTION WITH COMPREHENSIVE NUMBER ANALYSIS
# =============================================================================

import math

def comprehensive_number_analyzer():
    """Comprehensive number analysis with multiple mathematical properties"""
    
    print("\n" + "="*70)
    print("              COMPREHENSIVE NUMBER ANALYZER")
    print("="*70)
    
    def get_valid_integer(prompt):
        """Get a valid integer from user with error handling"""
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("❌ Invalid input! Please enter a valid integer.")
    
    def analyze_number(n):
        """Perform comprehensive analysis of a number"""
        analysis = {
            "number": n,
            "properties": [],
            "divisibility": [],
            "mathematical": [],
            "special": []
        }
        
        # Basic properties
        if n == 0:
            analysis["properties"].append("Zero")
        elif n > 0:
            analysis["properties"].append("Positive")
        else:
            analysis["properties"].append("Negative")
        
        # Even/Odd
        if n % 2 == 0:
            analysis["properties"].append("Even")
        else:
            analysis["properties"].append("Odd")
        
        # Divisibility tests
        divisors = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        for div in divisors:
            if n != 0 and n % div == 0:
                analysis["divisibility"].append(div)
        
        # Mathematical properties
        abs_n = abs(n)
        
        # Perfect square
        if abs_n > 0:
            sqrt_val = math.sqrt(abs_n)
            if sqrt_val == int(sqrt_val):
                analysis["mathematical"].append(f"Perfect square ({int(sqrt_val)}²)")
        
        # Perfect cube
        if abs_n > 0:
            cube_root = round(abs_n ** (1/3))
            if cube_root ** 3 == abs_n:
                analysis["mathematical"].append(f"Perfect cube ({cube_root}³)")
        
        # Prime number check (for positive numbers)
        if n > 1:
            is_prime = True
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    is_prime = False
                    break
            if is_prime:
                analysis["mathematical"].append("Prime number")
        
        # Fibonacci check
        if is_fibonacci(abs_n):
            analysis["special"].append("Fibonacci number")
        
        # Perfect number check (for small positive numbers)
        if 0 < n <= 10000 and is_perfect_number(n):
            analysis["special"].append("Perfect number")
        
        # Palindromic number
        if str(abs_n) == str(abs_n)[::-1]:
            analysis["special"].append("Palindromic number")
        
        # Power of 2
        if abs_n > 0 and (abs_n & (abs_n - 1)) == 0:
            power = int(math.log2(abs_n))
            analysis["special"].append(f"Power of 2 (2^{power})")
        
        return analysis
    
    def is_fibonacci(n):
        """Check if a number is a Fibonacci number"""
        if n < 0:
            return False
        
        # A number is Fibonacci if one of (5*n^2 + 4) or (5*n^2 - 4) is a perfect square
        def is_perfect_square(x):
            if x < 0:
                return False
            root = int(math.sqrt(x))
            return root * root == x
        
        return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)
    
    def is_perfect_number(n):
        """Check if a number is a perfect number (sum of proper divisors equals the number)"""
        if n <= 1:
            return False
        
        divisor_sum = 1  # 1 is always a proper divisor
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                divisor_sum += i
                if i != n // i:  # Add the other divisor if it's different
                    divisor_sum += n // i
        
        return divisor_sum == n
    
    def display_analysis(analysis):
        """Display comprehensive number analysis"""
        n = analysis["number"]
        print(f"\n🔍 ANALYSIS OF {n}:")
        print("=" * 40)
        
        # Basic properties
        if analysis["properties"]:
            print(f"Properties: {', '.join(analysis['properties'])}")
        
        # Divisibility
        if analysis["divisibility"]:
            div_list = ', '.join(map(str, analysis["divisibility"]))
            print(f"Divisible by: {div_list}")
        else:
            print("Divisible by: 1 only (or prime)")
        
        # Mathematical properties
        if analysis["mathematical"]:
            print(f"Mathematical: {', '.join(analysis['mathematical'])}")
        
        # Special properties
        if analysis["special"]:
            print(f"Special: {', '.join(analysis['special'])}")
        
        # Binary representation
        if abs(n) <= 1024:  # Only for reasonable-sized numbers
            print(f"Binary: {bin(n)}")
            print(f"Hexadecimal: {hex(n)}")
        
        # Factorization (for small positive numbers)
        if 0 < n <= 1000:
            factors = get_prime_factors(n)
            if len(factors) > 1:
                factor_str = ' × '.join(map(str, factors))
                print(f"Prime factorization: {factor_str}")
    
    def get_prime_factors(n):
        """Get prime factorization of a number"""
        factors = []
        d = 2
        while d * d <= n:
            while n % d == 0:
                factors.append(d)
                n //= d
            d += 1
        if n > 1:
            factors.append(n)
        return factors
    
    # Get number from user
    print("🔢 Enter a number for comprehensive analysis:")
    number = get_valid_integer("Enter an integer: ")
    
    # Perform analysis
    analysis = analyze_number(number)
    display_analysis(analysis)

def batch_number_analysis():
    """Analyze multiple numbers in batch for comparison"""
    
    print("\n" + "="*70)
    print("              BATCH NUMBER ANALYSIS")
    print("="*70)
    
    # Predefined interesting numbers for analysis
    interesting_numbers = [
        0,      # Zero
        1,      # Unity
        2,      # First prime
        3,      # Odd prime
        4,      # Perfect square
        5,      # Fibonacci prime
        6,      # Perfect number
        8,      # Power of 2
        9,      # Perfect square
        10,     # Base 10
        13,     # Fibonacci prime
        16,     # Perfect square, power of 2
        25,     # Perfect square
        28,     # Perfect number
        64,     # Perfect square, power of 2, perfect cube
        100,    # Perfect square
        121,    # Palindromic perfect square
        144,    # Fibonacci perfect square
        -5,     # Negative number
        -16,    # Negative perfect square
    ]
    
    print("Analyzing interesting numbers:")
    print("-" * 70)
    
    # Create table header
    print(f"{'Number':<8} {'Even/Odd':<8} {'Sign':<8} {'Special Properties':<45}")
    print("-" * 70)
    
    for num in interesting_numbers:
        # Basic properties
        even_odd = "Even" if num % 2 == 0 else "Odd" if num != 0 else "Zero"
        sign = "Positive" if num > 0 else "Negative" if num < 0 else "Zero"
        
        # Special properties (simplified for table)
        special = []
        abs_num = abs(num)
        
        # Perfect square
        if abs_num > 0 and math.sqrt(abs_num) == int(math.sqrt(abs_num)):
            special.append("Square")
        
        # Prime (simple check for small numbers)
        if num > 1:
            is_prime = all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1))
            if is_prime:
                special.append("Prime")
        
        # Power of 2
        if abs_num > 0 and (abs_num & (abs_num - 1)) == 0:
            special.append("Power2")
        
        # Fibonacci (basic check)
        fib_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
        if abs_num in fib_sequence:
            special.append("Fibonacci")
        
        special_str = ", ".join(special) if special else "None"
        
        print(f"{num:<8} {even_odd:<8} {sign:<8} {special_str:<45}")

def conditional_logic_examples():
    """Demonstrate various conditional logic patterns"""
    
    print("\n" + "="*70)
    print("              CONDITIONAL LOGIC EXAMPLES")
    print("="*70)
    
    def number_category_classifier(n):
        """Classify numbers using nested conditionals"""
        print(f"\n🏷️ CLASSIFYING NUMBER: {n}")
        print("-" * 30)
        
        # Primary classification
        if n == 0:
            category = "Zero"
            subcategory = "Neither positive nor negative"
        elif n > 0:
            category = "Positive"
            
            # Sub-classification for positive numbers
            if n == 1:
                subcategory = "Unity (multiplicative identity)"
            elif n < 10:
                subcategory = "Single digit"
            elif n < 100:
                subcategory = "Double digit"
            elif n < 1000:
                subcategory = "Triple digit"
            else:
                subcategory = "Large number"
        else:
            category = "Negative"
            
            # Sub-classification for negative numbers
            abs_n = abs(n)
            if abs_n == 1:
                subcategory = "Negative unity"
            elif abs_n < 10:
                subcategory = "Single digit magnitude"
            elif abs_n < 100:
                subcategory = "Double digit magnitude"
            else:
                subcategory = "Large magnitude"
        
        print(f"Category: {category}")
        print(f"Subcategory: {subcategory}")
        
        # Even/odd analysis
        if n != 0:
            parity = "even" if n % 2 == 0 else "odd"
            print(f"Parity: {parity}")
            
            # Divisibility analysis
            print("Divisibility tests:")
            for divisor in [2, 3, 5]:
                if n % divisor == 0:
                    print(f"  ✅ Divisible by {divisor}")
                else:
                    print(f"  ❌ Not divisible by {divisor}")
    
    # Test classification
    test_numbers = [0, 1, -1, 7, 12, -15, 42, 100, -256, 1337]
    
    for num in test_numbers:
        number_category_classifier(num)

def advanced_even_odd_applications():
    """Show practical applications of even/odd checking"""
    
    print("\n" + "="*70)
    print("              PRACTICAL EVEN/ODD APPLICATIONS")
    print("="*70)
    
    print("\n💼 REAL-WORLD APPLICATIONS:")
    print("-" * 35)
    
    # 1. Alternating patterns
    print("\n1. ALTERNATING ROW COLORS (like spreadsheet):")
    for row in range(1, 11):
        color = "Light Gray" if row % 2 == 0 else "White"
        print(f"Row {row:2}: {color}")
    
    # 2. Shift scheduling
    print("\n2. WORK SHIFT SCHEDULING:")
    for day in range(1, 15):
        shift = "Day Shift" if day % 2 == 1 else "Night Shift"
        print(f"Day {day:2}: {shift}")
    
    # 3. Tournament seeding
    print("\n3. TOURNAMENT BRACKET SEEDING:")
    players = ["Alice", "Bob", "Carol", "Dave", "Eve", "Frank", "Grace", "Henry"]
    for i, player in enumerate(players, 1):
        side = "Left Bracket" if i % 2 == 1 else "Right Bracket"
        print(f"Player {i} ({player}): {side}")
    
    # 4. Data validation
    print("\n4. DATA VALIDATION (Credit Card Check Digit):")
    def luhn_algorithm_demo(card_number):
        """Simplified demonstration of Luhn algorithm (uses even/odd positions)"""
        digits = [int(d) for d in str(card_number)]
        checksum = 0
        
        for i, digit in enumerate(reversed(digits)):
            if i % 2 == 1:  # Every second digit (from right)
                doubled = digit * 2
                checksum += doubled if doubled < 10 else doubled - 9
            else:
                checksum += digit
        
        is_valid = checksum % 10 == 0
        return is_valid, checksum
    
    test_cards = [
        "4532015112830366",  # Valid Visa
        "4532015112830367",  # Invalid (last digit changed)
    ]
    
    for card in test_cards:
        valid, checksum = luhn_algorithm_demo(card)
        status = "✅ Valid" if valid else "❌ Invalid"
        print(f"Card {card}: {status} (checksum: {checksum})")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    # Run comprehensive number analyzer
    comprehensive_number_analyzer()
    
    # Show batch analysis
    batch_number_analysis()
    
    # Show conditional logic examples
    conditional_logic_examples()
    
    # Show practical applications
    advanced_even_odd_applications()
    
    print("\n" + "="*70)
    print("                        LEARNING SUMMARY")
    print("="*70)
    
    print("""
📖 KEY CONCEPTS DEMONSTRATED:

1. CONDITIONAL STATEMENTS:
   • if/elif/else structure
   • Nested conditionals
   • Boolean expressions and operators
   • Comparison operators: ==, !=, <, >, <=, >=

2. MODULUS OPERATOR (%):
   • Check divisibility: n % d == 0
   • Even/odd checking: n % 2 == 0
   • Cyclic patterns: day % 7 for day of week
   • Remainder calculations

3. MATHEMATICAL ANALYSIS:
   • Prime number checking
   • Perfect squares and cubes
   • Number factorization
   • Special number sequences (Fibonacci, perfect numbers)

4. INPUT VALIDATION:
   • Try/except for error handling
   • Range validation
   • Type conversion safety

🎯 BEST PRACTICES:
   ✅ Use clear, descriptive condition names
   ✅ Handle edge cases (zero, negative numbers)
   ✅ Validate input before processing
   ✅ Use elif for mutually exclusive conditions
   ✅ Group related conditions logically

🚀 PRACTICAL APPLICATIONS:
   • Data validation algorithms
   • Alternating patterns in UI
   • Shift scheduling systems
   • Tournament bracket organization
   • Checksum calculations

💡 PROBLEM-SOLVING PATTERNS:
   • Break complex conditions into simple ones
   • Use helper functions for reusable logic
   • Test with edge cases and boundary values
   • Document the logic for future reference
""")
    
    print("🎉 Even/odd checker solution complete!")
    print("Next: Grading systems and complex conditionals!")
