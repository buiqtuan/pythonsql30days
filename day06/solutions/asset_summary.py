"""
Day 6 Solution: Mini Project: Asset Summary CLI
===============================================

Asset Summary CLI - asset_summary.py

This solution demonstrates:
1. Combining all concepts from Days 1-5
2. User input and data validation
3. Lists for data storage
4. Functions for organization and reusability
5. Mathematical calculations (total, average, min, max)
6. String formatting and output presentation
7. Error handling and input validation
8. Menu-driven CLI interface
9. Data persistence (optional save to file)

This mini-project showcases:
- Variables and data types (Day 1)
- Operators and expressions (Day 2)
- Control structures (Day 3)
- Loops and iterations (Day 4)
- Functions and scope (Day 5)
"""

import sys
from datetime import datetime

print("=== Day 6: Mini Project: Asset Summary CLI ===")
print("Solution: asset_summary.py")
print()

def display_welcome():
    """Display welcome message and program information"""
    print("=" * 60)
    print("         ASSET PORTFOLIO SUMMARY CALCULATOR")
    print("=" * 60)
    print("Track your assets and get instant portfolio analytics!")
    print("Features:")
    print("• Add multiple assets with names and values")
    print("• Calculate total portfolio value")
    print("• Get average asset value")
    print("• Find minimum and maximum asset values")
    print("• View detailed portfolio summary")
    print("• Save portfolio to file")
    print("-" * 60)

def get_asset_input():
    """
    Get asset name and value from user with validation
    
    Returns:
        tuple: (asset_name, asset_value) or (None, None) if user wants to stop
    """
    while True:
        # Get asset name
        asset_name = input("\nEnter asset name (or 'done' to finish): ").strip()
        
        if asset_name.lower() == 'done':
            return None, None
        
        if not asset_name:
            print("❌ Error: Asset name cannot be empty. Please try again.")
            continue
        
        # Get asset value
        try:
            value_input = input(f"Enter value for '{asset_name}': $").strip()
            if not value_input:
                print("❌ Error: Asset value cannot be empty. Please try again.")
                continue
                
            asset_value = float(value_input)
            
            if asset_value < 0:
                print("❌ Error: Asset value cannot be negative. Please try again.")
                continue
            
            return asset_name, asset_value
            
        except ValueError:
            print("❌ Error: Please enter a valid number for the asset value.")
            continue

def calculate_portfolio_stats(assets):
    """
    Calculate portfolio statistics
    
    Args:
        assets (list): List of tuples (asset_name, asset_value)
    
    Returns:
        dict: Dictionary containing portfolio statistics
    """
    if not assets:
        return {
            'total': 0,
            'average': 0,
            'minimum': 0,
            'maximum': 0,
            'count': 0
        }
    
    values = [value for name, value in assets]
    
    return {
        'total': sum(values),
        'average': sum(values) / len(values),
        'minimum': min(values),
        'maximum': max(values),
        'count': len(assets)
    }

def find_min_max_assets(assets):
    """
    Find the assets with minimum and maximum values
    
    Args:
        assets (list): List of tuples (asset_name, asset_value)
    
    Returns:
        tuple: (min_asset, max_asset) as tuples of (name, value)
    """
    if not assets:
        return None, None
    
    min_asset = min(assets, key=lambda x: x[1])
    max_asset = max(assets, key=lambda x: x[1])
    
    return min_asset, max_asset

def format_currency(amount):
    """
    Format a number as currency
    
    Args:
        amount (float): Amount to format
    
    Returns:
        str: Formatted currency string
    """
    return f"${amount:,.2f}"

def display_portfolio_summary(assets):
    """
    Display comprehensive portfolio summary
    
    Args:
        assets (list): List of tuples (asset_name, asset_value)
    """
    if not assets:
        print("\n📭 No assets in portfolio yet!")
        return
    
    stats = calculate_portfolio_stats(assets)
    min_asset, max_asset = find_min_max_assets(assets)
    
    print("\n" + "=" * 50)
    print("         PORTFOLIO SUMMARY REPORT")
    print("=" * 50)
    print(f"📊 Total Assets: {stats['count']}")
    print(f"💰 Total Portfolio Value: {format_currency(stats['total'])}")
    print(f"📈 Average Asset Value: {format_currency(stats['average'])}")
    print(f"📉 Minimum Asset Value: {format_currency(stats['minimum'])}")
    print(f"📊 Maximum Asset Value: {format_currency(stats['maximum'])}")
    print("-" * 50)
    
    # Show min/max asset details
    if min_asset and max_asset:
        print(f"🔻 Lowest Value Asset: {min_asset[0]} - {format_currency(min_asset[1])}")
        print(f"🔺 Highest Value Asset: {max_asset[0]} - {format_currency(max_asset[1])}")
        
        if stats['count'] > 1:
            value_range = stats['maximum'] - stats['minimum']
            print(f"📏 Value Range: {format_currency(value_range)}")
    
    print("-" * 50)

