"""
Day 3 Solution: Grading System
=============================

SOLUTION with comprehensive grading logic and advanced features

This solution demonstrates:
- Complex conditional statements (if/elif/else)
- Grade classification and GPA calculation
- Input validation and error handling
- Multiple grading systems and standards
- Statistical analysis of grades
"""

# =============================================================================
# BASIC SOLUTION
# =============================================================================

print("=== BASIC GRADING SYSTEM SOLUTION ===")

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

print("\n=== Basic Grade Conversion Complete ===")

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

print("\n🎉 Basic grading system complete!")

# =============================================================================
# ENHANCED SOLUTION WITH COMPREHENSIVE GRADING SYSTEMS
# =============================================================================

def comprehensive_grading_system():
    """Comprehensive grading system with multiple standards and features"""
    
    print("\n" + "="*70)
    print("              COMPREHENSIVE GRADING SYSTEM")
    print("="*70)
    
    def get_valid_score(prompt, min_score=0, max_score=100):
        """Get a valid score from user with error handling"""
        while True:
            try:
                score = float(input(prompt))
                if min_score <= score <= max_score:
                    return score
                else:
                    print(f"❌ Score must be between {min_score} and {max_score}!")
            except ValueError:
                print("❌ Invalid input! Please enter a valid number.")
    
    def standard_grading_system(score):
        """Standard A-F grading system"""
        if score >= 90:
            return "A", 4.0, "Excellent", "🎉"
        elif score >= 80:
            return "B", 3.0, "Good", "👍"
        elif score >= 70:
            return "C", 2.0, "Satisfactory", "📚"
        elif score >= 60:
            return "D", 1.0, "Below Average", "⚠️"
        else:
            return "F", 0.0, "Failing", "💪"
    
    def plus_minus_grading_system(score):
        """Enhanced grading with plus/minus modifiers"""
        if score >= 97:
            return "A+", 4.3, "Outstanding"
        elif score >= 93:
            return "A", 4.0, "Excellent"
        elif score >= 90:
            return "A-", 3.7, "Very Good"
        elif score >= 87:
            return "B+", 3.3, "Good Plus"
        elif score >= 83:
            return "B", 3.0, "Good"
        elif score >= 80:
            return "B-", 2.7, "Good Minus"
        elif score >= 77:
            return "C+", 2.3, "Satisfactory Plus"
        elif score >= 73:
            return "C", 2.0, "Satisfactory"
        elif score >= 70:
            return "C-", 1.7, "Satisfactory Minus"
        elif score >= 67:
            return "D+", 1.3, "Below Average Plus"
        elif score >= 63:
            return "D", 1.0, "Below Average"
        elif score >= 60:
            return "D-", 0.7, "Below Average Minus"
        else:
            return "F", 0.0, "Failing"
    
    def international_grading_systems(score):
        """Multiple international grading systems"""
        systems = {}
        
        # UK System
        if score >= 70:
            systems["UK"] = "First Class Honours"
        elif score >= 60:
            systems["UK"] = "Upper Second Class (2:1)"
        elif score >= 50:
            systems["UK"] = "Lower Second Class (2:2)"
        elif score >= 40:
            systems["UK"] = "Third Class Honours"
        else:
            systems["UK"] = "Fail"
        
        # German System (inverted scale)
        if score >= 95:
            systems["German"] = "1.0 (Sehr gut)"
        elif score >= 90:
            systems["German"] = "1.3 (Sehr gut)"
        elif score >= 85:
            systems["German"] = "1.7 (Gut)"
        elif score >= 80:
            systems["German"] = "2.0 (Gut)"
        elif score >= 75:
            systems["German"] = "2.3 (Gut)"
        elif score >= 70:
            systems["German"] = "2.7 (Befriedigend)"
        elif score >= 65:
            systems["German"] = "3.0 (Befriedigend)"
        elif score >= 60:
            systems["German"] = "3.3 (Befriedigend)"
        elif score >= 55:
            systems["German"] = "3.7 (Ausreichend)"
        elif score >= 50:
            systems["German"] = "4.0 (Ausreichend)"
        else:
            systems["German"] = "5.0 (Nicht ausreichend)"
        
        # French System (20-point scale converted)
        french_score = score / 5  # Convert 100-point to 20-point scale
        if french_score >= 18:
            systems["French"] = f"{french_score:.1f}/20 (Excellent)"
        elif french_score >= 16:
            systems["French"] = f"{french_score:.1f}/20 (Très bien)"
        elif french_score >= 14:
            systems["French"] = f"{french_score:.1f}/20 (Bien)"
        elif french_score >= 12:
            systems["French"] = f"{french_score:.1f}/20 (Assez bien)"
        elif french_score >= 10:
            systems["French"] = f"{french_score:.1f}/20 (Passable)"
        else:
            systems["French"] = f"{french_score:.1f}/20 (Insuffisant)"
        
        return systems
    
    def analyze_grade_distribution(scores):
        """Analyze grade distribution and statistics"""
        if not scores:
            return None
        
        total_scores = len(scores)
        
        # Calculate statistics
        average = sum(scores) / total_scores
        sorted_scores = sorted(scores)
        median = sorted_scores[total_scores // 2] if total_scores % 2 == 1 else \
                (sorted_scores[total_scores // 2 - 1] + sorted_scores[total_scores // 2]) / 2
        
        min_score = min(scores)
        max_score = max(scores)
        
        # Grade distribution
        grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
        for score in scores:
            grade, _, _, _ = standard_grading_system(score)
            grade_counts[grade] += 1
        
        # Calculate percentages
        grade_percentages = {grade: (count / total_scores) * 100 
                           for grade, count in grade_counts.items()}
        
        return {
            "total": total_scores,
            "average": average,
            "median": median,
            "min": min_score,
            "max": max_score,
            "grade_counts": grade_counts,
            "grade_percentages": grade_percentages
        }
    
    def display_comprehensive_grade_report(score):
        """Display comprehensive grade report for a single score"""
        print(f"\n📊 COMPREHENSIVE GRADE REPORT FOR SCORE: {score}")
        print("=" * 60)
        
        # Standard grading
        grade, gpa, description, emoji = standard_grading_system(score)
        print(f"\n🇺🇸 STANDARD US GRADING:")
        print(f"   Grade: {grade} {emoji}")
        print(f"   GPA: {gpa}")
        print(f"   Description: {description}")
        
        # Plus/minus grading
        pm_grade, pm_gpa, pm_desc = plus_minus_grading_system(score)
        print(f"\n📈 PLUS/MINUS GRADING:")
        print(f"   Grade: {pm_grade}")
        print(f"   GPA: {pm_gpa}")
        print(f"   Description: {pm_desc}")
        
        # International systems
        international = international_grading_systems(score)
        print(f"\n🌍 INTERNATIONAL GRADING SYSTEMS:")
        for country, grade_desc in international.items():
            print(f"   {country}: {grade_desc}")
        
        # Percentile and ranking info
        print(f"\n📈 PERFORMANCE ANALYSIS:")
        if score >= 95:
            print("   📊 Top 5% performance - Outstanding achievement!")
        elif score >= 90:
            print("   📊 Top 10% performance - Excellent work!")
        elif score >= 80:
            print("   📊 Top 25% performance - Very good job!")
        elif score >= 70:
            print("   📊 Above average performance - Good effort!")
        elif score >= 60:
            print("   📊 Average performance - Room for improvement.")
        else:
            print("   📊 Below average performance - Additional study needed.")
        
        # Improvement suggestions
        print(f"\n💡 IMPROVEMENT SUGGESTIONS:")
        if score < 60:
            print("   • Review fundamental concepts")
            print("   • Seek additional help from instructor")
            print("   • Form study groups with classmates")
            print("   • Use additional learning resources")
        elif score < 70:
            print("   • Focus on weak areas identified in assessment")
            print("   • Practice more problems in challenging topics")
            print("   • Review class notes regularly")
        elif score < 80:
            print("   • Aim for deeper understanding of concepts")
            print("   • Challenge yourself with advanced problems")
            print("   • Help others to reinforce your learning")
        elif score < 90:
            print("   • Strive for mastery in all areas")
            print("   • Explore advanced applications")
            print("   • Consider tutoring others")
        else:
            print("   • Maintain your excellent study habits")
            print("   • Consider advanced coursework")
            print("   • Share your success strategies with others")
    
    # Get score from user
    print("🎯 Enter a score for comprehensive grading analysis:")
    score = get_valid_score("Enter your score (0-100): ")
    
    # Display comprehensive report
    display_comprehensive_grade_report(score)

def batch_grading_system():
    """Demonstrate batch grading and class analysis"""
    
    print("\n" + "="*70)
    print("              BATCH GRADING AND CLASS ANALYSIS")
    print("="*70)
    
    # Sample class scores for demonstration
    sample_class_scores = [
        95, 88, 92, 76, 84, 69, 91, 87, 73, 82,
        89, 94, 78, 85, 71, 90, 83, 77, 86, 79,
        93, 81, 74, 88, 92, 70, 87, 85, 80, 75
    ]
    
    def analyze_class_performance(scores):
        """Comprehensive class performance analysis"""
        total_students = len(scores)
        
        # Basic statistics
        average = sum(scores) / total_students
        sorted_scores = sorted(scores)
        median = sorted_scores[total_students // 2] if total_students % 2 == 1 else \
                (sorted_scores[total_students // 2 - 1] + sorted_scores[total_students // 2]) / 2
        
        # Grade distribution
        grade_distribution = {"A": [], "B": [], "C": [], "D": [], "F": []}
        gpa_total = 0
        
        for score in scores:
            grade, gpa, _, _ = standard_grading_system(score)
            grade_distribution[grade].append(score)
            gpa_total += gpa
        
        class_gpa = gpa_total / total_students
        
        return {
            "total_students": total_students,
            "average": average,
            "median": median,
            "min_score": min(scores),
            "max_score": max(scores),
            "class_gpa": class_gpa,
            "grade_distribution": grade_distribution
        }
    
    def display_class_report(analysis):
        """Display comprehensive class performance report"""
        print(f"\n📚 CLASS PERFORMANCE REPORT")
        print("=" * 50)
        
        print(f"\n📊 CLASS STATISTICS:")
        print(f"   Total Students: {analysis['total_students']}")
        print(f"   Class Average: {analysis['average']:.2f}")
        print(f"   Median Score: {analysis['median']:.2f}")
        print(f"   Highest Score: {analysis['max_score']}")
        print(f"   Lowest Score: {analysis['min_score']}")
        print(f"   Class GPA: {analysis['class_gpa']:.2f}")
        
        print(f"\n📈 GRADE DISTRIBUTION:")
        total = analysis['total_students']
        
        for grade in ["A", "B", "C", "D", "F"]:
            count = len(analysis['grade_distribution'][grade])
            percentage = (count / total) * 100
            bar_length = int(percentage / 2)  # Scale for display
            bar = "█" * bar_length + "░" * (50 - bar_length)
            
            print(f"   {grade}: {count:2} students ({percentage:5.1f}%) |{bar[:20]}|")
        
        # Performance analysis
        print(f"\n💡 CLASS PERFORMANCE ANALYSIS:")
        a_count = len(analysis['grade_distribution']['A'])
        b_count = len(analysis['grade_distribution']['B'])
        f_count = len(analysis['grade_distribution']['F'])
        
        passing_rate = ((total - f_count) / total) * 100
        excellence_rate = ((a_count + b_count) / total) * 100
        
        print(f"   Passing Rate (D or better): {passing_rate:.1f}%")
        print(f"   Excellence Rate (A or B): {excellence_rate:.1f}%")
        
        if analysis['average'] >= 85:
            print("   🎉 Excellent class performance!")
        elif analysis['average'] >= 75:
            print("   👍 Good class performance!")
        elif analysis['average'] >= 65:
            print("   📚 Average class performance - room for improvement.")
        else:
            print("   ⚠️ Below average class performance - review curriculum.")
    
    # Analyze sample class
    print("Analyzing sample class performance...")
    analysis = analyze_class_performance(sample_class_scores)
    display_class_report(analysis)
    
    # Individual student lookup
    print(f"\n🔍 INDIVIDUAL STUDENT GRADES:")
    print(f"{'Student':<8} {'Score':<6} {'Grade':<6} {'GPA':<5} {'Status'}")
    print("-" * 40)
    
    for i, score in enumerate(sample_class_scores[:10], 1):  # Show first 10 students
        grade, gpa, _, emoji = standard_grading_system(score)
        status = "Pass" if gpa > 0 else "Fail"
        print(f"#{i:<7} {score:<6.1f} {grade:<6} {gpa:<5.1f} {status} {emoji}")

# Global grading function for reuse
def standard_grading_system(score):
    """Standard A-F grading system"""
    if score >= 90:
        return "A", 4.0, "Excellent", "🎉"
    elif score >= 80:
        return "B", 3.0, "Good", "👍"
    elif score >= 70:
        return "C", 2.0, "Satisfactory", "📚"
    elif score >= 60:
        return "D", 1.0, "Below Average", "⚠️"
    else:
        return "F", 0.0, "Failing", "💪"

def advanced_grading_features():
    """Demonstrate advanced grading features and calculations"""
    
    print("\n" + "="*70)
    print("              ADVANCED GRADING FEATURES")
    print("="*70)
    
    def weighted_grade_calculator():
        """Calculate weighted grades for different assignment types"""
        print(f"\n📝 WEIGHTED GRADE CALCULATOR:")
        print("-" * 35)
        
        # Sample grade categories with weights
        grade_categories = {
            "Homework": {"weight": 0.20, "scores": [85, 92, 78, 88, 90]},
            "Quizzes": {"weight": 0.25, "scores": [88, 91, 85, 94]},
            "Midterm": {"weight": 0.25, "scores": [87]},
            "Final Exam": {"weight": 0.30, "scores": [89]}
        }
        
        total_weighted_score = 0
        total_weight = 0
        
        print(f"{'Category':<12} {'Weight':<8} {'Avg Score':<10} {'Weighted':<10}")
        print("-" * 45)
        
        for category, data in grade_categories.items():
            avg_score = sum(data["scores"]) / len(data["scores"])
            weighted_contribution = avg_score * data["weight"]
            total_weighted_score += weighted_contribution
            total_weight += data["weight"]
            
            print(f"{category:<12} {data['weight']*100:>6.0f}% {avg_score:>9.1f} {weighted_contribution:>9.1f}")
        
        final_grade = total_weighted_score
        letter_grade, gpa, description, emoji = standard_grading_system(final_grade)
        
        print("-" * 45)
        print(f"{'FINAL GRADE':<12} {total_weight*100:>6.0f}% {final_grade:>9.1f}")
        print(f"\nLetter Grade: {letter_grade} {emoji}")
        print(f"GPA: {gpa}")
        print(f"Description: {description}")
    
    def curve_grading_system():
        """Demonstrate curve grading (bell curve adjustment)"""
        print(f"\n📈 CURVE GRADING SYSTEM:")
        print("-" * 30)
        
        # Sample raw scores
        raw_scores = [65, 72, 68, 85, 91, 78, 82, 77, 89, 74, 69, 95, 88, 76, 81]
        
        # Calculate curve adjustment
        class_average = sum(raw_scores) / len(raw_scores)
        target_average = 80  # Desired class average
        curve_adjustment = target_average - class_average
        
        print(f"Raw class average: {class_average:.1f}")
        print(f"Target average: {target_average}")
        print(f"Curve adjustment: +{curve_adjustment:.1f} points")
        
        print(f"\n{'Student':<8} {'Raw':<6} {'Curved':<7} {'Grade':<6}")
        print("-" * 30)
        
        for i, raw_score in enumerate(raw_scores, 1):
            curved_score = min(100, raw_score + curve_adjustment)  # Cap at 100
            grade, _, _, _ = standard_grading_system(curved_score)
            print(f"#{i:<7} {raw_score:<6.1f} {curved_score:<7.1f} {grade}")
    
    def grade_trend_analysis():
        """Analyze grade trends over time"""
        print(f"\n📊 GRADE TREND ANALYSIS:")
        print("-" * 30)
        
        # Sample student progress over semester
        weekly_scores = [
            ("Week 1", 75), ("Week 2", 78), ("Week 3", 82), ("Week 4", 79),
            ("Week 5", 85), ("Week 6", 88), ("Week 7", 84), ("Week 8", 91),
            ("Week 9", 89), ("Week 10", 93), ("Week 11", 90), ("Week 12", 95)
        ]
        
        print(f"{'Week':<8} {'Score':<6} {'Trend':<10} {'Grade'}")
        print("-" * 35)
        
        previous_score = None
        for week, score in weekly_scores:
            grade, _, _, _ = standard_grading_system(score)
            
            if previous_score is None:
                trend = "Baseline"
            elif score > previous_score:
                trend = f"↗ +{score - previous_score:.0f}"
            elif score < previous_score:
                trend = f"↘ {score - previous_score:.0f}"
            else:
                trend = "→ Same"
            
            print(f"{week:<8} {score:<6.1f} {trend:<10} {grade}")
            previous_score = score
        
        # Calculate overall trend
        first_score = weekly_scores[0][1]
        last_score = weekly_scores[-1][1]
        improvement = last_score - first_score
        
        print(f"\nOverall improvement: +{improvement:.1f} points")
        print(f"Performance trend: {'Improving ↗' if improvement > 0 else 'Declining ↘' if improvement < 0 else 'Stable →'}")
    
    # Run advanced features
    weighted_grade_calculator()
    curve_grading_system()
    grade_trend_analysis()

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    # Run comprehensive grading system
    comprehensive_grading_system()
    
    # Show batch grading
    batch_grading_system()
    
    # Show advanced features
    advanced_grading_features()
    
    print("\n" + "="*70)
    print("                        LEARNING SUMMARY")
    print("="*70)
    
    print("""
📖 KEY CONCEPTS DEMONSTRATED:

1. CONDITIONAL LOGIC:
   • if/elif/else chains for grade classification
   • Complex boolean expressions
   • Nested conditionals for subcategories
   • Multiple condition evaluation

2. GRADING SYSTEMS:
   • Standard A-F letter grades
   • Plus/minus grade modifiers
   • GPA calculation and conversion
   • International grading standards

3. DATA ANALYSIS:
   • Statistical calculations (mean, median, range)
   • Grade distribution analysis
   • Performance trend tracking
   • Class performance metrics

4. ADVANCED FEATURES:
   • Weighted grade calculations
   • Curve adjustments (bell curve)
   • Grade validation and bounds checking
   • Multi-criteria evaluation

🎯 BEST PRACTICES:
   ✅ Validate input ranges and types
   ✅ Use clear, consistent grading criteria
   ✅ Provide meaningful feedback messages
   ✅ Handle edge cases (perfect scores, failing grades)
   ✅ Document grading rubrics clearly

💼 REAL-WORLD APPLICATIONS:
   • Educational assessment systems
   • Employee performance evaluation
   • Quality control scoring
   • Competition judging systems
   • Certification testing platforms

🔍 PROBLEM-SOLVING TECHNIQUES:
   • Break complex grading into simple rules
   • Use lookup tables for grade conversions
   • Implement validation at multiple levels
   • Provide detailed feedback and analytics
   • Consider cultural and regional differences
""")
    
    print("🎉 Grading system solution complete!")
    print("Next: Loops and iteration patterns!")
