"""
Day 7 Solution: Refactored Exercises
===================================

This solution demonstrates comprehensive code refactoring principles by taking
poorly written code examples and transforming them into clean, maintainable,
and professional Python code.

Author: Python Learning Assistant
Date: 2024
"""

import math
import statistics
from typing import List, Dict, Optional, Union, Tuple, Any, Callable
from dataclasses import dataclass
from abc import ABC, abstractmethod
from datetime import datetime
import logging


# Configure logging for the module
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


# Example 1: Refactoring a poorly written calculator
# BEFORE: Messy, repetitive, no error handling
class BadCalculator:
    """Example of poorly written calculator class."""
    
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        return a / b  # No error handling for division by zero
    
    def calculate(self, operation, a, b):
        # Long if-elif chain, not extensible
        if operation == "add":
            return self.add(a, b)
        elif operation == "subtract":
            return self.subtract(a, b)
        elif operation == "multiply":
            return self.multiply(a, b)
        elif operation == "divide":
            return self.divide(a, b)
        else:
            return "Invalid operation"


# AFTER: Clean, extensible, with proper error handling
class RefactoredCalculator:
    """
    A well-designed calculator with proper error handling, extensibility,
    and clean architecture.
    """
    
    def __init__(self):
        self.operations = {
            'add': self._add,
            'subtract': self._subtract,
            'multiply': self._multiply,
            'divide': self._divide,
            'power': self._power,
            'modulo': self._modulo
        }
        self.history: List[Dict[str, Union[str, float]]] = []
    
    def _add(self, a: float, b: float) -> float:
        """Add two numbers."""
        return a + b
    
    def _subtract(self, a: float, b: float) -> float:
        """Subtract b from a."""
        return a - b
    
    def _multiply(self, a: float, b: float) -> float:
        """Multiply two numbers."""
        return a * b
    
    def _divide(self, a: float, b: float) -> float:
        """Divide a by b with zero division protection."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def _power(self, a: float, b: float) -> float:
        """Raise a to the power of b."""
        return a ** b
    
    def _modulo(self, a: float, b: float) -> float:
        """Return the remainder of a divided by b."""
        if b == 0:
            raise ValueError("Cannot perform modulo with zero")
        return a % b
    
    def calculate(self, operation: str, a: float, b: float) -> float:
        """
        Perform calculation with proper error handling and history tracking.
        
        Args:
            operation: The operation to perform
            a: First operand
            b: Second operand
            
        Returns:
            Result of the calculation
            
        Raises:
            ValueError: If operation is invalid or mathematical error occurs
        """
        operation = operation.lower().strip()
        
        if operation not in self.operations:
            available_ops = ', '.join(self.operations.keys())
            raise ValueError(f"Invalid operation '{operation}'. Available: {available_ops}")
        
        try:
            result = self.operations[operation](a, b)
            
            # Record in history
            self.history.append({
                'operation': operation,
                'operand_a': a,
                'operand_b': b,
                'result': result,
                'timestamp': datetime.now().isoformat()
            })
            
            logger.info(f"Calculation: {a} {operation} {b} = {result}")
            return result
            
        except Exception as e:
            logger.error(f"Calculation error: {e}")
            raise
    
    def get_history(self) -> List[Dict[str, Union[str, float]]]:
        """Return calculation history."""
        return self.history.copy()
    
    def clear_history(self) -> None:
        """Clear calculation history."""
        self.history.clear()
        logger.info("Calculation history cleared")


# Example 2: Refactoring data processing functions
# BEFORE: Poorly structured data processing
def bad_data_processor(data):
    """Example of poorly written data processing function."""
    # No type hints, unclear variable names, no error handling
    result = []
    for i in data:
        if i > 0:
            if i % 2 == 0:
                result.append(i * 2)
            else:
                result.append(i * 3)
    return result


# AFTER: Clean, well-documented data processing
@dataclass
class DataProcessorConfig:
    """Configuration for data processing operations."""
    even_multiplier: float = 2.0
    odd_multiplier: float = 3.0
    include_negative: bool = False
    include_zero: bool = False


class DataProcessor:
    """
    A robust data processor with configurable operations and comprehensive
    error handling.
    """
    
    def __init__(self, config: Optional[DataProcessorConfig] = None):
        self.config = config or DataProcessorConfig()
    
    def process_numbers(self, data: List[Union[int, float]]) -> List[float]:
        """
        Process a list of numbers according to configuration rules.
        
        Args:
            data: List of numbers to process
            
        Returns:
            Processed list of numbers
            
        Raises:
            TypeError: If data contains non-numeric values
            ValueError: If data is empty
        """
        if not data:
            raise ValueError("Data list cannot be empty")
        
        if not all(isinstance(x, (int, float)) for x in data):
            raise TypeError("All data elements must be numeric")
        
        result = []
        
        for number in data:
            if not self._should_include_number(number):
                continue
            
            processed_value = self._process_single_number(number)
            result.append(processed_value)
        
        logger.info(f"Processed {len(data)} numbers, returned {len(result)} results")
        return result
    
    def _should_include_number(self, number: Union[int, float]) -> bool:
        """Determine if a number should be included based on configuration."""
        if number < 0 and not self.config.include_negative:
            return False
        if number == 0 and not self.config.include_zero:
            return False
        return True
    
    def _process_single_number(self, number: Union[int, float]) -> float:
        """Process a single number according to even/odd rules."""
        if number <= 0:
            return float(number)  # Return as-is for non-positive numbers
        
        if number % 2 == 0:
            return number * self.config.even_multiplier
        else:
            return number * self.config.odd_multiplier
    
    def get_statistics(self, data: List[Union[int, float]]) -> Dict[str, float]:
        """
        Calculate comprehensive statistics for the dataset.
        
        Args:
            data: List of numbers
            
        Returns:
            Dictionary containing various statistics
        """
        if not data:
            return {}
        
        processed_data = self.process_numbers(data)
        
        return {
            'count': len(processed_data),
            'sum': sum(processed_data),
            'mean': statistics.mean(processed_data),
            'median': statistics.median(processed_data),
            'min': min(processed_data),
            'max': max(processed_data),
            'std_dev': statistics.stdev(processed_data) if len(processed_data) > 1 else 0.0
        }


# Example 3: Refactoring class hierarchy with poor design
# BEFORE: Poor inheritance structure
class BadAnimal:
    """Example of poorly designed base class."""
    
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        if self.name == "dog":
            return "Woof!"
        elif self.name == "cat":
            return "Meow!"
        elif self.name == "bird":
            return "Tweet!"
        else:
            return "Unknown sound"


# AFTER: Proper object-oriented design
class Animal(ABC):
    """
    Abstract base class for all animals with proper OOP design.
    """
    
    def __init__(self, name: str, species: str, age: int = 0):
        self.name = name
        self.species = species
        self.age = age
        self.health_status = "healthy"
    
    @abstractmethod
    def make_sound(self) -> str:
        """Abstract method that must be implemented by subclasses."""
        pass
    
    @abstractmethod
    def get_diet_type(self) -> str:
        """Abstract method to return the animal's diet type."""
        pass
    
    def get_info(self) -> Dict[str, Union[str, int]]:
        """Return comprehensive information about the animal."""
        return {
            'name': self.name,
            'species': self.species,
            'age': self.age,
            'health_status': self.health_status,
            'sound': self.make_sound(),
            'diet_type': self.get_diet_type()
        }
    
    def celebrate_birthday(self) -> None:
        """Increment the animal's age."""
        self.age += 1
        logger.info(f"{self.name} is now {self.age} years old!")
    
    def __str__(self) -> str:
        return f"{self.name} the {self.species} (age {self.age})"
    
    def __repr__(self) -> str:
        return f"Animal(name='{self.name}', species='{self.species}', age={self.age})"


