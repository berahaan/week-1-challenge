"""
Pytest configuration and shared fixtures.
"""
import pytest
import pandas as pd
import numpy as np
from datetime import datetime, timedelta


@pytest.fixture
def sample_stock_data():
    """Create sample stock data for testing."""
    dates = pd.date_range('2020-01-01', periods=100, freq='D')
    np.random.seed(42)  # For reproducible tests
    
    data = {
        'Date': dates,
        'Open': 100 + np.cumsum(np.random.randn(100) * 2),
        'High': 100 + np.cumsum(np.random.randn(100) * 2) + np.random.rand(100) * 5,
        'Low': 100 + np.cumsum(np.random.randn(100) * 2) - np.random.rand(100) * 5,
        'Close': 100 + np.cumsum(np.random.randn(100) * 2),
        'Volume': np.random.randint(1000000, 10000000, 100)
    }
    
    df = pd.DataFrame(data)
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    
    # Ensure High >= Close >= Low
    df['High'] = df[['High', 'Close']].max(axis=1)
    df['Low'] = df[['Low', 'Close']].min(axis=1)
    
    return df


@pytest.fixture
def sample_news_data():
    """Create sample news data for testing."""
    dates = pd.date_range('2020-01-01', periods=50, freq='D')
    
    headlines = [
        "Stocks That Hit 52-Week Highs On Friday",
        "Apple Reports Strong Earnings",
        "Price Target Raised by Analyst",
        "FDA Approval for New Drug",
        "Market Analysis Shows Bullish Trend"
    ] * 10
    
    data = {
        'date': dates[:50],
        'headline': headlines[:50],
        'publisher': ['Publisher A', 'Publisher B', 'Publisher C'] * 17 + ['Publisher A'],
        'stock': ['AAPL', 'MSFT', 'GOOG'] * 17 + ['AAPL'],
        'url': [f'https://example.com/article{i}' for i in range(50)]
    }
    
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])
    
    return df


@pytest.fixture
def sample_returns():
    """Create sample returns data for testing."""
    np.random.seed(42)
    dates = pd.date_range('2020-01-01', periods=252, freq='D')  # 1 year of trading days
    returns = np.random.randn(252) * 0.02  # 2% daily volatility
    
    df = pd.DataFrame({
        'Date': dates,
        'Daily_Return': returns
    })
    df.set_index('Date', inplace=True)
    
    return df

