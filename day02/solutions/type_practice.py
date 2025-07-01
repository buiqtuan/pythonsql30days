"""
Day 2 Solution: Type Practice
============================

SOLUTION with comprehensive type handling and conversion examples

This solution demonstrates:
- Type checking with type() and isinstance()
- Type conversion (casting) with error handling
- Type validation and input sanitization
- Advanced type manipulation techniques
- Real-world type handling scenarios
"""

# =============================================================================
# BASIC SOLUTION
# =============================================================================

print("=== BASIC TYPE PRACTICE SOLUTION ===\n")

# Create variables of different types
name = "Alice"
age = 28
height = 5.7
is_student = True
account_balance = 1500.50

# Check types
print("1. Checking Data Types:")
print(f"name = '{name}' → type: {type(name).__name__}")
print(f"age = {age} → type: {type(age).__name__}")
print(f"height = {height} → type: {type(height).__name__}")
print(f"is_student = {is_student} → type: {type(is_student).__name__}")
print(f"account_balance = {account_balance} → type: {type(account_balance).__name__}")

print("\n2. Type Casting Examples:")

# String to number conversions
str_number = "42"
str_float = "3.14"
print(f"'{str_number}' → int: {int(str_number)}")
print(f"'{str_float}' → float: {float(str_float)}")

# Number to string conversions
print(f"{age} → string: '{str(age)}'")
print(f"{height} → string: '{str(height)}'")

# Boolean conversions
print(f"bool(1): {bool(1)}")
print(f"bool(0): {bool(0)}")
print(f"bool('hello'): {bool('hello')}")
print(f"bool(''): {bool('')}")

print("\n3. Type Checking with isinstance():")
print(f"isinstance(age, int): {isinstance(age, int)}")
print(f"isinstance(height, float): {isinstance(height, float)}")
print(f"isinstance(name, str): {isinstance(name, str)}")
print(f"isinstance(age, (int, float)): {isinstance(age, (int, float))}")

print("\n🎉 Basic type practice complete!")

# =============================================================================
# ENHANCED SOLUTION WITH COMPREHENSIVE TYPE HANDLING
# =============================================================================

