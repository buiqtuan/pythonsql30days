# 30-Day Python & SQL Learning Plan (Updated)

**Total Duration:** 30 consecutive days  
**Daily Study Time:** 4 hours (2 hours theory + 2 hours practice)  
**Allocation:** 20 days for Python, 10 days for SQL  
**Day 30:** Final Capstone Project Demo (Integrating Python & SQL)  

---
## Day 1: Introduction to Python & Development Environment
### Objectives
- Install Python, VS Code or JupyterLab
- Use pip and virtualenv for environment management
- Understand REPL vs script mode and write your first program
### Exercises
- Create a virtual environment and install packages using pip
- Write `hello.py` to print 'Hello, Data!'
- Display different data types: int, float, str

## Day 2: Variables, Data Types & Operators
### Objectives
- Use variables with data types: int, float, str, bool
- Type casting, f-strings, arithmetic operators
### Exercises
- Build `calc.py` that takes two numbers and displays sum, product, and average
- Use `type()` to check data types and perform arithmetic operations

## Day 3: Conditional Statements
### Objectives
- Use `if`, `elif`, and `else`
- Apply comparison and logical operators
### Exercises
- Create `grading.py` to convert numeric scores to letter grades (A–F)
- Write a program to check if a number is even or odd

## Day 4: Loops & List Comprehensions
### Objectives
- Master `for`, `while`, `break`, and `continue`
- Use list comprehensions for efficient list creation
### Exercises
- Create a list of even numbers under 50 using a loop and a comprehension
- Compute factorial using a while loop

## Day 5: Functions & Variable Scope
### Objectives
- Define functions, use arguments and return values
- Understand local vs global variables
### Exercises
- Write `compound_interest(principal, rate, years)`
- Call the function with sample inputs and display the result

## Day 6: Mini Project: Asset Summary CLI
### Objectives
- Combine knowledge from Days 1–5 into a real program
### Exercises
- Build `asset_summary.py` to input asset names and values, then calculate total, average, min, and max

## Day 7: Review & Code Refactoring
### Objectives
- Review earlier exercises and improve code quality
### Exercises
- Refactor code for readability and error handling
- Document your functions using comments

## Day 8: Lists and Tuples
### Objectives
- Use list methods like append, pop, slicing
- Understand tuple packing and unpacking
### Exercises
- Manipulate a list of stock prices
- Unpack a tuple of customer information

## Day 9: Dictionaries and Sets
### Objectives
- Create, access, and loop through dictionaries
- Use set operations: union, intersection, difference
### Exercises
- Build a stock portfolio using a dictionary
- Compare two sets of tickers for overlap

## Day 10: File I/O and CSV Handling
### Objectives
- Use `open()`, `with`, and the `csv` module to read/write files
### Exercises
- Read `transactions.csv`, aggregate totals by category, and write `summary.csv`

## Day 11: Error Handling and Logging
### Objectives
- Use `try`, `except`, and `finally` for exception handling
- Implement logging for debugging
### Exercises
- Add logging to file I/O operations and handle missing file exceptions

## Day 12: Standard Libraries
### Objectives
- Use `datetime`, `json`, and `collections.Counter`
### Exercises
- Group transactions by month and export to JSON

## Day 13: Object-Oriented Programming (OOP) – Part 1
### Objectives
- Define classes and constructors
- Use attributes and methods
### Exercises
- Create a `Customer` class with ID and name
- Add a method to display customer information

## Day 14: OOP – Inheritance and Encapsulation
### Objectives
- Use class inheritance
- Encapsulate methods and use special methods
### Exercises
- Create a `PremiumCustomer` subclass
- Track method calls with logging

## Day 15: Managing Python Libraries
### Objectives
- Create and activate virtual environments
- Install, freeze, and export dependencies
### Exercises
- Create a project environment and install `pandas` and `numpy`

## Day 16: Unit Testing in Python
### Objectives
- Use the `unittest` module to test functions
### Exercises
- Write unit tests for `compound_interest()` using multiple test cases

## Day 17: Introduction to Pandas
### Objectives
- Use `Series` and `DataFrame` objects
- Read data from CSV into DataFrame
### Exercises
- Filter transactions based on amount
- Summarize data using `groupby()`

## Day 18: Advanced Pandas
### Objectives
- Sort values, apply custom functions, plot data
### Exercises
- Plot spending by category
- Use `apply()` to calculate percentage change

## Day 19: Introduction to NumPy
### Objectives
- Create arrays, perform slicing and broadcasting
### Exercises
- Perform operations on financial data arrays
- Compute mean, max, min using NumPy

## Day 20: Python Review & Small Project
### Objectives
- Integrate skills from previous days into a small application
### Exercises
- Build a basic financial analysis tool using Pandas and NumPy

## Day 21: Introduction to RDBMS & SQLite/PostgreSQL
### Objectives
- Understand tables, schemas, primary and foreign keys
### Exercises
- Create schema with `customers` and `transactions` tables

## Day 22: Basic SQL Queries
### Objectives
- Use SELECT, WHERE, ORDER BY, LIMIT
### Exercises
- Query transactions > 100 and sort by date

## Day 23: Aggregation and GROUP BY
### Objectives
- Use SUM, AVG, COUNT, GROUP BY, HAVING
### Exercises
- Calculate total spending per customer

## Day 24: Advanced Joins
### Objectives
- Perform INNER, LEFT, RIGHT JOINs
### Exercises
- List customers with and without transactions

## Day 25: Window Functions
### Objectives
- Use ROW_NUMBER(), RANK(), and PARTITION BY
### Exercises
- Rank transactions and calculate running total

## Day 26: Performance Optimization
### Objectives
- Use EXPLAIN and INDEX
### Exercises
- Compare query performance before and after indexing

## Day 27: Integrating SQL with Python
### Objectives
- Use `sqlite3` or `psycopg2` to connect and run queries
### Exercises
- Load CSV data into DB and query it from Python

## Day 28: Capstone Project Design
### Objectives
- Define project goals and schema design
### Exercises
- Write project outline and initial setup code

## Day 29: Writing Capstone Queries
### Objectives
- Combine JOINs, subqueries, and aggregations
### Exercises
- Export analytics summary to CSV

## Day 30: Capstone Demo & Review
### Objectives
- Present the capstone project and review final code
### Exercises
- Live demo with data flow and reporting
