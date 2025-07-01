"""
Day 8 Solution: Tuple Examples
==============================

This solution provides comprehensive examples of Python tuples, demonstrating
their immutability, use cases, and advanced operations.

Author: Python Learning Assistant
Date: 2024
"""

import statistics
from typing import Tuple, List, Dict, NamedTuple, Optional, Union
from collections import namedtuple, Counter
from dataclasses import dataclass


# Example 1: Basic Tuple Operations
def demonstrate_basic_tuples():
    """Demonstrate fundamental tuple operations and characteristics."""
    print("1. Basic Tuple Operations")
    print("-" * 30)
    
    # Creating tuples
    empty_tuple = ()
    single_item_tuple = (42,)  # Note the comma for single-item tuples
    multi_item_tuple = (1, 2, 3, 4, 5)
    mixed_tuple = ("Alice", 25, True, 3.14)
    
    print(f"Empty tuple: {empty_tuple} (length: {len(empty_tuple)})")
    print(f"Single item: {single_item_tuple} (length: {len(single_item_tuple)})")
    print(f"Multi-item: {multi_item_tuple} (length: {len(multi_item_tuple)})")
    print(f"Mixed types: {mixed_tuple} (length: {len(mixed_tuple)})")
    
    # Accessing elements
    print(f"\nAccessing elements in {multi_item_tuple}:")
    print(f"First element: {multi_item_tuple[0]}")
    print(f"Last element: {multi_item_tuple[-1]}")
    print(f"Slice [1:4]: {multi_item_tuple[1:4]}")
    
    # Tuple immutability
    try:
        # This would raise an error
        # multi_item_tuple[0] = 999
        print("\n✅ Tuples are immutable - cannot modify elements")
    except TypeError as e:
        print(f"❌ Error trying to modify tuple: {e}")
    
    # Tuple methods
    sample_tuple = (1, 2, 3, 2, 4, 2, 5)
    print(f"\nTuple methods for {sample_tuple}:")
    print(f"Count of 2: {sample_tuple.count(2)}")
    print(f"Index of first 3: {sample_tuple.index(3)}")
    
    print()


# Example 2: Named Tuples for Structured Data
def demonstrate_named_tuples():
    """Show how to use named tuples for structured data."""
    print("2. Named Tuples for Structured Data")
    print("-" * 40)
    
    # Define named tuple using namedtuple factory
    Point = namedtuple('Point', ['x', 'y'])
    Person = namedtuple('Person', ['name', 'age', 'city'])
    
    # Create instances
    point1 = Point(10, 20)
    point2 = Point(x=30, y=40)
    
    person1 = Person("Alice", 30, "New York")
    person2 = Person(name="Bob", age=25, city="Los Angeles")
    
    print(f"Points: {point1}, {point2}")
    print(f"People: {person1}, {person2}")
    
    # Access by name or index
    print(f"\nAccessing point1:")
    print(f"By name: x={point1.x}, y={point1.y}")
    print(f"By index: x={point1[0]}, y={point1[1]}")
    
    # Named tuple methods
    print(f"\nNamed tuple methods:")
    print(f"point1._asdict(): {point1._asdict()}")
    print(f"point1._fields: {point1._fields}")
    
    # Create new tuple with modified values
    point3 = point1._replace(x=100)
    print(f"Modified point: {point3}")
    
    print()


# Example 3: Advanced Named Tuples with typing.NamedTuple
class Employee(NamedTuple):
    """Employee record using typing.NamedTuple."""
    employee_id: int
    name: str
    department: str
    salary: float
    is_active: bool = True
    
    def get_annual_salary(self) -> float:
        """Calculate annual salary."""
        return self.salary * 12
    
    def get_info(self) -> str:
        """Get formatted employee information."""
        status = "Active" if self.is_active else "Inactive"
        return f"{self.name} (ID: {self.employee_id}) - {self.department} - ${self.salary:,.2f}/month - {status}"


