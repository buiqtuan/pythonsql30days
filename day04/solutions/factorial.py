"""
Day 4 Solution: Factorial Calculator
===================================

SOLUTION with comprehensive factorial implementations and optimizations

This solution demonstrates:
- Iterative and recursive factorial calculation
- Loop structures (for, while)
- Error handling and input validation
- Mathematical optimizations
- Performance comparisons
"""

# =============================================================================
# BASIC SOLUTION
# =============================================================================

print("=== BASIC FACTORIAL CALCULATOR SOLUTION ===")

def basic_factorial_iterative(n):
    """Calculate factorial using iterative approach"""
    if n < 0:
        return None  # Factorial not defined for negative numbers
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def basic_factorial_recursive(n):
    """Calculate factorial using recursive approach"""
    if n < 0:
        return None  # Factorial not defined for negative numbers
    elif n == 0 or n == 1:
        return 1
    else:
        return n * basic_factorial_recursive(n - 1)

# Get input from user
try:
    number = int(input("Enter a non-negative integer to calculate its factorial: "))
    
    if number < 0:
        print("Error: Factorial is not defined for negative numbers!")
    else:
        # Calculate using both methods
        iterative_result = basic_factorial_iterative(number)
        recursive_result = basic_factorial_recursive(number)
        
        print(f"\n{number}! (iterative) = {iterative_result}")
        print(f"{number}! (recursive) = {recursive_result}")
        
        # Show the calculation breakdown for small numbers
        if number <= 10:
            calculation = " × ".join(str(i) for i in range(1, number + 1)) if number > 0 else "1"
            print(f"Calculation: {calculation} = {iterative_result}")

except ValueError:
    print("Error: Please enter a valid integer!")

print("\n🎉 Basic factorial calculation complete!")

# =============================================================================
# ENHANCED SOLUTION WITH COMPREHENSIVE FEATURES
# =============================================================================

import math
import time
from functools import lru_cache

