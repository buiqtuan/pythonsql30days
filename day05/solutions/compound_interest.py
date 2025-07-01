"""
Day 5 Solution: Compound Interest Calculator
===========================================

This solution demonstrates comprehensive compound interest calculations with 
multiple approaches and practical applications.

Author: Python Learning Assistant
Date: 2024
"""

import math
from typing import Dict, List, Tuple, Optional
from datetime import datetime, timedelta
import matplotlib.pyplot as plt


# Basic compound interest calculation
def calculate_compound_interest(principal: float, rate: float, time: float, 
                              compound_frequency: int = 1) -> float:
    """
    Calculate compound interest using the standard formula.
    
    Formula: A = P(1 + r/n)^(nt)
    Where:
    - A = final amount
    - P = principal amount
    - r = annual interest rate (as decimal)
    - n = number of times interest compounds per year
    - t = time in years
    
    Args:
        principal: Initial investment amount
        rate: Annual interest rate (as decimal, e.g., 0.05 for 5%)
        time: Time period in years
        compound_frequency: How many times per year interest compounds
        
    Returns:
        Final amount after compound interest
    """
    amount = principal * (1 + rate / compound_frequency) ** (compound_frequency * time)
    return round(amount, 2)


def calculate_interest_earned(principal: float, rate: float, time: float, 
                            compound_frequency: int = 1) -> float:
    """Calculate just the interest earned (not total amount)."""
    final_amount = calculate_compound_interest(principal, rate, time, compound_frequency)
    return round(final_amount - principal, 2)


# Enhanced compound interest with continuous compounding
def calculate_continuous_compound_interest(principal: float, rate: float, time: float) -> float:
    """
    Calculate compound interest with continuous compounding.
    
    Formula: A = Pe^(rt)
    Where e is Euler's number (approximately 2.71828)
    
    Args:
        principal: Initial investment amount
        rate: Annual interest rate (as decimal)
        time: Time period in years
        
    Returns:
        Final amount with continuous compounding
    """
    amount = principal * math.exp(rate * time)
    return round(amount, 2)


# Investment comparison functions
def compare_compounding_frequencies(principal: float, rate: float, time: float) -> Dict[str, float]:
    """Compare different compounding frequencies."""
    frequencies = {
        "Annually": 1,
        "Semi-annually": 2,
        "Quarterly": 4,
        "Monthly": 12,
        "Weekly": 52,
        "Daily": 365,
        "Continuous": "continuous"
    }
    
    results = {}
    for name, freq in frequencies.items():
        if freq == "continuous":
            results[name] = calculate_continuous_compound_interest(principal, rate, time)
        else:
            results[name] = calculate_compound_interest(principal, rate, time, freq)
    
    return results


# Investment planning functions
def calculate_time_to_goal(principal: float, goal_amount: float, rate: float, 
                          compound_frequency: int = 12) -> float:
    """
    Calculate time needed to reach a financial goal.
    
    Formula: t = ln(A/P) / (n * ln(1 + r/n))
    """
    if goal_amount <= principal:
        return 0.0
    
    time_years = math.log(goal_amount / principal) / (
        compound_frequency * math.log(1 + rate / compound_frequency)
    )
    return round(time_years, 2)


def calculate_required_rate(principal: float, goal_amount: float, time: float, 
                           compound_frequency: int = 12) -> float:
    """Calculate the required interest rate to reach a goal."""
    if goal_amount <= principal or time <= 0:
        return 0.0
    
    rate = compound_frequency * (
        (goal_amount / principal) ** (1 / (compound_frequency * time)) - 1
    )
    return round(rate, 4)


