"""
Day 5 Solution: Variable Scope Examples
======================================

This solution provides comprehensive examples of Python variable scope concepts
including local, global, nonlocal, and built-in scopes with practical applications.

Author: Python Learning Assistant
Date: 2024
"""

from typing import List, Dict, Any, Callable
import math


# Global variables for demonstration
global_counter = 0
global_config = {
    "debug": True,
    "max_retries": 3,
    "timeout": 30
}


# Example 1: Basic Local vs Global Scope
def demonstrate_basic_scope():
    """Demonstrate basic local vs global scope."""
    print("1. Basic Local vs Global Scope")
    print("-" * 35)
    
    # Global variable
    global global_counter
    local_variable = "I'm local to this function"
    
    print(f"Global counter (before): {global_counter}")
    global_counter += 1
    print(f"Global counter (after): {global_counter}")
    print(f"Local variable: {local_variable}")
    
    # This would cause an error if uncommented:
    # print(local_variable)  # NameError: name 'local_variable' is not defined
    print()


# Example 2: Variable Shadowing
def demonstrate_shadowing():
    """Demonstrate how local variables can shadow global ones."""
    print("2. Variable Shadowing")
    print("-" * 25)
    
    # Local variable shadows global
    global_counter = "I'm a local variable shadowing the global one"
    print(f"Local global_counter: {global_counter}")
    print(f"Actual global counter: {globals()['global_counter']}")
    print()


# Example 3: Global Keyword
def demonstrate_global_keyword():
    """Demonstrate proper use of global keyword."""
    print("3. Global Keyword Usage")
    print("-" * 25)
    
    global global_counter
    
    print(f"Global counter before modification: {global_counter}")
    global_counter *= 2
    print(f"Global counter after modification: {global_counter}")
    
    # Modifying global config
    global global_config
    global_config["debug"] = False
    print(f"Modified global config: {global_config}")
    print()


# Example 4: Nonlocal Keyword (Nested Functions)
def demonstrate_nonlocal():
    """Demonstrate nonlocal keyword with nested functions."""
    print("4. Nonlocal Keyword (Nested Functions)")
    print("-" * 40)
    
    # Enclosing scope variable
    enclosing_var = "Original value"
    counter = 0
    
    def inner_function():
        nonlocal enclosing_var, counter
        enclosing_var = "Modified by inner function"
        counter += 1
        
        def deeply_nested():
            nonlocal counter
            counter += 10
            print(f"    Deeply nested - counter: {counter}")
        
        deeply_nested()
        print(f"  Inner function - enclosing_var: {enclosing_var}")
        print(f"  Inner function - counter: {counter}")
    
    print(f"Before inner function - enclosing_var: {enclosing_var}")
    print(f"Before inner function - counter: {counter}")
    inner_function()
    print(f"After inner function - enclosing_var: {enclosing_var}")
    print(f"After inner function - counter: {counter}")
    print()


# Example 5: Closure and Scope
def create_counter(initial_value: int = 0):
    """Create a counter function using closure."""
    count = initial_value
    
    def increment(step: int = 1):
        nonlocal count
        count += step
        return count
    
    def decrement(step: int = 1):
        nonlocal count
        count -= step
        return count
    
    def get_value():
        return count
    
    def reset():
        nonlocal count
        count = initial_value
        return count
    
    # Return a dictionary of functions that form a closure
    return {
        "increment": increment,
        "decrement": decrement,
        "get_value": get_value,
        "reset": reset
    }


def demonstrate_closures():
    """Demonstrate closures and how they capture scope."""
    print("5. Closures and Scope Capture")
    print("-" * 35)
    
    # Create two independent counters
    counter1 = create_counter(10)
    counter2 = create_counter(100)
    
    print(f"Counter1 initial: {counter1['get_value']()}")
    print(f"Counter2 initial: {counter2['get_value']()}")
    
    print(f"Counter1 after increment(5): {counter1['increment'](5)}")
    print(f"Counter2 after increment(20): {counter2['increment'](20)}")
    
    print(f"Counter1 after decrement(3): {counter1['decrement'](3)}")
    print(f"Counter2 current value: {counter2['get_value']()}")
    
    counter1['reset']()
    print(f"Counter1 after reset: {counter1['get_value']()}")
    print()


