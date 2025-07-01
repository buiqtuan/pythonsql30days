"""
Day 6 Solution: Asset Summary CLI
=================================

This solution provides a comprehensive asset management CLI application that demonstrates
file I/O, data structures, error handling, and command-line interfaces.

Author: Python Learning Assistant
Date: 2024
"""

import json
import csv
import os
import sys
from datetime import datetime, date
from typing import Dict, List, Optional, Union, Any
from dataclasses import dataclass, asdict
from enum import Enum
import argparse


# Enums for asset types and categories
class AssetType(Enum):
    """Enumeration of supported asset types."""
    STOCK = "stock"
    BOND = "bond"
    CRYPTO = "crypto"
    REAL_ESTATE = "real_estate"
    CASH = "cash"
    COMMODITY = "commodity"
    OTHER = "other"


class AssetCategory(Enum):
    """Enumeration of asset categories."""
    EQUITY = "equity"
    FIXED_INCOME = "fixed_income"
    ALTERNATIVE = "alternative"
    CASH_EQUIVALENT = "cash_equivalent"


# Data classes for asset management
@dataclass
class Asset:
    """Represents a financial asset."""
    name: str
    asset_type: AssetType
    category: AssetCategory
    quantity: float
    purchase_price: float
    current_price: float
    purchase_date: str
    notes: str = ""
    
    @property
    def total_value(self) -> float:
        """Calculate total current value."""
        return self.quantity * self.current_price
    
    @property
    def total_cost(self) -> float:
        """Calculate total purchase cost."""
        return self.quantity * self.purchase_price
    
    @property
    def gain_loss(self) -> float:
        """Calculate gain/loss amount."""
        return self.total_value - self.total_cost
    
    @property
    def gain_loss_percentage(self) -> float:
        """Calculate gain/loss percentage."""
        if self.total_cost == 0:
            return 0.0
        return (self.gain_loss / self.total_cost) * 100
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization."""
        data = asdict(self)
        data['asset_type'] = self.asset_type.value
        data['category'] = self.category.value
        return data
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Asset':
        """Create Asset from dictionary."""
        data['asset_type'] = AssetType(data['asset_type'])
        data['category'] = AssetCategory(data['category'])
        return cls(**data)


class AssetPortfolio:
    """Manages a collection of assets."""
    
    def __init__(self, name: str = "My Portfolio"):
        self.name = name
        self.assets: List[Asset] = []
        self.created_date = datetime.now().isoformat()
        self.last_updated = self.created_date
    
    def add_asset(self, asset: Asset) -> None:
        """Add an asset to the portfolio."""
        self.assets.append(asset)
        self.last_updated = datetime.now().isoformat()
    
    def remove_asset(self, asset_name: str) -> bool:
        """Remove an asset by name."""
        for i, asset in enumerate(self.assets):
            if asset.name.lower() == asset_name.lower():
                del self.assets[i]
                self.last_updated = datetime.now().isoformat()
                return True
        return False
    
    def find_asset(self, asset_name: str) -> Optional[Asset]:
        """Find an asset by name."""
        for asset in self.assets:
            if asset.name.lower() == asset_name.lower():
                return asset
        return None
    
    def update_asset_price(self, asset_name: str, new_price: float) -> bool:
        """Update the current price of an asset."""
        asset = self.find_asset(asset_name)
        if asset:
            asset.current_price = new_price
            self.last_updated = datetime.now().isoformat()
            return True
        return False
    
    def get_total_value(self) -> float:
        """Calculate total portfolio value."""
        return sum(asset.total_value for asset in self.assets)
    
    def get_total_cost(self) -> float:
        """Calculate total portfolio cost."""
        return sum(asset.total_cost for asset in self.assets)
    
    def get_total_gain_loss(self) -> float:
        """Calculate total portfolio gain/loss."""
        return self.get_total_value() - self.get_total_cost()
    
    def get_total_gain_loss_percentage(self) -> float:
        """Calculate total portfolio gain/loss percentage."""
        total_cost = self.get_total_cost()
        if total_cost == 0:
            return 0.0
        return (self.get_total_gain_loss() / total_cost) * 100
    
    def get_assets_by_type(self, asset_type: AssetType) -> List[Asset]:
        """Get all assets of a specific type."""
        return [asset for asset in self.assets if asset.asset_type == asset_type]
    
    def get_assets_by_category(self, category: AssetCategory) -> List[Asset]:
        """Get all assets of a specific category."""
        return [asset for asset in self.assets if asset.category == category]
    
    def get_allocation_by_type(self) -> Dict[AssetType, float]:
        """Get portfolio allocation by asset type."""
        total_value = self.get_total_value()
        if total_value == 0:
            return {}
        
        allocation = {}
        for asset_type in AssetType:
            assets = self.get_assets_by_type(asset_type)
            type_value = sum(asset.total_value for asset in assets)
            if type_value > 0:
                allocation[asset_type] = (type_value / total_value) * 100
        
        return allocation
    
    def get_allocation_by_category(self) -> Dict[AssetCategory, float]:
        """Get portfolio allocation by category."""
        total_value = self.get_total_value()
        if total_value == 0:
            return {}
        
        allocation = {}
        for category in AssetCategory:
            assets = self.get_assets_by_category(category)
            category_value = sum(asset.total_value for asset in assets)
            if category_value > 0:
                allocation[category] = (category_value / total_value) * 100
        
        return allocation
    
    def get_top_performers(self, limit: int = 5) -> List[Asset]:
        """Get top performing assets by percentage gain."""
        return sorted(self.assets, key=lambda x: x.gain_loss_percentage, reverse=True)[:limit]
    
    def get_worst_performers(self, limit: int = 5) -> List[Asset]:
        """Get worst performing assets by percentage gain."""
        return sorted(self.assets, key=lambda x: x.gain_loss_percentage)[:limit]


class AssetManager:
    """Main class for managing asset portfolios with file I/O."""
    
    def __init__(self, data_file: str = "portfolio_data.json"):
        self.data_file = data_file
        self.portfolio = AssetPortfolio()
        self.load_portfolio()
    
    def load_portfolio(self) -> None:
        """Load portfolio from file."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    self.portfolio.name = data.get('name', 'My Portfolio')
                    self.portfolio.created_date = data.get('created_date', datetime.now().isoformat())
                    self.portfolio.last_updated = data.get('last_updated', datetime.now().isoformat())
                    
                    for asset_data in data.get('assets', []):
                        asset = Asset.from_dict(asset_data)
                        self.portfolio.assets.append(asset)
                
                print(f"✅ Portfolio loaded from {self.data_file}")
            except Exception as e:
                print(f"❌ Error loading portfolio: {e}")
                print("Starting with empty portfolio...")
        else:
            print("📁 No existing portfolio found. Starting fresh...")
    
    def save_portfolio(self) -> None:
        """Save portfolio to file."""
        try:
            data = {
                'name': self.portfolio.name,
                'created_date': self.portfolio.created_date,
                'last_updated': self.portfolio.last_updated,
                'assets': [asset.to_dict() for asset in self.portfolio.assets]
            }
            
            with open(self.data_file, 'w') as f:
                json.dump(data, f, indent=2)
            
            print(f"✅ Portfolio saved to {self.data_file}")
        except Exception as e:
            print(f"❌ Error saving portfolio: {e}")
    
    def export_to_csv(self, filename: str = "portfolio_export.csv") -> None:
        """Export portfolio to CSV format."""
        try:
            with open(filename, 'w', newline='') as f:
                writer = csv.writer(f)
                
                # Write header
                writer.writerow([
                    'Name', 'Type', 'Category', 'Quantity', 'Purchase Price',
                    'Current Price', 'Total Cost', 'Total Value', 'Gain/Loss',
                    'Gain/Loss %', 'Purchase Date', 'Notes'
                ])
                
                # Write asset data
                for asset in self.portfolio.assets:
                    writer.writerow([
                        asset.name,
                        asset.asset_type.value,
                        asset.category.value,
                        asset.quantity,
                        f"${asset.purchase_price:.2f}",
                        f"${asset.current_price:.2f}",
                        f"${asset.total_cost:.2f}",
                        f"${asset.total_value:.2f}",
                        f"${asset.gain_loss:.2f}",
                        f"{asset.gain_loss_percentage:.2f}%",
                        asset.purchase_date,
                        asset.notes
                    ])
            
            print(f"✅ Portfolio exported to {filename}")
        except Exception as e:
            print(f"❌ Error exporting portfolio: {e}")
    
    def add_asset_interactive(self) -> None:
        """Add an asset through interactive prompts."""
        print("\n📈 Add New Asset")
        print("-" * 20)
        
        try:
            name = input("Asset name: ").strip()
            if not name:
                print("❌ Asset name cannot be empty")
                return
            
            # Check if asset already exists
            if self.portfolio.find_asset(name):
                print(f"❌ Asset '{name}' already exists")
                return
            
            # Asset type selection
            print("\nAsset Types:")
            for i, asset_type in enumerate(AssetType, 1):
                print(f"{i}. {asset_type.value.replace('_', ' ').title()}")
            
            type_choice = int(input("Select asset type (number): ")) - 1
            asset_type = list(AssetType)[type_choice]
            
            # Category selection
            print("\nCategories:")
            for i, category in enumerate(AssetCategory, 1):
                print(f"{i}. {category.value.replace('_', ' ').title()}")
            
            category_choice = int(input("Select category (number): ")) - 1
            category = list(AssetCategory)[category_choice]
            
            quantity = float(input("Quantity: "))
            purchase_price = float(input("Purchase price per unit: $"))
            current_price = float(input("Current price per unit: $"))
            purchase_date = input("Purchase date (YYYY-MM-DD) or press Enter for today: ").strip()
            
            if not purchase_date:
                purchase_date = date.today().isoformat()
            
            notes = input("Notes (optional): ").strip()
            
            asset = Asset(
                name=name,
                asset_type=asset_type,
                category=category,
                quantity=quantity,
                purchase_price=purchase_price,
                current_price=current_price,
                purchase_date=purchase_date,
                notes=notes
            )
            
            self.portfolio.add_asset(asset)
            print(f"✅ Asset '{name}' added successfully!")
            
        except (ValueError, IndexError) as e:
            print(f"❌ Invalid input: {e}")
        except KeyboardInterrupt:
            print("\n❌ Operation cancelled")
    
    def display_portfolio_summary(self) -> None:
        """Display comprehensive portfolio summary."""
        if not self.portfolio.assets:
            print("📊 Portfolio is empty. Add some assets to get started!")
            return
        
        print(f"\n📊 Portfolio Summary: {self.portfolio.name}")
        print("=" * 60)
        
        # Basic statistics
        total_value = self.portfolio.get_total_value()
        total_cost = self.portfolio.get_total_cost()
        total_gain_loss = self.portfolio.get_total_gain_loss()
        total_percentage = self.portfolio.get_total_gain_loss_percentage()
        
        print(f"Total Portfolio Value: ${total_value:,.2f}")
        print(f"Total Cost Basis:      ${total_cost:,.2f}")
        print(f"Total Gain/Loss:       ${total_gain_loss:,.2f} ({total_percentage:+.2f}%)")
        print(f"Number of Assets:      {len(self.portfolio.assets)}")
        print(f"Last Updated:          {self.portfolio.last_updated[:19].replace('T', ' ')}")
        print()
        
        # Asset type allocation
        print("📋 Allocation by Asset Type:")
        print("-" * 30)
        type_allocation = self.portfolio.get_allocation_by_type()
        for asset_type, percentage in type_allocation.items():
            print(f"{asset_type.value.replace('_', ' ').title():15}: {percentage:6.2f}%")
        print()
        
        # Category allocation
        print("📋 Allocation by Category:")
        print("-" * 30)
        category_allocation = self.portfolio.get_allocation_by_category()
        for category, percentage in category_allocation.items():
            print(f"{category.value.replace('_', ' ').title():15}: {percentage:6.2f}%")
        print()
        
        # Top and worst performers
        print("🚀 Top 3 Performers:")
        print("-" * 20)
        top_performers = self.portfolio.get_top_performers(3)
        for i, asset in enumerate(top_performers, 1):
            print(f"{i}. {asset.name}: {asset.gain_loss_percentage:+.2f}% (${asset.gain_loss:+,.2f})")
        print()
        
        print("📉 Worst 3 Performers:")
        print("-" * 22)
        worst_performers = self.portfolio.get_worst_performers(3)
        for i, asset in enumerate(worst_performers, 1):
            print(f"{i}. {asset.name}: {asset.gain_loss_percentage:+.2f}% (${asset.gain_loss:+,.2f})")
        print()
    
    def display_detailed_assets(self) -> None:
        """Display detailed information for all assets."""
        if not self.portfolio.assets:
            print("📊 No assets to display.")
            return
        
        print(f"\n📋 Detailed Asset List: {self.portfolio.name}")
        print("=" * 80)
        
        # Header
        print(f"{'Name':<20} {'Type':<12} {'Qty':<8} {'Price':<10} {'Value':<12} {'Gain/Loss':<15}")
        print("-" * 80)
        
        # Asset details
        for asset in sorted(self.portfolio.assets, key=lambda x: x.total_value, reverse=True):
            gain_loss_str = f"${asset.gain_loss:+,.2f} ({asset.gain_loss_percentage:+.1f}%)"
            print(f"{asset.name:<20} {asset.asset_type.value:<12} {asset.quantity:<8.2f} "
                  f"${asset.current_price:<9.2f} ${asset.total_value:<11,.2f} {gain_loss_str:<15}")
    
    def update_prices_interactive(self) -> None:
        """Update asset prices through interactive interface."""
        if not self.portfolio.assets:
            print("📊 No assets to update.")
            return
        
        print("\n💰 Update Asset Prices")
        print("-" * 25)
        
        print("Available assets:")
        for i, asset in enumerate(self.portfolio.assets, 1):
            print(f"{i}. {asset.name} (Current: ${asset.current_price:.2f})")
        
        try:
            choice = int(input("\nSelect asset to update (number): ")) - 1
            asset = self.portfolio.assets[choice]
            
            print(f"\nUpdating: {asset.name}")
            print(f"Current price: ${asset.current_price:.2f}")
            
            new_price = float(input("New price: $"))
            old_price = asset.current_price
            asset.current_price = new_price
            self.portfolio.last_updated = datetime.now().isoformat()
            
            print(f"✅ Updated {asset.name}: ${old_price:.2f} → ${new_price:.2f}")
            
        except (ValueError, IndexError) as e:
            print(f"❌ Invalid selection: {e}")
        except KeyboardInterrupt:
            print("\n❌ Operation cancelled")