def demonstrate_advanced_named_tuples():
    """Demonstrate advanced named tuple features."""
    print("3. Advanced Named Tuples with Methods")
    print("-" * 45)
    
    # Create employees
    employees = [
        Employee(1001, "Alice Johnson", "Engineering", 8500.0),
        Employee(1002, "Bob Smith", "Marketing", 6200.0),
        Employee(1003, "Carol Davis", "Engineering", 9200.0, False),
        Employee(1004, "David Wilson", "Sales", 5800.0)
    ]
    
    print("Employee Records:")
    for emp in employees:
        print(f"  {emp.get_info()}")
        print(f"    Annual Salary: ${emp.get_annual_salary():,.2f}")
    
    # Filter and analyze
    active_employees = [emp for emp in employees if emp.is_active]
    engineering_employees = [emp for emp in employees if emp.department == "Engineering"]
    
    print(f"\nActive employees: {len(active_employees)}")
    print(f"Engineering employees: {len(engineering_employees)}")
    
    if active_employees:
        avg_salary = sum(emp.salary for emp in active_employees) / len(active_employees)
        print(f"Average active employee salary: ${avg_salary:,.2f}")
    
    print()


# Example 4: Coordinate System with Tuples
class CoordinateSystem:
    """A coordinate system using tuples for points."""
    
    def __init__(self):
        self.points: List[Tuple[float, float]] = []
    
    def add_point(self, x: float, y: float) -> None:
        """Add a point to the coordinate system."""
        self.points.append((x, y))
    
    def add_points(self, points: List[Tuple[float, float]]) -> None:
        """Add multiple points."""
        self.points.extend(points)
    
    def get_distance(self, point1: Tuple[float, float], point2: Tuple[float, float]) -> float:
        """Calculate Euclidean distance between two points."""
        x1, y1 = point1
        x2, y2 = point2
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    
    def find_closest_points(self) -> Optional[Tuple[Tuple[float, float], Tuple[float, float], float]]:
        """Find the two closest points in the system."""
        if len(self.points) < 2:
            return None
        
        min_distance = float('inf')
        closest_pair = None
        
        for i in range(len(self.points)):
            for j in range(i + 1, len(self.points)):
                distance = self.get_distance(self.points[i], self.points[j])
                if distance < min_distance:
                    min_distance = distance
                    closest_pair = (self.points[i], self.points[j], distance)
        
        return closest_pair
    
    def get_centroid(self) -> Optional[Tuple[float, float]]:
        """Calculate the centroid of all points."""
        if not self.points:
            return None
        
        avg_x = sum(point[0] for point in self.points) / len(self.points)
        avg_y = sum(point[1] for point in self.points) / len(self.points)
        
        return (avg_x, avg_y)
    
    def get_bounding_box(self) -> Optional[Tuple[Tuple[float, float], Tuple[float, float]]]:
        """Get the bounding box (min and max coordinates)."""
        if not self.points:
            return None
        
        min_x = min(point[0] for point in self.points)
        max_x = max(point[0] for point in self.points)
        min_y = min(point[1] for point in self.points)
        max_y = max(point[1] for point in self.points)
        
        return ((min_x, min_y), (max_x, max_y))


def demonstrate_coordinate_system():
    """Demonstrate coordinate system using tuples."""
    print("4. Coordinate System with Tuples")
    print("-" * 40)
    
    # Create coordinate system
    coord_sys = CoordinateSystem()
    
    # Add some points
    points = [
        (0, 0), (3, 4), (1, 1), (5, 2), (2, 6), (8, 1), (4, 5)
    ]
    coord_sys.add_points(points)
    
    print(f"Points in system: {coord_sys.points}")
    
    # Find closest points
    closest = coord_sys.find_closest_points()
    if closest:
        point1, point2, distance = closest
        print(f"Closest points: {point1} and {point2}")
        print(f"Distance: {distance:.2f}")
    
    # Calculate centroid
    centroid = coord_sys.get_centroid()
    if centroid:
        print(f"Centroid: ({centroid[0]:.2f}, {centroid[1]:.2f})")
    
    # Get bounding box
    bbox = coord_sys.get_bounding_box()
    if bbox:
        min_point, max_point = bbox
        print(f"Bounding box: {min_point} to {max_point}")
    
    print()


