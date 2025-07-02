"""
Day 5 Solution: Compound Interest
========================================

Functions & Variable Scope - compound_interest.py

This solution demonstrates:
1. Function with multiple parameters
2. Mathematical calculations within functions
3. Return multiple values (tuple)
4. Function composition and reuse
5. Input validation and error handling
6. Formatting functions for output
7. Practical financial calculations

Key Formula: A = P(1 + r/n)^(nt)
Where:
- A = final amount
- P = principal amount  
- r = annual interest rate (as decimal)
- n = number of times interest is compounded per year
- t = number of years
"""

print("=== Day 5: Functions & Variable Scope ===")
print("Solution: compound_interest.py")
print()

# Exercise 2: Compound Interest Calculator

def compound_interest(principal, rate, years, compound_frequency=1):
    """
    Calculate compound interest
    
    Formula: A = P(1 + r/n)^(nt)
    
    Args:
        principal (float): Initial amount of money
        rate (float): Annual interest rate (as percentage, e.g., 5 for 5%)
        years (int): Number of years
        compound_frequency (int): How many times per year interest is compounded (default: 1)
    
    Returns:
        tuple: (final_amount, interest_earned)
    """
    # Convert percentage to decimal
    rate_decimal = rate / 100
    
    # Calculate compound interest
    final_amount = principal * (1 + rate_decimal / compound_frequency) ** (compound_frequency * years)
    
    # Calculate interest earned
    interest_earned = final_amount - principal
    
    return final_amount, interest_earned

def simple_interest(principal, rate, years):
    """
    Calculate simple interest for comparison
    
    Formula: SI = P * r * t
    
    Args:
        principal (float): Initial amount of money
        rate (float): Annual interest rate (as percentage)
        years (int): Number of years
    
    Returns:
        tuple: (final_amount, interest_earned)
    """
    # Convert percentage to decimal
    rate_decimal = rate / 100
    
    # Calculate simple interest
    interest_earned = principal * rate_decimal * years
    final_amount = principal + interest_earned
    
    return final_amount, interest_earned

def format_currency(amount):
    """
    Format a number as currency
    Args:
        amount (float): Amount to format
    Returns:
        str: Formatted currency string
    """
    return f"${amount:,.2f}"

def display_investment_summary(principal, rate, years, compound_freq=1):
    """
    Display a comprehensive investment summary
    """
    print(f"\n=== Investment Summary ===")
    print(f"Principal: {format_currency(principal)}")
    print(f"Annual Interest Rate: {rate}%")
    print(f"Investment Period: {years} years")
    print(f"Compounding Frequency: {compound_freq} time(s) per year")
    print("-" * 40)
    
    # Calculate compound interest
    final_compound, interest_compound = compound_interest(principal, rate, years, compound_freq)
    
    # Calculate simple interest for comparison
    final_simple, interest_simple = simple_interest(principal, rate, years)
    
    print(f"Compound Interest Results:")
    print(f"  Final Amount: {format_currency(final_compound)}")
    print(f"  Interest Earned: {format_currency(interest_compound)}")
    print(f"  Total Return: {(interest_compound/principal)*100:.2f}%")
    print()
    
    print(f"Simple Interest (for comparison):")
    print(f"  Final Amount: {format_currency(final_simple)}")
    print(f"  Interest Earned: {format_currency(interest_simple)}")
    print(f"  Total Return: {(interest_simple/principal)*100:.2f}%")
    print()
    
    # Show the advantage of compound interest
    advantage = interest_compound - interest_simple
    print(f"Compound Interest Advantage: {format_currency(advantage)}")
    if interest_simple > 0:
        print(f"Percentage Advantage: {(advantage/interest_simple)*100:.2f}%")

def validate_input(principal, rate, years):
    """
    Validate investment parameters
    Args:
        principal (float): Principal amount
        rate (float): Interest rate
        years (int): Number of years
    Returns:
        bool: True if all inputs are valid
    """
    if principal <= 0:
        print("Error: Principal must be positive")
        return False
    if rate < 0:
        print("Error: Interest rate cannot be negative")
        return False
    if years <= 0:
        print("Error: Years must be positive")
        return False
    return True

def main():
    """Main function to run the exercise"""
    print("Starting solution...")
    print()
    
    # Test with predefined examples as specified in curriculum
    print("=== Curriculum Requirement: compound_interest(principal, rate, years) ===")
    
    # Basic test cases
    test_cases = [
        (1000, 5, 10),      # $1000 at 5% for 10 years
        (5000, 7, 15),      # $5000 at 7% for 15 years  
        (2500, 4.5, 8),     # $2500 at 4.5% for 8 years
        (10000, 6, 30),     # Retirement scenario
    ]
    
    for i, (principal, rate, years) in enumerate(test_cases, 1):
        print(f"Test Case {i}: compound_interest({principal}, {rate}, {years})")
        
        if validate_input(principal, rate, years):
            final_amount, interest_earned = compound_interest(principal, rate, years)
            print(f"  Principal: {format_currency(principal)}")
            print(f"  Rate: {rate}% annually")
            print(f"  Years: {years}")
            print(f"  Final Amount: {format_currency(final_amount)}")
            print(f"  Interest Earned: {format_currency(interest_earned)}")
            print(f"  Total Return: {(interest_earned/principal)*100:.2f}%")
        print()
    
    # Extended examples with different compounding frequencies
    print("=== Extended Examples with Different Compounding ===")
    
    examples = [
        ("Annual Compounding", 1000, 5, 10, 1),
        ("Quarterly Compounding", 1000, 5, 10, 4),
        ("Monthly Compounding", 1000, 5, 10, 12),
        ("Daily Compounding", 1000, 5, 10, 365),
    ]
    
    print("Comparing compounding frequencies for $1000 at 5% for 10 years:")
    print("-" * 60)
    
    for description, principal, rate, years, freq in examples:
        final_amount, interest_earned = compound_interest(principal, rate, years, freq)
        print(f"{description:20}: {format_currency(final_amount)} (Interest: {format_currency(interest_earned)})")
    
    print()
    
    # Demonstrate key concepts
    print("=== Key Concepts Demonstrated ===")
    print("✓ Function with multiple parameters")
    print("✓ Default parameter values")
    print("✓ Mathematical calculations in functions")
    print("✓ Return multiple values using tuples")
    print("✓ Function composition (calling functions from other functions)")
    print("✓ Input validation")
    print("✓ Number formatting")
    print("✓ Practical financial calculations")
    print()
    
    # Show the power of compound interest
    print("=== The Power of Compound Interest ===")
    principal = 1000
    rate = 8
    years_list = [5, 10, 20, 30]
    
    print(f"Growth of {format_currency(principal)} at {rate}% annually:")
    for years in years_list:
        final_amount, interest_earned = compound_interest(principal, rate, years)
        multiplier = final_amount / principal
        print(f"  After {years:2d} years: {format_currency(final_amount)} ({multiplier:.2f}x original)")
    
    print()
    print("Solution completed!")

if __name__ == "__main__":
    main()
