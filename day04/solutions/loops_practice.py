"""
Day 4 Solution: Loops Practice
=====================================

SOLUTION with comprehensive loop patterns and techniques

This solution demonstrates:
- for loops with different iterables
- while loops with various conditions
- Loop control statements (break, continue)
- Nested loops and loop patterns
- Real-world loop applications
"""

# =============================================================================
# BASIC SOLUTION - FUNDAMENTAL LOOP PATTERNS
# =============================================================================

print("=== BASIC LOOPS PRACTICE SOLUTION ===")

# 1. Basic for loop with range
print("\n1. BASIC FOR LOOP WITH RANGE:")
print("Counting from 1 to 10:")
for i in range(1, 11):
    print(f"Count: {i}")

# 2. For loop with step
print("\n2. FOR LOOP WITH STEP:")
print("Even numbers from 2 to 20:")
for i in range(2, 21, 2):
    print(f"Even: {i}")

# 3. Basic while loop
print("\n3. BASIC WHILE LOOP:")
print("Countdown from 5:")
count = 5
while count > 0:
    print(f"Countdown: {count}")
    count -= 1
print("Blast off! 🚀")

# 4. Loop through a list
print("\n4. LOOP THROUGH A LIST:")
fruits = ["apple", "banana", "orange", "grape", "kiwi"]
print("Fruits in the basket:")
for fruit in fruits:
    print(f"- {fruit}")

# 5. Loop with enumerate
print("\n5. LOOP WITH ENUMERATE:")
print("Numbered fruit list:")
for index, fruit in enumerate(fruits, 1):
    print(f"{index}. {fruit}")

print("\n🎉 Basic loops practice complete!")

# =============================================================================
# ENHANCED SOLUTION WITH COMPREHENSIVE LOOP TECHNIQUES
# =============================================================================