def comprehensive_type_demonstration():
    """Comprehensive demonstration of type handling in Python"""
    
    print("\n" + "="*70)
    print("              COMPREHENSIVE TYPE HANDLING DEMO")
    print("="*70)
    
    # =============================================================================
    # 1. TYPE INTROSPECTION
    # =============================================================================
    
    print("\n🔍 TYPE INTROSPECTION:")
    print("-" * 25)
    
    sample_values = [
        42,                    # int
        3.14,                  # float
        "Hello",               # str
        True,                  # bool
        None,                  # NoneType
        [1, 2, 3],            # list
        (1, 2, 3),            # tuple
        {"a": 1},             # dict
        {1, 2, 3},            # set
        3 + 4j,               # complex
    ]
    
    print(f"{'Value':<15} {'Type':<15} {'Type Name':<15} {'Class'}")
    print("-" * 65)
    
    for value in sample_values:
        value_str = str(value)[:12] + "..." if len(str(value)) > 12 else str(value)
        print(f"{value_str:<15} {str(type(value)):<15} {type(value).__name__:<15} {value.__class__.__name__}")
    
    # =============================================================================
    # 2. SAFE TYPE CONVERSION
    # =============================================================================
    
    print("\n🛡️ SAFE TYPE CONVERSION:")
    print("-" * 30)
    
    def safe_int_convert(value):
        """Safely convert value to integer with detailed feedback"""
        try:
            result = int(value)
            return result, True, f"Successfully converted '{value}' to {result}"
        except ValueError as e:
            return None, False, f"Cannot convert '{value}' to int: {e}"
        except OverflowError as e:
            return None, False, f"Number too large to convert: {e}"
    
    def safe_float_convert(value):
        """Safely convert value to float with detailed feedback"""
        try:
            result = float(value)
            return result, True, f"Successfully converted '{value}' to {result}"
        except ValueError as e:
            return None, False, f"Cannot convert '{value}' to float: {e}"
        except OverflowError as e:
            return None, False, f"Number too large to convert: {e}"
    
    # Test cases for conversion
    test_values = [
        "123",          # Valid integer string
        "45.67",        # Valid float string
        "3.14e2",       # Scientific notation
        "abc",          # Invalid string
        "",             # Empty string
        "123abc",       # Mixed string
        "  89  ",       # String with whitespace
        True,           # Boolean
        False,          # Boolean
        None,           # None value
    ]
    
    print("Testing integer conversion:")
    for value in test_values:
        result, success, message = safe_int_convert(value)
        status = "✅" if success else "❌"
        print(f"{status} {message}")
    
    print("\nTesting float conversion:")
    for value in test_values[:7]:  # Skip problematic ones for float
        result, success, message = safe_float_convert(value)
        status = "✅" if success else "❌"
        print(f"{status} {message}")
    
    # =============================================================================
    # 3. TYPE VALIDATION
    # =============================================================================
    
    print("\n✅ TYPE VALIDATION:")
    print("-" * 20)
    
    def validate_user_data(data):
        """Validate user data with comprehensive type checking"""
        validations = []
        
        # Check if it's a valid name (string, not empty, only letters and spaces)
        if isinstance(data, str):
            if data.strip():
                if data.replace(" ", "").isalpha():
                    validations.append(("Name", "Valid string name"))
                else:
                    validations.append(("Name", "Invalid - contains non-alphabetic characters"))
            else:
                validations.append(("Name", "Invalid - empty string"))
        
        # Check if it's a valid age (integer, positive, reasonable range)
        if isinstance(data, (int, float)):
            if isinstance(data, int) or data.is_integer():
                age = int(data)
                if 0 <= age <= 150:
                    validations.append(("Age", f"Valid age: {age}"))
                else:
                    validations.append(("Age", f"Invalid age range: {age}"))
            else:
                validations.append(("Age", "Invalid - not a whole number"))
        
        # Check if it's a valid price (number, positive)
        if isinstance(data, (int, float)):
            if data >= 0:
                validations.append(("Price", f"Valid price: ${data:.2f}"))
            else:
                validations.append(("Price", f"Invalid price: ${data:.2f} (negative)"))
        
        # Check if it's a valid boolean
        if isinstance(data, bool):
            validations.append(("Boolean", f"Valid boolean: {data}"))
        
        return validations
    
    # Test validation
    test_data = [
        "John Doe",
        25,
        -5,
        99.99,
        True,
        "123",
        "",
        "John123",
        3.5,  # Age with decimal
    ]
    
    for item in test_data:
        print(f"\nValidating: {repr(item)}")
        validations = validate_user_data(item)
        for category, message in validations:
            print(f"  {category}: {message}")
    
    # =============================================================================
    # 4. ADVANCED TYPE CONVERSIONS
    # =============================================================================
    
    print("\n🚀 ADVANCED TYPE CONVERSIONS:")
    print("-" * 35)
    
    # String to various types
    data_strings = [
        "123",           # Integer
        "45.67",         # Float
        "true",          # Boolean (string)
        "false",         # Boolean (string)
        "1,234.56",      # Number with comma
        "$99.99",        # Currency
        "25%",           # Percentage
        "2023-12-25",    # Date string
    ]
    
    print("Advanced string conversions:")
    for s in data_strings:
        print(f"\nInput: '{s}'")
        
        # Try integer conversion
        try:
            # Handle comma-separated numbers
            clean_s = s.replace(",", "").replace("$", "").replace("%", "")
            if s.endswith("%"):
                # Convert percentage to decimal
                num_val = float(clean_s) / 100
                print(f"  As percentage: {num_val:.4f} ({num_val:.2%})")
            elif s.startswith("$"):
                # Convert currency
                currency_val = float(clean_s)
                print(f"  As currency: ${currency_val:.2f}")
            elif s.lower() in ["true", "false"]:
                # Convert boolean strings
                bool_val = s.lower() == "true"
                print(f"  As boolean: {bool_val}")
            else:
                # Try numeric conversion
                if "." in clean_s:
                    float_val = float(clean_s)
                    print(f"  As float: {float_val}")
                else:
                    int_val = int(clean_s)
                    print(f"  As integer: {int_val}")
        except ValueError:
            print(f"  Cannot convert to number")
    
    # =============================================================================
    # 5. TYPE COERCION AND DUCK TYPING
    # =============================================================================
    
    print("\n🦆 TYPE COERCION AND DUCK TYPING:")
    print("-" * 40)
    
    def process_numeric_data(data):
        """Process data that 'looks like' a number (duck typing)"""
        try:
            # Try to use it as a number
            numeric_value = float(data)
            return {
                "original": data,
                "type": type(data).__name__,
                "numeric_value": numeric_value,
                "doubled": numeric_value * 2,
                "square": numeric_value ** 2,
                "is_integer": numeric_value.is_integer(),
                "absolute": abs(numeric_value)
            }
        except (ValueError, TypeError):
            return {
                "original": data,
                "type": type(data).__name__,
                "error": "Cannot be processed as numeric data"
            }
    
    # Test duck typing
    duck_test_data = [
        42,           # int
        3.14,         # float
        "123",        # string that looks like number
        "45.67",      # string that looks like float
        True,         # bool (True == 1)
        False,        # bool (False == 0)
        "abc",        # string that doesn't look like number
    ]
    
    print("Duck typing test - processing 'numeric-like' data:")
    for item in duck_test_data:
        result = process_numeric_data(item)
        print(f"\nInput: {repr(item)} ({result['type']})")
        if 'error' in result:
            print(f"  ❌ {result['error']}")
        else:
            print(f"  ✅ Numeric value: {result['numeric_value']}")
            print(f"     Doubled: {result['doubled']}")
            print(f"     Square: {result['square']}")