def comprehensive_factorial_calculator():
    """Comprehensive factorial calculator with multiple implementations and analysis"""
    
    print("\n" + "="*70)
    print("              COMPREHENSIVE FACTORIAL CALCULATOR")
    print("="*70)
    
    def get_valid_integer(prompt, min_value=0):
        """Get a valid integer from user with error handling"""
        while True:
            try:
                value = int(input(prompt))
                if value >= min_value:
                    return value
                else:
                    print(f"❌ Please enter a number >= {min_value}")
            except ValueError:
                print("❌ Invalid input! Please enter a valid integer.")
    
    # =============================================================================
    # MULTIPLE FACTORIAL IMPLEMENTATIONS
    # =============================================================================
    
    def factorial_iterative_basic(n):
        """Basic iterative implementation"""
        if n < 0:
            raise ValueError("Factorial not defined for negative numbers")
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
    
    def factorial_recursive_basic(n):
        """Basic recursive implementation"""
        if n < 0:
            raise ValueError("Factorial not defined for negative numbers")
        if n <= 1:
            return 1
        return n * factorial_recursive_basic(n - 1)
    
    @lru_cache(maxsize=None)
    def factorial_recursive_memoized(n):
        """Memoized recursive implementation for better performance"""
        if n < 0:
            raise ValueError("Factorial not defined for negative numbers")
        if n <= 1:
            return 1
        return n * factorial_recursive_memoized(n - 1)
    
    def factorial_while_loop(n):
        """While loop implementation"""
        if n < 0:
            raise ValueError("Factorial not defined for negative numbers")
        result = 1
        i = 1
        while i <= n:
            result *= i
            i += 1
        return result
    
    def factorial_builtin(n):
        """Using Python's built-in math.factorial"""
        if n < 0:
            raise ValueError("Factorial not defined for negative numbers")
        return math.factorial(n)
    
    def factorial_reduce(n):
        """Using functools.reduce"""
        if n < 0:
            raise ValueError("Factorial not defined for negative numbers")
        if n <= 1:
            return 1
        from functools import reduce
        import operator
        return reduce(operator.mul, range(1, n + 1), 1)
    
    # =============================================================================
    # PERFORMANCE COMPARISON
    # =============================================================================
    
    def benchmark_factorial_methods(n):
        """Benchmark different factorial implementations"""
        methods = [
            ("Iterative (basic)", factorial_iterative_basic),
            ("Recursive (basic)", factorial_recursive_basic),
            ("Recursive (memoized)", factorial_recursive_memoized),
            ("While loop", factorial_while_loop),
            ("Built-in math.factorial", factorial_builtin),
            ("Using reduce", factorial_reduce),
        ]
        
        print(f"\n⚡ PERFORMANCE BENCHMARK FOR {n}!:")
        print("-" * 50)
        print(f"{'Method':<25} {'Time (ms)':<12} {'Result'}")
        print("-" * 50)
        
        results = {}
        for method_name, method_func in methods:
            try:
                start_time = time.perf_counter()
                result = method_func(n)
                end_time = time.perf_counter()
                
                execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
                results[method_name] = (execution_time, result)
                
                # Truncate very long results for display
                result_str = str(result)[:20] + "..." if len(str(result)) > 20 else str(result)
                
                print(f"{method_name:<25} {execution_time:<12.4f} {result_str}")
                
            except RecursionError:
                print(f"{method_name:<25} {'OVERFLOW':<12} {'Too deep recursion'}")
                results[method_name] = (float('inf'), None)
            except Exception as e:
                print(f"{method_name:<25} {'ERROR':<12} {str(e)[:20]}")
                results[method_name] = (float('inf'), None)
        
        return results
    
    # =============================================================================
    # FACTORIAL ANALYSIS AND PROPERTIES
    # =============================================================================
    
    def analyze_factorial_properties(n):
        """Analyze mathematical properties of factorial"""
        print(f"\n🔍 FACTORIAL ANALYSIS FOR {n}!:")
        print("-" * 40)
        
        if n < 0:
            print("❌ Factorial not defined for negative numbers")
            return
        
        factorial_value = factorial_builtin(n)
        
        print(f"Value: {factorial_value}")
        print(f"Number of digits: {len(str(factorial_value))}")
        
        # Trailing zeros (factors of 10)
        trailing_zeros = count_trailing_zeros(n)
        print(f"Trailing zeros: {trailing_zeros}")
        
        # Prime factorization info
        if n <= 20:  # Only for small numbers
            prime_factors = get_factorial_prime_factors(n)
            print(f"Prime factors: {prime_factors}")
        
        # Growth rate analysis
        if n > 0:
            previous_factorial = factorial_builtin(n - 1) if n > 1 else 1
            growth_factor = factorial_value / previous_factorial
            print(f"Growth from (n-1)!: {growth_factor:.1f}x")
        
        # Mathematical relationships
        print(f"\nMathematical relationships:")
        print(f"n! = n × (n-1)! = {n} × {factorial_builtin(n-1) if n > 0 else 'N/A'}")
        
        if n >= 2:
            # Stirling's approximation
            stirling_approx = stirling_approximation(n)
            accuracy = (stirling_approx / factorial_value) * 100
            print(f"Stirling's approximation: {stirling_approx:.2e} ({accuracy:.1f}% accurate)")
    
    def count_trailing_zeros(n):
        """Count trailing zeros in n! (number of factors of 10)"""
        count = 0
        power_of_5 = 5
        while power_of_5 <= n:
            count += n // power_of_5
            power_of_5 *= 5
        return count
    
    def get_factorial_prime_factors(n):
        """Get prime factorization information for n!"""
        if n <= 1:
            return {}
        
        # Count each prime factor in n!
        factors = {}
        for p in range(2, n + 1):
            if is_prime(p):
                count = 0
                power = p
                while power <= n:
                    count += n // power
                    power *= p
                factors[p] = count
        
        return factors
    
    def is_prime(n):
        """Check if a number is prime"""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def stirling_approximation(n):
        """Calculate Stirling's approximation of n!"""
        if n == 0:
            return 1
        return math.sqrt(2 * math.pi * n) * (n / math.e) ** n
    
    # =============================================================================
    # FACTORIAL APPLICATIONS
    # =============================================================================
    
    def factorial_applications():
        """Demonstrate practical applications of factorial"""
        print(f"\n💼 PRACTICAL APPLICATIONS OF FACTORIAL:")
        print("-" * 45)
        
        # Permutations
        print("\n1. PERMUTATIONS:")
        n_items = 5
        print(f"   Number of ways to arrange {n_items} items: {n_items}! = {factorial_builtin(n_items):,}")
        
        # Combinations (using factorial)
        print("\n2. COMBINATIONS:")
        def combination(n, r):
            return factorial_builtin(n) // (factorial_builtin(r) * factorial_builtin(n - r))
        
        n, r = 10, 3
        comb_result = combination(n, r)
        print(f"   Choose {r} items from {n}: C({n},{r}) = {n}!/({r}!×{n-r}!) = {comb_result}")
        
        # Probability calculations
        print("\n3. PROBABILITY:")
        total_cards = 52
        cards_drawn = 5
        total_hands = combination(total_cards, cards_drawn)
        print(f"   Possible 5-card poker hands: C(52,5) = {total_hands:,}")
        
        # Series expansions
        print("\n4. MATHEMATICAL SERIES:")
        def e_approximation(terms):
            return sum(1 / factorial_builtin(i) for i in range(terms))
        
        e_approx = e_approximation(10)
        print(f"   e ≈ sum(1/n!) for n=0 to 9 = {e_approx:.6f}")
        print(f"   Actual e = {math.e:.6f}")
        
        # Taylor series
        print("\n5. TAYLOR SERIES (sin(x) at x=1):")
        def sin_taylor_approximation(x, terms):
            result = 0
            for n in range(terms):
                term = ((-1) ** n) * (x ** (2*n + 1)) / factorial_builtin(2*n + 1)
                result += term
            return result
        
        x = 1
        sin_approx = sin_taylor_approximation(x, 5)
        print(f"   sin(1) ≈ {sin_approx:.6f} (using 5 terms)")
        print(f"   Actual sin(1) = {math.sin(1):.6f}")
    
    # =============================================================================
    # INTERACTIVE FACTORIAL EXPLORER
    # =============================================================================
    
    def factorial_table(start, end):
        """Display a table of factorials"""
        print(f"\n📊 FACTORIAL TABLE ({start}! to {end}!):")
        print("-" * 60)
        print(f"{'n':<3} {'n!':<20} {'Digits':<8} {'Trailing Zeros':<15}")
        print("-" * 60)
        
        for i in range(start, end + 1):
            if i > 100:  # Prevent extremely large calculations
                print(f"{i:<3} {'Too large to compute':<20}")
                break
                
            fact = factorial_builtin(i)
            digits = len(str(fact))
            zeros = count_trailing_zeros(i)
            
            # Format large numbers
            if digits > 15:
                fact_str = f"{fact:.2e}"
            else:
                fact_str = f"{fact:,}"
            
            print(f"{i:<3} {fact_str:<20} {digits:<8} {zeros:<15}")
    
    # Get number from user
    print("🔢 Enter a number for comprehensive factorial analysis:")
    number = get_valid_integer("Enter a non-negative integer: ")
    
    # Perform comprehensive analysis
    analyze_factorial_properties(number)
    
    # Benchmark performance (for reasonable numbers)
    if number <= 20:
        benchmark_factorial_methods(number)
    else:
        print(f"\n⚠️ Skipping performance benchmark for large number ({number})")
    
    # Show applications
    factorial_applications()
    
    # Show factorial table
    if number <= 20:
        factorial_table(0, number)
    else:
        factorial_table(0, 20)
        print(f"\n... (showing first 20, requested {number} is too large for full table)")