def comprehensive_loop_demonstrations():
    """Comprehensive demonstration of loop patterns and techniques"""
    
    print("\n" + "="*70)
    print("              COMPREHENSIVE LOOP DEMONSTRATIONS")
    print("="*70)
    
    # =============================================================================
    # 1. DIFFERENT TYPES OF LOOPS
    # =============================================================================
    
    def basic_loop_types():
        """Demonstrate different basic loop types"""
        print("\n🔄 BASIC LOOP TYPES:")
        print("-" * 25)
        
        # Range-based loops
        print("\nA. Range-based loops:")
        print("   range(5):", end=" ")
        for i in range(5):
            print(i, end=" ")
        print()
        
        print("   range(2, 8):", end=" ")
        for i in range(2, 8):
            print(i, end=" ")
        print()
        
        print("   range(0, 10, 2):", end=" ")
        for i in range(0, 10, 2):
            print(i, end=" ")
        print()
        
        print("   range(10, 0, -1):", end=" ")
        for i in range(10, 0, -1):
            print(i, end=" ")
        print()
        
        # String iteration
        print("\nB. String iteration:")
        word = "Python"
        print(f"   Letters in '{word}':", end=" ")
        for char in word:
            print(char, end=" ")
        print()
        
        # List iteration
        print("\nC. List iteration:")
        numbers = [10, 20, 30, 40, 50]
        print(f"   Numbers: {numbers}")
        for num in numbers:
            print(f"   Processing: {num}")
        
        # Dictionary iteration
        print("\nD. Dictionary iteration:")
        student_grades = {"Alice": 95, "Bob": 87, "Carol": 92}
        print("   Student grades:")
        for name, grade in student_grades.items():
            print(f"   {name}: {grade}")
    
    def while_loop_patterns():
        """Demonstrate various while loop patterns"""
        print("\n⏳ WHILE LOOP PATTERNS:")
        print("-" * 25)
        
        # Counter-based while loop
        print("\nA. Counter-based while loop:")
        counter = 0
        print("   Counting to 5:", end=" ")
        while counter < 5:
            print(counter, end=" ")
            counter += 1
        print()
        
        # Condition-based while loop
        print("\nB. Condition-based while loop:")
        number = 1
        print("   Powers of 2 less than 100:", end=" ")
        while number < 100:
            print(number, end=" ")
            number *= 2
        print()
        
        # Input validation loop (simulated)
        print("\nC. Input validation pattern:")
        valid_inputs = ["yes", "no", "maybe"]
        simulated_inputs = ["invalid", "bad", "yes"]  # Simulated user inputs
        
        for i, user_input in enumerate(simulated_inputs):
            print(f"   Attempt {i+1}: User enters '{user_input}'")
            if user_input in valid_inputs:
                print(f"   ✅ Valid input accepted: {user_input}")
                break
            else:
                print(f"   ❌ Invalid input, try again...")
        
        # Accumulator pattern
        print("\nD. Accumulator pattern:")
        total = 0
        numbers = [5, 10, 15, 20]
        i = 0
        print(f"   Adding numbers {numbers}:")
        while i < len(numbers):
            total += numbers[i]
            print(f"   Step {i+1}: total = {total}")
            i += 1
        print(f"   Final total: {total}")
    
    # =============================================================================
    # 2. LOOP CONTROL STATEMENTS
    # =============================================================================
    
    def loop_control_statements():
        """Demonstrate break, continue, and else in loops"""
        print("\n🎮 LOOP CONTROL STATEMENTS:")
        print("-" * 30)
        
        # Break statement
        print("\nA. BREAK statement - exit loop early:")
        print("   Finding first number divisible by 7:")
        for num in range(10, 50):
            if num % 7 == 0:
                print(f"   Found: {num} is divisible by 7")
                break
            print(f"   Checking: {num}")
        
        # Continue statement
        print("\nB. CONTINUE statement - skip iteration:")
        print("   Printing only even numbers from 1 to 10:")
        for num in range(1, 11):
            if num % 2 != 0:  # Skip odd numbers
                continue
            print(f"   Even number: {num}")
        
        # Loop with else
        print("\nC. LOOP with ELSE - executes if loop completes:")
        print("   Searching for number 15 in list [1, 5, 10, 20]:")
        search_list = [1, 5, 10, 20]
        target = 15
        for num in search_list:
            if num == target:
                print(f"   Found {target}!")
                break
            print(f"   Checking: {num}")
        else:
            print(f"   {target} not found in the list")
        
        # Nested break and continue
        print("\nD. NESTED loops with break/continue:")
        print("   Finding prime numbers from 2 to 20:")
        for num in range(2, 21):
            is_prime = True
            for divisor in range(2, int(num**0.5) + 1):
                if num % divisor == 0:
                    is_prime = False
                    break  # Break inner loop
            if is_prime:
                print(f"   Prime: {num}")
    
    # =============================================================================
    # 3. NESTED LOOPS AND PATTERNS
    # =============================================================================
    
    def nested_loop_patterns():
        """Demonstrate nested loops and pattern creation"""
        print("\n🎨 NESTED LOOP PATTERNS:")
        print("-" * 30)
        
        # Multiplication table
        print("\nA. Multiplication table (5x5):")
        print("     ", end="")
        for j in range(1, 6):
            print(f"{j:4}", end="")
        print()
        
        for i in range(1, 6):
            print(f"{i:4}:", end="")
            for j in range(1, 6):
                print(f"{i*j:4}", end="")
            print()
        
        # Star patterns
        print("\nB. Star patterns:")
        
        # Right triangle
        print("   Right triangle:")
        for i in range(1, 6):
            for j in range(i):
                print("*", end="")
            print()
        
        # Pyramid
        print("\n   Pyramid:")
        for i in range(1, 6):
            # Print spaces
            for j in range(5 - i):
                print(" ", end="")
            # Print stars
            for j in range(2 * i - 1):
                print("*", end="")
            print()
        
        # Number patterns
        print("\nC. Number patterns:")
        print("   Pascal's triangle (first 5 rows):")
        for i in range(5):
            # Calculate Pascal's triangle values
            for j in range(5 - i):
                print(" ", end="")
            
            for j in range(i + 1):
                # Calculate binomial coefficient
                if j == 0 or j == i:
                    value = 1
                else:
                    # Simple calculation for small numbers
                    value = 1
                    for k in range(j):
                        value = value * (i - k) // (k + 1)
                print(f"{value:2}", end="")
            print()
    
    # =============================================================================
    # 4. ADVANCED LOOP TECHNIQUES
    # =============================================================================
    
    def advanced_loop_techniques():
        """Demonstrate advanced loop techniques and optimizations"""
        print("\n🚀 ADVANCED LOOP TECHNIQUES:")
        print("-" * 35)
        
        # Zip for parallel iteration
        print("\nA. ZIP for parallel iteration:")
        names = ["Alice", "Bob", "Carol"]
        ages = [25, 30, 35]
        cities = ["New York", "London", "Tokyo"]
        
        print("   Student information:")
        for name, age, city in zip(names, ages, cities):
            print(f"   {name} is {age} years old and lives in {city}")
        
        # Enumerate with start parameter
        print("\nB. ENUMERATE with custom start:")
        tasks = ["Review code", "Write tests", "Update docs", "Deploy"]
        print("   Project tasks:")
        for priority, task in enumerate(tasks, start=1):
            print(f"   Priority {priority}: {task}")
        
        # Reversed iteration
        print("\nC. REVERSED iteration:")
        countdown_list = [5, 4, 3, 2, 1]
        print("   Countdown:", end=" ")
        for num in reversed(countdown_list):
            print(num, end=" ")
        print("Blast off! 🚀")
        
        # Sorted iteration
        print("\nD. SORTED iteration:")
        unsorted_scores = [85, 92, 78, 96, 81]
        print(f"   Original scores: {unsorted_scores}")
        print("   Sorted scores (ascending):", end=" ")
        for score in sorted(unsorted_scores):
            print(score, end=" ")
        print()
        
        print("   Sorted scores (descending):", end=" ")
        for score in sorted(unsorted_scores, reverse=True):
            print(score, end=" ")
        print()
        
        # Filter with loop
        print("\nE. FILTER pattern in loop:")
        all_numbers = range(1, 21)
        print("   Even numbers from 1-20:", end=" ")
        for num in all_numbers:
            if num % 2 == 0:
                print(num, end=" ")
        print()
        
        # Map pattern with loop
        print("\nF. MAP pattern in loop:")
        celsius_temps = [0, 10, 20, 30, 40]
        print("   Celsius to Fahrenheit conversion:")
        for celsius in celsius_temps:
            fahrenheit = (celsius * 9/5) + 32
            print(f"   {celsius}°C = {fahrenheit}°F")
    
    # Run all demonstrations
    basic_loop_types()
    while_loop_patterns()
    loop_control_statements()
    nested_loop_patterns()
    advanced_loop_techniques()