# Example 6: Function Parameters and Scope
def demonstrate_parameter_scope(param1, param2="default"):
    """Demonstrate how parameters create local scope."""
    print("6. Function Parameter Scope")
    print("-" * 30)
    
    # Parameters are local to the function
    print(f"param1 (local): {param1}")
    print(f"param2 (local): {param2}")
    
    # Modifying parameters doesn't affect outside variables
    param1 = "modified"
    param2 = "also modified"
    
    print(f"Modified param1: {param1}")
    print(f"Modified param2: {param2}")
    print()


# Example 7: List/Dict Modifications and Scope
def demonstrate_mutable_scope():
    """Demonstrate scope behavior with mutable objects."""
    print("7. Mutable Objects and Scope")
    print("-" * 35)
    
    def modify_list(lst: List[int]):
        """Modifying mutable objects affects the original."""
        print(f"  Inside function - original list: {lst}")
        lst.append(999)  # This modifies the original list
        lst[0] = 1000   # This also modifies the original
        print(f"  Inside function - modified list: {lst}")
    
    def reassign_list(lst: List[int]):
        """Reassigning creates a new local variable."""
        print(f"  Inside function - original list: {lst}")
        lst = [7, 8, 9]  # This creates a new local variable
        print(f"  Inside function - reassigned list: {lst}")
    
    original_list = [1, 2, 3, 4, 5]
    print(f"Original list: {original_list}")
    
    modify_list(original_list)
    print(f"After modify_list: {original_list}")
    
    reassign_list(original_list)
    print(f"After reassign_list: {original_list}")
    print()


# Example 8: Built-in Scope
def demonstrate_builtin_scope():
    """Demonstrate built-in scope and how to shadow built-ins."""
    print("8. Built-in Scope")
    print("-" * 20)
    
    # Using built-in functions
    print(f"Built-in len([1,2,3]): {len([1, 2, 3])}")
    print(f"Built-in max([1,5,3]): {max([1, 5, 3])}")
    
    # Shadowing built-ins (not recommended!)
    def len(obj):
        """Custom len function that shadows built-in."""
        return "Custom len function called!"
    
    print(f"Shadowed len([1,2,3]): {len([1, 2, 3])}")
    
    # Accessing original built-in
    import builtins
    print(f"Original len via builtins: {builtins.len([1, 2, 3])}")
    print()


