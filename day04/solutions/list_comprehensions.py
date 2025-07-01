"""
Day 4 Solution: List Comprehensions
==========================================

SOLUTION with comprehensive list comprehension patterns and techniques

This solution demonstrates:
- Basic list comprehension syntax
- Conditional list comprehensions
- Nested list comprehensions
- Dictionary and set comprehensions
- Generator expressions
- Performance comparisons with traditional loops
"""

# =============================================================================
# BASIC SOLUTION - FUNDAMENTAL LIST COMPREHENSIONS
# =============================================================================

print("=== BASIC LIST COMPREHENSIONS SOLUTION ===")

# 1. Basic list comprehension - squares
print("\n1. BASIC LIST COMPREHENSION:")
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(f"Original numbers: {numbers}")
print(f"Squares: {squares}")

# 2. List comprehension with condition
print("\n2. LIST COMPREHENSION WITH CONDITION:")
all_numbers = range(1, 11)
even_numbers = [x for x in all_numbers if x % 2 == 0]
print(f"All numbers: {list(all_numbers)}")
print(f"Even numbers: {even_numbers}")

# 3. List comprehension with transformation and condition
print("\n3. TRANSFORMATION WITH CONDITION:")
words = ["hello", "world", "python", "programming", "list", "comprehension"]
long_words_upper = [word.upper() for word in words if len(word) > 5]
print(f"Original words: {words}")
print(f"Long words (>5 chars) in uppercase: {long_words_upper}")

# 4. Nested list comprehension
print("\n4. NESTED LIST COMPREHENSION:")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(f"Original matrix: {matrix}")
print(f"Flattened: {flattened}")

# 5. Multiple conditions
print("\n5. MULTIPLE CONDITIONS:")
numbers = range(1, 21)
special_numbers = [x for x in numbers if x % 2 == 0 if x % 3 == 0]
print(f"Numbers divisible by both 2 and 3: {special_numbers}")

print("\n🎉 Basic list comprehensions complete!")

# =============================================================================
# ENHANCED SOLUTION WITH COMPREHENSIVE COMPREHENSION TECHNIQUES
# =============================================================================