def practical_loop_applications():
    """Demonstrate practical applications of loops"""
    
    print("\n" + "="*70)
    print("              PRACTICAL LOOP APPLICATIONS")
    print("="*70)
    
    # =============================================================================
    # 1. DATA PROCESSING
    # =============================================================================
    
    def data_processing_examples():
        """Real-world data processing with loops"""
        print("\n💾 DATA PROCESSING EXAMPLES:")
        print("-" * 35)
        
        # Sales data analysis
        print("\nA. Sales data analysis:")
        daily_sales = [1200, 1450, 980, 1650, 1800, 1320, 1100]
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        
        total_sales = 0
        max_sales = 0
        best_day = ""
        
        print("   Daily sales report:")
        for day, sales in zip(days, daily_sales):
            total_sales += sales
            if sales > max_sales:
                max_sales = sales
                best_day = day
            print(f"   {day}: ${sales:,}")
        
        average_sales = total_sales / len(daily_sales)
        print(f"\n   📊 Summary:")
        print(f"   Total weekly sales: ${total_sales:,}")
        print(f"   Average daily sales: ${average_sales:,.2f}")
        print(f"   Best sales day: {best_day} (${max_sales:,})")
        
        # Grade processing
        print("\nB. Student grade processing:")
        student_data = [
            ("Alice", [85, 92, 78, 88]),
            ("Bob", [90, 87, 85, 91]),
            ("Carol", [78, 82, 85, 80]),
            ("David", [95, 89, 92, 96])
        ]
        
        print("   Student grade analysis:")
        class_total = 0
        student_count = 0
        
        for name, grades in student_data:
            student_average = sum(grades) / len(grades)
            class_total += student_average
            student_count += 1
            
            letter_grade = "A" if student_average >= 90 else "B" if student_average >= 80 else "C"
            print(f"   {name}: Average = {student_average:.1f} (Grade: {letter_grade})")
        
        class_average = class_total / student_count
        print(f"\n   📚 Class average: {class_average:.1f}")
    
    def algorithm_implementations():
        """Implement common algorithms using loops"""
        print("\n🧮 ALGORITHM IMPLEMENTATIONS:")
        print("-" * 35)
        
        # Bubble sort
        print("\nA. Bubble sort algorithm:")
        numbers = [64, 34, 25, 12, 22, 11, 90]
        print(f"   Original: {numbers}")
        
        # Create a copy for sorting
        sorted_numbers = numbers.copy()
        n = len(sorted_numbers)
        
        for i in range(n):
            for j in range(0, n - i - 1):
                if sorted_numbers[j] > sorted_numbers[j + 1]:
                    # Swap elements
                    sorted_numbers[j], sorted_numbers[j + 1] = sorted_numbers[j + 1], sorted_numbers[j]
        
        print(f"   Sorted:   {sorted_numbers}")
        
        # Linear search
        print("\nB. Linear search algorithm:")
        search_list = [10, 23, 45, 70, 11, 15]
        target = 70
        
        print(f"   Searching for {target} in {search_list}")
        found_index = -1
        
        for i, value in enumerate(search_list):
            print(f"   Checking index {i}: {value}")
            if value == target:
                found_index = i
                break
        
        if found_index != -1:
            print(f"   ✅ Found {target} at index {found_index}")
        else:
            print(f"   ❌ {target} not found")
        
        # Fibonacci sequence generation
        print("\nC. Fibonacci sequence generation:")
        print("   First 10 Fibonacci numbers:")
        
        fib_count = 10
        a, b = 0, 1
        fibonacci_sequence = []
        
        for i in range(fib_count):
            fibonacci_sequence.append(a)
            a, b = b, a + b
        
        print(f"   {fibonacci_sequence}")
        
        # Prime number sieve
        print("\nD. Prime number sieve (up to 30):")
        max_num = 30
        is_prime = [True] * (max_num + 1)
        is_prime[0] = is_prime[1] = False
        
        for i in range(2, int(max_num**0.5) + 1):
            if is_prime[i]:
                for j in range(i*i, max_num + 1, i):
                    is_prime[j] = False
        
        primes = []
        for i in range(2, max_num + 1):
            if is_prime[i]:
                primes.append(i)
        
        print(f"   Prime numbers: {primes}")
    
    def text_processing_examples():
        """Text processing with loops"""
        print("\n📝 TEXT PROCESSING EXAMPLES:")
        print("-" * 35)
        
        # Character frequency count
        print("\nA. Character frequency analysis:")
        text = "hello world programming"
        char_count = {}
        
        for char in text:
            if char.isalpha():  # Only count letters
                char = char.lower()
                char_count[char] = char_count.get(char, 0) + 1
        
        print(f"   Text: '{text}'")
        print("   Character frequencies:")
        for char in sorted(char_count.keys()):
            print(f"   '{char}': {char_count[char]}")
        
        # Word processing
        print("\nB. Word analysis:")
        sentence = "The quick brown fox jumps over the lazy dog"
        words = sentence.lower().split()
        
        word_lengths = {}
        for word in words:
            length = len(word)
            word_lengths[length] = word_lengths.get(length, 0) + 1
        
        print(f"   Sentence: '{sentence}'")
        print("   Word length distribution:")
        for length in sorted(word_lengths.keys()):
            print(f"   {length} letters: {word_lengths[length]} words")
        
        # Password validation
        print("\nC. Password validation:")
        passwords = ["weak", "Better123", "VeryStr0ng!", "short"]
        
        for password in passwords:
            print(f"\n   Validating: '{password}'")
            
            # Check various criteria
            has_upper = any(c.isupper() for c in password)
            has_lower = any(c.islower() for c in password)
            has_digit = any(c.isdigit() for c in password)
            has_special = any(c in "!@#$%^&*" for c in password)
            min_length = len(password) >= 8
            
            criteria = [
                ("Minimum 8 characters", min_length),
                ("Has uppercase letter", has_upper),
                ("Has lowercase letter", has_lower),
                ("Has digit", has_digit),
                ("Has special character", has_special)
            ]
            
            passed_count = 0
            for criterion, passed in criteria:
                status = "✅" if passed else "❌"
                print(f"   {status} {criterion}")
                if passed:
                    passed_count += 1
            
            strength = "Strong" if passed_count >= 4 else "Medium" if passed_count >= 3 else "Weak"
            print(f"   🔒 Password strength: {strength}")
    
    # Run practical applications
    data_processing_examples()
    algorithm_implementations()
    text_processing_examples()