class Dog(Animal):
    """Dog implementation with breed-specific behavior."""
    
    def __init__(self, name: str, breed: str, age: int = 0):
        super().__init__(name, "Dog", age)
        self.breed = breed
    
    def make_sound(self) -> str:
        """Dogs bark."""
        return "Woof! Woof!"
    
    def get_diet_type(self) -> str:
        """Dogs are omnivores."""
        return "omnivore"
    
    def fetch(self) -> str:
        """Dog-specific behavior."""
        return f"{self.name} is fetching the ball!"


class Cat(Animal):
    """Cat implementation with feline-specific behavior."""
    
    def __init__(self, name: str, indoor: bool = True, age: int = 0):
        super().__init__(name, "Cat", age)
        self.indoor = indoor
    
    def make_sound(self) -> str:
        """Cats meow."""
        return "Meow!"
    
    def get_diet_type(self) -> str:
        """Cats are carnivores."""
        return "carnivore"
    
    def purr(self) -> str:
        """Cat-specific behavior."""
        return f"{self.name} is purring contentedly."


class Bird(Animal):
    """Bird implementation with avian-specific behavior."""
    
    def __init__(self, name: str, can_fly: bool = True, age: int = 0):
        super().__init__(name, "Bird", age)
        self.can_fly = can_fly
    
    def make_sound(self) -> str:
        """Birds tweet."""
        return "Tweet! Tweet!"
    
    def get_diet_type(self) -> str:
        """Most birds are omnivores."""
        return "omnivore"
    
    def fly(self) -> str:
        """Bird-specific behavior."""
        if self.can_fly:
            return f"{self.name} is soaring through the sky!"
        else:
            return f"{self.name} cannot fly but is walking around."