# Example 5: Data Processing with Tuples
def demonstrate_data_processing():
    """Show data processing techniques using tuples."""
    print("5. Data Processing with Tuples")
    print("-" * 35)
    
    # Student data: (name, grade1, grade2, grade3)
    students = [
        ("Alice", 85, 92, 78),
        ("Bob", 76, 81, 89),
        ("Carol", 94, 88, 96),
        ("David", 67, 73, 82),
        ("Eve", 88, 85, 91)
    ]
    
    print("Student Grade Processing:")
    print("=" * 40)
    
    # Process each student
    processed_data = []
    for student in students:
        name = student[0]
        grades = student[1:]  # All grades except name
        
        average = sum(grades) / len(grades)
        highest = max(grades)
        lowest = min(grades)
        
        # Create result tuple
        result = (name, average, highest, lowest, grades)
        processed_data.append(result)
        
        print(f"{name:6}: Avg={average:5.1f}, High={highest:2d}, Low={lowest:2d}, Grades={grades}")
    
    # Find top performer
    top_student = max(processed_data, key=lambda x: x[1])  # Sort by average
    print(f"\nTop performer: {top_student[0]} with average {top_student[1]:.1f}")
    
    # Calculate class statistics
    all_averages = [data[1] for data in processed_data]
    class_average = sum(all_averages) / len(all_averages)
    print(f"Class average: {class_average:.1f}")
    
    print()


# Example 6: Tuple Unpacking and Multiple Assignment
def demonstrate_tuple_unpacking():
    """Demonstrate various tuple unpacking techniques."""
    print("6. Tuple Unpacking and Multiple Assignment")
    print("-" * 50)
    
    # Basic unpacking
    point = (10, 20)
    x, y = point
    print(f"Unpacked point: x={x}, y={y}")
    
    # Multiple assignment (creates a tuple implicitly)
    a, b, c = 1, 2, 3
    print(f"Multiple assignment: a={a}, b={b}, c={c}")
    
    # Swapping variables
    a, b = b, a
    print(f"After swapping: a={a}, b={b}")
    
    # Extended unpacking with *
    numbers = (1, 2, 3, 4, 5, 6)
    first, second, *middle, last = numbers
    print(f"Extended unpacking: first={first}, second={second}, middle={middle}, last={last}")
    
    # Unpacking in function calls
    def calculate_area(length, width, height=1):
        return length * width * height
    
    dimensions = (5, 3, 2)
    area = calculate_area(*dimensions)
    print(f"Area with unpacked dimensions {dimensions}: {area}")
    
    # Unpacking in loops
    coordinate_pairs = [(0, 0), (1, 1), (2, 4), (3, 9)]
    print("\nCoordinate pairs:")
    for x, y in coordinate_pairs:
        print(f"  Point: ({x}, {y}), y = x²: {y == x**2}")
    
    print()


# Example 7: Return Multiple Values with Tuples
def analyze_numbers(numbers: List[Union[int, float]]) -> Tuple[float, float, float, int, float]:
    """
    Analyze a list of numbers and return multiple statistics.
    
    Returns:
        Tuple containing (mean, median, std_dev, count, sum)
    """
    if not numbers:
        return (0.0, 0.0, 0.0, 0, 0.0)
    
    mean = sum(numbers) / len(numbers)
    median = statistics.median(numbers)
    std_dev = statistics.stdev(numbers) if len(numbers) > 1 else 0.0
    count = len(numbers)
    total = sum(numbers)
    
    return (mean, median, std_dev, count, total)


def find_min_max_with_indices(data: List[Union[int, float]]) -> Tuple[Tuple[int, Union[int, float]], Tuple[int, Union[int, float]]]:
    """
    Find minimum and maximum values with their indices.
    
    Returns:
        Tuple containing ((min_index, min_value), (max_index, max_value))
    """
    if not data:
        return ((0, 0), (0, 0))
    
    min_index = 0
    max_index = 0
    
    for i, value in enumerate(data):
        if value < data[min_index]:
            min_index = i
        if value > data[max_index]:
            max_index = i
    
    return ((min_index, data[min_index]), (max_index, data[max_index]))


def demonstrate_return_tuples():
    """Demonstrate functions returning multiple values via tuples."""
    print("7. Functions Returning Multiple Values")
    print("-" * 45)
    
    # Test data
    test_numbers = [23, 45, 12, 78, 34, 56, 89, 23, 67, 45]
    
    # Analyze numbers
    mean, median, std_dev, count, total = analyze_numbers(test_numbers)
    
    print(f"Analysis of {test_numbers}:")
    print(f"  Count: {count}")
    print(f"  Sum: {total}")
    print(f"  Mean: {mean:.2f}")
    print(f"  Median: {median:.2f}")
    print(f"  Standard Deviation: {std_dev:.2f}")
    
    # Find min/max with indices
    (min_idx, min_val), (max_idx, max_val) = find_min_max_with_indices(test_numbers)
    
    print(f"\nMin/Max Analysis:")
    print(f"  Minimum: {min_val} at index {min_idx}")
    print(f"  Maximum: {max_val} at index {max_idx}")
    
    print()