# Example 9: Practical Scope Application - Configuration Manager
class ConfigManager:
    """A practical example of scope management in a class."""
    
    _instance = None  # Class variable
    _config = {}      # Class variable
    
    def __new__(cls):
        """Singleton pattern using class scope."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        """Initialize with default configuration."""
        if not hasattr(self, 'initialized'):
            self._load_default_config()
            self.initialized = True
    
    def _load_default_config(self):
        """Load default configuration (private method)."""
        self._config = {
            "app_name": "Python Learning App",
            "version": "1.0.0",
            "debug": False,
            "log_level": "INFO"
        }
    
    def get_config(self, key: str = None):
        """Get configuration value(s)."""
        if key is None:
            return self._config.copy()  # Return copy to prevent external modification
        return self._config.get(key)
    
    def set_config(self, key: str, value: Any):
        """Set configuration value."""
        self._config[key] = value
    
    def update_config(self, config_dict: Dict[str, Any]):
        """Update multiple configuration values."""
        self._config.update(config_dict)


def demonstrate_practical_scope():
    """Demonstrate practical scope usage with ConfigManager."""
    print("9. Practical Scope Example - Configuration Manager")
    print("-" * 55)
    
    # Create config manager instances
    config1 = ConfigManager()
    config2 = ConfigManager()
    
    print(f"Same instance? {config1 is config2}")  # Should be True (singleton)
    
    print(f"Initial config: {config1.get_config()}")
    
    # Modify config through one instance
    config1.set_config("debug", True)
    config1.set_config("custom_setting", "value")
    
    # Check if change is reflected in other instance
    print(f"Config from instance 2: {config2.get_config()}")
    print()


# Example 10: Scope Chain and Variable Resolution
def demonstrate_scope_chain():
    """Demonstrate how Python resolves variables through scope chain (LEGB)."""
    print("10. Scope Chain (LEGB Rule)")
    print("-" * 35)
    print("LEGB: Local -> Enclosing -> Global -> Built-in")
    print()
    
    # Global variable
    variable = "Global"
    
    def enclosing_function():
        variable = "Enclosing"
        
        def local_function():
            variable = "Local"
            print(f"  Local scope: {variable}")
            
            # Access different scopes explicitly
            print(f"  Enclosing scope: {enclosing_function.__code__.co_names}")
            print(f"  Global scope: {globals()['variable'] if 'variable' in globals() else 'Not found'}")
            
            # Built-in scope example
            print(f"  Built-in scope example - abs(-5): {abs(-5)}")
        
        print(f"Enclosing scope: {variable}")
        local_function()
    
    print(f"Global scope: {variable}")
    enclosing_function()
    print()


# Example 11: Decorator and Scope
def scope_logging_decorator(func: Callable) -> Callable:
    """Decorator that demonstrates scope capture."""
    func_name = func.__name__
    call_count = 0
    
    def wrapper(*args, **kwargs):
        nonlocal call_count
        call_count += 1
        print(f"[Call #{call_count}] Calling {func_name} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"[Call #{call_count}] {func_name} returned: {result}")
        return result
    
    wrapper.call_count = lambda: call_count
    wrapper.reset_count = lambda: nonlocal_reset()
    
    def nonlocal_reset():
        nonlocal call_count
        call_count = 0
    
    return wrapper


@scope_logging_decorator
def calculate_area(length: float, width: float) -> float:
    """Calculate rectangle area (decorated function)."""
    return length * width


def demonstrate_decorator_scope():
    """Demonstrate scope in decorators."""
    print("11. Decorator Scope")
    print("-" * 25)
    
    area1 = calculate_area(5, 3)
    area2 = calculate_area(10, 7)
    area3 = calculate_area(2.5, 4.2)
    
    print(f"Total calls made: {calculate_area.call_count()}")
    print()


# Main demonstration function
def main():
    """Run all scope demonstration examples."""
    print("=== Day 5: Variable Scope Examples ===")
    print()
    
    # Run all demonstrations
    demonstrate_basic_scope()
    demonstrate_shadowing()
    demonstrate_global_keyword()
    demonstrate_nonlocal()
    demonstrate_closures()
    
    # Test parameter scope
    test_var = "outside variable"
    demonstrate_parameter_scope(test_var, "custom param")
    print(f"test_var after function call: {test_var}")  # Unchanged
    print()
    
    demonstrate_mutable_scope()
    demonstrate_builtin_scope()
    demonstrate_practical_scope()
    demonstrate_scope_chain()
    demonstrate_decorator_scope()
    
    # Final scope summary
    print("📚 Key Learning Points:")
    print("• LEGB Rule: Local -> Enclosing -> Global -> Built-in scope resolution")
    print("• Use 'global' keyword to modify global variables inside functions")
    print("• Use 'nonlocal' keyword to modify enclosing scope variables")
    print("• Local variables shadow global variables with the same name")
    print("• Function parameters create local scope")
    print("• Mutable objects can be modified through references")
    print("• Closures capture and remember enclosing scope")
    print("• Avoid shadowing built-in functions")
    print("• Scope management is crucial for maintainable code")
    print("• Class variables vs instance variables have different scope rules")


if __name__ == "__main__":
    main()
