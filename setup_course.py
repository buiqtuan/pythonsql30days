#!/usr/bin/env python3
"""
30-Day Python & SQL Course Setup Script
=======================================

This script helps you set up your learning environment for the 30-day course.

Usage: python setup_course.py
"""

import os
import sys
import subprocess
from pathlib import Path

def print_header():
    """Print a welcome header"""
    print("=" * 60)
    print("🐍 30-Day Python & SQL Learning Course Setup")
    print("=" * 60)
    print()

def check_python_version():
    """Check if Python version is compatible"""
    print("🔍 Checking Python version...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} - Compatible!")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor}.{version.micro} - Need Python 3.8+")
        return False

def create_virtual_environment():
    """Create a virtual environment for the course"""
    print("\n🏗️  Creating virtual environment...")
    
    venv_path = Path("venv")
    if venv_path.exists():
        print("⚠️  Virtual environment already exists. Skipping creation.")
        return True
    
    try:
        subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
        print("✅ Virtual environment created successfully!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to create virtual environment")
        return False

def get_activation_command():
    """Get the appropriate activation command for the OS"""
    if os.name == 'nt':  # Windows
        return "venv\\Scripts\\activate"
    else:  # Unix/Linux/macOS
        return "source venv/bin/activate"

def install_requirements():
    """Install required packages"""
    print("\n📦 Installing required packages...")
    
    # Requirements for the course
    requirements = [
        "pandas>=1.5.0",
        "numpy>=1.24.0", 
        "matplotlib>=3.6.0",
        "jupyter>=1.0.0",
        "pytest>=7.0.0"
    ]
    
    # Write requirements to file
    req_file = Path("requirements.txt")
    with open(req_file, "w") as f:
        f.write("# 30-Day Python & SQL Course Requirements\n")
        for req in requirements:
            f.write(f"{req}\n")
    
    print("📝 Created requirements.txt file")
    
    # Determine pip path
    if os.name == 'nt':  # Windows
        pip_path = Path("venv/Scripts/pip")
    else:  # Unix/Linux/macOS
        pip_path = Path("venv/bin/pip")
    
    try:
        subprocess.run([str(pip_path), "install", "--upgrade", "pip"], check=True)
        subprocess.run([str(pip_path), "install", "-r", "requirements.txt"], check=True)
        print("✅ All packages installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install packages")
        return False

def verify_installation():
    """Verify that key packages are installed"""
    print("\n🧪 Verifying installation...")
    
    # Determine python path in venv
    if os.name == 'nt':  # Windows
        python_path = Path("venv/Scripts/python")
    else:  # Unix/Linux/macOS
        python_path = Path("venv/bin/python")
    
    test_script = '''
import sys
try:
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import sqlite3
    import pytest
    print("✅ All required packages are working!")
    print(f"📊 Pandas version: {pd.__version__}")
    print(f"🔢 NumPy version: {np.__version__}")
    print(f"📈 Matplotlib version: {plt.__version__.__version__ if hasattr(plt.__version__, '__version__') else 'installed'}")
    print(f"🗄️  SQLite3 version: {sqlite3.sqlite_version}")
except ImportError as e:
    print(f"❌ Missing package: {e}")
    sys.exit(1)
'''
    
    try:
        result = subprocess.run([str(python_path), "-c", test_script], 
                              capture_output=True, text=True, check=True)
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Verification failed: {e.stderr}")
        return False

def create_course_checklist():
    """Create a progress checklist file"""
    print("\n📋 Creating progress checklist...")
    
    checklist_content = """# 30-Day Python & SQL Course Progress

## Week 1: Python Fundamentals
- [ ] Day 1: Introduction to Python & Development Environment
- [ ] Day 2: Variables, Data Types & Operators
- [ ] Day 3: Conditional Statements
- [ ] Day 4: Loops & List Comprehensions
- [ ] Day 5: Functions & Variable Scope
- [ ] Day 6: Mini Project: Asset Summary CLI
- [ ] Day 7: Review & Code Refactoring

## Week 2: Data Structures & OOP
- [ ] Day 8: Lists and Tuples
- [ ] Day 9: Dictionaries and Sets
- [ ] Day 10: File I/O and CSV Handling
- [ ] Day 11: Error Handling and Logging
- [ ] Day 12: Standard Libraries
- [ ] Day 13: Object-Oriented Programming (OOP) – Part 1
- [ ] Day 14: OOP – Inheritance and Encapsulation

## Week 3: Libraries & Testing
- [ ] Day 15: Managing Python Libraries
- [ ] Day 16: Unit Testing in Python
- [ ] Day 17: Introduction to Pandas
- [ ] Day 18: Advanced Pandas
- [ ] Day 19: Introduction to NumPy
- [ ] Day 20: Python Review & Small Project
- [ ] Day 21: Introduction to RDBMS & SQLite/PostgreSQL

## Week 4: SQL & Integration
- [ ] Day 22: Basic SQL Queries
- [ ] Day 23: Aggregation and GROUP BY
- [ ] Day 24: Advanced Joins
- [ ] Day 25: Window Functions
- [ ] Day 26: Performance Optimization
- [ ] Day 27: Integrating SQL with Python
- [ ] Day 28: Capstone Project Design

## Final Days: Capstone Project
- [ ] Day 29: Writing Capstone Queries
- [ ] Day 30: Capstone Demo & Review

## Notes
- Check off each day as you complete it
- Don't skip days - each builds on the previous
- If you get stuck, review previous concepts
- Join Python and SQL communities for help

## Study Tips
- Study 4 hours daily (2 theory + 2 practice)
- Code along with every example
- Complete all exercises before moving on
- Ask questions and seek help when needed

Good luck with your learning journey! 🚀
"""
    
    with open("PROGRESS_CHECKLIST.md", "w") as f:
        f.write(checklist_content)
    
    print("✅ Progress checklist created!")

def print_next_steps():
    """Print next steps for the user"""
    activation_cmd = get_activation_command()
    
    print("\n" + "=" * 60)
    print("🎉 Setup Complete! Here's what to do next:")
    print("=" * 60)
    
    print(f"""
1. Activate your virtual environment:
   {activation_cmd}

2. Start with Day 1:
   cd day01
   python exercises/hello.py

3. Follow the daily structure:
   - Read README.md for objectives
   - Complete exercises in order
   - Check solutions only after attempting

4. Track your progress:
   - Use PROGRESS_CHECKLIST.md
   - Mark off each completed day

5. Need help?
   - Review previous concepts
   - Check additional resources in each day's README
   - Join Python and SQL communities

🚀 Ready to start your 30-day learning journey!
""")

def main():
    """Main setup function"""
    print_header()
    
    # Check Python version
    if not check_python_version():
        print("\n❌ Please install Python 3.8 or higher and try again.")
        return
    
    # Create virtual environment
    if not create_virtual_environment():
        print("\n❌ Setup failed. Please check your Python installation.")
        return
    
    # Install requirements
    if not install_requirements():
        print("\n❌ Failed to install packages. Check your internet connection.")
        return
    
    # Verify installation
    if not verify_installation():
        print("\n❌ Installation verification failed.")
        return
    
    # Create progress checklist
    create_course_checklist()
    
    # Print next steps
    print_next_steps()

if __name__ == "__main__":
    main()
