"""
Day 8 Solution: Stock Prices Analysis
=====================================

This solution demonstrates comprehensive stock price analysis using lists and tuples,
including statistical analysis, trend detection, and financial calculations.

Author: Python Learning Assistant
Date: 2024
"""

import statistics
import random
from typing import List, Tuple, Dict, Optional, NamedTuple
from datetime import datetime, timedelta
from dataclasses import dataclass
from enum import Enum


# Enums for stock analysis
class TrendDirection(Enum):
    """Stock price trend directions."""
    BULLISH = "bullish"      # Upward trend
    BEARISH = "bearish"      # Downward trend
    SIDEWAYS = "sideways"    # No clear trend


class SignalType(Enum):
    """Trading signal types."""
    BUY = "buy"
    SELL = "sell"
    HOLD = "hold"


# Data structures for stock data
class StockPrice(NamedTuple):
    """Represents a single stock price data point."""
    date: str
    open_price: float
    high: float
    low: float
    close: float
    volume: int
    
    @property
    def day_change(self) -> float:
        """Calculate daily price change."""
        return self.close - self.open_price
    
    @property
    def day_change_percent(self) -> float:
        """Calculate daily percentage change."""
        if self.open_price == 0:
            return 0.0
        return (self.day_change / self.open_price) * 100
    
    @property
    def day_range(self) -> float:
        """Calculate daily trading range."""
        return self.high - self.low
    
    @property
    def typical_price(self) -> float:
        """Calculate typical price (HLC/3)."""
        return (self.high + self.low + self.close) / 3


@dataclass
class StockAnalysis:
    """Comprehensive stock analysis results."""
    symbol: str
    analysis_period: str
    current_price: float
    price_change: float
    percent_change: float
    trend_direction: TrendDirection
    support_level: float
    resistance_level: float
    moving_average_20: float
    moving_average_50: float
    volatility: float
    total_volume: int
    recommendation: SignalType