def comprehensive_comprehension_demonstrations():
    """Comprehensive demonstration of all comprehension types and patterns"""
    
    print("\n" + "="*70)
    print("              COMPREHENSIVE COMPREHENSION DEMONSTRATIONS")
    print("="*70)
    
    # =============================================================================
    # 1. LIST COMPREHENSION PATTERNS
    # =============================================================================
    
    def list_comprehension_patterns():
        """Demonstrate various list comprehension patterns"""
        print("\n📝 LIST COMPREHENSION PATTERNS:")
        print("-" * 35)
        
        # Basic transformations
        print("\nA. Basic transformations:")
        numbers = [1, 2, 3, 4, 5]
        
        # Square each number
        squares = [x**2 for x in numbers]
        print(f"   Squares: {squares}")
        
        # Double each number
        doubled = [x * 2 for x in numbers]
        print(f"   Doubled: {doubled}")
        
        # Convert to strings
        str_numbers = [str(x) for x in numbers]
        print(f"   As strings: {str_numbers}")
        
        # More complex transformations
        print("\nB. Complex transformations:")
        temperatures_celsius = [0, 10, 20, 30, 40]
        temperatures_fahrenheit = [(c * 9/5) + 32 for c in temperatures_celsius]
        print(f"   Celsius: {temperatures_celsius}")
        print(f"   Fahrenheit: {temperatures_fahrenheit}")
        
        # String operations
        print("\nC. String operations:")
        names = ["alice", "bob", "charlie", "diana"]
        
        # Capitalize names
        capitalized = [name.capitalize() for name in names]
        print(f"   Capitalized: {capitalized}")
        
        # Get initials
        initials = [name[0].upper() for name in names]
        print(f"   Initials: {initials}")
        
        # Get name lengths
        name_lengths = [len(name) for name in names]
        print(f"   Name lengths: {name_lengths}")
        
        # Conditional filtering
        print("\nD. Conditional filtering:")
        scores = [85, 92, 78, 96, 81, 89, 73, 94]
        
        # High scores (90+)
        high_scores = [score for score in scores if score >= 90]
        print(f"   High scores (90+): {high_scores}")
        
        # Passing scores (70+) with grade
        passing_with_grade = [(score, "A" if score >= 90 else "B" if score >= 80 else "C") 
                             for score in scores if score >= 70]
        print(f"   Passing scores with grades: {passing_with_grade}")
        
        # Conditional transformation
        print("\nE. Conditional transformation:")
        mixed_numbers = [-3, -1, 0, 2, 5, -2, 8]
        
        # Absolute values of negative numbers, squares of positive
        transformed = [abs(x) if x < 0 else x**2 for x in mixed_numbers]
        print(f"   Original: {mixed_numbers}")
        print(f"   Transformed: {transformed}")
        
        # Replace negatives with zero, keep positives
        cleaned = [x if x >= 0 else 0 for x in mixed_numbers]
        print(f"   Cleaned (negatives → 0): {cleaned}")
    
    def nested_comprehensions():
        """Demonstrate nested list comprehensions"""
        print("\n🔄 NESTED COMPREHENSIONS:")
        print("-" * 25)
        
        # Create multiplication table
        print("\nA. Multiplication table (5x5):")
        mult_table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
        print("   Table:")
        for row in mult_table:
            print(f"   {row}")
        
        # Flatten nested lists
        print("\nB. Flattening nested structures:")
        nested_lists = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
        flattened = [item for sublist in nested_lists for item in sublist]
        print(f"   Nested: {nested_lists}")
        print(f"   Flattened: {flattened}")
        
        # Matrix operations
        print("\nC. Matrix operations:")
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        
        # Transpose matrix
        transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
        print(f"   Original matrix:")
        for row in matrix:
            print(f"   {row}")
        print(f"   Transposed matrix:")
        for row in transposed:
            print(f"   {row}")
        
        # Filter matrix elements
        print("\nD. Filter matrix elements:")
        # Get even numbers from matrix
        even_from_matrix = [num for row in matrix for num in row if num % 2 == 0]
        print(f"   Even numbers from matrix: {even_from_matrix}")
        
        # Create matrix with conditions
        conditional_matrix = [[x if x % 2 == 0 else 0 for x in row] for row in matrix]
        print(f"   Matrix with odd numbers replaced by 0:")
        for row in conditional_matrix:
            print(f"   {row}")
    
    # =============================================================================
    # 2. DICTIONARY COMPREHENSIONS
    # =============================================================================
    
    def dictionary_comprehensions():
        """Demonstrate dictionary comprehension patterns"""
        print("\n📚 DICTIONARY COMPREHENSIONS:")
        print("-" * 30)
        
        # Basic dictionary comprehension
        print("\nA. Basic dictionary comprehensions:")
        numbers = [1, 2, 3, 4, 5]
        
        # Number to square mapping
        squares_dict = {x: x**2 for x in numbers}
        print(f"   Numbers to squares: {squares_dict}")
        
        # String to length mapping
        words = ["apple", "banana", "cherry", "date"]
        word_lengths = {word: len(word) for word in words}
        print(f"   Word lengths: {word_lengths}")
        
        # Conditional dictionary comprehension
        print("\nB. Conditional dictionary comprehensions:")
        scores = {"Alice": 85, "Bob": 92, "Carol": 78, "David": 96, "Eve": 81}
        
        # High performers only
        high_performers = {name: score for name, score in scores.items() if score >= 90}
        print(f"   High performers (90+): {high_performers}")
        
        # Grade assignment
        grades = {name: "A" if score >= 90 else "B" if score >= 80 else "C" 
                 for name, score in scores.items()}
        print(f"   Letter grades: {grades}")
        
        # Dictionary transformations
        print("\nC. Dictionary transformations:")
        original_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
        
        # Swap keys and values
        swapped = {value: key for key, value in original_dict.items()}
        print(f"   Original: {original_dict}")
        print(f"   Swapped: {swapped}")
        
        # Transform values
        doubled_values = {key: value * 2 for key, value in original_dict.items()}
        print(f"   Doubled values: {doubled_values}")
        
        # Filter and transform
        even_doubled = {key: value * 2 for key, value in original_dict.items() 
                       if value % 2 == 0}
        print(f"   Even values doubled: {even_doubled}")
    
    def set_comprehensions():
        """Demonstrate set comprehension patterns"""
        print("\n🎯 SET COMPREHENSIONS:")
        print("-" * 22)
        
        # Basic set comprehension
        print("\nA. Basic set comprehensions:")
        numbers = [1, 2, 2, 3, 3, 3, 4, 4, 5]
        
        # Unique squares
        unique_squares = {x**2 for x in numbers}
        print(f"   Numbers: {numbers}")
        print(f"   Unique squares: {unique_squares}")
        
        # Character set from string
        text = "hello world"
        unique_chars = {char for char in text if char.isalpha()}
        print(f"   Text: '{text}'")
        print(f"   Unique characters: {unique_chars}")
        
        # Conditional set comprehension
        print("\nB. Conditional set comprehensions:")
        words = ["apple", "banana", "cherry", "apricot", "blueberry", "avocado"]
        
        # First letters of words starting with 'a'
        a_words_first_letters = {word[0] for word in words if word.startswith('a')}
        print(f"   Words: {words}")
        print(f"   First letters of 'a' words: {a_words_first_letters}")
        
        # Lengths of long words
        long_word_lengths = {len(word) for word in words if len(word) > 5}
        print(f"   Lengths of long words (>5 chars): {long_word_lengths}")
        
        # Mathematical sets
        print("\nC. Mathematical set operations with comprehensions:")
        # Factors of numbers
        number = 24
        factors = {i for i in range(1, number + 1) if number % i == 0}
        print(f"   Factors of {number}: {factors}")
        
        # Prime numbers up to 30
        primes = {n for n in range(2, 31) 
                 if all(n % i != 0 for i in range(2, int(n**0.5) + 1))}
        print(f"   Prime numbers up to 30: {primes}")
    
    # =============================================================================
    # 3. GENERATOR EXPRESSIONS
    # =============================================================================
    
    def generator_expressions():
        """Demonstrate generator expressions for memory efficiency"""
        print("\n⚡ GENERATOR EXPRESSIONS:")
        print("-" * 25)
        
        # Basic generator expression
        print("\nA. Basic generator expressions:")
        numbers = range(1, 6)
        
        # Generator for squares
        squares_gen = (x**2 for x in numbers)
        print(f"   Generator object: {squares_gen}")
        print(f"   Generated squares: {list(squares_gen)}")
        
        # Memory efficiency demonstration
        print("\nB. Memory efficiency:")
        import sys
        
        # List comprehension (stores all values in memory)
        large_list = [x**2 for x in range(10000)]
        list_size = sys.getsizeof(large_list)
        
        # Generator expression (generates values on demand)
        large_gen = (x**2 for x in range(10000))
        gen_size = sys.getsizeof(large_gen)
        
        print(f"   List comprehension size: {list_size:,} bytes")
        print(f"   Generator expression size: {gen_size:,} bytes")
        print(f"   Memory saved: {list_size/gen_size:.1f}x less memory")
        
        # Using generators with functions
        print("\nC. Generators with built-in functions:")
        numbers = range(1, 101)
        
        # Sum of squares using generator
        sum_of_squares = sum(x**2 for x in numbers)
        print(f"   Sum of squares (1-100): {sum_of_squares:,}")
        
        # Maximum of transformed values
        max_transformed = max(x**3 - x**2 + x for x in range(1, 11))
        print(f"   Max of x³-x²+x (1-10): {max_transformed}")
        
        # Any/all with generators
        has_even = any(x % 2 == 0 for x in [1, 3, 5, 7, 8])
        all_positive = all(x > 0 for x in [1, 2, 3, 4, 5])
        print(f"   Has even number: {has_even}")
        print(f"   All positive: {all_positive}")
    
    # Run all demonstrations
    list_comprehension_patterns()
    nested_comprehensions()
    dictionary_comprehensions()
    set_comprehensions()
    generator_expressions()

