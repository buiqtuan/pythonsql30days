"""
Day 3 Exercise: Even/Odd Number Checker
=======================================

Write a program to check if a number is even or odd

Instructions:
1. Get a number from user input
2. Use modulus operator (%) to check even/odd
3. Display appropriate message
"""

print("=== Even/Odd Number Checker ===")

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

print("\n=== Check Complete ===")

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