# Investment scenarios
class InvestmentScenario:
    """Class to model and analyze investment scenarios."""
    
    def __init__(self, name: str, principal: float, monthly_contribution: float = 0):
        self.name = name
        self.principal = principal
        self.monthly_contribution = monthly_contribution
        self.balance = principal
        self.months = 0
        self.history: List[Tuple[int, float]] = [(0, principal)]
    
    def add_month(self, monthly_rate: float) -> float:
        """Add a month of growth and contributions."""
        # Apply interest
        self.balance *= (1 + monthly_rate)
        # Add monthly contribution
        self.balance += self.monthly_contribution
        self.months += 1
        
        self.history.append((self.months, round(self.balance, 2)))
        return self.balance
    
    def project_growth(self, annual_rate: float, years: int) -> float:
        """Project growth over multiple years."""
        monthly_rate = annual_rate / 12
        for _ in range(years * 12):
            self.add_month(monthly_rate)
        return self.balance
    
    def get_summary(self) -> Dict[str, float]:
        """Get investment summary."""
        total_contributions = self.principal + (self.monthly_contribution * self.months)
        total_interest = self.balance - total_contributions
        
        return {
            "Final Balance": round(self.balance, 2),
            "Total Contributions": round(total_contributions, 2),
            "Interest Earned": round(total_interest, 2),
            "Return Rate": round((total_interest / total_contributions) * 100, 2) if total_contributions > 0 else 0
        }


# Advanced calculations
def calculate_effective_annual_rate(nominal_rate: float, compound_frequency: int) -> float:
    """
    Calculate effective annual rate (APY) from nominal rate.
    
    Formula: EAR = (1 + r/n)^n - 1
    """
    ear = (1 + nominal_rate / compound_frequency) ** compound_frequency - 1
    return round(ear * 100, 4)  # Return as percentage


def calculate_real_return(nominal_rate: float, inflation_rate: float) -> float:
    """
    Calculate real return rate adjusted for inflation.
    
    Formula: Real Rate = (1 + nominal) / (1 + inflation) - 1
    """
    real_rate = (1 + nominal_rate) / (1 + inflation_rate) - 1
    return round(real_rate * 100, 4)  # Return as percentage


# Practical application functions
def retirement_calculator(current_age: int, retirement_age: int, current_savings: float,
                         monthly_contribution: float, annual_return: float) -> Dict[str, float]:
    """Calculate retirement savings projection."""
    years_to_retirement = retirement_age - current_age
    
    if years_to_retirement <= 0:
        return {"error": "Already at or past retirement age"}
    
    scenario = InvestmentScenario("Retirement", current_savings, monthly_contribution)
    final_balance = scenario.project_growth(annual_return, years_to_retirement)
    
    # Calculate 4% withdrawal rule (common retirement planning guideline)
    annual_withdrawal = final_balance * 0.04
    monthly_withdrawal = annual_withdrawal / 12
    
    return {
        "Years to Retirement": years_to_retirement,
        "Final Balance": round(final_balance, 2),
        "Annual 4% Withdrawal": round(annual_withdrawal, 2),
        "Monthly 4% Withdrawal": round(monthly_withdrawal, 2),
        "Total Contributions": round(current_savings + (monthly_contribution * years_to_retirement * 12), 2)
    }


def loan_vs_investment_analysis(loan_amount: float, loan_rate: float, loan_term: float,
                               investment_rate: float) -> Dict[str, float]:
    """Analyze whether to pay off loan early or invest the money."""
    # Calculate loan total cost
    monthly_loan_rate = loan_rate / 12
    monthly_payments = loan_term * 12
    monthly_payment = loan_amount * (monthly_loan_rate * (1 + monthly_loan_rate) ** monthly_payments) / \
                     ((1 + monthly_loan_rate) ** monthly_payments - 1)
    total_loan_cost = monthly_payment * monthly_payments
    total_interest_paid = total_loan_cost - loan_amount
    
    # Calculate investment growth
    investment_value = calculate_compound_interest(loan_amount, investment_rate, loan_term, 12)
    investment_gain = investment_value - loan_amount
    
    return {
        "Loan Amount": round(loan_amount, 2),
        "Total Loan Cost": round(total_loan_cost, 2),
        "Total Interest Paid": round(total_interest_paid, 2),
        "Investment Value": round(investment_value, 2),
        "Investment Gain": round(investment_gain, 2),
        "Net Difference": round(investment_gain - total_interest_paid, 2),
        "Better Strategy": "Invest" if investment_gain > total_interest_paid else "Pay off loan"
    }