class StockPriceAnalyzer:
    """Comprehensive stock price analysis system."""
    
    def __init__(self, symbol: str):
        self.symbol = symbol
        self.prices: List[StockPrice] = []
    
    def add_price_data(self, price_data: StockPrice) -> None:
        """Add a single price data point."""
        self.prices.append(price_data)
        # Keep prices sorted by date
        self.prices.sort(key=lambda p: p.date)
    
    def add_multiple_prices(self, price_list: List[StockPrice]) -> None:
        """Add multiple price data points."""
        self.prices.extend(price_list)
        self.prices.sort(key=lambda p: p.date)
    
    def get_price_list(self, price_type: str = 'close') -> List[float]:
        """
        Extract a specific price type as a list.
        
        Args:
            price_type: 'open', 'high', 'low', 'close'
        """
        if price_type == 'open':
            return [p.open_price for p in self.prices]
        elif price_type == 'high':
            return [p.high for p in self.prices]
        elif price_type == 'low':
            return [p.low for p in self.prices]
        elif price_type == 'close':
            return [p.close for p in self.prices]
        else:
            raise ValueError(f"Invalid price type: {price_type}")
    
    def calculate_moving_average(self, period: int, price_type: str = 'close') -> List[float]:
        """Calculate moving average for specified period."""
        prices = self.get_price_list(price_type)
        moving_averages = []
        
        for i in range(len(prices)):
            if i < period - 1:
                # Not enough data for full period
                moving_averages.append(None)
            else:
                # Calculate average for the period
                period_prices = prices[i - period + 1:i + 1]
                avg = sum(period_prices) / len(period_prices)
                moving_averages.append(avg)
        
        return moving_averages
    
    def calculate_volatility(self, period: int = 20) -> float:
        """Calculate price volatility (standard deviation of returns)."""
        if len(self.prices) < 2:
            return 0.0
        
        # Calculate daily returns
        returns = []
        for i in range(1, min(len(self.prices), period + 1)):
            prev_close = self.prices[i-1].close
            curr_close = self.prices[i].close
            if prev_close != 0:
                daily_return = (curr_close - prev_close) / prev_close
                returns.append(daily_return)
        
        if len(returns) < 2:
            return 0.0
        
        return statistics.stdev(returns) * 100  # Return as percentage
    
    def find_support_resistance(self) -> Tuple[float, float]:
        """
        Find support and resistance levels using recent price data.
        
        Returns:
            Tuple of (support_level, resistance_level)
        """
        if not self.prices:
            return (0.0, 0.0)
        
        # Use recent 20 periods or all available data
        recent_prices = self.prices[-20:] if len(self.prices) >= 20 else self.prices
        
        # Support: lowest low in recent period
        support = min(price.low for price in recent_prices)
        
        # Resistance: highest high in recent period
        resistance = max(price.high for price in recent_prices)
        
        return (support, resistance)
    
    def detect_trend(self, period: int = 10) -> TrendDirection:
        """
        Detect price trend using moving averages.
        
        Args:
            period: Number of periods to analyze
        """
        if len(self.prices) < period:
            return TrendDirection.SIDEWAYS
        
        # Compare recent prices with earlier prices
        recent_prices = [p.close for p in self.prices[-period:]]
        earlier_prices = [p.close for p in self.prices[-period*2:-period]] if len(self.prices) >= period * 2 else recent_prices
        
        recent_avg = sum(recent_prices) / len(recent_prices)
        earlier_avg = sum(earlier_prices) / len(earlier_prices)
        
        threshold = 0.02  # 2% threshold for trend detection
        
        if recent_avg > earlier_avg * (1 + threshold):
            return TrendDirection.BULLISH
        elif recent_avg < earlier_avg * (1 - threshold):
            return TrendDirection.BEARISH
        else:
            return TrendDirection.SIDEWAYS
    
    def generate_trading_signal(self) -> SignalType:
        """Generate a simple trading signal based on technical analysis."""
        if len(self.prices) < 20:
            return SignalType.HOLD
        
        current_price = self.prices[-1].close
        ma_20 = self.calculate_moving_average(20)[-1]
        ma_50 = self.calculate_moving_average(50)[-1] if len(self.prices) >= 50 else ma_20
        
        trend = self.detect_trend()
        support, resistance = self.find_support_resistance()
        
        # Simple signal logic
        if (current_price > ma_20 and 
            (ma_50 is None or ma_20 > ma_50) and 
            trend == TrendDirection.BULLISH and
            current_price > support * 1.02):  # Above support with buffer
            return SignalType.BUY
        elif (current_price < ma_20 and 
              (ma_50 is None or ma_20 < ma_50) and 
              trend == TrendDirection.BEARISH and
              current_price < resistance * 0.98):  # Below resistance with buffer
            return SignalType.SELL
        else:
            return SignalType.HOLD
    
    def get_comprehensive_analysis(self) -> StockAnalysis:
        """Generate comprehensive stock analysis."""
        if not self.prices:
            return StockAnalysis(
                symbol=self.symbol,
                analysis_period="No data",
                current_price=0.0,
                price_change=0.0,
                percent_change=0.0,
                trend_direction=TrendDirection.SIDEWAYS,
                support_level=0.0,
                resistance_level=0.0,
                moving_average_20=0.0,
                moving_average_50=0.0,
                volatility=0.0,
                total_volume=0,
                recommendation=SignalType.HOLD
            )
        
        # Calculate metrics
        current_price = self.prices[-1].close
        first_price = self.prices[0].open_price
        price_change = current_price - first_price
        percent_change = (price_change / first_price * 100) if first_price != 0 else 0.0
        
        trend = self.detect_trend()
        support, resistance = self.find_support_resistance()
        
        ma_20_list = self.calculate_moving_average(20)
        ma_50_list = self.calculate_moving_average(50)
        
        ma_20 = ma_20_list[-1] if ma_20_list[-1] is not None else current_price
        ma_50 = ma_50_list[-1] if len(ma_50_list) > 0 and ma_50_list[-1] is not None else current_price
        
        volatility = self.calculate_volatility()
        total_volume = sum(p.volume for p in self.prices)
        recommendation = self.generate_trading_signal()
        
        analysis_period = f"{self.prices[0].date} to {self.prices[-1].date}"
        
        return StockAnalysis(
            symbol=self.symbol,
            analysis_period=analysis_period,
            current_price=current_price,
            price_change=price_change,
            percent_change=percent_change,
            trend_direction=trend,
            support_level=support,
            resistance_level=resistance,
            moving_average_20=ma_20,
            moving_average_50=ma_50,
            volatility=volatility,
            total_volume=total_volume,
            recommendation=recommendation
        )


