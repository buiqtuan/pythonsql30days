"""
Day 5 Solution: Variable Scope Examples
=======================================

Functions & Variable Scope - scope_examples.py

This solution demonstrates:
1. Local vs global variable scope
2. Using the global keyword for variable modification
3. Scope conflicts and resolution
4. Nested functions and enclosing scope
5. Using nonlocal keyword appropriately
6. Variable lifetime and scope best practices
7. Practical scope examples

Key Learning Objectives:
- Understand Python's LEGB rule (Local, Enclosing, Global, Built-in)
- Learn when and how to use global and nonlocal keywords
- Recognize scope conflicts and how to resolve them
- Implement nested functions with proper scope management
- Apply scope best practices in real-world scenarios
"""

print("=== Day 5: Functions & Variable Scope ===")
print("Solution: scope_examples.py")
print()

# Global variables - accessible throughout the module
global_counter = 0
company_name = "TechCorp Solutions"
tax_rate = 0.085  # 8.5% tax rate
base_salary = 50000

def demonstrate_local_scope():
    """
    Demonstrate local variable scope
    Local variables are only accessible within the function where they're defined
    """
    print("=== 1. Local Scope Demonstration ===")
    
    # Local variables - only accessible within this function
    local_message = "I'm a local variable"
    employee_id = 12345
    department = "Engineering"
    
    print(f"Local message: {local_message}")
    print(f"Employee ID: {employee_id}")
    print(f"Department: {department}")
    
    # Local variables can access global variables (read-only by default)
    print(f"Accessing global company_name: {company_name}")
    print(f"Accessing global tax_rate: {tax_rate * 100}%")
    
    # Demonstrate that local variables override global ones with same name
    company_name = "Local Company Name"  # This creates a local variable
    print(f"Local company_name (shadows global): {company_name}")
    
    print("-" * 50)

def demonstrate_global_access():
    """
    Demonstrate accessing global variables (read-only)
    """
    print("=== 2. Global Variable Access ===")
    
    # Reading global variables - no special syntax needed
    print(f"Company: {company_name}")
    print(f"Tax Rate: {tax_rate * 100}%")
    print(f"Base Salary: ${base_salary:,}")
    print(f"Current Global Counter: {global_counter}")
    
    # Calculate something using global variables
    annual_tax = base_salary * tax_rate
    net_salary = base_salary - annual_tax
    
    print(f"Annual Tax: ${annual_tax:,.2f}")
    print(f"Net Salary: ${net_salary:,.2f}")
    
    print("-" * 50)

def demonstrate_global_modification():
    """
    Demonstrate modifying global variables using the global keyword
    """
    print("=== 3. Global Variable Modification ===")
    
    # To modify a global variable, we MUST use the 'global' keyword
    global global_counter, company_name
    
    print(f"Global counter before increment: {global_counter}")
    global_counter += 1
    print(f"Global counter after increment: {global_counter}")
    
    # Modifying a global string
    original_name = company_name
    company_name = "TechCorp Advanced Solutions"
    print(f"Company name changed from '{original_name}' to '{company_name}'")
    
    print("-" * 50)

def calculate_employee_details(employee_name, hours_worked, hourly_rate=25.0):
    """
    Function that demonstrates mixed use of local and global variables
    
    Args:
        employee_name (str): Name of the employee
        hours_worked (float): Number of hours worked
        hourly_rate (float): Hourly rate (default: $25.0)
    
    Returns:
        dict: Employee details including gross pay, tax, and net pay
    """
    # Local calculations using global tax_rate
    gross_pay = hours_worked * hourly_rate
    tax_amount = gross_pay * tax_rate  # Using global tax_rate
    net_pay = gross_pay - tax_amount
    
    # Create local data structure
    employee_details = {
        'name': employee_name,
        'hours': hours_worked,
        'rate': hourly_rate,
        'gross_pay': gross_pay,
        'tax': tax_amount,
        'net_pay': net_pay,
        'tax_rate_used': tax_rate
    }
    
    return employee_details

def scope_conflict_resolution():
    """
    Demonstrate how Python resolves scope conflicts
    """
    print("=== 4. Scope Conflict Resolution ===")
    
    # Create local variables with same names as global ones
    tax_rate = 0.15  # Local tax rate (different from global)
    company_name = "Local Startup Inc."  # Local company name
    
    print(f"Local tax_rate: {tax_rate * 100}%")
    print(f"Local company_name: {company_name}")
    
    # Access global variables explicitly using globals()
    print(f"Global tax_rate: {globals()['tax_rate'] * 100}%")
    print(f"Global company_name: {globals()['company_name']}")
    
    # Demonstrate LEGB rule resolution
    def inner_function():
        print(f"Inner function sees local tax_rate: {tax_rate}")
        print(f"Inner function sees local company_name: {company_name}")
    
    inner_function()
    
    print("-" * 50)