# Example 4: Refactoring utility functions
# BEFORE: Scattered utility functions with poor error handling
def bad_string_utils():
    """Example of poorly organized utility functions."""
    
    def reverse_string(s):
        return s[::-1]
    
    def count_words(s):
        return len(s.split())
    
    def capitalize_words(s):
        return s.title()


# AFTER: Well-organized utility class with comprehensive functionality
class StringUtils:
    """
    Comprehensive string utility class with robust error handling
    and extensive functionality.
    """
    
    @staticmethod
    def reverse_string(text: str) -> str:
        """
        Reverse a string.
        
        Args:
            text: String to reverse
            
        Returns:
            Reversed string
            
        Raises:
            TypeError: If input is not a string
        """
        if not isinstance(text, str):
            raise TypeError("Input must be a string")
        return text[::-1]
    
    @staticmethod
    def count_words(text: str, delimiter: str = None) -> int:
        """
        Count words in a string.
        
        Args:
            text: String to analyze
            delimiter: Custom word delimiter (default: whitespace)
            
        Returns:
            Number of words
        """
        if not isinstance(text, str):
            raise TypeError("Input must be a string")
        
        if not text.strip():
            return 0
        
        if delimiter:
            return len([word for word in text.split(delimiter) if word.strip()])
        else:
            return len(text.split())
    
    @staticmethod
    def capitalize_words(text: str, preserve_existing: bool = False) -> str:
        """
        Capitalize words in a string.
        
        Args:
            text: String to capitalize
            preserve_existing: If True, preserve existing capitalization
            
        Returns:
            String with capitalized words
        """
        if not isinstance(text, str):
            raise TypeError("Input must be a string")
        
        if preserve_existing:
            # Only capitalize words that are all lowercase
            words = text.split()
            capitalized = []
            for word in words:
                if word.islower():
                    capitalized.append(word.capitalize())
                else:
                    capitalized.append(word)
            return ' '.join(capitalized)
        else:
            return text.title()
    
    @staticmethod
    def extract_numbers(text: str) -> List[float]:
        """
        Extract all numbers from a string.
        
        Args:
            text: String to analyze
            
        Returns:
            List of numbers found in the string
        """
        import re
        if not isinstance(text, str):
            raise TypeError("Input must be a string")
        
        # Pattern to match integers and floats (including negative)
        pattern = r'-?\d+\.?\d*'
        matches = re.findall(pattern, text)
        
        numbers = []
        for match in matches:
            try:
                if '.' in match:
                    numbers.append(float(match))
                else:
                    numbers.append(float(int(match)))
            except ValueError:
                continue  # Skip invalid matches
        
        return numbers
    
    @staticmethod
    def clean_whitespace(text: str) -> str:
        """
        Clean and normalize whitespace in a string.
        
        Args:
            text: String to clean
            
        Returns:
            String with normalized whitespace
        """
        if not isinstance(text, str):
            raise TypeError("Input must be a string")
        
        # Replace multiple whitespace with single space and strip
        import re
        cleaned = re.sub(r'\s+', ' ', text.strip())
        return cleaned
    
    @staticmethod
    def analyze_text(text: str) -> Dict[str, Union[int, float, List[str]]]:
        """
        Perform comprehensive text analysis.
        
        Args:
            text: String to analyze
            
        Returns:
            Dictionary containing various text metrics
        """
        if not isinstance(text, str):
            raise TypeError("Input must be a string")
        
        cleaned_text = StringUtils.clean_whitespace(text)
        words = cleaned_text.split() if cleaned_text else []
        
        return {
            'character_count': len(text),
            'character_count_no_spaces': len(text.replace(' ', '')),
            'word_count': len(words),
            'sentence_count': len([s for s in text.split('.') if s.strip()]),
            'average_word_length': sum(len(word) for word in words) / len(words) if words else 0,
            'unique_words': list(set(word.lower() for word in words)),
            'numbers_found': StringUtils.extract_numbers(text),
            'is_uppercase': text.isupper(),
            'is_lowercase': text.islower(),
            'is_title_case': text.istitle()
        }


