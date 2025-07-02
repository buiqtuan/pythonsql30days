# Day 5: Functions & Variable Scope

## Learning Objectives

- Define functions with parameters and return values
- Understand local vs global variables and scope rules
- Use default parameters and variable arguments
- Apply function best practices and documentation

## Theory (2 hours)

### Core Concepts

#### 1. Function Basics
- **Function Definition**: Using `def` keyword to create reusable code blocks
- **Parameters vs Arguments**: Understanding the difference between function definition parameters and calling arguments
- **Return Values**: How functions return data back to the caller
- **Function Documentation**: Using docstrings to document function purpose and usage

#### 2. Variable Scope
- **Local Scope**: Variables defined inside functions are only accessible within that function
- **Global Scope**: Variables defined at module level are accessible throughout the module
- **Global Keyword**: Using `global` to modify global variables from within functions
- **Nonlocal Keyword**: Using `nonlocal` to modify variables in enclosing scope

#### 3. Advanced Function Features
- **Default Parameters**: Providing default values for function parameters
- **Variable Arguments**: Using `*args` to accept variable number of positional arguments
- **Keyword Arguments**: Using `**kwargs` to accept variable number of keyword arguments

### Key Topics
- **Function Design Principles**: How to write clean, reusable functions
- **Scope Resolution**: Understanding Python's LEGB rule (Local, Enclosing, Global, Built-in)
- **Common Pitfalls**: Variable shadowing, mutable default arguments, and scope conflicts

## Practical Exercises (2 hours)

### Exercise 1: Functions Introduction (`functions_intro.py`)
- Create basic functions with parameters and return values
- Practice function documentation with docstrings
- Implement functions with default parameters
- Use variable arguments (*args)
- Build interactive functions with user input

### Exercise 2: Compound Interest Calculator (`compound_interest.py`)
- **Primary Goal**: Write `compound_interest(principal, rate, years)` function as specified in curriculum
- Implement mathematical calculations within functions
- Return multiple values using tuples
- Create helper functions for formatting and validation
- Demonstrate function composition and reuse

### Exercise 3: Variable Scope Examples (`scope_examples.py`)
- Explore local vs global variable scope
- Practice using `global` keyword for variable modification
- Understand scope conflicts and resolution
- Implement nested functions and enclosing scope
- Use `nonlocal` keyword appropriately

## Files to Work With

- `exercises/functions_intro.py` - Basic function concepts and usage
- `exercises/compound_interest.py` - Financial calculation function (curriculum requirement)
- `exercises/scope_examples.py` - Variable scope demonstrations
- `solutions/` - Complete solutions with detailed explanations

## Key Concepts Learned

### Functions
1. **Function Definition**: `def function_name(parameters):`
2. **Return Statements**: `return value` to send data back
3. **Default Parameters**: `def func(param=default_value):`
4. **Variable Arguments**: `def func(*args)` for multiple arguments
5. **Documentation**: Using triple-quoted docstrings

### Variable Scope
1. **Local Variables**: Defined inside functions, only accessible within
2. **Global Variables**: Defined at module level, accessible everywhere
3. **Global Keyword**: `global variable_name` to modify global variables
4. **Nonlocal Keyword**: `nonlocal variable_name` for enclosing scope
5. **Scope Resolution**: Python's LEGB rule for variable lookup

### Best Practices
1. Keep functions focused and single-purpose
2. Use descriptive function and parameter names
3. Document functions with docstrings
4. Minimize use of global variables
5. Prefer function parameters over global variables
6. Handle edge cases and validate inputs

## Sample Code Patterns

```python
# Basic function with return value
def calculate_area(length, width):
    """Calculate rectangle area."""
    return length * width

# Function with default parameter
def greet(name, greeting="Hello"):
    """Greet a person with optional greeting."""
    return f"{greeting}, {name}!"

# Function using global variable
counter = 0
def increment_counter():
    """Increment global counter."""
    global counter
    counter += 1
    return counter

# Compound interest function (curriculum requirement)
def compound_interest(principal, rate, years):
    """Calculate compound interest."""
    rate_decimal = rate / 100
    final_amount = principal * (1 + rate_decimal) ** years
    interest_earned = final_amount - principal
    return final_amount, interest_earned
```

## Next Day Preview
Tomorrow (Day 6) we'll build on today's concepts to create a Mini Project: Asset Summary CLI that combines functions, variables, and user interaction into a complete program.

## Additional Resources
- [Python Functions Documentation](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Python Scope and LEGB Rule](https://realpython.com/python-scope-legb-rule/)
- [Function Best Practices](https://realpython.com/python-functions/)

## Notes
- Complete all exercises before moving to the next day
- Pay special attention to the compound_interest function as it's specifically mentioned in the curriculum
- Practice writing docstrings for all your functions
- Experiment with different scope scenarios to solidify understanding
- Ask for help if you get stuck on variable scope concepts