class PortfolioAnalyzer:
    """Analyze a portfolio of multiple stocks."""
    
    def __init__(self):
        self.stocks: Dict[str, StockPriceAnalyzer] = {}
        self.holdings: Dict[str, int] = {}  # Symbol -> number of shares
    
    def add_stock(self, symbol: str, analyzer: StockPriceAnalyzer, shares: int = 0) -> None:
        """Add a stock to the portfolio."""
        self.stocks[symbol] = analyzer
        self.holdings[symbol] = shares
    
    def get_portfolio_value(self) -> float:
        """Calculate total portfolio value."""
        total_value = 0.0
        for symbol, shares in self.holdings.items():
            if symbol in self.stocks and self.stocks[symbol].prices:
                current_price = self.stocks[symbol].prices[-1].close
                total_value += shares * current_price
        return total_value
    
    def get_portfolio_performance(self) -> Dict[str, float]:
        """Get performance metrics for the entire portfolio."""
        total_current_value = 0.0
        total_cost_basis = 0.0
        
        for symbol, shares in self.holdings.items():
            if symbol in self.stocks and self.stocks[symbol].prices:
                analyzer = self.stocks[symbol]
                current_price = analyzer.prices[-1].close
                first_price = analyzer.prices[0].open_price
                
                current_value = shares * current_price
                cost_basis = shares * first_price
                
                total_current_value += current_value
                total_cost_basis += cost_basis
        
        if total_cost_basis == 0:
            return {'total_value': 0.0, 'total_gain_loss': 0.0, 'percent_return': 0.0}
        
        total_gain_loss = total_current_value - total_cost_basis
        percent_return = (total_gain_loss / total_cost_basis) * 100
        
        return {
            'total_value': total_current_value,
            'total_gain_loss': total_gain_loss,
            'percent_return': percent_return
        }


def generate_sample_stock_data(symbol: str, days: int = 30, start_price: float = 100.0) -> List[StockPrice]:
    """Generate realistic sample stock price data."""
    prices = []
    current_price = start_price
    
    # Generate dates
    start_date = datetime.now() - timedelta(days=days)
    
    for i in range(days):
        date = (start_date + timedelta(days=i)).strftime('%Y-%m-%d')
        
        # Simulate realistic price movement
        daily_volatility = 0.02  # 2% daily volatility
        price_change = random.normalvariate(0, daily_volatility)
        
        # Open price (close to previous close)
        open_price = current_price * (1 + random.normalvariate(0, 0.005))
        
        # Daily range
        day_range = open_price * random.uniform(0.01, 0.05)  # 1-5% daily range
        
        # High and low
        high = open_price + day_range * random.uniform(0.3, 1.0)
        low = open_price - day_range * random.uniform(0.3, 1.0)
        
        # Close price
        close_price = low + (high - low) * random.random()
        
        # Volume (random but realistic)
        volume = random.randint(100000, 2000000)
        
        # Ensure logical price relationships
        high = max(high, open_price, close_price)
        low = min(low, open_price, close_price)
        
        price_point = StockPrice(
            date=date,
            open_price=round(open_price, 2),
            high=round(high, 2),
            low=round(low, 2),
            close=round(close_price, 2),
            volume=volume
        )
        
        prices.append(price_point)
        current_price = close_price
    
    return prices


def demonstrate_stock_analysis():
    """Demonstrate comprehensive stock price analysis."""
    print("=== Stock Price Analysis Demo ===")
    print()
    
    # Generate sample data for multiple stocks
    stocks_data = {
        'AAPL': generate_sample_stock_data('AAPL', 50, 150.0),
        'GOOGL': generate_sample_stock_data('GOOGL', 50, 2500.0),
        'MSFT': generate_sample_stock_data('MSFT', 50, 300.0),
        'TSLA': generate_sample_stock_data('TSLA', 50, 800.0)
    }
    
    # Analyze each stock
    for symbol, price_data in stocks_data.items():
        print(f"📈 Analysis for {symbol}")
        print("-" * 30)
        
        # Create analyzer
        analyzer = StockPriceAnalyzer(symbol)
        analyzer.add_multiple_prices(price_data)
        
        # Get comprehensive analysis
        analysis = analyzer.get_comprehensive_analysis()
        
        # Display results
        print(f"Symbol: {analysis.symbol}")
        print(f"Period: {analysis.analysis_period}")
        print(f"Current Price: ${analysis.current_price:.2f}")
        print(f"Price Change: ${analysis.price_change:+.2f} ({analysis.percent_change:+.2f}%)")
        print(f"Trend: {analysis.trend_direction.value.upper()}")
        print(f"Support Level: ${analysis.support_level:.2f}")
        print(f"Resistance Level: ${analysis.resistance_level:.2f}")
        print(f"20-day MA: ${analysis.moving_average_20:.2f}")
        print(f"50-day MA: ${analysis.moving_average_50:.2f}")
        print(f"Volatility: {analysis.volatility:.2f}%")
        print(f"Total Volume: {analysis.total_volume:,}")
        print(f"Recommendation: {analysis.recommendation.value.upper()}")
        
        # Show recent prices
        print(f"\nRecent Prices (last 5 days):")
        for price in price_data[-5:]:
            change_indicator = "📈" if price.day_change >= 0 else "📉"
            print(f"  {price.date}: ${price.close:.2f} {change_indicator} {price.day_change_percent:+.1f}%")
        
        print()


