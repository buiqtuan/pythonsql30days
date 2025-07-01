#!/usr/bin/env python3
"""
30-Day Python & SQL Curriculum Generator
========================================

This script generates the complete directory structure and content for the 
30-day Python and SQL learning curriculum.

Usage: python generate_curriculum.py
"""

import os
from pathlib import Path

# Curriculum data structure
CURRICULUM = {
    4: {
        "title": "Loops & List Comprehensions",
        "objectives": [
            "Master `for`, `while`, `break`, and `continue`",
            "Use list comprehensions for efficient list creation"
        ],
        "exercises": [
            "Create a list of even numbers under 50 using a loop and a comprehension",
            "Compute factorial using a while loop"
        ],
        "files": ["loops_practice.py", "list_comprehensions.py", "factorial.py"]
    },
    5: {
        "title": "Functions & Variable Scope",
        "objectives": [
            "Define functions, use arguments and return values",
            "Understand local vs global variables"
        ],
        "exercises": [
            "Write `compound_interest(principal, rate, years)`",
            "Call the function with sample inputs and display the result"
        ],
        "files": ["functions_intro.py", "compound_interest.py", "scope_examples.py"]
    },
    6: {
        "title": "Mini Project: Asset Summary CLI",
        "objectives": [
            "Combine knowledge from Days 1–5 into a real program"
        ],
        "exercises": [
            "Build `asset_summary.py` to input asset names and values, then calculate total, average, min, and max"
        ],
        "files": ["asset_summary.py", "project_planning.md"]
    },
    7: {
        "title": "Review & Code Refactoring",
        "objectives": [
            "Review earlier exercises and improve code quality"
        ],
        "exercises": [
            "Refactor code for readability and error handling",
            "Document your functions using comments"
        ],
        "files": ["refactored_exercises.py", "code_review_checklist.md"]
    },
    8: {
        "title": "Lists and Tuples",
        "objectives": [
            "Use list methods like append, pop, slicing",
            "Understand tuple packing and unpacking"
        ],
        "exercises": [
            "Manipulate a list of stock prices",
            "Unpack a tuple of customer information"
        ],
        "files": ["list_operations.py", "tuple_examples.py", "stock_prices.py"]
    },
    9: {
        "title": "Dictionaries and Sets",
        "objectives": [
            "Create, access, and loop through dictionaries",
            "Use set operations: union, intersection, difference"
        ],
        "exercises": [
            "Build a stock portfolio using a dictionary",
            "Compare two sets of tickers for overlap"
        ],
        "files": ["dictionary_practice.py", "set_operations.py", "portfolio.py"]
    },
    10: {
        "title": "File I/O and CSV Handling",
        "objectives": [
            "Use `open()`, `with`, and the `csv` module to read/write files"
        ],
        "exercises": [
            "Read `transactions.csv`, aggregate totals by category, and write `summary.csv`"
        ],
        "files": ["file_operations.py", "csv_handler.py", "transactions.csv"]
    },
    11: {
        "title": "Error Handling and Logging",
        "objectives": [
            "Use `try`, `except`, and `finally` for exception handling",
            "Implement logging for debugging"
        ],
        "exercises": [
            "Add logging to file I/O operations and handle missing file exceptions"
        ],
        "files": ["error_handling.py", "logging_example.py", "robust_file_reader.py"]
    },
    12: {
        "title": "Standard Libraries",
        "objectives": [
            "Use `datetime`, `json`, and `collections.Counter`"
        ],
        "exercises": [
            "Group transactions by month and export to JSON"
        ],
        "files": ["datetime_practice.py", "json_operations.py", "collections_examples.py"]
    },
    13: {
        "title": "Object-Oriented Programming (OOP) – Part 1",
        "objectives": [
            "Define classes and constructors",
            "Use attributes and methods"
        ],
        "exercises": [
            "Create a `Customer` class with ID and name",
            "Add a method to display customer information"
        ],
        "files": ["oop_basics.py", "customer_class.py", "class_examples.py"]
    },
    14: {
        "title": "OOP – Inheritance and Encapsulation",
        "objectives": [
            "Use class inheritance",
            "Encapsulate methods and use special methods"
        ],
        "exercises": [
            "Create a `PremiumCustomer` subclass",
            "Track method calls with logging"
        ],
        "files": ["inheritance.py", "encapsulation.py", "premium_customer.py"]
    },
    15: {
        "title": "Managing Python Libraries",
        "objectives": [
            "Create and activate virtual environments",
            "Install, freeze, and export dependencies"
        ],
        "exercises": [
            "Create a project environment and install `pandas` and `numpy`"
        ],
        "files": ["requirements.txt", "environment_setup.py", "package_management.md"]
    },
    16: {
        "title": "Unit Testing in Python",
        "objectives": [
            "Use the `unittest` module to test functions"
        ],
        "exercises": [
            "Write unit tests for `compound_interest()` using multiple test cases"
        ],
        "files": ["test_functions.py", "unittest_examples.py", "testing_guide.md"]
    },
    17: {
        "title": "Introduction to Pandas",
        "objectives": [
            "Use `Series` and `DataFrame` objects",
            "Read data from CSV into DataFrame"
        ],
        "exercises": [
            "Filter transactions based on amount",
            "Summarize data using `groupby()`"
        ],
        "files": ["pandas_intro.py", "dataframe_basics.py", "data_analysis.py"]
    },
    18: {
        "title": "Advanced Pandas",
        "objectives": [
            "Sort values, apply custom functions, plot data"
        ],
        "exercises": [
            "Plot spending by category",
            "Use `apply()` to calculate percentage change"
        ],
        "files": ["advanced_pandas.py", "data_visualization.py", "pandas_plotting.py"]
    },
    19: {
        "title": "Introduction to NumPy",
        "objectives": [
            "Create arrays, perform slicing and broadcasting"
        ],
        "exercises": [
            "Perform operations on financial data arrays",
            "Compute mean, max, min using NumPy"
        ],
        "files": ["numpy_basics.py", "array_operations.py", "financial_calculations.py"]
    },
    20: {
        "title": "Python Review & Small Project",
        "objectives": [
            "Integrate skills from previous days into a small application"
        ],
        "exercises": [
            "Build a basic financial analysis tool using Pandas and NumPy"
        ],
        "files": ["financial_analyzer.py", "project_review.md", "integration_test.py"]
    },
    21: {
        "title": "Introduction to RDBMS & SQLite/PostgreSQL",
        "objectives": [
            "Understand tables, schemas, primary and foreign keys"
        ],
        "exercises": [
            "Create schema with `customers` and `transactions` tables"
        ],
        "files": ["schema_design.sql", "database_setup.py", "sqlite_intro.py"]
    },
    22: {
        "title": "Basic SQL Queries",
        "objectives": [
            "Use SELECT, WHERE, ORDER BY, LIMIT"
        ],
        "exercises": [
            "Query transactions > 100 and sort by date"
        ],
        "files": ["basic_queries.sql", "select_examples.sql", "query_practice.py"]
    },
    23: {
        "title": "Aggregation and GROUP BY",
        "objectives": [
            "Use SUM, AVG, COUNT, GROUP BY, HAVING"
        ],
        "exercises": [
            "Calculate total spending per customer"
        ],
        "files": ["aggregation.sql", "groupby_examples.sql", "summary_queries.sql"]
    },
    24: {
        "title": "Advanced Joins",
        "objectives": [
            "Perform INNER, LEFT, RIGHT JOINs"
        ],
        "exercises": [
            "List customers with and without transactions"
        ],
        "files": ["joins_practice.sql", "join_examples.sql", "complex_queries.sql"]
    },
    25: {
        "title": "Window Functions",
        "objectives": [
            "Use ROW_NUMBER(), RANK(), and PARTITION BY"
        ],
        "exercises": [
            "Rank transactions and calculate running total"
        ],
        "files": ["window_functions.sql", "ranking_queries.sql", "analytical_sql.sql"]
    },
    26: {
        "title": "Performance Optimization",
        "objectives": [
            "Use EXPLAIN and INDEX"
        ],
        "exercises": [
            "Compare query performance before and after indexing"
        ],
        "files": ["performance_tuning.sql", "indexing_examples.sql", "explain_analysis.py"]
    },
    27: {
        "title": "Integrating SQL with Python",
        "objectives": [
            "Use `sqlite3` or `psycopg2` to connect and run queries"
        ],
        "exercises": [
            "Load CSV data into DB and query it from Python"
        ],
        "files": ["python_sql.py", "database_connector.py", "data_pipeline.py"]
    },
    28: {
        "title": "Capstone Project Design",
        "objectives": [
            "Define project goals and schema design"
        ],
        "exercises": [
            "Write project outline and initial setup code"
        ],
        "files": ["project_spec.md", "capstone_setup.py", "requirements_analysis.md"]
    },
    29: {
        "title": "Writing Capstone Queries",
        "objectives": [
            "Combine JOINs, subqueries, and aggregations"
        ],
        "exercises": [
            "Export analytics summary to CSV"
        ],
        "files": ["capstone_queries.sql", "data_export.py", "analytics_report.py"]
    },
    30: {
        "title": "Capstone Demo & Review",
        "objectives": [
            "Present the capstone project and review final code"
        ],
        "exercises": [
            "Live demo with data flow and reporting"
        ],
        "files": ["final_demo.py", "project_presentation.md", "course_review.md"]
    }
}

