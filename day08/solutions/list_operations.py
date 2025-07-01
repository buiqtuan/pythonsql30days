"""
Day 8 Solution: List Operations
===============================

This solution provides comprehensive examples of Python list operations,
demonstrating advanced techniques, performance considerations, and practical applications.

Author: Python Learning Assistant
Date: 2024
"""

import random
import time
from typing import List, Tuple, Optional, Union, Callable, Any
from collections import Counter, deque
import copy


# Example 1: Basic List Operations and Characteristics
def demonstrate_basic_list_operations():
    """Demonstrate fundamental list operations."""
    print("1. Basic List Operations")
    print("-" * 30)
    
    # Creating lists
    empty_list = []
    numbers = [1, 2, 3, 4, 5]
    mixed_list = ["hello", 42, 3.14, True, [1, 2, 3]]
    
    print(f"Empty list: {empty_list}")
    print(f"Numbers: {numbers}")
    print(f"Mixed types: {mixed_list}")
    
    # List methods - adding elements
    fruits = ["apple", "banana"]
    print(f"\nOriginal fruits: {fruits}")
    
    fruits.append("orange")  # Add to end
    print(f"After append: {fruits}")
    
    fruits.insert(1, "grape")  # Insert at position
    print(f"After insert: {fruits}")
    
    fruits.extend(["mango", "kiwi"])  # Add multiple items
    print(f"After extend: {fruits}")
    
    # List methods - removing elements
    fruits.remove("banana")  # Remove first occurrence
    print(f"After remove: {fruits}")
    
    popped = fruits.pop()  # Remove and return last item
    print(f"After pop: {fruits}, popped: {popped}")
    
    popped_index = fruits.pop(1)  # Remove and return item at index
    print(f"After pop(1): {fruits}, popped: {popped_index}")
    
    # List slicing
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"\nOriginal numbers: {numbers}")
    print(f"First 5: {numbers[:5]}")
    print(f"Last 5: {numbers[-5:]}")
    print(f"Every 2nd: {numbers[::2]}")
    print(f"Reversed: {numbers[::-1]}")
    print(f"Middle slice: {numbers[3:7]}")
    
    print()


# Example 2: Advanced List Methods and Operations
def demonstrate_advanced_list_methods():
    """Demonstrate advanced list methods and operations."""
    print("2. Advanced List Methods")
    print("-" * 30)
    
    # Sorting and reversing
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original: {numbers}")
    
    # Sort (modifies original)
    numbers_copy = numbers.copy()
    numbers_copy.sort()
    print(f"Sorted (ascending): {numbers_copy}")
    
    numbers_copy.sort(reverse=True)
    print(f"Sorted (descending): {numbers_copy}")
    
    # Sorted (returns new list)
    sorted_asc = sorted(numbers)
    sorted_desc = sorted(numbers, reverse=True)
    print(f"Original unchanged: {numbers}")
    print(f"Sorted new list: {sorted_asc}")
    
    # Reverse
    numbers_copy = numbers.copy()
    numbers_copy.reverse()
    print(f"Reversed: {numbers_copy}")
    
    # List searching
    search_list = [10, 20, 30, 20, 40, 20, 50]
    print(f"\nSearching in: {search_list}")
    print(f"Index of 20: {search_list.index(20)}")  # First occurrence
    print(f"Count of 20: {search_list.count(20)}")
    print(f"30 in list: {30 in search_list}")
    print(f"100 in list: {100 in search_list}")
    
    # List comprehensions vs traditional loops
    squares_traditional = []
    for x in range(10):
        squares_traditional.append(x ** 2)
    
    squares_comprehension = [x ** 2 for x in range(10)]
    
    print(f"\nSquares (traditional): {squares_traditional}")
    print(f"Squares (comprehension): {squares_comprehension}")
    
    # Conditional list comprehensions
    even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
    print(f"Even squares: {even_squares}")
    
    print()