def practical_type_handling():
    """Practical examples of type handling in real scenarios"""
    
    print("\n" + "="*70)
    print("              PRACTICAL TYPE HANDLING SCENARIOS")
    print("="*70)
    
    # =============================================================================
    # 1. USER INPUT PROCESSING
    # =============================================================================
    
    print("\n👤 USER INPUT PROCESSING:")
    print("-" * 30)
    
    def get_validated_input(prompt, expected_type, validator=None):
        """Get validated input from user (simulated)"""
        # Simulated user inputs
        simulated_inputs = {
            "age": ["25", "abc", "-5", "150", "30"],
            "price": ["99.99", "-10", "abc", "0", "1000.50"],
            "name": ["John Doe", "", "123", "John123", "Alice"]
        }
        
        # Get the appropriate simulation based on prompt
        if "age" in prompt.lower():
            inputs = simulated_inputs["age"]
        elif "price" in prompt.lower():
            inputs = simulated_inputs["price"]
        else:
            inputs = simulated_inputs["name"]
        
        print(f"\nSimulating input for: {prompt}")
        
        for user_input in inputs:
            print(f"  User enters: '{user_input}'")
            
            try:
                if expected_type == int:
                    value = int(user_input)
                    if validator and not validator(value):
                        print(f"    ❌ Validation failed")
                        continue
                    print(f"    ✅ Valid integer: {value}")
                    return value
                    
                elif expected_type == float:
                    value = float(user_input)
                    if validator and not validator(value):
                        print(f"    ❌ Validation failed")
                        continue
                    print(f"    ✅ Valid float: {value}")
                    return value
                    
                elif expected_type == str:
                    if validator and not validator(user_input):
                        print(f"    ❌ Validation failed")
                        continue
                    print(f"    ✅ Valid string: '{user_input}'")
                    return user_input
                    
            except ValueError:
                print(f"    ❌ Invalid {expected_type.__name__}")
                continue
        
        print(f"    ❌ No valid input found")
        return None
    
    # Validators
    def valid_age(age):
        return 0 <= age <= 120
    
    def valid_price(price):
        return price >= 0
    
    def valid_name(name):
        return name.strip() and name.replace(" ", "").isalpha()
    
    # Simulate getting validated inputs
    age = get_validated_input("Enter your age: ", int, valid_age)
    price = get_validated_input("Enter price: ", float, valid_price)
    name = get_validated_input("Enter your name: ", str, valid_name)
    
    # =============================================================================
    # 2. DATA CLEANING AND NORMALIZATION
    # =============================================================================
    
    print("\n🧹 DATA CLEANING AND NORMALIZATION:")
    print("-" * 40)
    
    def clean_and_normalize_data(raw_data):
        """Clean and normalize various types of data"""
        cleaned_data = []
        
        for item in raw_data:
            original = item
            result = {"original": original, "cleaned": None, "type": None, "errors": []}
            
            try:
                # Handle None values
                if item is None:
                    result["cleaned"] = None
                    result["type"] = "null"
                
                # Handle strings
                elif isinstance(item, str):
                    # Remove extra whitespace
                    cleaned = item.strip()
                    
                    # Try to convert to number if it looks like one
                    if cleaned.replace(".", "").replace("-", "").isdigit():
                        try:
                            if "." in cleaned:
                                result["cleaned"] = float(cleaned)
                                result["type"] = "float"
                            else:
                                result["cleaned"] = int(cleaned)
                                result["type"] = "integer"
                        except ValueError:
                            result["cleaned"] = cleaned
                            result["type"] = "string"
                    # Check for boolean strings
                    elif cleaned.lower() in ["true", "false", "yes", "no", "1", "0"]:
                        bool_map = {"true": True, "false": False, "yes": True, "no": False, "1": True, "0": False}
                        result["cleaned"] = bool_map[cleaned.lower()]
                        result["type"] = "boolean"
                    else:
                        result["cleaned"] = cleaned
                        result["type"] = "string"
                
                # Handle numbers
                elif isinstance(item, (int, float)):
                    result["cleaned"] = item
                    result["type"] = "integer" if isinstance(item, int) else "float"
                
                # Handle booleans
                elif isinstance(item, bool):
                    result["cleaned"] = item
                    result["type"] = "boolean"
                
                else:
                    result["cleaned"] = str(item)
                    result["type"] = "string"
                    result["errors"].append("Unknown type converted to string")
                    
            except Exception as e:
                result["errors"].append(f"Processing error: {e}")
                result["cleaned"] = str(item)
                result["type"] = "string"
            
            cleaned_data.append(result)
        
        return cleaned_data
    
    # Test data cleaning
    messy_data = [
        "  123  ",      # String with whitespace
        "45.67",        # Numeric string
        "true",         # Boolean string
        "",             # Empty string
        None,           # None value
        42,             # Integer
        3.14,           # Float
        "abc",          # Regular string
        "  YES  ",      # Boolean-like string
        "0",            # Zero string
    ]
    
    print("Cleaning messy data:")
    cleaned_results = clean_and_normalize_data(messy_data)
    
    for result in cleaned_results:
        status = "✅" if not result["errors"] else "⚠️"
        print(f"{status} {repr(result['original']):>15} → {repr(result['cleaned']):>15} ({result['type']})")
        if result["errors"]:
            for error in result["errors"]:
                print(f"   ⚠️  {error}")