def create_day_structure(day_num, day_info, base_path):
    """Create directory structure and files for a specific day"""
    
    day_path = base_path / f"day{day_num:02d}"
    day_path.mkdir(exist_ok=True)
    
    # Create exercises directory
    exercises_path = day_path / "exercises"
    exercises_path.mkdir(exist_ok=True)
    
    # Create solutions directory
    solutions_path = day_path / "solutions"
    solutions_path.mkdir(exist_ok=True)
    
    # Create resources directory
    resources_path = day_path / "resources"
    resources_path.mkdir(exist_ok=True)
    
    # Create README.md
    readme_content = generate_readme(day_num, day_info)
    with open(day_path / "README.md", "w") as f:
        f.write(readme_content)
    
    # Create exercise files
    for file_name in day_info["files"]:
        if file_name.endswith('.py'):
            exercise_content = generate_python_exercise_template(day_num, day_info["title"], file_name)
            with open(exercises_path / file_name, "w") as f:
                f.write(exercise_content)
        elif file_name.endswith('.sql'):
            sql_content = generate_sql_template(day_num, day_info["title"], file_name)
            with open(exercises_path / file_name, "w") as f:
                f.write(sql_content)
        elif file_name.endswith('.md'):
            md_content = generate_markdown_template(day_num, day_info["title"], file_name)
            with open(exercises_path / file_name, "w") as f:
                f.write(md_content)
        elif file_name.endswith('.csv'):
            csv_content = generate_sample_csv(file_name)
            with open(resources_path / file_name, "w") as f:
                f.write(csv_content)
        elif file_name == 'requirements.txt':
            req_content = generate_requirements()
            with open(exercises_path / file_name, "w") as f:
                f.write(req_content)

