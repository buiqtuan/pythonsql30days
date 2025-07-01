"""
Day 1 Exercise: Data Types Exploration
======================================

Demonstrate different Python data types: int, float, str, bool

Instructions:
1. Create variables of different types
2. Use type() function to check data types
3. Display the values and their types
"""

# Integer
age = 25
print(f"Age: {age}, Type: {type(age)}")

# Float
height = 5.8
print(f"Height: {height}, Type: {type(height)}")

# String
name = "Python Learner"
print(f"Name: {name}, Type: {type(name)}")

# Boolean
is_learning = True
print(f"Is Learning: {is_learning}, Type: {type(is_learning)}")

# More examples
print("\n" + "="*50)
print("EXPLORING DATA TYPES")
print("="*50)

# Numbers
whole_number = 42
decimal_number = 3.14159
print(f"Whole Number: {whole_number} ({type(whole_number).__name__})")
print(f"Decimal Number: {decimal_number} ({type(decimal_number).__name__})")

# Text
greeting = "Hello, World!"
multiline_text = """This is a
multiline string
in Python!"""
print(f"Greeting: '{greeting}' ({type(greeting).__name__})")
print(f"Multiline text: {repr(multiline_text)} ({type(multiline_text).__name__})")

# Boolean values
is_python_fun = True
is_difficult = False
print(f"Is Python fun? {is_python_fun} ({type(is_python_fun).__name__})")
print(f"Is it difficult? {is_difficult} ({type(is_difficult).__name__})")

# None type
nothing = None
print(f"Nothing: {nothing} ({type(nothing).__name__})")

print("\n🎉 Data types exploration complete!")
