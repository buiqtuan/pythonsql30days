"""
Day 3 Exercise: Grading System
=============================

Create grading.py to convert numeric scores to letter grades (A–F)

Instructions:
1. Get a numeric score from user input
2. Convert to letter grade using if/elif/else
3. Display the grade with a message
"""

print("=== Grade Conversion System ===")

# Get score from user
try:
    score = float(input("Enter your numeric score (0-100): "))
    
    # Validate score range
    if score < 0 or score > 100:
        print("Error: Score must be between 0 and 100!")
    else:
        # Grade conversion logic
        if score >= 90:
            grade = "A"
            message = "Excellent work!"
        elif score >= 80:
            grade = "B"
            message = "Good job!"
        elif score >= 70:
            grade = "C"
            message = "Satisfactory performance."
        elif score >= 60:
            grade = "D"
            message = "You passed, but consider studying more."
        else:
            grade = "F"
            message = "Unfortunately, you failed. Don't give up!"
        
        # Display results
        print(f"\nScore: {score}")
        print(f"Grade: {grade}")
        print(f"Comment: {message}")
        
        # Additional feedback based on grade
        if grade in ["A", "B"]:
            print("🎉 Keep up the great work!")
        elif grade == "C":
            print("📚 Good effort, room for improvement!")
        elif grade == "D":
            print("⚠️ Consider getting extra help!")
        else:
            print("💪 Don't give up, you can do better!")

except ValueError:
    print("Error: Please enter a valid number!")

print("\n=== Grade Conversion Complete ===")

# Bonus: Grade point calculation
def calculate_gpa(grade):
    """Convert letter grade to GPA points"""
    gpa_scale = {
        "A": 4.0,
        "B": 3.0,
        "C": 2.0,
        "D": 1.0,
        "F": 0.0
    }
    return gpa_scale.get(grade, 0.0)

if 'grade' in locals():
    gpa = calculate_gpa(grade)
    print(f"GPA Points: {gpa}")