def generate_readme(day_num, day_info):
    """Generate README.md content for a day"""
    
    objectives_list = "\n".join([f"- {obj}" for obj in day_info["objectives"]])
    exercises_list = "\n".join([f"- {ex}" for ex in day_info["exercises"]])
    files_list = "\n".join([f"- `{file}`" for file in day_info["files"]])
    
    return f"""# Day {day_num}: {day_info["title"]}

## Learning Objectives

{objectives_list}

## Theory (2 hours)

### Core Concepts
[Detailed theory content would go here based on the day's topic]

### Key Topics
- Topic 1: Understanding the fundamentals
- Topic 2: Practical applications
- Topic 3: Best practices and common pitfalls

## Practical Exercises (2 hours)

{exercises_list}

## Files to Work With

{files_list}

## Key Concepts
- Concept 1
- Concept 2  
- Concept 3

## Next Day Preview
Tomorrow we'll build on today's concepts and explore new topics.

## Additional Resources
- [Python Documentation](https://docs.python.org/3/)
- [SQL Tutorial](https://www.w3schools.com/sql/)

## Notes
- Complete all exercises before moving to the next day
- Ask for help if you get stuck
- Practice makes perfect!
"""

def generate_python_exercise_template(day_num, title, filename):
    """Generate Python exercise template"""
    
    return f'''"""
Day {day_num} Exercise: {filename.replace('.py', '').replace('_', ' ').title()}
{"=" * (len(filename) + 20)}

{title} - {filename}

Instructions:
1. Complete the exercise according to the requirements
2. Test your code thoroughly
3. Add comments to explain your logic
"""

print("=== Day {day_num}: {title} ===")
print("Exercise: {filename}")
print()

# TODO: Implement the exercise
def main():
    """Main function to run the exercise"""
    print("Starting exercise...")
    
    # Your code here
    
    print("Exercise completed!")

if __name__ == "__main__":
    main()
'''