def display_asset_list(assets):
    """
    Display detailed list of all assets
    
    Args:
        assets (list): List of tuples (asset_name, asset_value)
    """
    if not assets:
        print("\n📭 No assets to display!")
        return
    
    print("\n" + "=" * 40)
    print("         ASSET PORTFOLIO")
    print("=" * 40)
    print(f"{'#':<3} {'Asset Name':<20} {'Value':<15}")
    print("-" * 40)
    
    for i, (name, value) in enumerate(assets, 1):
        print(f"{i:<3} {name:<20} {format_currency(value):<15}")
    
    print("-" * 40)
    total_value = sum(value for name, value in assets)
    print(f"{'TOTAL:':<24} {format_currency(total_value):<15}")
    print("=" * 40)

def save_portfolio_to_file(assets):
    """
    Save portfolio to a text file
    
    Args:
        assets (list): List of tuples (asset_name, asset_value)
    """
    if not assets:
        print("\n❌ No assets to save!")
        return
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"portfolio_summary_{timestamp}.txt"
    
    try:
        with open(filename, 'w') as file:
            file.write("ASSET PORTFOLIO SUMMARY REPORT\n")
            file.write("=" * 50 + "\n")
            file.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            # Asset list
            file.write("ASSET LIST:\n")
            file.write("-" * 30 + "\n")
            for i, (name, value) in enumerate(assets, 1):
                file.write(f"{i:2d}. {name:<20} {format_currency(value)}\n")
            
            # Statistics
            stats = calculate_portfolio_stats(assets)
            min_asset, max_asset = find_min_max_assets(assets)
            
            file.write("\nPORTFOLIO STATISTICS:\n")
            file.write("-" * 30 + "\n")
            file.write(f"Total Assets: {stats['count']}\n")
            file.write(f"Total Value: {format_currency(stats['total'])}\n")
            file.write(f"Average Value: {format_currency(stats['average'])}\n")
            file.write(f"Minimum Value: {format_currency(stats['minimum'])}\n")
            file.write(f"Maximum Value: {format_currency(stats['maximum'])}\n")
            
            if min_asset and max_asset:
                file.write(f"\nLowest Value Asset: {min_asset[0]} - {format_currency(min_asset[1])}\n")
                file.write(f"Highest Value Asset: {max_asset[0]} - {format_currency(max_asset[1])}\n")
        
        print(f"\n✅ Portfolio saved to '{filename}'")
        
    except Exception as e:
        print(f"\n❌ Error saving file: {e}")

def display_menu():
    """Display the main menu options"""
    print("\n" + "=" * 40)
    print("           MAIN MENU")
    print("=" * 40)
    print("1. Add Assets to Portfolio")
    print("2. View Asset List")
    print("3. View Portfolio Summary")
    print("4. Save Portfolio to File")
    print("5. Clear Portfolio")
    print("6. Exit Program")
    print("-" * 40)

def get_menu_choice():
    """
    Get user's menu choice with validation
    
    Returns:
        int: Valid menu choice (1-6)
    """
    while True:
        try:
            choice = input("Enter your choice (1-6): ").strip()
            choice_num = int(choice)
            
            if 1 <= choice_num <= 6:
                return choice_num
            else:
                print("❌ Please enter a number between 1 and 6.")
                
        except ValueError:
            print("❌ Please enter a valid number.")

def add_assets_batch(assets):
    """
    Add multiple assets in batch mode
    
    Args:
        assets (list): Current list of assets to add to
    
    Returns:
        int: Number of assets added
    """
    print("\n📝 Asset Entry Mode")
    print("Enter asset details below. Type 'done' when finished.")
    print("-" * 40)
    
    added_count = 0
    
    while True:
        asset_name, asset_value = get_asset_input()
        
        if asset_name is None:  # User typed 'done'
            break
        
        assets.append((asset_name, asset_value))
        added_count += 1
        print(f"✅ Added: {asset_name} - {format_currency(asset_value)}")
    
    if added_count > 0:
        print(f"\n🎉 Successfully added {added_count} asset(s) to your portfolio!")
    else:
        print("\n📭 No assets were added.")
    
    return added_count