# Example 5: Refactoring error-prone file operations
# BEFORE: Poor file handling
def bad_file_operations():
    """Example of poor file handling practices."""
    
    def read_file(filename):
        file = open(filename, 'r')  # No error handling, no context manager
        content = file.read()
        file.close()
        return content
    
    def write_file(filename, content):
        file = open(filename, 'w')  # No error handling
        file.write(content)
        file.close()


# AFTER: Robust file operations with proper error handling
class FileOperations:
    """
    Robust file operations with comprehensive error handling,
    logging, and utility features.
    """
    
    @staticmethod
    def read_file(filepath: str, encoding: str = 'utf-8') -> str:
        """
        Safely read a file with proper error handling.
        
        Args:
            filepath: Path to the file
            encoding: File encoding (default: utf-8)
            
        Returns:
            File contents as string
            
        Raises:
            FileNotFoundError: If file doesn't exist
            PermissionError: If no read permission
            UnicodeDecodeError: If encoding issues
        """
        try:
            with open(filepath, 'r', encoding=encoding) as file:
                content = file.read()
                logger.info(f"Successfully read file: {filepath}")
                return content
        except FileNotFoundError:
            logger.error(f"File not found: {filepath}")
            raise
        except PermissionError:
            logger.error(f"Permission denied reading file: {filepath}")
            raise
        except UnicodeDecodeError as e:
            logger.error(f"Encoding error reading file {filepath}: {e}")
            raise
    
    @staticmethod
    def write_file(filepath: str, content: str, encoding: str = 'utf-8', 
                   append: bool = False) -> None:
        """
        Safely write to a file with proper error handling.
        
        Args:
            filepath: Path to the file
            content: Content to write
            encoding: File encoding (default: utf-8)
            append: If True, append to file instead of overwriting
            
        Raises:
            PermissionError: If no write permission
            OSError: If disk space or other OS issues
        """
        mode = 'a' if append else 'w'
        
        try:
            with open(filepath, mode, encoding=encoding) as file:
                file.write(content)
                logger.info(f"Successfully wrote to file: {filepath}")
        except PermissionError:
            logger.error(f"Permission denied writing to file: {filepath}")
            raise
        except OSError as e:
            logger.error(f"OS error writing to file {filepath}: {e}")
            raise
    
    @staticmethod
    def file_exists(filepath: str) -> bool:
        """Check if a file exists."""
        import os
        return os.path.isfile(filepath)
    
    @staticmethod
    def get_file_size(filepath: str) -> int:
        """
        Get file size in bytes.
        
        Args:
            filepath: Path to the file
            
        Returns:
            File size in bytes
            
        Raises:
            FileNotFoundError: If file doesn't exist
        """
        import os
        if not FileOperations.file_exists(filepath):
            raise FileNotFoundError(f"File not found: {filepath}")
        
        return os.path.getsize(filepath)
    
    @staticmethod
    def backup_file(filepath: str, backup_suffix: str = '.backup') -> str:
        """
        Create a backup copy of a file.
        
        Args:
            filepath: Path to the original file
            backup_suffix: Suffix for backup file
            
        Returns:
            Path to the backup file
        """
        import shutil
        
        if not FileOperations.file_exists(filepath):
            raise FileNotFoundError(f"File not found: {filepath}")
        
        backup_path = f"{filepath}{backup_suffix}"
        shutil.copy2(filepath, backup_path)
        logger.info(f"Created backup: {backup_path}")
        
        return backup_path


