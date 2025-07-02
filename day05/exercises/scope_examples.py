"""
Day 5 Exercise: Scope Examples
=====================================

Functions & Variable Scope - scope_examples.py

Instructions:
1. Complete the exercise according to the requirements
2. Test your code thoroughly
3. Add comments to explain your logic
"""

print("=== Day 5: Functions & Variable Scope ===")
print("Exercise: scope_examples.py")
print()

# Exercise 3: Variable Scope Examples

# Global variables
global_counter = 0
company_name = "TechCorp"
tax_rate = 0.08

def demonstrate_local_scope():
    """
    Demonstrate local variable scope
    """
    print("=== Local Scope Example ===")
    
    # Local variables - only accessible within this function
    local_var = "I'm local to this function"
    employee_name = "Alice"
    salary = 50000
    
    print(f"Local variable: {local_var}")
    print(f"Employee: {employee_name}")
    print(f"Salary: ${salary:,}")
    
    # Try to access global variable
    print(f"Company name (global): {company_name}")
    print()

def demonstrate_global_access():
    """
    Demonstrate accessing global variables
    """
    print("=== Global Access Example ===")
    
    # Accessing global variables (read-only)
    print(f"Company name: {company_name}")
    print(f"Tax rate: {tax_rate * 100}%")
    print(f"Global counter: {global_counter}")
    print()

def demonstrate_global_modification():
    """
    Demonstrate modifying global variables
    """
    print("=== Global Modification Example ===")
    
    # To modify a global variable, we need the 'global' keyword
    global global_counter
    global_counter += 1
    
    print(f"Global counter incremented to: {global_counter}")
    print()

def calculate_net_salary(gross_salary):
    """
    Function that uses both local and global variables
    Args:
        gross_salary (float): Gross salary amount
    Returns:
        tuple: (net_salary, tax_amount)
    """
    # Local calculation
    tax_amount = gross_salary * tax_rate  # Using global tax_rate
    net_salary = gross_salary - tax_amount
    
    return net_salary, tax_amount

def scope_conflict_example():
    """
    Demonstrate what happens when local and global variables have same name
    """
    print("=== Scope Conflict Example ===")
    
    # Local variable with same name as global
    company_name = "LocalTech"  # This creates a local variable
    
    print(f"Local company_name: {company_name}")
    print(f"Global company_name: {globals()['company_name']}")  # Access global explicitly
    print()

def nested_function_example():
    """
    Demonstrate nested functions and scope
    """
    print("=== Nested Function Scope Example ===")
    
    outer_var = "I'm in the outer function"
    
    def inner_function():
        inner_var = "I'm in the inner function"
        print(f"Inner function can access outer_var: {outer_var}")
        print(f"Inner function local variable: {inner_var}")
        
        # Can also access global variables
        print(f"Inner function accessing global: {company_name}")
    
    print(f"Outer function variable: {outer_var}")
    inner_function()
    
    # Note: outer_var is not accessible here
    # print(inner_var)  # This would cause an error
    print()

def enclosing_scope_example():
    """
    Demonstrate enclosing scope with nonlocal keyword
    """
    print("=== Enclosing Scope with nonlocal Example ===")
    
    counter = 0
    
    def increment():
        nonlocal counter  # Refers to the counter in enclosing scope
        counter += 1
        print(f"Counter incremented to: {counter}")
    
    def reset():
        nonlocal counter
        counter = 0
        print("Counter reset to 0")
    
    # Test the nested functions
    increment()
    increment()
    increment()
    reset()
    increment()
    print()

def variable_lifetime_example():
    """
    Demonstrate variable lifetime and scope
    """
    print("=== Variable Lifetime Example ===")
    
    for i in range(3):
        loop_var = f"Iteration {i}"
        print(f"Inside loop: {loop_var}")
    
    # In Python, loop variables persist after the loop
    print(f"After loop, loop_var still exists: {loop_var}")
    
    # But function-local variables don't persist outside the function
    function_local = "This won't be accessible outside this function"
    print(f"Function local variable: {function_local}")
    print()

def practical_scope_example():
    """
    Practical example showing good scope practices
    """
    print("=== Practical Scope Example ===")
    
    # Configuration (could be global)
    discount_rate = 0.10
    
    def calculate_discount(price, customer_type="regular"):
        """Calculate discount based on customer type"""
        if customer_type == "premium":
            actual_discount = discount_rate * 2  # 20% for premium
        else:
            actual_discount = discount_rate  # 10% for regular
        
        discount_amount = price * actual_discount
        final_price = price - discount_amount
        
        return final_price, discount_amount
    
    # Test with different scenarios
    regular_price, regular_discount = calculate_discount(100)
    premium_price, premium_discount = calculate_discount(100, "premium")
    
    print(f"Regular customer: $100 → ${regular_price:.2f} (discount: ${regular_discount:.2f})")
    print(f"Premium customer: $100 → ${premium_price:.2f} (discount: ${premium_discount:.2f})")
    print()

def scope_best_practices():
    """
    Demonstrate scope best practices
    """
    print("=== Scope Best Practices ===")
    print("1. Minimize use of global variables")
    print("2. Use function parameters instead of global variables when possible")
    print("3. Use descriptive variable names to avoid conflicts")
    print("4. Keep variable scope as narrow as possible")
    print("5. Use 'global' keyword explicitly when modifying global variables")
    print("6. Use 'nonlocal' keyword for enclosing scope variables")
    print()

def main():
    """Main function to run the exercise"""
    print("Starting exercise...")
    print()
    
    # Demonstrate different types of scope
    demonstrate_local_scope()
    demonstrate_global_access()
    demonstrate_global_modification()
    demonstrate_global_modification()  # Call again to see counter increment
    
    # Practical example
    print("=== Salary Calculation Example ===")
    gross = 60000
    net, tax = calculate_net_salary(gross)
    print(f"Gross salary: ${gross:,}")
    print(f"Tax amount: ${tax:,.2f}")
    print(f"Net salary: ${net:,.2f}")
    print()
    
    # More advanced scope examples
    scope_conflict_example()
    nested_function_example()
    enclosing_scope_example()
    variable_lifetime_example()
    practical_scope_example()
    scope_best_practices()
    
    # Final global counter check
    print(f"Final global counter value: {global_counter}")
    
    print("Exercise completed!")

if __name__ == "__main__":
    main()
