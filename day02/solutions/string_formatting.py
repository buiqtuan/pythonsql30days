"""
Day 2 Solution: String Formatting Practice
==========================================

SOLUTION with comprehensive string formatting techniques

This solution demonstrates:
- F-string formatting (modern Python 3.6+)
- .format() method (Python 2.7+)
- % formatting (legacy)
- Advanced formatting options
- Real-world formatting scenarios
"""

# =============================================================================
# BASIC SOLUTION
# =============================================================================

print("=== BASIC STRING FORMATTING SOLUTION ===\n")

# Sample data
name = "John Doe"
age = 30
salary = 75000.50
city = "New York"
is_employed = True

print("1. F-String Formatting (Recommended):")
print(f"Hello, {name}!")
print(f"You are {age} years old.")
print(f"Your salary is ${salary:,.2f}")
print(f"You live in {city}.")
print(f"Employment status: {is_employed}")

print(f"\nDetailed info: {name} is {age} years old, earns ${salary:,.2f} per year, and lives in {city}.")

print("\n2. Format Method:")
print("Hello, {}!".format(name))
print("You are {} years old.".format(age))
print("Your salary is ${:,.2f}".format(salary))

# Named placeholders
print("Name: {person_name}, Age: {person_age}".format(person_name=name, person_age=age))

print("\n3. Advanced F-String Formatting:")

# Number formatting
pi = 3.14159265359
large_number = 1234567890

print(f"Pi rounded to 2 decimals: {pi:.2f}")
print(f"Pi rounded to 4 decimals: {pi:.4f}")
print(f"Large number with commas: {large_number:,}")
print(f"Large number in scientific notation: {large_number:.2e}")

# Percentage formatting
growth_rate = 0.1234
print(f"Growth rate: {growth_rate:.2%}")

# String alignment and padding
print(f"Left aligned: '{name:<20}'")
print(f"Right aligned: '{name:>20}'")
print(f"Center aligned: '{name:^20}'")

# Date formatting (bonus)
from datetime import datetime
now = datetime.now()
print(f"Current date and time: {now:%Y-%m-%d %H:%M:%S}")
print(f"Just the date: {now:%B %d, %Y}")

print("\n4. Multi-line F-Strings:")
report = f"""
Employee Report
===============
Name: {name}
Age: {age}
Salary: ${salary:,.2f}
Location: {city}
Status: {'Active' if is_employed else 'Inactive'}
"""
print(report)

print("\n5. Expression in F-Strings:")
x = 10
y = 20
print(f"Sum: {x} + {y} = {x + y}")
print(f"Is x greater than y? {x > y}")
print(f"Square of x: {x}² = {x**2}")

# Mathematical expressions
print(f"Area of circle (r=5): π × 5² = {3.14159 * 5**2:.2f}")

print("\n🎉 Basic string formatting complete!")

# =============================================================================
# ENHANCED SOLUTION WITH COMPREHENSIVE EXAMPLES
# =============================================================================