# Demonstration and testing functions
def demonstrate_refactoring():
    """Demonstrate all refactored examples."""
    print("=== Refactoring Demonstrations ===")
    print()
    
    # 1. Calculator refactoring
    print("1. Calculator Refactoring")
    print("-" * 30)
    
    calc = RefactoredCalculator()
    try:
        result1 = calc.calculate("add", 10, 5)
        result2 = calc.calculate("divide", 20, 4)
        result3 = calc.calculate("power", 2, 3)
        
        print(f"10 + 5 = {result1}")
        print(f"20 ÷ 4 = {result2}")
        print(f"2^3 = {result3}")
        
        # Test error handling
        try:
            calc.calculate("divide", 10, 0)
        except ValueError as e:
            print(f"Error handled: {e}")
        
        print(f"Calculation history: {len(calc.get_history())} operations")
        
    except Exception as e:
        print(f"Calculator error: {e}")
    
    print()
    
    # 2. Data processor refactoring
    print("2. Data Processor Refactoring")
    print("-" * 35)
    
    config = DataProcessorConfig(even_multiplier=2.5, odd_multiplier=3.5, include_negative=True)
    processor = DataProcessor(config)
    
    test_data = [1, 2, 3, 4, 5, -2, 0, 8, 9]
    try:
        processed = processor.process_numbers(test_data)
        stats = processor.get_statistics(test_data)
        
        print(f"Original data: {test_data}")
        print(f"Processed data: {processed}")
        print(f"Statistics: Mean={stats['mean']:.2f}, Max={stats['max']:.2f}")
        
    except Exception as e:
        print(f"Data processor error: {e}")
    
    print()
    
    # 3. Animal class hierarchy
    print("3. Animal Class Hierarchy")
    print("-" * 30)
    
    animals = [
        Dog("Buddy", "Golden Retriever", 3),
        Cat("Whiskers", indoor=True, age=2),
        Bird("Tweety", can_fly=True, age=1)
    ]
    
    for animal in animals:
        print(f"{animal}: {animal.make_sound()}")
        print(f"  Diet: {animal.get_diet_type()}")
        
        # Demonstrate polymorphism and specific behaviors
        if isinstance(animal, Dog):
            print(f"  {animal.fetch()}")
        elif isinstance(animal, Cat):
            print(f"  {animal.purr()}")
        elif isinstance(animal, Bird):
            print(f"  {animal.fly()}")
    
    print()
    
    # 4. String utilities
    print("4. String Utilities")
    print("-" * 20)
    
    sample_text = "Hello World! This has 123 numbers and   extra    spaces."
    
    try:
        print(f"Original: '{sample_text}'")
        print(f"Reversed: '{StringUtils.reverse_string(sample_text)}'")
        print(f"Word count: {StringUtils.count_words(sample_text)}")
        print(f"Capitalized: '{StringUtils.capitalize_words(sample_text)}'")
        print(f"Numbers found: {StringUtils.extract_numbers(sample_text)}")
        print(f"Cleaned: '{StringUtils.clean_whitespace(sample_text)}'")
        
        analysis = StringUtils.analyze_text(sample_text)
        print(f"Analysis: {analysis['word_count']} words, {analysis['character_count']} chars")
        
    except Exception as e:
        print(f"String utilities error: {e}")
    
    print()