# Example 3: List Performance Analysis
def demonstrate_list_performance():
    """Analyze performance characteristics of different list operations."""
    print("3. List Performance Analysis")
    print("-" * 35)
    
    def time_operation(operation_func: Callable, *args) -> float:
        """Time a function operation."""
        start = time.time()
        operation_func(*args)
        return time.time() - start
    
    # Test different list sizes
    sizes = [1000, 10000, 100000]
    
    for size in sizes:
        print(f"\nTesting with {size:,} elements:")
        
        # List creation methods
        def create_list_append():
            lst = []
            for i in range(size):
                lst.append(i)
            return lst
        
        def create_list_comprehension():
            return [i for i in range(size)]
        
        def create_list_range():
            return list(range(size))
        
        append_time = time_operation(create_list_append)
        comprehension_time = time_operation(create_list_comprehension)
        range_time = time_operation(create_list_range)
        
        print(f"  Append method: {append_time:.4f}s")
        print(f"  Comprehension: {comprehension_time:.4f}s")
        print(f"  Range method: {range_time:.4f}s")
        
        # Search performance
        test_list = list(range(size))
        search_value = size - 1  # Last element (worst case)
        
        def linear_search():
            return search_value in test_list
        
        search_time = time_operation(linear_search)
        print(f"  Linear search: {search_time:.4f}s")
    
    print()