def nested_functions_example():
    """
    Demonstrate nested functions and their scope behavior
    """
    print("=== 5. Nested Functions and Scope ===")
    
    outer_variable = "I'm in the outer function"
    outer_counter = 0
    
    def inner_function():
        # Inner function can access outer function's variables
        inner_variable = "I'm in the inner function"
        
        print(f"Inner accessing outer variable: {outer_variable}")
        print(f"Inner local variable: {inner_variable}")
        print(f"Inner accessing global: {company_name}")
        
        # Can read but cannot modify outer variables without nonlocal
        print(f"Outer counter (read-only): {outer_counter}")
    
    def another_inner():
        # Each nested function has its own local scope
        another_var = "I'm in another inner function"
        print(f"Another inner variable: {another_var}")
        print(f"Also accessing outer: {outer_variable}")
    
    print(f"Outer variable: {outer_variable}")
    inner_function()
    another_inner()
    
    # Note: inner_variable is not accessible here
    # print(inner_variable)  # This would cause NameError
    
    print("-" * 50)

def enclosing_scope_with_nonlocal():
    """
    Demonstrate enclosing scope modification using nonlocal keyword
    """
    print("=== 6. Enclosing Scope with nonlocal ===")
    
    operation_count = 0
    total_amount = 0.0
    
    def add_transaction(amount):
        nonlocal operation_count, total_amount
        operation_count += 1
        total_amount += amount
        print(f"Transaction #{operation_count}: Added ${amount:.2f}")
        print(f"Running total: ${total_amount:.2f}")
    
    def subtract_transaction(amount):
        nonlocal operation_count, total_amount
        operation_count += 1
        total_amount -= amount
        print(f"Transaction #{operation_count}: Subtracted ${amount:.2f}")
        print(f"Running total: ${total_amount:.2f}")
    
    def get_summary():
        print(f"Summary: {operation_count} operations, Total: ${total_amount:.2f}")
    
    def reset_account():
        nonlocal operation_count, total_amount
        operation_count = 0
        total_amount = 0.0
        print("Account reset!")
    
    # Test the nested functions
    add_transaction(100.0)
    add_transaction(250.5)
    subtract_transaction(75.25)
    get_summary()
    
    add_transaction(50.0)
    get_summary()
    
    reset_account()
    get_summary()
    
    print("-" * 50)

def variable_lifetime_demo():
    """
    Demonstrate variable lifetime in different scopes
    """
    print("=== 7. Variable Lifetime Demo ===")
    
    # Function-level variable
    function_var = "Function scope variable"
    
    # Block scope - In Python, variables in loops/if statements are function-scoped
    if True:
        block_var = "Block variable (but actually function-scoped in Python)"
    
    for i in range(3):
        loop_var = f"Loop iteration {i}"
        print(f"Loop variable: {loop_var}")
    
    # These variables persist after their "blocks" because Python uses function scope
    print(f"Block variable after if: {block_var}")
    print(f"Loop variable after loop: {loop_var}")
    print(f"Loop counter after loop: {i}")
    
    # Demonstrate function scope boundary
    def inner_scope():
        inner_var = "This won't exist outside the function"
        return inner_var
    
    result = inner_scope()
    print(f"Returned from inner function: {result}")
    # print(inner_var)  # This would cause NameError
    
    print("-" * 50)

def closure_example():
    """
    Demonstrate closures - functions that capture variables from enclosing scope
    """
    print("=== 8. Closure Example ===")
    
    def create_multiplier(factor):
        """
        Factory function that creates and returns a multiplier function
        The returned function 'remembers' the factor value (closure)
        """
        def multiplier(value):
            return value * factor  # 'factor' is captured from enclosing scope
        
        return multiplier
    
    # Create different multiplier functions
    double = create_multiplier(2)
    triple = create_multiplier(3)
    times_ten = create_multiplier(10)
    
    # Test the closures
    test_value = 5
    print(f"Original value: {test_value}")
    print(f"Double: {double(test_value)}")
    print(f"Triple: {triple(test_value)}")
    print(f"Times ten: {times_ten(test_value)}")
    
    # Each closure maintains its own copy of the captured variable
    print(f"Double factor: {double.__closure__[0].cell_contents}")
    print(f"Triple factor: {triple.__closure__[0].cell_contents}")
    
    print("-" * 50)

def practical_scope_patterns():
    """
    Demonstrate practical scope patterns and best practices
    """
    print("=== 9. Practical Scope Patterns ===")
    
    # Pattern 1: Configuration at module level (global)
    default_discount = 0.10
    premium_discount = 0.20
    
    def calculate_price(base_price, customer_type="regular", custom_discount=None):
        """
        Calculate final price with discounts
        Uses global discount rates but allows override
        """
        if custom_discount is not None:
            discount_rate = custom_discount
        elif customer_type == "premium":
            discount_rate = premium_discount  # Using enclosing scope
        else:
            discount_rate = default_discount  # Using enclosing scope
        
        discount_amount = base_price * discount_rate
        final_price = base_price - discount_amount
        
        return {
            'base_price': base_price,
            'discount_rate': discount_rate,
            'discount_amount': discount_amount,
            'final_price': final_price
        }
    
    # Test different scenarios
    regular_result = calculate_price(100.0)
    premium_result = calculate_price(100.0, "premium")
    custom_result = calculate_price(100.0, custom_discount=0.25)
    
    print("Regular customer:", regular_result)
    print("Premium customer:", premium_result)
    print("Custom discount:", custom_result)
    
    print("-" * 50)