def performance_comparisons():
    """Compare performance of comprehensions vs traditional loops"""
    
    print("\n" + "="*70)
    print("              PERFORMANCE COMPARISONS")
    print("="*70)
    
    import time
    
    def benchmark_list_creation():
        """Benchmark different methods of list creation"""
        print("\n⚡ LIST CREATION BENCHMARKS:")
        print("-" * 30)
        
        n = 100000
        
        # Method 1: Traditional for loop
        start_time = time.perf_counter()
        result1 = []
        for i in range(n):
            result1.append(i**2)
        end_time = time.perf_counter()
        time1 = (end_time - start_time) * 1000
        
        # Method 2: List comprehension
        start_time = time.perf_counter()
        result2 = [i**2 for i in range(n)]
        end_time = time.perf_counter()
        time2 = (end_time - start_time) * 1000
        
        # Method 3: Map function
        start_time = time.perf_counter()
        result3 = list(map(lambda x: x**2, range(n)))
        end_time = time.perf_counter()
        time3 = (end_time - start_time) * 1000
        
        # Method 4: Generator expression with list()
        start_time = time.perf_counter()
        result4 = list(i**2 for i in range(n))
        end_time = time.perf_counter()
        time4 = (end_time - start_time) * 1000
        
        print(f"   Traditional loop: {time1:.2f} ms")
        print(f"   List comprehension: {time2:.2f} ms")
        print(f"   Map function: {time3:.2f} ms")
        print(f"   Generator → list: {time4:.2f} ms")
        
        print(f"\n   Performance ratios (vs list comprehension):")
        print(f"   Traditional loop: {time1/time2:.1f}x slower")
        print(f"   Map function: {time3/time2:.1f}x")
        print(f"   Generator → list: {time4/time2:.1f}x")
    
    def benchmark_filtering():
        """Benchmark different filtering methods"""
        print("\n🔍 FILTERING BENCHMARKS:")
        print("-" * 25)
        
        data = list(range(100000))
        
        # Method 1: Traditional loop with append
        start_time = time.perf_counter()
        result1 = []
        for x in data:
            if x % 2 == 0:
                result1.append(x)
        end_time = time.perf_counter()
        time1 = (end_time - start_time) * 1000
        
        # Method 2: List comprehension with condition
        start_time = time.perf_counter()
        result2 = [x for x in data if x % 2 == 0]
        end_time = time.perf_counter()
        time2 = (end_time - start_time) * 1000
        
        # Method 3: Filter function
        start_time = time.perf_counter()
        result3 = list(filter(lambda x: x % 2 == 0, data))
        end_time = time.perf_counter()
        time3 = (end_time - start_time) * 1000
        
        print(f"   Traditional loop: {time1:.2f} ms")
        print(f"   List comprehension: {time2:.2f} ms")
        print(f"   Filter function: {time3:.2f} ms")
        
        print(f"\n   List comprehension is {time1/time2:.1f}x faster than loop")
        print(f"   Filter function is {time2/time3:.1f}x relative to comprehension")
    
    def memory_usage_comparison():
        """Compare memory usage of different approaches"""
        print("\n💾 MEMORY USAGE COMPARISON:")
        print("-" * 30)
        
        import sys
        
        n = 10000
        
        # List comprehension
        list_comp = [x**2 for x in range(n)]
        list_size = sys.getsizeof(list_comp)
        
        # Generator expression
        gen_expr = (x**2 for x in range(n))
        gen_size = sys.getsizeof(gen_expr)
        
        # Traditional list building
        traditional_list = []
        for x in range(n):
            traditional_list.append(x**2)
        trad_size = sys.getsizeof(traditional_list)
        
        print(f"   List comprehension: {list_size:,} bytes")
        print(f"   Generator expression: {gen_size:,} bytes")
        print(f"   Traditional list: {trad_size:,} bytes")
        
        print(f"\n   Memory savings with generator: {list_size/gen_size:.0f}x less")
        
        # Demonstrate lazy evaluation
        print(f"\n   🔄 Lazy evaluation demonstration:")
        print(f"   Generator creates values on-demand, not all at once")
        
        # Show first 5 values from generator
        gen_demo = (x**2 for x in range(n))
        first_five = [next(gen_demo) for _ in range(5)]
        print(f"   First 5 values from generator: {first_five}")
    
    # Run benchmarks
    benchmark_list_creation()
    benchmark_filtering()
    memory_usage_comparison()