def compare_old_vs_new():
    """Compare old vs new implementations to show improvements."""
    print("=== Old vs New Comparison ===")
    print()
    
    # Calculator comparison
    print("Calculator Comparison:")
    print("-" * 25)
    
    # Old way
    bad_calc = BadCalculator()
    old_result = bad_calc.calculate("divide", 10, 0)  # No error handling
    print(f"Old calculator (divide by zero): {old_result}")
    
    # New way
    good_calc = RefactoredCalculator()
    try:
        good_calc.calculate("divide", 10, 0)
    except ValueError as e:
        print(f"New calculator (divide by zero): Properly handled - {e}")
    
    print()
    
    # Data processing comparison
    print("Data Processing Comparison:")
    print("-" * 30)
    
    test_data = [1, 2, 3, 4, 5]
    
    # Old way
    old_result = bad_data_processor(test_data)
    print(f"Old processor result: {old_result}")
    
    # New way
    new_processor = DataProcessor()
    new_result = new_processor.process_numbers(test_data)
    stats = new_processor.get_statistics(test_data)
    print(f"New processor result: {new_result}")
    print(f"New processor includes statistics: {stats}")
    
    print()


def refactoring_best_practices():
    """Demonstrate refactoring best practices."""
    print("=== Refactoring Best Practices ===")
    print()
    
    practices = [
        "1. Use Type Hints - Improve code readability and catch errors early",
        "2. Add Comprehensive Error Handling - Fail gracefully with meaningful messages",
        "3. Follow Single Responsibility Principle - Each function/class should have one purpose",
        "4. Use Descriptive Names - Variables and functions should be self-documenting",
        "5. Add Logging - Track what your code is doing for debugging",
        "6. Write Docstrings - Document what functions do, their parameters, and return values",
        "7. Use Context Managers - Properly handle resources like files",
        "8. Prefer Composition over Inheritance - Use ABC for true inheritance relationships",
        "9. Validate Input Data - Check types and ranges before processing",
        "10. Make Code Testable - Design functions that are easy to unit test"
    ]
    
    for practice in practices:
        print(f"✅ {practice}")
    
    print()
    
    print("🔍 Code Smells to Watch For:")
    smells = [
        "• Long functions (> 20-30 lines)",
        "• Deep nesting (> 3-4 levels)",
        "• Duplicate code",
        "• Magic numbers/strings",
        "• Poor variable names",
        "• No error handling",
        "• Missing documentation",
        "• Tight coupling between classes"
    ]
    
    for smell in smells:
        print(smell)
    
    print()


def main():
    """Main function demonstrating all refactoring concepts."""
    print("=== Day 7: Code Refactoring Solutions ===")
    print()
    
    # Run all demonstrations
    demonstrate_refactoring()
    compare_old_vs_new()
    refactoring_best_practices()
    
    # Summary of refactoring improvements
    print("📚 Key Refactoring Improvements Made:")
    print("• Added comprehensive type hints throughout")
    print("• Implemented proper error handling with meaningful messages")
    print("• Used abstract base classes for better OOP design")
    print("• Added logging for debugging and monitoring")
    print("• Created configuration classes for flexibility")
    print("• Implemented proper file handling with context managers")
    print("• Added comprehensive documentation and docstrings")
    print("• Made code more testable and maintainable")
    print("• Separated concerns into focused classes and methods")
    print("• Added utility methods for common operations")
    print()
    
    print("🎯 Learning Outcomes:")
    print("• Understanding of clean code principles")
    print("• Knowledge of Python best practices")
    print("• Experience with object-oriented design patterns")
    print("• Skills in error handling and validation")
    print("• Appreciation for code maintainability")
    print("• Understanding of when and how to refactor")


if __name__ == "__main__":
    main()