def generate_sql_template(day_num, title, filename):
    """Generate SQL template"""
    
    return f"""-- Day {day_num}: {title}
-- File: {filename}
-- =====================================

-- Exercise: Implement SQL queries for {title}

-- TODO: Add your SQL queries here

-- Example query structure:
-- SELECT column1, column2
-- FROM table_name
-- WHERE condition;

"""

def generate_markdown_template(day_num, title, filename):
    """Generate Markdown template"""
    
    return f"""# Day {day_num}: {title}

## {filename.replace('.md', '').replace('_', ' ').title()}

### Overview
This document provides additional information for Day {day_num}.

### Instructions
1. Follow the guidelines provided
2. Complete all sections
3. Review and validate your work

### Notes
- Add your notes here
- Track your progress
- Document any issues

### Resources
- [Link to resource 1](#)
- [Link to resource 2](#)
"""

def generate_sample_csv(filename):
    """Generate sample CSV data"""
    
    if 'transaction' in filename.lower():
        return """id,customer_id,amount,category,date,description
1,101,250.50,groceries,2024-01-15,Weekly shopping
2,102,89.99,electronics,2024-01-16,Phone case
3,101,1200.00,rent,2024-01-01,Monthly rent
4,103,45.75,dining,2024-01-17,Restaurant dinner
5,102,67.30,gas,2024-01-18,Gas station fill-up
"""
    else:
        return """id,name,value
1,Sample Item 1,100
2,Sample Item 2,200
3,Sample Item 3,300
"""

def generate_requirements():
    """Generate requirements.txt content"""
    return """# Python requirements for 30-Day Python & SQL Course
pandas>=1.5.0
numpy>=1.24.0
matplotlib>=3.6.0
jupyter>=1.0.0
sqlite3
pytest>=7.0.0
"""

def main():
    """Main function to generate the curriculum"""
    
    # Get the base directory (where this script is located)
    base_path = Path(__file__).parent
    
    print("🚀 Generating 30-Day Python & SQL Curriculum...")
    print(f"📁 Base directory: {base_path}")
    
    # Generate days 4-30 (days 1-3 already created manually)
    for day_num in range(4, 31):
        if day_num in CURRICULUM:
            print(f"📝 Creating Day {day_num:02d}: {CURRICULUM[day_num]['title']}")
            create_day_structure(day_num, CURRICULUM[day_num], base_path)
        else:
            print(f"⚠️  Day {day_num} not found in curriculum data")
    
    print("\n✅ Curriculum generation complete!")
    print("🎓 Ready to start your 30-day learning journey!")
    
    # Create a quick start guide
    quick_start = """# Quick Start Guide

## How to Use This Curriculum

1. **Daily Routine**:
   - Navigate to `dayXX` folder
   - Read the `README.md` for objectives and theory
   - Complete exercises in the `exercises` folder
   - Check solutions only after attempting exercises

2. **File Structure**:
   ```
   dayXX/
   ├── README.md          # Daily lesson plan
   ├── exercises/         # Practice exercises
   ├── solutions/         # Example solutions
   └── resources/         # Data files and materials
   ```

3. **Prerequisites**:
   - Python 3.8 or higher
   - Text editor (VS Code recommended)
   - SQLite (included with Python)

4. **Setup**:
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate (Windows)
   venv\\Scripts\\activate
   
   # Install dependencies
   pip install -r day15/exercises/requirements.txt
   ```

Happy Learning! 🐍📊
"""
    
    with open(base_path / "QUICK_START.md", "w") as f:
        f.write(quick_start)

if __name__ == "__main__":
    main()