class AssetSummaryCLI:
    """Command-line interface for the Asset Summary application."""
    
    def __init__(self):
        self.manager = AssetManager()
    
    def show_menu(self) -> None:
        """Display the main menu."""
        print("\n🏦 Asset Summary CLI")
        print("=" * 30)
        print("1. View Portfolio Summary")
        print("2. View Detailed Assets")
        print("3. Add New Asset")
        print("4. Update Asset Prices")
        print("5. Remove Asset")
        print("6. Export to CSV")
        print("7. Save Portfolio")
        print("8. Load Sample Data")
        print("9. Exit")
        print("-" * 30)
    
    def load_sample_data(self) -> None:
        """Load sample portfolio data for demonstration."""
        sample_assets = [
            Asset("Apple Inc", AssetType.STOCK, AssetCategory.EQUITY, 100, 150.00, 175.50, "2023-01-15", "Tech stock"),
            Asset("Microsoft Corp", AssetType.STOCK, AssetCategory.EQUITY, 50, 250.00, 280.75, "2023-02-01", "Cloud leader"),
            Asset("Bitcoin", AssetType.CRYPTO, AssetCategory.ALTERNATIVE, 0.5, 45000.00, 42000.00, "2023-03-10", "Digital gold"),
            Asset("10-Year Treasury", AssetType.BOND, AssetCategory.FIXED_INCOME, 10, 1000.00, 980.00, "2023-01-20", "Government bond"),
            Asset("Savings Account", AssetType.CASH, AssetCategory.CASH_EQUIVALENT, 1, 25000.00, 25000.00, "2023-01-01", "Emergency fund"),
            Asset("Gold ETF", AssetType.COMMODITY, AssetCategory.ALTERNATIVE, 25, 180.00, 195.50, "2023-02-15", "Precious metals")
        ]
        
        for asset in sample_assets:
            self.manager.portfolio.add_asset(asset)
        
        print("✅ Sample portfolio data loaded!")
    
    def remove_asset_interactive(self) -> None:
        """Remove an asset through interactive interface."""
        if not self.manager.portfolio.assets:
            print("📊 No assets to remove.")
            return
        
        print("\n🗑️ Remove Asset")
        print("-" * 15)
        
        print("Available assets:")
        for i, asset in enumerate(self.manager.portfolio.assets, 1):
            print(f"{i}. {asset.name}")
        
        try:
            choice = int(input("\nSelect asset to remove (number): ")) - 1
            asset = self.manager.portfolio.assets[choice]
            asset_name = asset.name
            
            confirm = input(f"Are you sure you want to remove '{asset_name}'? (y/N): ").lower()
            if confirm == 'y':
                del self.manager.portfolio.assets[choice]
                self.manager.portfolio.last_updated = datetime.now().isoformat()
                print(f"✅ Removed '{asset_name}'")
            else:
                print("❌ Operation cancelled")
                
        except (ValueError, IndexError) as e:
            print(f"❌ Invalid selection: {e}")
        except KeyboardInterrupt:
            print("\n❌ Operation cancelled")
    
    def run(self) -> None:
        """Run the main CLI loop."""
        print("🏦 Welcome to Asset Summary CLI!")
        print("Your comprehensive portfolio management tool")
        
        while True:
            try:
                self.show_menu()
                choice = input("Select an option (1-9): ").strip()
                
                if choice == '1':
                    self.manager.display_portfolio_summary()
                elif choice == '2':
                    self.manager.display_detailed_assets()
                elif choice == '3':
                    self.manager.add_asset_interactive()
                elif choice == '4':
                    self.manager.update_prices_interactive()
                elif choice == '5':
                    self.remove_asset_interactive()
                elif choice == '6':
                    filename = input("CSV filename (press Enter for 'portfolio_export.csv'): ").strip()
                    if not filename:
                        filename = "portfolio_export.csv"
                    self.manager.export_to_csv(filename)
                elif choice == '7':
                    self.manager.save_portfolio()
                elif choice == '8':
                    self.load_sample_data()
                elif choice == '9':
                    print("💾 Saving portfolio before exit...")
                    self.manager.save_portfolio()
                    print("👋 Thank you for using Asset Summary CLI!")
                    break
                else:
                    print("❌ Invalid option. Please select 1-9.")
                    
            except KeyboardInterrupt:
                print("\n\n💾 Saving portfolio before exit...")
                self.manager.save_portfolio()
                print("👋 Goodbye!")
                break
            except Exception as e:
                print(f"❌ Unexpected error: {e}")