# Example 8: Tuple Performance and Memory Efficiency
def demonstrate_tuple_performance():
    """Compare tuple performance and memory usage with lists."""
    print("8. Tuple Performance and Memory")
    print("-" * 40)
    
    import sys
    import time
    
    # Memory comparison
    list_data = [1, 2, 3, 4, 5]
    tuple_data = (1, 2, 3, 4, 5)
    
    list_size = sys.getsizeof(list_data)
    tuple_size = sys.getsizeof(tuple_data)
    
    print(f"Memory usage comparison:")
    print(f"  List:  {list_size} bytes")
    print(f"  Tuple: {tuple_size} bytes")
    print(f"  Difference: {list_size - tuple_size} bytes ({((list_size - tuple_size) / list_size * 100):.1f}% savings)")
    
    # Creation time comparison
    n = 100000
    
    # Time list creation
    start = time.time()
    for _ in range(n):
        _ = [1, 2, 3, 4, 5]
    list_time = time.time() - start
    
    # Time tuple creation
    start = time.time()
    for _ in range(n):
        _ = (1, 2, 3, 4, 5)
    tuple_time = time.time() - start
    
    print(f"\nCreation time comparison ({n:,} iterations):")
    print(f"  List:  {list_time:.4f} seconds")
    print(f"  Tuple: {tuple_time:.4f} seconds")
    print(f"  Speedup: {list_time / tuple_time:.1f}x faster")
    
    print()


# Example 9: Practical Tuple Applications
def demonstrate_practical_applications():
    """Show practical applications of tuples."""
    print("9. Practical Tuple Applications")
    print("-" * 40)
    
    # 1. RGB Color representation
    colors = {
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'blue': (0, 0, 255),
        'white': (255, 255, 255),
        'black': (0, 0, 0),
        'purple': (128, 0, 128)
    }
    
    print("Color palette (RGB tuples):")
    for name, rgb in colors.items():
        r, g, b = rgb
        print(f"  {name:7}: RGB{rgb} - Brightness: {(r + g + b) / 3:.1f}")
    
    # 2. Database records simulation
    print("\nDatabase records (tuple as immutable record):")
    database_records = [
        (1, "Alice", "Engineer", 75000),
        (2, "Bob", "Designer", 65000),
        (3, "Carol", "Manager", 85000),
        (4, "David", "Analyst", 60000)
    ]
    
    # Process records
    for record in database_records:
        emp_id, name, role, salary = record
        print(f"  ID {emp_id}: {name:6} - {role:8} - ${salary:,}")
    
    # 3. Configuration settings (immutable)
    config = (
        ('host', 'localhost'),
        ('port', 5432),
        ('database', 'myapp'),
        ('timeout', 30),
        ('ssl', True)
    )
    
    print("\nConfiguration settings:")
    config_dict = dict(config)
    for key, value in config_dict.items():
        print(f"  {key}: {value}")
    
    print()


# Main demonstration function
def main():
    """Run all tuple demonstration examples."""
    print("=== Day 8: Tuple Examples Solutions ===")
    print()
    
    # Run all demonstrations
    demonstrate_basic_tuples()
    demonstrate_named_tuples()
    demonstrate_advanced_named_tuples()
    demonstrate_coordinate_system()
    demonstrate_data_processing()
    demonstrate_tuple_unpacking()
    demonstrate_return_tuples()
    demonstrate_tuple_performance()
    demonstrate_practical_applications()
    
    # Summary
    print("📚 Key Learning Points:")
    print("• Tuples are immutable - cannot change after creation")
    print("• Tuples are ordered - maintain element sequence")
    print("• Tuples are hashable - can be used as dictionary keys")
    print("• Named tuples provide structure with attribute access")
    print("• Tuple unpacking enables elegant multiple assignment")
    print("• Tuples are memory efficient compared to lists")
    print("• Tuples are faster to create and access than lists")
    print("• Use tuples for fixed data that won't change")
    print("• Use tuples to return multiple values from functions")
    print("• Tuples work well for coordinates, RGB values, database records")


if __name__ == "__main__":
    main()
