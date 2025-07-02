"""
Day 5 Exercise: Compound Interest
========================================

Functions & Variable Scope - compound_interest.py

Instructions:
1. Complete the exercise according to the requirements
2. Test your code thoroughly
3. Add comments to explain your logic
"""

print("=== Day 5: Functions & Variable Scope ===")
print("Exercise: compound_interest.py")
print()

# Exercise 2: Compound Interest Calculator

def compound_interest(principal, rate, years, compound_frequency=1):
    """
    Calculate compound interest
    
    Formula: A = P(1 + r/n)^(nt)
    Where:
    A = final amount
    P = principal amount
    r = annual interest rate (as decimal)
    n = number of times interest is compounded per year
    t = number of years
    
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
    print(f"Percentage Advantage: {(advantage/interest_simple)*100:.2f}%")

def get_investment_input():
    """
    Get investment parameters from user input
    Returns:
        tuple: (principal, rate, years, compound_frequency)
    """
    try:
        print("=== Compound Interest Calculator ===")
        principal = float(input("Enter the principal amount ($): "))
        rate = float(input("Enter the annual interest rate (%): "))
        years = int(input("Enter the number of years: "))
        
        print("\nCompounding options:")
        print("1 = Annually")
        print("4 = Quarterly") 
        print("12 = Monthly")
        print("365 = Daily")
        
        compound_freq = int(input("Enter compounding frequency (default 1): ") or "1")
        
        return principal, rate, years, compound_freq
    
    except ValueError:
        print("Error: Please enter valid numeric values")
        return None

def main():
    """Main function to run the exercise"""
    print("Starting exercise...")
    print()
    
    # Test with predefined examples
    print("=== Predefined Examples ===")
    
    # Example 1: Basic compound interest
    print("Example 1: $1000 at 5% for 10 years (annual compounding)")
    display_investment_summary(1000, 5, 10, 1)
    
    # Example 2: Monthly compounding
    print("\nExample 2: $5000 at 7% for 15 years (monthly compounding)")
    display_investment_summary(5000, 7, 15, 12)
    
    # Example 3: High frequency compounding
    print("\nExample 3: $2500 at 4.5% for 8 years (daily compounding)")
    display_investment_summary(2500, 4.5, 8, 365)
    
    # Example 4: Retirement savings scenario
    print("\nExample 4: Retirement savings - $10000 at 6% for 30 years (quarterly compounding)")
    display_investment_summary(10000, 6, 30, 4)
    
    # Interactive calculator
    print("\n" + "="*50)
    print("Interactive Calculator")
    print("="*50)
    
    while True:
        user_input = get_investment_input()
        if user_input:
            principal, rate, years, compound_freq = user_input
            display_investment_summary(principal, rate, years, compound_freq)
        
        again = input("\nWould you like to calculate another investment? (y/n): ").lower()
        if again not in ['y', 'yes']:
            break
    
    print("\nThank you for using the Compound Interest Calculator!")
    print("Exercise completed!")

if __name__ == "__main__":
    main()