# Main demonstration
def main():
    """Demonstrate comprehensive compound interest calculations."""
    print("=== Day 5: Compound Interest Calculator Solutions ===")
    print()
    
    # Basic compound interest examples
    print("1. Basic Compound Interest Examples")
    print("-" * 40)
    
    principal = 10000
    rate = 0.06  # 6% annual rate
    time = 10   # 10 years
    
    # Different compounding frequencies
    comparisons = compare_compounding_frequencies(principal, rate, time)
    print(f"Investment: ${principal:,} at {rate*100}% for {time} years")
    print()
    
    for frequency, amount in comparisons.items():
        interest = amount - principal
        print(f"{frequency:15}: ${amount:8,.2f} (Interest: ${interest:7,.2f})")
    
    print()
    
    # Investment planning examples
    print("2. Investment Planning")
    print("-" * 40)
    
    goal_amount = 50000
    time_needed = calculate_time_to_goal(principal, goal_amount, rate)
    print(f"Time to grow ${principal:,} to ${goal_amount:,} at {rate*100}%: {time_needed} years")
    
    required_rate = calculate_required_rate(principal, goal_amount, 8)
    print(f"Rate needed to reach ${goal_amount:,} in 8 years: {required_rate*100:.2f}%")
    print()
    
    # Investment scenario with monthly contributions
    print("3. Investment Scenario with Monthly Contributions")
    print("-" * 50)
    
    scenario = InvestmentScenario("Savings Plan", 5000, 500)  # $5000 start, $500/month
    final_balance = scenario.project_growth(0.07, 15)  # 7% return, 15 years
    summary = scenario.get_summary()
    
    print("Investment Scenario: $5,000 initial + $500/month for 15 years at 7%")
    for key, value in summary.items():
        if key == "Return Rate":
            print(f"{key:20}: {value}%")
        else:
            print(f"{key:20}: ${value:,.2f}")
    print()
    
    # Retirement planning example
    print("4. Retirement Planning")
    print("-" * 30)
    
    retirement_plan = retirement_calculator(25, 65, 10000, 800, 0.08)
    print("Retirement Plan: Age 25 to 65, $10,000 start, $800/month, 8% return")
    for key, value in retirement_plan.items():
        if "Years" in key:
            print(f"{key:25}: {value}")
        else:
            print(f"{key:25}: ${value:,.2f}")
    print()
    
    # Advanced calculations
    print("5. Advanced Interest Calculations")
    print("-" * 40)
    
    nominal_rate = 0.06
    compound_freq = 12
    inflation_rate = 0.03
    
    effective_rate = calculate_effective_annual_rate(nominal_rate, compound_freq)
    real_return = calculate_real_return(nominal_rate, inflation_rate)
    
    print(f"Nominal Rate: {nominal_rate*100}% compounded monthly")
    print(f"Effective Annual Rate (APY): {effective_rate}%")
    print(f"Real Return (after {inflation_rate*100}% inflation): {real_return}%")
    print()
    
    # Loan vs Investment analysis
    print("6. Loan vs Investment Analysis")
    print("-" * 40)
    
    analysis = loan_vs_investment_analysis(20000, 0.05, 5, 0.07)
    print("Should I pay off my $20,000 loan at 5% or invest at 7% for 5 years?")
    for key, value in analysis.items():
        if key == "Better Strategy":
            print(f"{key:20}: {value}")
        else:
            print(f"{key:20}: ${value:,.2f}")
    print()
    
    # Learning summary
    print("📚 Key Learning Points:")
    print("• Compound interest is 'interest on interest' - earnings generate their own earnings")
    print("• More frequent compounding leads to higher returns (but diminishing returns)")
    print("• Time is the most powerful factor - start investing early")
    print("• Regular contributions amplify the compounding effect significantly")
    print("• Consider inflation when evaluating real returns")
    print("• Compare loan rates vs investment returns for financial decisions")
    print("• The 'Rule of 72': Divide 72 by interest rate to estimate doubling time")
    
    rule_of_72 = 72 / (rate * 100)
    actual_doubling = calculate_time_to_goal(principal, principal * 2, rate)
    print(f"• Rule of 72 estimate: {rule_of_72:.1f} years vs Actual: {actual_doubling} years")


if __name__ == "__main__":
    main()