def demonstrate_portfolio_analysis():
    """Demonstrate portfolio-level analysis."""
    print("=== Portfolio Analysis Demo ===")
    print()
    
    # Create portfolio
    portfolio = PortfolioAnalyzer()
    
    # Add stocks to portfolio with holdings
    stocks_info = [
        ('AAPL', 150.0, 100),   # 100 shares
        ('GOOGL', 2500.0, 10),  # 10 shares
        ('MSFT', 300.0, 50),    # 50 shares
        ('TSLA', 800.0, 25)     # 25 shares
    ]
    
    print("Portfolio Holdings:")
    print("-" * 40)
    
    total_cost_basis = 0.0
    for symbol, start_price, shares in stocks_info:
        # Generate data and create analyzer
        price_data = generate_sample_stock_data(symbol, 30, start_price)
        analyzer = StockPriceAnalyzer(symbol)
        analyzer.add_multiple_prices(price_data)
        
        # Add to portfolio
        portfolio.add_stock(symbol, analyzer, shares)
        
        # Calculate position details
        current_price = price_data[-1].close
        position_value = shares * current_price
        cost_basis = shares * start_price
        position_gain_loss = position_value - cost_basis
        position_return = (position_gain_loss / cost_basis) * 100
        
        total_cost_basis += cost_basis
        
        print(f"{symbol}: {shares} shares @ ${current_price:.2f}")
        print(f"  Position Value: ${position_value:,.2f}")
        print(f"  Gain/Loss: ${position_gain_loss:+,.2f} ({position_return:+.1f}%)")
        print()
    
    # Portfolio summary
    performance = portfolio.get_portfolio_performance()
    print("Portfolio Summary:")
    print("-" * 25)
    print(f"Total Value: ${performance['total_value']:,.2f}")
    print(f"Total Cost Basis: ${total_cost_basis:,.2f}")
    print(f"Total Gain/Loss: ${performance['total_gain_loss']:+,.2f}")
    print(f"Portfolio Return: {performance['percent_return']:+.2f}%")
    print()


def demonstrate_price_patterns():
    """Demonstrate detection of common price patterns."""
    print("=== Price Pattern Analysis ===")
    print()
    
    # Create different trend patterns
    patterns = {
        'Bullish': [100, 102, 105, 103, 107, 110, 108, 112, 115, 118],
        'Bearish': [100, 98, 95, 97, 93, 90, 92, 88, 85, 82],
        'Sideways': [100, 101, 99, 102, 98, 101, 99, 100, 102, 98]
    }
    
    for pattern_name, prices in patterns.items():
        print(f"📊 {pattern_name} Pattern Analysis")
        print("-" * 30)
        
        # Create price data
        price_data = []
        base_date = datetime.now() - timedelta(days=len(prices))
        
        for i, price in enumerate(prices):
            date = (base_date + timedelta(days=i)).strftime('%Y-%m-%d')
            # Create realistic OHLC data
            open_price = price
            close_price = price
            high = price * random.uniform(1.0, 1.02)
            low = price * random.uniform(0.98, 1.0)
            volume = random.randint(100000, 500000)
            
            price_data.append(StockPrice(date, open_price, high, low, close_price, volume))
        
        # Analyze pattern
        analyzer = StockPriceAnalyzer(f"PATTERN_{pattern_name}")
        analyzer.add_multiple_prices(price_data)
        
        analysis = analyzer.get_comprehensive_analysis()
        
        print(f"Trend Direction: {analysis.trend_direction.value.upper()}")
        print(f"Price Change: {analysis.percent_change:+.2f}%")
        print(f"Volatility: {analysis.volatility:.2f}%")
        print(f"Recommendation: {analysis.recommendation.value.upper()}")
        print(f"Prices: {[p.close for p in price_data]}")
        print()


def main():
    """Main function demonstrating stock price analysis."""
    print("=== Day 8: Stock Price Analysis Solutions ===")
    print()
    
    # Run demonstrations
    demonstrate_stock_analysis()
    demonstrate_portfolio_analysis()
    demonstrate_price_patterns()
    
    # Educational summary
    print("📚 Key Concepts Learned:")
    print("• Stock price data structure using NamedTuple")
    print("• OHLC (Open, High, Low, Close) price representation")
    print("• Moving averages for trend analysis")
    print("• Support and resistance level calculation")
    print("• Volatility measurement using standard deviation")
    print("• Portfolio-level analysis and performance tracking")
    print("• Trading signal generation using technical indicators")
    print("• Price pattern recognition and trend detection")
    print("• Risk management through position sizing")
    print("• Data organization using lists and tuples for financial data")
    print()
    
    print("💡 Real-World Applications:")
    print("• Algorithmic trading systems")
    print("• Portfolio management tools")
    print("• Risk assessment applications")
    print("• Financial reporting dashboards")
    print("• Investment research platforms")


if __name__ == "__main__":
    main()