def comprehensive_formatting_demo():
    """Comprehensive demonstration of all string formatting techniques"""
    
    print("\n" + "="*70)
    print("              COMPREHENSIVE STRING FORMATTING DEMO")
    print("="*70)
    
    # Sample data for demonstrations
    employee = {
        'name': 'Alice Johnson',
        'id': 12345,
        'department': 'Data Science',
        'salary': 95750.25,
        'start_date': datetime(2020, 3, 15),
        'performance_rating': 4.7,
        'is_remote': True,
        'projects_completed': 23
    }
    
    # =============================================================================
    # 1. F-STRING FORMATTING (PYTHON 3.6+)
    # =============================================================================
    
    print("\n🔤 F-STRING FORMATTING (Modern Python):")
    print("-" * 45)
    
    # Basic f-string usage
    print(f"Employee: {employee['name']}")
    print(f"ID: {employee['id']}")
    print(f"Department: {employee['department']}")
    
    # Number formatting
    print(f"Salary: ${employee['salary']:,.2f}")
    print(f"Performance: {employee['performance_rating']:.1f}/5.0")
    print(f"Projects: {employee['projects_completed']:,}")
    
    # Date formatting
    print(f"Start Date: {employee['start_date']:%B %d, %Y}")
    print(f"Years of Service: {(datetime.now() - employee['start_date']).days // 365}")
    
    # Conditional formatting
    status = "Remote" if employee['is_remote'] else "On-site"
    print(f"Work Status: {status}")
    print(f"Rating Level: {'Excellent' if employee['performance_rating'] >= 4.5 else 'Good' if employee['performance_rating'] >= 3.5 else 'Needs Improvement'}")
    
    # =============================================================================
    # 2. ADVANCED F-STRING FEATURES
    # =============================================================================
    
    print("\n⚡ ADVANCED F-STRING FEATURES:")
    print("-" * 35)
    
    # Expressions in f-strings
    monthly_salary = employee['salary'] / 12
    print(f"Monthly Salary: ${monthly_salary:,.2f}")
    print(f"Daily Rate (22 working days): ${monthly_salary/22:,.2f}")
    
    # Function calls in f-strings
    def calculate_bonus(salary, rating):
        return salary * (rating / 5) * 0.1
    
    bonus = calculate_bonus(employee['salary'], employee['performance_rating'])
    print(f"Annual Bonus: ${bonus:,.2f}")
    
    # String methods in f-strings
    print(f"Name (uppercase): {employee['name'].upper()}")
    print(f"Department (title case): {employee['department'].title()}")
    print(f"Initials: {'.'.join([part[0] for part in employee['name'].split()])}")
    
    # =============================================================================
    # 3. ALIGNMENT AND PADDING
    # =============================================================================
    
    print("\n📐 ALIGNMENT AND PADDING:")
    print("-" * 30)
    
    fields = [
        ("Name", employee['name']),
        ("ID", str(employee['id'])),
        ("Department", employee['department']),
        ("Salary", f"${employee['salary']:,.2f}"),
    ]
    
    print("Left-aligned (width 15):")
    for label, value in fields:
        print(f"{label}: {value:<15}")
    
    print("\nRight-aligned (width 20):")
    for label, value in fields:
        print(f"{label}: {value:>20}")
    
    print("\nCenter-aligned (width 25):")
    for label, value in fields:
        print(f"{label}: {value:^25}")
    
    # Padding with specific characters
    print(f"\nPadded with dots: {employee['name']:.<30}")
    print(f"Padded with dashes: {employee['department']:->30}")
    print(f"Padded with stars: {str(employee['salary']):*>20}")
    
    # =============================================================================
    # 4. NUMBER FORMATTING
    # =============================================================================
    
    print("\n🔢 NUMBER FORMATTING:")
    print("-" * 25)
    
    numbers = [
        1234.5,
        1234567.89,
        0.12345,
        0.001234,
        1234567890
    ]
    
    for num in numbers:
        print(f"Original: {num}")
        print(f"  2 decimals: {num:.2f}")
        print(f"  With commas: {num:,}")
        print(f"  Scientific: {num:.2e}")
        print(f"  As percentage: {num:.2%}")
        print(f"  Fixed width (15): {num:15.2f}")
        print()
    
    # =============================================================================
    # 5. .FORMAT() METHOD
    # =============================================================================
    
    print("\n🎯 .FORMAT() METHOD (Compatible with older Python):")
    print("-" * 55)
    
    # Positional arguments
    print("Hello, {}! You work in {}.".format(employee['name'], employee['department']))
    
    # Indexed arguments
    print("Employee {0} (ID: {1}) earns ${2:,.2f}".format(
        employee['name'], employee['id'], employee['salary']))
    
    # Named arguments
    print("Name: {name}, Department: {dept}, Salary: ${salary:,.2f}".format(
        name=employee['name'],
        dept=employee['department'],
        salary=employee['salary']
    ))
    
    # Dictionary unpacking
    print("Employee {name} has been with us since {start_date:%Y}".format(**employee))
    
    # =============================================================================
    # 6. LEGACY % FORMATTING
    # =============================================================================
    
    print("\n📜 LEGACY % FORMATTING (for reference):")
    print("-" * 40)
    
    print("Name: %s" % employee['name'])
    print("ID: %d" % employee['id'])
    print("Salary: $%.2f" % employee['salary'])
    print("Performance: %.1f/5.0" % employee['performance_rating'])
    
    # Multiple values
    print("Employee %s (ID: %d) earns $%.2f" % (
        employee['name'], employee['id'], employee['salary']))

