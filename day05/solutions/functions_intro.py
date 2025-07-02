"""
Day 5 Solution: Functions Intro
======================================

Functions & Variable Scope - functions_intro.py

This solution demonstrates:
1. Basic function definition and calling
2. Functions with parameters and return values
3. Default parameters
4. Variable number of arguments (*args)
5. Function documentation with docstrings
6. Interactive user input with functions
"""

print("=== Day 5: Functions & Variable Scope ===")
print("Solution: functions_intro.py")
print()

# Exercise 1: Basic function definitions and usage

def greet_user(name):
    """
    Function that takes a name and returns a greeting
    Args:
        name (str): The name of the person to greet
    Returns:
        str: A greeting message
    """
    return f"Hello, {name}! Welcome to Python functions!"

def add_numbers(a, b):
    """
    Function that adds two numbers
    Args:
        a (int/float): First number
        b (int/float): Second number
    Returns:
        int/float: Sum of the two numbers
    """
    return a + b

def calculate_area(length, width):
    """
    Function that calculates the area of a rectangle
    Args:
        length (float): Length of the rectangle
        width (float): Width of the rectangle
    Returns:
        float: Area of the rectangle
    """
    area = length * width
    return area

def get_user_info(name, age, city="Unknown"):
    """
    Function with default parameter
    Args:
        name (str): Person's name
        age (int): Person's age
        city (str): Person's city (default: "Unknown")
    Returns:
        str: Formatted user information
    """
    return f"Name: {name}, Age: {age}, City: {city}"

def calculate_average(*numbers):
    """
    Function that accepts variable number of arguments
    Args:
        *numbers: Variable number of numeric arguments
    Returns:
        float: Average of all numbers
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def main():
    """Main function to run the exercise"""
    print("Starting solution...")
    print()
    
    # Test greet_user function
    print("=== Testing greet_user function ===")
    greeting1 = greet_user("Alice")
    greeting2 = greet_user("Bob")
    print(greeting1)
    print(greeting2)
    print()
    
    # Test add_numbers function
    print("=== Testing add_numbers function ===")
    result1 = add_numbers(5, 3)
    result2 = add_numbers(10.5, 7.2)
    print(f"5 + 3 = {result1}")
    print(f"10.5 + 7.2 = {result2}")
    print()
    
    # Test calculate_area function
    print("=== Testing calculate_area function ===")
    room_area = calculate_area(12, 8)
    garden_area = calculate_area(15.5, 10.2)
    print(f"Room area (12 x 8): {room_area} square units")
    print(f"Garden area (15.5 x 10.2): {garden_area:.2f} square units")
    print()
    
    # Test get_user_info function with default parameter
    print("=== Testing get_user_info function ===")
    user1 = get_user_info("John", 25, "New York")
    user2 = get_user_info("Jane", 30)  # Using default city
    print(user1)
    print(user2)
    print()
    
    # Test calculate_average function with variable arguments
    print("=== Testing calculate_average function ===")
    avg1 = calculate_average(10, 20, 30)
    avg2 = calculate_average(5, 15, 25, 35, 45)
    avg3 = calculate_average(100)
    print(f"Average of 10, 20, 30: {avg1}")
    print(f"Average of 5, 15, 25, 35, 45: {avg2}")
    print(f"Average of 100: {avg3}")
    print()
    
    # Demonstrate key concepts
    print("=== Key Concepts Demonstrated ===")
    print("✓ Function definition with def keyword")
    print("✓ Function parameters and arguments")
    print("✓ Return values")
    print("✓ Default parameters")
    print("✓ Variable number of arguments (*args)")
    print("✓ Function documentation with docstrings")
    print("✓ Function scope (local variables)")
    print()
    
    print("Solution completed!")

if __name__ == "__main__":
    main()