# =============================================================================
# GLOBAL FACTORIAL FUNCTIONS (for reuse across modules)
# =============================================================================

def factorial_builtin(n):
    """Using Python's built-in math.factorial"""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    return math.factorial(n)

def count_trailing_zeros(n):
    """Count trailing zeros in n! (number of factors of 10)"""
    count = 0
    power_of_5 = 5
    while power_of_5 <= n:
        count += n // power_of_5
        power_of_5 *= 5
    return count

def factorial_games_and_puzzles():
    """Interactive factorial games and puzzles"""
    
    print("\n" + "="*70)
    print("              FACTORIAL GAMES AND PUZZLES")
    print("="*70)
    
    def factorial_guessing_game():
        """Game: guess the factorial result"""
        print("\n🎮 FACTORIAL GUESSING GAME:")
        print("-" * 30)
        
        import random
        
        # Generate random number for factorial
        n = random.randint(3, 8)
        correct_answer = factorial_builtin(n)
        
        print(f"What is {n}! ?")
        print("Hint: Think about how many ways you can arrange {n} items!")
        
        # Simulate user guesses (in real implementation, get from user)
        user_guesses = [24, 120, correct_answer]  # Simulated guesses
        
        for i, guess in enumerate(user_guesses, 1):
            print(f"Attempt {i}: {guess}")
            
            if guess == correct_answer:
                print(f"🎉 Correct! {n}! = {correct_answer}")
                break
            elif guess < correct_answer:
                print("Too low! Try higher.")
            else:
                print("Too high! Try lower.")
        else:
            print(f"😔 The correct answer was {correct_answer}")
    
    def factorial_puzzle_solver():
        """Solve factorial-based puzzles"""
        print("\n🧩 FACTORIAL PUZZLES:")
        print("-" * 25)
        
        # Puzzle 1: Find n where n! has exactly k trailing zeros
        print("Puzzle 1: Find the smallest n where n! has exactly 10 trailing zeros")
        
        for n in range(1, 50):
            zeros = count_trailing_zeros(n)
            if zeros == 10:
                print(f"Answer: n = {n} (since {n}! has {zeros} trailing zeros)")
                break
        
        # Puzzle 2: Factorial equation
        print("\nPuzzle 2: Solve for x: x! + (x+1)! = 42")
        
        for x in range(1, 10):
            if factorial_builtin(x) + factorial_builtin(x + 1) == 42:
                print(f"Answer: x = {x}")
                print(f"Verification: {x}! + {x+1}! = {factorial_builtin(x)} + {factorial_builtin(x+1)} = {factorial_builtin(x) + factorial_builtin(x+1)}")
                break
        
        # Puzzle 3: Sum of factorials
        print("\nPuzzle 3: Find the sum 1! + 2! + 3! + 4! + 5!")
        factorial_sum = sum(factorial_builtin(i) for i in range(1, 6))
        print(f"Answer: {' + '.join(f'{i}!' for i in range(1, 6))} = {factorial_sum}")
    
    
    # Run games and puzzles
    factorial_guessing_game()
    factorial_puzzle_solver()

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    # Run comprehensive factorial calculator
    comprehensive_factorial_calculator()
    
    # Show games and puzzles
    factorial_games_and_puzzles()
    
    print("\n" + "="*70)
    print("                        LEARNING SUMMARY")
    print("="*70)
    
    print("""
📖 KEY CONCEPTS DEMONSTRATED:

1. LOOP STRUCTURES:
   • for loops with range()
   • while loops with counters
   • Loop accumulation patterns
   • Iterative vs recursive approaches

2. FACTORIAL IMPLEMENTATIONS:
   • Basic iterative calculation
   • Recursive calculation with base cases
   • Memoization for optimization
   • Built-in library functions

3. MATHEMATICAL CONCEPTS:
   • Factorial definition and properties
   • Growth rates and approximations
   • Trailing zeros and prime factorization
   • Applications in combinatorics

4. PERFORMANCE ANALYSIS:
   • Time complexity comparisons
   • Memory usage considerations
   • Optimization techniques
   • Benchmarking methods

🎯 BEST PRACTICES:
   ✅ Handle edge cases (0!, negative numbers)
   ✅ Use appropriate data types for large numbers
   ✅ Implement input validation
   ✅ Choose efficient algorithms for the use case
   ✅ Consider memory vs speed tradeoffs

💼 REAL-WORLD APPLICATIONS:
   • Permutation and combination calculations
   • Probability and statistics
   • Mathematical series approximations
   • Cryptography and security algorithms
   • Scientific computing

🚀 OPTIMIZATION TECHNIQUES:
   • Memoization for repeated calculations
   • Iterative over recursive for large numbers
   • Early termination for specific conditions
   • Using built-in optimized functions
""")
    
    print("🎉 Factorial calculator solution complete!")
    print("Next: Advanced loop patterns and list comprehensions!")