def practical_comprehension_examples():
    """Real-world examples using comprehensions"""
    
    print("\n" + "="*70)
    print("              PRACTICAL COMPREHENSION EXAMPLES")
    print("="*70)
    
    def data_analysis_examples():
        """Data analysis tasks using comprehensions"""
        print("\n📊 DATA ANALYSIS EXAMPLES:")
        print("-" * 30)
        
        # Student data analysis
        print("\nA. Student grade analysis:")
        students = [
            {"name": "Alice", "grades": [85, 92, 78, 88]},
            {"name": "Bob", "grades": [90, 87, 85, 91]},
            {"name": "Carol", "grades": [78, 82, 85, 80]},
            {"name": "David", "grades": [95, 89, 92, 96]},
            {"name": "Eve", "grades": [88, 85, 90, 87]}
        ]
        
        # Calculate averages using comprehension
        averages = {student["name"]: sum(student["grades"])/len(student["grades"]) 
                   for student in students}
        print("   Student averages:")
        for name, avg in averages.items():
            print(f"   {name}: {avg:.1f}")
        
        # Find high performers (average >= 90)
        high_performers = [student["name"] for student in students 
                          if sum(student["grades"])/len(student["grades"]) >= 90]
        print(f"   High performers (avg >= 90): {high_performers}")
        
        # Get all individual grades above 90
        high_grades = [grade for student in students for grade in student["grades"] 
                      if grade >= 90]
        print(f"   Individual grades >= 90: {high_grades}")
        
        # Sales data analysis
        print("\nB. Sales data analysis:")
        sales_data = [
            {"product": "Laptop", "price": 999, "quantity": 50},
            {"product": "Mouse", "price": 25, "quantity": 200},
            {"product": "Keyboard", "price": 75, "quantity": 150},
            {"product": "Monitor", "price": 300, "quantity": 80},
            {"product": "Headphones", "price": 150, "quantity": 120}
        ]
        
        # Calculate total revenue per product
        revenues = {item["product"]: item["price"] * item["quantity"] 
                   for item in sales_data}
        print("   Product revenues:")
        for product, revenue in revenues.items():
            print(f"   {product}: ${revenue:,}")
        
        # Find high-value products (revenue > $10,000)
        high_value = [item["product"] for item in sales_data 
                     if item["price"] * item["quantity"] > 10000]
        print(f"   High-value products (>$10k): {high_value}")
        
        # Price categories
        price_categories = {item["product"]: 
                           "Premium" if item["price"] > 200 else 
                           "Mid-range" if item["price"] > 50 else "Budget"
                           for item in sales_data}
        print("   Price categories:")
        for product, category in price_categories.items():
            print(f"   {product}: {category}")
    
    def text_processing_examples():
        """Text processing using comprehensions"""
        print("\n📝 TEXT PROCESSING EXAMPLES:")
        print("-" * 35)
        
        # Word analysis
        print("\nA. Word analysis:")
        text = "The quick brown fox jumps over the lazy dog"
        words = text.split()
        
        # Word lengths
        word_lengths = [len(word) for word in words]
        print(f"   Text: '{text}'")
        print(f"   Word lengths: {word_lengths}")
        
        # Long words (>4 characters)
        long_words = [word for word in words if len(word) > 4]
        print(f"   Long words: {long_words}")
        
        # Word frequency (simplified)
        unique_words = set(word.lower() for word in words)
        word_freq = {word: sum(1 for w in words if w.lower() == word) 
                    for word in unique_words}
        print(f"   Word frequencies: {word_freq}")
        
        # CSV data processing
        print("\nB. CSV-like data processing:")
        csv_data = [
            "name,age,city,salary",
            "Alice,25,New York,75000",
            "Bob,30,London,85000", 
            "Carol,35,Tokyo,95000",
            "David,28,Paris,80000"
        ]
        
        # Parse CSV data
        header = csv_data[0].split(",")
        rows = [row.split(",") for row in csv_data[1:]]
        
        # Create dictionaries for each person
        people = [{header[i]: (int(row[i]) if row[i].isdigit() else row[i]) 
                  for i in range(len(header))} for row in rows]
        
        print("   Parsed data:")
        for person in people:
            print(f"   {person}")
        
        # High earners (salary > 80000)
        high_earners = [person["name"] for person in people 
                       if person["salary"] > 80000]
        print(f"   High earners (>$80k): {high_earners}")
        
        # Email generation
        emails = [f"{person['name'].lower()}@company.com" for person in people]
        print(f"   Generated emails: {emails}")
    
    def algorithm_implementations():
        """Algorithm implementations using comprehensions"""
        print("\n🧮 ALGORITHM IMPLEMENTATIONS:")
        print("-" * 35)
        
        # Prime number generation
        print("\nA. Prime number generation:")
        def is_prime(n):
            return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
        
        primes_up_to_50 = [n for n in range(2, 51) if is_prime(n)]
        print(f"   Prime numbers up to 50: {primes_up_to_50}")
        
        # Fibonacci sequence
        print("\nB. Fibonacci sequence generation:")
        def fibonacci_gen(n):
            fib = [0, 1]
            [fib.append(fib[-1] + fib[-2]) for _ in range(n-2)]
            return fib[:n]
        
        fib_10 = fibonacci_gen(10)
        print(f"   First 10 Fibonacci numbers: {fib_10}")
        
        # Matrix operations
        print("\nC. Matrix operations:")
        matrix_a = [[1, 2], [3, 4]]
        matrix_b = [[5, 6], [7, 8]]
        
        # Matrix addition
        matrix_sum = [[matrix_a[i][j] + matrix_b[i][j] for j in range(len(matrix_a[0]))] 
                     for i in range(len(matrix_a))]
        print(f"   Matrix A: {matrix_a}")
        print(f"   Matrix B: {matrix_b}")
        print(f"   A + B: {matrix_sum}")
        
        # Diagonal elements
        diagonal = [matrix_a[i][i] for i in range(len(matrix_a))]
        print(f"   Diagonal elements of A: {diagonal}")
        
        # Combinatorics
        print("\nD. Combinatorics:")
        # Generate all pairs from two lists
        colors = ["red", "blue", "green"]
        sizes = ["small", "medium", "large"]
        combinations = [(color, size) for color in colors for size in sizes]
        print(f"   Color-size combinations: {combinations}")
        
        # Permutations of a small list (using indices)
        items = ["A", "B", "C"]
        # Simple 2-permutations
        perms_2 = [(items[i], items[j]) for i in range(len(items)) 
                  for j in range(len(items)) if i != j]
        print(f"   2-permutations of {items}: {perms_2}")
    
    # Run practical examples
    data_analysis_examples()
    text_processing_examples()
    algorithm_implementations()

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    # Run comprehensive comprehension demonstrations
    comprehensive_comprehension_demonstrations()
    
    # Show performance comparisons
    performance_comparisons()
    
    # Show practical examples
    practical_comprehension_examples()
    
    print("\n" + "="*70)
    print("                        LEARNING SUMMARY")
    print("="*70)
    
    print("""
📖 KEY CONCEPTS DEMONSTRATED:

1. COMPREHENSION TYPES:
   • List comprehensions: [expr for item in iterable if condition]
   • Dictionary comprehensions: {key: value for item in iterable}
   • Set comprehensions: {expr for item in iterable if condition}
   • Generator expressions: (expr for item in iterable if condition)

2. SYNTAX PATTERNS:
   • Basic: [x for x in items]
   • With condition: [x for x in items if condition]
   • With transformation: [f(x) for x in items]
   • Nested: [x for sublist in lists for x in sublist]
   • Multiple conditions: [x for x in items if cond1 if cond2]

3. PERFORMANCE BENEFITS:
   • Faster than traditional loops
   • More memory efficient (generators)
   • More readable and Pythonic
   • Built-in optimization

4. ADVANCED TECHNIQUES:
   • Conditional expressions in comprehensions
   • Nested comprehensions for complex data
   • Generator expressions for memory efficiency
   • Combining with built-in functions

🎯 BEST PRACTICES:
   ✅ Use comprehensions for simple transformations and filtering
   ✅ Prefer generators for large datasets or infinite sequences
   ✅ Keep comprehensions readable - break complex ones into functions
   ✅ Use appropriate comprehension type for the data structure needed
   ✅ Consider performance implications for nested comprehensions

💼 REAL-WORLD APPLICATIONS:
   • Data transformation and cleaning
   • Filtering and analysis
   • Mathematical computations
   • Text processing and parsing
   • API response processing

🚀 WHEN TO USE EACH TYPE:
   • List comprehensions: Need all results immediately
   • Generators: Large datasets, memory constraints
   • Dictionary comprehensions: Key-value transformations
   • Set comprehensions: Unique values needed
   • Traditional loops: Complex logic, multiple operations

⚡ PERFORMANCE TIPS:
   • List comprehensions are ~2x faster than loops
   • Generators use constant memory regardless of size
   • Avoid deeply nested comprehensions (>2 levels)
   • Use built-in functions with generators when possible
   • Profile code to verify performance improvements
""")
    
    print("🎉 List comprehensions solution complete!")
    print("Next: Functions and variable scope!")