def type_handling_best_practices():
    """Demonstrate best practices for type handling"""
    
    print("\n" + "="*70)
    print("              TYPE HANDLING BEST PRACTICES")
    print("="*70)
    
    print("""
📖 TYPE HANDLING CONCEPTS:

1. TYPE CHECKING:
   • type(obj): Returns exact type
   • isinstance(obj, type): Checks if object is instance of type
   • hasattr(obj, 'method'): Checks if object has attribute/method

2. TYPE CONVERSION:
   • Explicit: int(), float(), str(), bool()
   • Implicit: Python automatically converts in some operations
   • Custom: Implement __int__(), __float__(), __str__() methods

3. TYPE VALIDATION:
   • Always validate user input
   • Handle conversion errors gracefully
   • Use appropriate data types for your data

🎯 BEST PRACTICES:

1. USE isinstance() for type checking:
   ✅ isinstance(value, (int, float))  # Multiple types
   ❌ type(value) == int               # Exact type only

2. HANDLE conversion errors:
   ✅ try: int(value) except ValueError: handle_error()
   ❌ int(value)  # Can raise unhandled exception

3. VALIDATE input data:
   ✅ Validate range, format, and business rules
   ✅ Provide clear error messages
   ✅ Sanitize input before processing

4. USE appropriate data types:
   ✅ Decimal for financial calculations
   ✅ datetime for dates and times
   ✅ Enum for limited choices

5. DOCUMENT expected types:
   ✅ Use type hints: def func(value: int) -> str:
   ✅ Document in docstrings
   ✅ Validate at runtime when needed

❌ COMMON MISTAKES:
   • Not handling ValueError in type conversion
   • Using == instead of isinstance() for type checking
   • Not validating user input
   • Assuming string input is always valid
   • Not providing fallback values for conversion failures

🔍 DEBUGGING TIPS:
   • Use repr() to see exact string content
   • Check for hidden whitespace with .strip()
   • Test edge cases: None, empty strings, negative numbers
   • Use debugger to inspect variable types during execution
""")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    # Run comprehensive type demonstration
    comprehensive_type_demonstration()
    
    # Show practical examples
    practical_type_handling()
    
    # Show best practices
    type_handling_best_practices()
    
    print("\n🎉 Type practice solution complete!")
    print("Next: Control structures and conditional logic!")