def scope_best_practices():
    """
    Demonstrate and explain scope best practices
    """
    print("=== 10. Scope Best Practices ===")
    print()
    
    print("✅ GOOD PRACTICES:")
    print("1. Minimize use of global variables")
    print("2. Pass data through function parameters instead of global access")
    print("3. Use descriptive variable names to avoid naming conflicts")
    print("4. Keep variable scope as narrow as possible")
    print("5. Use 'global' keyword explicitly when modifying global variables")
    print("6. Use 'nonlocal' keyword for enclosing scope variables")
    print("7. Prefer function return values over global variable modification")
    print("8. Use constants for global configuration values")
    print()
    
    print("❌ PRACTICES TO AVOID:")
    print("1. Excessive use of global variables")
    print("2. Modifying global variables without 'global' keyword (creates local)")
    print("3. Using same names for local and global variables")
    print("4. Deep nesting of functions with complex scope chains")
    print("5. Relying on variable shadowing for program logic")
    print()
    
    # Example of good practice
    def good_function(input_value, multiplier=2):
        """Good: Uses parameters, clear scope, returns result"""
        result = input_value * multiplier
        return result
    
    # Example of poor practice (commented out)
    # global_value = 10  # Poor: relies on global state
    # def poor_function():
    #     global global_value
    #     global_value *= 2  # Poor: modifies global state
    
    print("Example - Good practice:")
    result = good_function(5, 3)
    print(f"good_function(5, 3) = {result}")
    
    print("-" * 50)

def interactive_scope_demo():
    """
    Interactive demonstration of scope concepts
    """
    print("=== 11. Interactive Scope Demo ===")
    
    # Simulate a simple banking system to show scope in action
    account_balance = 1000.0  # Enclosing scope variable
    transaction_log = []      # Enclosing scope list
    
    def deposit(amount):
        nonlocal account_balance
        if amount > 0:
            account_balance += amount
            transaction_log.append(f"DEPOSIT: +${amount:.2f}")
            print(f"Deposited ${amount:.2f}. New balance: ${account_balance:.2f}")
        else:
            print("Deposit amount must be positive")
    
    def withdraw(amount):
        nonlocal account_balance
        if amount > 0 and amount <= account_balance:
            account_balance -= amount
            transaction_log.append(f"WITHDRAWAL: -${amount:.2f}")
            print(f"Withdrew ${amount:.2f}. New balance: ${account_balance:.2f}")
        else:
            print("Invalid withdrawal amount")
    
    def get_balance():
        print(f"Current balance: ${account_balance:.2f}")
        return account_balance
    
    def get_transaction_history():
        print("Transaction History:")
        for i, transaction in enumerate(transaction_log, 1):
            print(f"  {i}. {transaction}")
        if not transaction_log:
            print("  No transactions yet")
    
    # Simulate banking operations
    print("Initial setup:")
    get_balance()
    
    print("\nPerforming transactions:")
    deposit(250.0)
    withdraw(100.0)
    deposit(50.0)
    withdraw(75.0)
    
    print("\nFinal state:")
    get_balance()
    get_transaction_history()
    
    print("-" * 50)

def main():
    """Main function to run all scope examples"""
    print("Starting Variable Scope Examples Solution...")
    print("=" * 60)
    print()
    
    # Run all demonstrations
    demonstrate_local_scope()
    demonstrate_global_access()
    demonstrate_global_modification()
    
    # Practical example with employee calculations
    print("=== Employee Calculation Example ===")
    emp1 = calculate_employee_details("Alice Johnson", 40, 30.0)
    emp2 = calculate_employee_details("Bob Smith", 35)  # Using default rate
    
    for emp in [emp1, emp2]:
        print(f"Employee: {emp['name']}")
        print(f"  Hours: {emp['hours']}, Rate: ${emp['rate']:.2f}")
        print(f"  Gross: ${emp['gross_pay']:.2f}, Tax: ${emp['tax']:.2f}, Net: ${emp['net_pay']:.2f}")
    print("-" * 50)
    
    # Continue with other demonstrations
    scope_conflict_resolution()
    nested_functions_example()
    enclosing_scope_with_nonlocal()
    variable_lifetime_demo()
    closure_example()
    practical_scope_patterns()
    scope_best_practices()
    interactive_scope_demo()
    
    # Final state check
    print("=== Final Global State ===")
    print(f"Global counter final value: {global_counter}")
    print(f"Company name final value: {company_name}")
    print(f"Tax rate: {tax_rate * 100}%")
    
    print()
    print("🎓 Variable Scope Examples Complete!")
    print("Key concepts demonstrated:")
    print("✓ Local vs Global scope")
    print("✓ Global keyword usage")
    print("✓ Nonlocal keyword usage")
    print("✓ Scope conflict resolution")
    print("✓ Nested functions and closures")
    print("✓ Variable lifetime")
    print("✓ Scope best practices")
    print("✓ Practical scope patterns")

if __name__ == "__main__":
    main()