def practical_formatting_examples():
    """Real-world formatting examples for common scenarios"""
    
    print("\n" + "="*70)
    print("              PRACTICAL FORMATTING EXAMPLES")
    print("="*70)
    
    # =============================================================================
    # 1. FINANCIAL REPORTS
    # =============================================================================
    
    print("\n💰 FINANCIAL REPORT FORMATTING:")
    print("-" * 35)
    
    financial_data = [
        ("Revenue", 1250000.75),
        ("Expenses", 890000.50),
        ("Profit", 360000.25),
        ("Tax", 54000.04),
        ("Net Profit", 306000.21)
    ]
    
    print("QUARTERLY FINANCIAL REPORT")
    print("=" * 35)
    for item, amount in financial_data:
        print(f"{item:<12}: ${amount:>12,.2f}")
    
    print(f"{'Total':<12}: ${'=' * 12}")
    
    # =============================================================================
    # 2. DATA TABLE FORMATTING
    # =============================================================================
    
    print("\n📊 DATA TABLE FORMATTING:")
    print("-" * 30)
    
    employees_data = [
        ("Alice Johnson", "Data Science", 95750, 4.7),
        ("Bob Smith", "Engineering", 105000, 4.2),
        ("Carol Davis", "Marketing", 78000, 4.9),
        ("David Wilson", "Sales", 85000, 3.8),
    ]
    
    # Header
    print(f"{'Name':<15} {'Department':<12} {'Salary':<10} {'Rating':<6}")
    print("-" * 50)
    
    # Data rows
    for name, dept, salary, rating in employees_data:
        print(f"{name:<15} {dept:<12} ${salary:<9,} {rating:<6.1f}")
    
    # =============================================================================
    # 3. LOG MESSAGE FORMATTING
    # =============================================================================
    
    print("\n📝 LOG MESSAGE FORMATTING:")
    print("-" * 30)
    
    import datetime
    
    log_levels = ["INFO", "WARNING", "ERROR", "DEBUG"]
    messages = [
        "User logged in successfully",
        "Database connection timeout",
        "Failed to process payment",
        "Cache cleared"
    ]
    
    for level, message in zip(log_levels, messages):
        timestamp = datetime.datetime.now()
        print(f"[{timestamp:%Y-%m-%d %H:%M:%S}] {level:<7} | {message}")
    
    # =============================================================================
    # 4. PROGRESS INDICATORS
    # =============================================================================
    
    print("\n⏳ PROGRESS INDICATOR FORMATTING:")
    print("-" * 35)
    
    total_tasks = 50
    completed_tasks = 32
    progress = completed_tasks / total_tasks
    
    # Progress bar
    bar_length = 30
    filled_length = int(bar_length * progress)
    bar = "█" * filled_length + "░" * (bar_length - filled_length)
    
    print(f"Progress: |{bar}| {progress:.1%} ({completed_tasks}/{total_tasks})")
    print(f"Remaining: {total_tasks - completed_tasks} tasks")
    print(f"ETA: {(total_tasks - completed_tasks) * 0.5:.1f} hours")

def string_formatting_best_practices():
    """Demonstrate best practices for string formatting"""
    
    print("\n" + "="*70)
    print("              STRING FORMATTING BEST PRACTICES")
    print("="*70)
    
    print("""
📖 FORMATTING METHOD COMPARISON:

1. F-STRINGS (Recommended for Python 3.6+):
   ✅ Most readable and concise
   ✅ Fastest performance
   ✅ Supports expressions and function calls
   ✅ Easy to debug

2. .FORMAT() METHOD:
   ✅ Compatible with older Python versions
   ✅ Good for complex formatting
   ✅ Supports named parameters
   ⚠️  Slightly more verbose

3. % FORMATTING (Legacy):
   ⚠️  Older style, avoid in new code
   ⚠️  Less readable
   ⚠️  Limited functionality
   ✅ Still used in some libraries

🎯 BEST PRACTICES:

1. USE F-STRINGS when possible:
   • More readable: f"Hello {name}!"
   • Better performance
   • Supports expressions: f"{value * 1.1:.2f}"

2. FORMAT NUMBERS appropriately:
   • Currency: f"${amount:,.2f}"
   • Percentages: f"{rate:.2%}"
   • Scientific: f"{value:.2e}"

3. ALIGN TEXT for tables:
   • Left: f"{text:<20}"
   • Right: f"{text:>20}"
   • Center: f"{text:^20}"

4. USE DESCRIPTIVE formatting:
   • Include units: f"Weight: {weight:.1f} kg"
   • Add context: f"Score: {score}/100"

5. HANDLE EDGE CASES:
   • Check for None values
   • Handle division by zero
   • Validate input types

❌ COMMON MISTAKES:
   • Not specifying decimal places for money
   • Inconsistent alignment in tables
   • Missing error handling for formatting
   • Using % formatting in new code
""")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    # Run comprehensive formatting demonstration
    comprehensive_formatting_demo()
    
    # Show practical examples
    practical_formatting_examples()
    
    # Show best practices
    string_formatting_best_practices()
    
    print("\n🎉 String formatting solution complete!")
    print("Next: Variables, operators, and type conversions!")