# Example 4: Advanced List Algorithms
class ListAlgorithms:
    """Collection of advanced list algorithms."""
    
    @staticmethod
    def bubble_sort(lst: List[int]) -> List[int]:
        """Implement bubble sort algorithm."""
        arr = lst.copy()
        n = len(arr)
        
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        
        return arr
    
    @staticmethod
    def quick_sort(lst: List[int]) -> List[int]:
        """Implement quicksort algorithm."""
        if len(lst) <= 1:
            return lst
        
        pivot = lst[len(lst) // 2]
        left = [x for x in lst if x < pivot]
        middle = [x for x in lst if x == pivot]
        right = [x for x in lst if x > pivot]
        
        return ListAlgorithms.quick_sort(left) + middle + ListAlgorithms.quick_sort(right)
    
    @staticmethod
    def merge_sort(lst: List[int]) -> List[int]:
        """Implement merge sort algorithm."""
        if len(lst) <= 1:
            return lst
        
        mid = len(lst) // 2
        left = ListAlgorithms.merge_sort(lst[:mid])
        right = ListAlgorithms.merge_sort(lst[mid:])
        
        return ListAlgorithms._merge(left, right)
    
    @staticmethod
    def _merge(left: List[int], right: List[int]) -> List[int]:
        """Helper function for merge sort."""
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    @staticmethod
    def binary_search(lst: List[int], target: int) -> int:
        """Implement binary search (requires sorted list)."""
        left, right = 0, len(lst) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if lst[mid] == target:
                return mid
            elif lst[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1  # Not found
    
    @staticmethod
    def find_two_sum(lst: List[int], target: int) -> Optional[Tuple[int, int]]:
        """Find two numbers that add up to target."""
        seen = {}
        for i, num in enumerate(lst):
            complement = target - num
            if complement in seen:
                return (seen[complement], i)
            seen[num] = i
        return None
    
    @staticmethod
    def remove_duplicates(lst: List[Any]) -> List[Any]:
        """Remove duplicates while preserving order."""
        seen = set()
        result = []
        for item in lst:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return result
    
    @staticmethod
    def rotate_list(lst: List[Any], k: int) -> List[Any]:
        """Rotate list to the right by k positions."""
        if not lst:
            return lst
        
        k = k % len(lst)  # Handle k > len(lst)
        return lst[-k:] + lst[:-k]


def demonstrate_list_algorithms():
    """Demonstrate advanced list algorithms."""
    print("4. Advanced List Algorithms")
    print("-" * 35)
    
    # Test sorting algorithms
    test_data = [64, 34, 25, 12, 22, 11, 90, 5, 77, 30]
    print(f"Original data: {test_data}")
    
    bubble_sorted = ListAlgorithms.bubble_sort(test_data)
    quick_sorted = ListAlgorithms.quick_sort(test_data)
    merge_sorted = ListAlgorithms.merge_sort(test_data)
    
    print(f"Bubble sort: {bubble_sorted}")
    print(f"Quick sort:  {quick_sorted}")
    print(f"Merge sort:  {merge_sorted}")
    
    # Test searching
    sorted_data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 7
    index = ListAlgorithms.binary_search(sorted_data, target)
    print(f"\nBinary search for {target} in {sorted_data}: index {index}")
    
    # Test two sum problem
    numbers = [2, 7, 11, 15]
    target_sum = 9
    result = ListAlgorithms.find_two_sum(numbers, target_sum)
    print(f"Two sum: {numbers}, target {target_sum} -> indices {result}")
    
    # Test duplicate removal
    with_duplicates = [1, 2, 2, 3, 4, 4, 5, 1, 6]
    without_duplicates = ListAlgorithms.remove_duplicates(with_duplicates)
    print(f"Remove duplicates: {with_duplicates} -> {without_duplicates}")
    
    # Test list rotation
    original = [1, 2, 3, 4, 5, 6, 7]
    rotated = ListAlgorithms.rotate_list(original, 3)
    print(f"Rotate by 3: {original} -> {rotated}")
    
    print()


# Example 5: List Data Analysis
class ListAnalyzer:
    """Advanced list analysis tools."""
    
    @staticmethod
    def get_statistics(numbers: List[Union[int, float]]) -> Dict[str, float]:
        """Calculate comprehensive statistics for a list of numbers."""
        if not numbers:
            return {}
        
        sorted_nums = sorted(numbers)
        n = len(numbers)
        
        # Basic statistics
        total = sum(numbers)
        mean = total / n
        
        # Median
        if n % 2 == 0:
            median = (sorted_nums[n//2 - 1] + sorted_nums[n//2]) / 2
        else:
            median = sorted_nums[n//2]
        
        # Mode (most frequent value)
        counts = Counter(numbers)
        mode_count = max(counts.values())
        modes = [k for k, v in counts.items() if v == mode_count]
        
        # Range
        range_val = max(numbers) - min(numbers)
        
        # Variance and standard deviation
        variance = sum((x - mean) ** 2 for x in numbers) / n
        std_dev = variance ** 0.5
        
        return {
            'count': n,
            'sum': total,
            'mean': mean,
            'median': median,
            'mode': modes[0] if len(modes) == 1 else modes,
            'min': min(numbers),
            'max': max(numbers),
            'range': range_val,
            'variance': variance,
            'std_dev': std_dev
        }
    
    @staticmethod
    def find_outliers(numbers: List[Union[int, float]], method: str = 'iqr') -> List[Union[int, float]]:
        """Find outliers in a dataset."""
        if len(numbers) < 4:
            return []
        
        sorted_nums = sorted(numbers)
        n = len(sorted_nums)
        
        if method == 'iqr':
            # Interquartile Range method
            q1_idx = n // 4
            q3_idx = 3 * n // 4
            q1 = sorted_nums[q1_idx]
            q3 = sorted_nums[q3_idx]
            iqr = q3 - q1
            
            lower_bound = q1 - 1.5 * iqr
            upper_bound = q3 + 1.5 * iqr
            
            return [x for x in numbers if x < lower_bound or x > upper_bound]
        
        elif method == 'zscore':
            # Z-score method
            stats = ListAnalyzer.get_statistics(numbers)
            mean = stats['mean']
            std_dev = stats['std_dev']
            
            if std_dev == 0:
                return []
            
            threshold = 2.5  # Common threshold for outliers
            return [x for x in numbers if abs((x - mean) / std_dev) > threshold]
        
        return []
    
    @staticmethod
    def group_by_frequency(lst: List[Any]) -> List[Tuple[Any, int]]:
        """Group list elements by frequency."""
        counter = Counter(lst)
        return counter.most_common()
    
    @staticmethod
    def find_patterns(lst: List[Any], pattern_length: int = 2) -> List[Tuple[Tuple[Any, ...], int]]:
        """Find repeating patterns in a list."""
        patterns = Counter()
        
        for i in range(len(lst) - pattern_length + 1):
            pattern = tuple(lst[i:i + pattern_length])
            patterns[pattern] += 1
        
        # Return patterns that occur more than once
        return [(pattern, count) for pattern, count in patterns.items() if count > 1]


def demonstrate_list_analysis():
    """Demonstrate advanced list analysis techniques."""
    print("5. Advanced List Analysis")
    print("-" * 30)
    
    # Generate sample data
    random.seed(42)  # For reproducible results
    sample_data = [random.randint(1, 100) for _ in range(50)]
    sample_data.extend([150, 200, 5])  # Add some outliers
    
    print(f"Sample data ({len(sample_data)} elements): {sample_data[:10]}...")
    
    # Calculate statistics
    stats = ListAnalyzer.get_statistics(sample_data)
    print(f"\nStatistics:")
    for key, value in stats.items():
        if isinstance(value, float):
            print(f"  {key}: {value:.2f}")
        else:
            print(f"  {key}: {value}")
    
    # Find outliers
    outliers_iqr = ListAnalyzer.find_outliers(sample_data, 'iqr')
    outliers_zscore = ListAnalyzer.find_outliers(sample_data, 'zscore')
    
    print(f"\nOutliers (IQR method): {outliers_iqr}")
    print(f"Outliers (Z-score method): {outliers_zscore}")
    
    # Frequency analysis
    text_data = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple', 'date']
    frequencies = ListAnalyzer.group_by_frequency(text_data)
    
    print(f"\nFrequency analysis of {text_data}:")
    for item, count in frequencies:
        print(f"  {item}: {count}")
    
    # Pattern detection
    sequence = [1, 2, 3, 1, 2, 3, 4, 5, 1, 2, 6, 7]
    patterns = ListAnalyzer.find_patterns(sequence, 2)
    
    print(f"\nPattern detection in {sequence}:")
    for pattern, count in patterns:
        print(f"  Pattern {pattern}: {count} occurrences")
    
    print()


# Example 6: Memory and Shallow/Deep Copy
def demonstrate_memory_concepts():
    """Demonstrate list memory concepts and copying."""
    print("6. Memory Concepts and Copying")
    print("-" * 40)
    
    # Reference vs copy
    original = [1, 2, [3, 4], 5]
    reference = original  # Same object
    shallow_copy = original.copy()  # or original[:]
    deep_copy = copy.deepcopy(original)
    
    print(f"Original: {original}")
    print(f"Reference: {reference}")
    print(f"Shallow copy: {shallow_copy}")
    print(f"Deep copy: {deep_copy}")
    
    print(f"\nIdentity checks:")
    print(f"original is reference: {original is reference}")
    print(f"original is shallow_copy: {original is shallow_copy}")
    print(f"original is deep_copy: {original is deep_copy}")
    
    # Modify nested list
    original[2][0] = 999
    
    print(f"\nAfter modifying nested element:")
    print(f"Original: {original}")
    print(f"Reference: {reference}")
    print(f"Shallow copy: {shallow_copy}")  # Also changed!
    print(f"Deep copy: {deep_copy}")  # Unchanged
    
    # Memory usage comparison
    import sys
    
    small_list = [1, 2, 3, 4, 5]
    large_list = list(range(10000))
    
    print(f"\nMemory usage:")
    print(f"Small list (5 elements): {sys.getsizeof(small_list)} bytes")
    print(f"Large list (10,000 elements): {sys.getsizeof(large_list)} bytes")
    
    print()


# Example 7: Practical List Applications
def demonstrate_practical_applications():
    """Show practical applications of advanced list operations."""
    print("7. Practical List Applications")
    print("-" * 40)
    
    # 1. Data cleaning and processing
    messy_data = [
        "  Alice  ", "", "BOB", None, "charlie", "  ", "DAVID", "eve  "
    ]
    
    # Clean the data
    cleaned_data = [
        item.strip().title() for item in messy_data 
        if item and str(item).strip()
    ]
    
    print(f"Messy data: {messy_data}")
    print(f"Cleaned data: {cleaned_data}")
    
    # 2. Grade analysis system
    student_grades = [
        ("Alice", [85, 92, 78, 96]),
        ("Bob", [76, 81, 89, 83]),
        ("Carol", [94, 88, 96, 91]),
        ("David", [67, 73, 82, 79])
    ]
    
    # Calculate averages and letter grades
    def get_letter_grade(average):
        if average >= 90: return 'A'
        elif average >= 80: return 'B'
        elif average >= 70: return 'C'
        elif average >= 60: return 'D'
        else: return 'F'
    
    print(f"\nGrade Analysis:")
    class_averages = []
    
    for name, grades in student_grades:
        average = sum(grades) / len(grades)
        letter = get_letter_grade(average)
        class_averages.append(average)
        
        print(f"{name}: {grades} -> Average: {average:.1f} ({letter})")
    
    class_average = sum(class_averages) / len(class_averages)
    print(f"Class Average: {class_average:.1f}")
    
    # 3. Shopping cart with operations
    shopping_cart = [
        {"item": "laptop", "price": 999.99, "quantity": 1},
        {"item": "mouse", "price": 29.99, "quantity": 2},
        {"item": "keyboard", "price": 89.99, "quantity": 1},
        {"item": "monitor", "price": 299.99, "quantity": 1}
    ]
    
    print(f"\nShopping Cart Analysis:")
    
    # Calculate totals
    total_items = sum(item["quantity"] for item in shopping_cart)
    total_cost = sum(item["price"] * item["quantity"] for item in shopping_cart)
    
    print(f"Total items: {total_items}")
    print(f"Total cost: ${total_cost:.2f}")
    
    # Most expensive item
    most_expensive = max(shopping_cart, key=lambda x: x["price"])
    print(f"Most expensive: {most_expensive['item']} (${most_expensive['price']})")
    
    # Sort by total cost per item type
    cart_with_totals = [
        {**item, "total": item["price"] * item["quantity"]}
        for item in shopping_cart
    ]
    cart_sorted = sorted(cart_with_totals, key=lambda x: x["total"], reverse=True)
    
    print(f"Items by total cost:")
    for item in cart_sorted:
        print(f"  {item['item']}: ${item['total']:.2f}")
    
    print()


def main():
    """Main function demonstrating all list operations."""
    print("=== Day 8: List Operations Solutions ===")
    print()
    
    # Run all demonstrations
    demonstrate_basic_list_operations()
    demonstrate_advanced_list_methods()
    demonstrate_list_performance()
    demonstrate_list_algorithms()
    demonstrate_list_analysis()
    demonstrate_memory_concepts()
    demonstrate_practical_applications()
    
    # Summary
    print("📚 Key Learning Points:")
    print("• Lists are mutable, ordered collections")
    print("• Rich set of built-in methods for manipulation")
    print("• List comprehensions provide concise syntax")
    print("• Understanding performance characteristics is crucial")
    print("• Sorting algorithms have different time/space complexity")
    print("• Binary search requires sorted data")
    print("• Shallow vs deep copying affects nested objects")
    print("• Statistical analysis can reveal data insights")
    print("• Lists are fundamental to many algorithms")
    print("• Memory efficiency considerations for large datasets")
    print()
    
    print("🔧 Best Practices:")
    print("• Use list comprehensions for simple transformations")
    print("• Consider using deque for frequent insertions/deletions at ends")
    print("• Use built-in sort() for best performance")
    print("• Be aware of memory usage with large lists")
    print("• Use appropriate algorithms for your data size")
    print("• Consider using sets for fast membership testing")
    print("• Use enumerate() when you need index and value")
    print("• Prefer slicing over loops for simple operations")


if __name__ == "__main__":
    main()