def loop_performance_and_optimization():
    """Demonstrate loop performance considerations and optimizations"""
    
    print("\n" + "="*70)
    print("              LOOP PERFORMANCE AND OPTIMIZATION")
    print("="*70)
    
    import time
    
    def performance_comparisons():
        """Compare performance of different loop approaches"""
        print("\n⚡ PERFORMANCE COMPARISONS:")
        print("-" * 30)
        
        # Large dataset for testing
        large_list = list(range(100000))
        
        # Method 1: Traditional for loop with index
        print("\nA. Traditional for loop with index:")
        start_time = time.perf_counter()
        total1 = 0
        for i in range(len(large_list)):
            total1 += large_list[i]
        end_time = time.perf_counter()
        time1 = (end_time - start_time) * 1000
        print(f"   Time: {time1:.2f} ms, Result: {total1}")
        
        # Method 2: Direct iteration
        print("\nB. Direct iteration:")
        start_time = time.perf_counter()
        total2 = 0
        for value in large_list:
            total2 += value
        end_time = time.perf_counter()
        time2 = (end_time - start_time) * 1000
        print(f"   Time: {time2:.2f} ms, Result: {total2}")
        
        # Method 3: Built-in sum function
        print("\nC. Built-in sum function:")
        start_time = time.perf_counter()
        total3 = sum(large_list)
        end_time = time.perf_counter()
        time3 = (end_time - start_time) * 1000
        print(f"   Time: {time3:.2f} ms, Result: {total3}")
        
        print(f"\n📊 Performance summary:")
        print(f"   Direct iteration is {time1/time2:.1f}x faster than indexed")
        print(f"   Built-in sum is {time2/time3:.1f}x faster than loops")
    
    def optimization_techniques():
        """Demonstrate loop optimization techniques"""
        print("\n🚀 OPTIMIZATION TECHNIQUES:")
        print("-" * 35)
        
        # Technique 1: Early termination
        print("\nA. Early termination with break:")
        numbers = list(range(1, 1000000))
        target = 500000
        
        start_time = time.perf_counter()
        for i, num in enumerate(numbers):
            if num == target:
                result_index = i
                break
        end_time = time.perf_counter()
        
        print(f"   Found {target} at index {result_index}")
        print(f"   Time with early termination: {(end_time - start_time)*1000:.2f} ms")
        
        # Technique 2: List comprehension vs loop
        print("\nB. List comprehension vs traditional loop:")
        
        # Traditional loop
        start_time = time.perf_counter()
        squares_loop = []
        for i in range(10000):
            squares_loop.append(i ** 2)
        end_time = time.perf_counter()
        time_loop = (end_time - start_time) * 1000
        
        # List comprehension
        start_time = time.perf_counter()
        squares_comp = [i ** 2 for i in range(10000)]
        end_time = time.perf_counter()
        time_comp = (end_time - start_time) * 1000
        
        print(f"   Traditional loop: {time_loop:.2f} ms")
        print(f"   List comprehension: {time_comp:.2f} ms")
        print(f"   List comprehension is {time_loop/time_comp:.1f}x faster")
        
        # Technique 3: Avoiding repeated calculations
        print("\nC. Avoiding repeated calculations:")
        text_list = ["hello"] * 10000
        
        # Inefficient: repeated len() call
        start_time = time.perf_counter()
        count1 = 0
        for text in text_list:
            if len(text) > 3:  # len() called every iteration
                count1 += 1
        end_time = time.perf_counter()
        time_inefficient = (end_time - start_time) * 1000
        
        # Efficient: calculate once outside loop
        start_time = time.perf_counter()
        count2 = 0
        min_length = 3
        for text in text_list:
            if len(text) > min_length:
                count2 += 1
        end_time = time.perf_counter()
        time_efficient = (end_time - start_time) * 1000
        
        print(f"   With repeated calculation: {time_inefficient:.2f} ms")
        print(f"   With pre-calculation: {time_efficient:.2f} ms")
        print(f"   Improvement: {time_inefficient/time_efficient:.1f}x faster")
    
    # Run performance demonstrations
    performance_comparisons()
    optimization_techniques()

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    # Run comprehensive loop demonstrations
    comprehensive_loop_demonstrations()
    
    # Show practical applications
    practical_loop_applications()
    
    # Show performance considerations
    loop_performance_and_optimization()
    
    print("\n" + "="*70)
    print("                        LEARNING SUMMARY")
    print("="*70)
    
    print("""
📖 KEY CONCEPTS DEMONSTRATED:

1. LOOP TYPES:
   • for loops: range(), iterables, enumerate(), zip()
   • while loops: condition-based, counter-based
   • Nested loops for multi-dimensional operations
   • Loop control: break, continue, else clause

2. ITERATION PATTERNS:
   • Accumulator pattern (building results)
   • Filter pattern (conditional processing)
   • Map pattern (transformation)
   • Search pattern (finding elements)

3. ADVANCED TECHNIQUES:
   • Parallel iteration with zip()
   • Reversed and sorted iteration
   • Enumerate for index tracking
   • List comprehensions vs loops

4. PERFORMANCE OPTIMIZATION:
   • Early termination with break
   • Avoiding repeated calculations
   • Using built-in functions when appropriate
   • List comprehensions for better performance

🎯 BEST PRACTICES:
   ✅ Use appropriate loop type for the task
   ✅ Prefer direct iteration over index-based when possible
   ✅ Use break and continue for flow control
   ✅ Consider list comprehensions for simple transformations
   ✅ Optimize loops for performance-critical code

💼 REAL-WORLD APPLICATIONS:
   • Data processing and analysis
   • Algorithm implementations
   • Text processing and validation
   • Pattern generation and matching
   • Search and sorting operations

🚀 PROBLEM-SOLVING PATTERNS:
   • Identify the iteration pattern needed
   • Choose the most readable and efficient approach
   • Handle edge cases (empty collections, single items)
   • Consider performance implications for large datasets
   • Use appropriate data structures for the task
""")
    
    print("🎉 Loops practice solution complete!")
    print("Next: List comprehensions and advanced iteration!")