def main():
    """Main function to run the Asset Summary CLI."""
    print("=== Day 6: Asset Summary CLI Solution ===")
    print()
    
    # Check if script is run with command line arguments
    if len(sys.argv) > 1:
        parser = argparse.ArgumentParser(description="Asset Summary CLI")
        parser.add_argument("--demo", action="store_true", help="Run demonstration mode")
        parser.add_argument("--file", type=str, default="portfolio_data.json", help="Portfolio data file")
        
        args = parser.parse_args()
        
        if args.demo:
            # Run demonstration mode
            print("🎯 Running in demonstration mode...")
            manager = AssetManager(args.file)
            
            # Create sample portfolio
            sample_assets = [
                Asset("Apple Inc", AssetType.STOCK, AssetCategory.EQUITY, 100, 150.00, 175.50, "2023-01-15"),
                Asset("Bitcoin", AssetType.CRYPTO, AssetCategory.ALTERNATIVE, 0.5, 45000.00, 42000.00, "2023-03-10"),
                Asset("Savings", AssetType.CASH, AssetCategory.CASH_EQUIVALENT, 1, 25000.00, 25000.00, "2023-01-01")
            ]
            
            for asset in sample_assets:
                manager.portfolio.add_asset(asset)
            
            manager.display_portfolio_summary()
            manager.display_detailed_assets()
            manager.export_to_csv("demo_export.csv")
            
            print("\n📚 Key Features Demonstrated:")
            print("• Object-oriented design with dataclasses and enums")
            print("• File I/O with JSON and CSV support")
            print("• Error handling and data validation")
            print("• Interactive command-line interface")
            print("• Portfolio analytics and reporting")
            print("• Type hints and documentation")
            print("• Modular, extensible architecture")
            
            return
    
    # Run interactive CLI
    cli = AssetSummaryCLI()
    cli.run()


if __name__ == "__main__":
    main()