def clear_portfolio(assets):
    """
    Clear all assets from portfolio with confirmation
    
    Args:
        assets (list): List of assets to clear
    
    Returns:
        bool: True if portfolio was cleared, False otherwise
    """
    if not assets:
        print("\n📭 Portfolio is already empty!")
        return False
    
    print(f"\n⚠️  Warning: This will remove all {len(assets)} assets from your portfolio!")
    confirmation = input("Are you sure? Type 'yes' to confirm: ").strip().lower()
    
    if confirmation == 'yes':
        assets.clear()
        print("\n🗑️  Portfolio cleared successfully!")
        return True
    else:
        print("\n❌ Operation cancelled.")
        return False

def run_demo_mode():
    """
    Run a demonstration with sample data
    
    Returns:
        list: Sample assets for demonstration
    """
    print("\n🎬 Demo Mode: Loading sample portfolio...")
    
    sample_assets = [
        ("Apple Stock (AAPL)", 15000.00),
        ("Bitcoin", 25000.00),
        ("Real Estate Fund", 50000.00),
        ("Savings Account", 5000.00),
        ("Gold ETF", 8000.00),
        ("Tesla Stock (TSLA)", 12000.00),
        ("Emergency Fund", 10000.00)
    ]
    
    print("✅ Sample portfolio loaded with 7 assets!")
    return sample_assets.copy()

def main():
    """Main function to run the Asset Summary CLI"""
    # Initialize portfolio
    assets = []
    
    # Display welcome message
    display_welcome()
    
    # Ask if user wants demo mode
    demo_choice = input("\nWould you like to start with sample data? (y/n): ").strip().lower()
    if demo_choice == 'y':
        assets = run_demo_mode()
        display_portfolio_summary(assets)
    
    # Main program loop
    while True:
        display_menu()
        choice = get_menu_choice()
        
        if choice == 1:  # Add Assets
            add_assets_batch(assets)
            
        elif choice == 2:  # View Asset List
            display_asset_list(assets)
            
        elif choice == 3:  # View Portfolio Summary
            display_portfolio_summary(assets)
            
        elif choice == 4:  # Save Portfolio
            save_portfolio_to_file(assets)
            
        elif choice == 5:  # Clear Portfolio
            clear_portfolio(assets)
            
        elif choice == 6:  # Exit
            print("\n👋 Thank you for using Asset Portfolio Manager!")
            print("Your financial future is in your hands! 💪")
            break
    
    # Final summary before exit
    if assets:
        print(f"\n📊 Final Portfolio Stats:")
        stats = calculate_portfolio_stats(assets)
        print(f"   • Total Assets: {stats['count']}")
        print(f"   • Total Value: {format_currency(stats['total'])}")
        print(f"   • Average Value: {format_currency(stats['average'])}")

def run_basic_example():
    """
    Run a basic example as specified in curriculum requirements
    This demonstrates the core functionality without the full CLI
    """
    print("\n=== Basic Asset Summary Example (Core Requirements) ===")
    
    # Sample asset data
    test_assets = [
        ("Stocks Portfolio", 25000.50),
        ("Real Estate", 150000.00),
        ("Savings Account", 8500.00),
        ("Cryptocurrency", 12750.25),
        ("Bonds", 5000.00)
    ]
    
    print("Sample Asset Portfolio:")
    print("-" * 30)
    for i, (name, value) in enumerate(test_assets, 1):
        print(f"{i}. {name}: {format_currency(value)}")
    
    # Calculate and display core statistics
    stats = calculate_portfolio_stats(test_assets)
    
    print("\n📊 Portfolio Analytics:")
    print(f"Total Portfolio Value: {format_currency(stats['total'])}")
    print(f"Average Asset Value: {format_currency(stats['average'])}")
    print(f"Minimum Asset Value: {format_currency(stats['minimum'])}")
    print(f"Maximum Asset Value: {format_currency(stats['maximum'])}")
    print(f"Number of Assets: {stats['count']}")
    
    # Find and display min/max assets
    min_asset, max_asset = find_min_max_assets(test_assets)
    print(f"\nLowest Value: {min_asset[0]} - {format_currency(min_asset[1])}")
    print(f"Highest Value: {max_asset[0]} - {format_currency(max_asset[1])}")
    
    print("\n✅ Core requirements demonstrated!")

if __name__ == "__main__":
    print("Choose mode:")
    print("1. Run Full CLI Application")
    print("2. Run Basic Example (Core Requirements)")
    
    mode_choice = input("Enter choice (1 or 2): ").strip()
    
    if mode_choice == "2":
        run_basic_example()
    else:
        main()
    
    print("\n🎓 Day 6 Solution Complete!")
    print("Key concepts mastered:")
    print("✓ User input and validation")
    print("✓ Data structures (lists and tuples)")
    print("✓ Functions and code organization")
    print("✓ Mathematical calculations")
    print("✓ String formatting and presentation")
    print("✓ Error handling")
    print("✓ File I/O operations")
    print("✓ Menu-driven interface design")
