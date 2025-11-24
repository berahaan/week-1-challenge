"""
Tests for utility functions.
"""
import pytest
import pandas as pd
import numpy as np


class TestDataValidation:
    """Test data validation functions."""
    
    def test_check_required_columns(self):
        """Test checking for required columns."""
        required_cols = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
        df = pd.DataFrame({
            'Date': pd.date_range('2020-01-01', periods=10),
            'Open': range(10),
            'High': range(10),
            'Low': range(10),
            'Close': range(10),
            'Volume': range(10)
        })
        
        missing_cols = [col for col in required_cols if col not in df.columns]
        assert len(missing_cols) == 0
    
    def test_check_missing_values(self):
        """Test checking for missing values."""
        df = pd.DataFrame({
            'Close': [100, 101, None, 103, 104],
            'Volume': [1000, 2000, 3000, 4000, 5000]
        })
        
        missing_count = df.isnull().sum()
        assert missing_count['Close'] == 1
        assert missing_count['Volume'] == 0
    
    def test_check_data_types(self):
        """Test checking data types."""
        df = pd.DataFrame({
            'Close': [100.5, 101.2, 102.3],
            'Volume': [1000000, 2000000, 3000000],
            'Date': pd.date_range('2020-01-01', periods=3)
        })
        
        assert pd.api.types.is_numeric_dtype(df['Close'])
        assert pd.api.types.is_numeric_dtype(df['Volume'])
        assert pd.api.types.is_datetime64_any_dtype(df['Date'])


class TestDataTransformation:
    """Test data transformation functions."""
    
    def test_normalize_prices(self):
        """Test price normalization."""
        prices = [100, 110, 120, 115, 125]
        base_price = prices[0]
        normalized = [(p / base_price) * 100 for p in prices]
        
        assert normalized[0] == 100.0
        assert all(n >= 0 for n in normalized)
    
    def test_calculate_percentage_change(self):
        """Test percentage change calculation."""
        prices = [100, 110, 105, 115]
        pct_change = [(prices[i] / prices[i-1] - 1) * 100 
                     for i in range(1, len(prices))]
        
        assert len(pct_change) == 3
        assert abs(pct_change[0] - 10.0) < 0.01  # 10% increase
        assert abs(pct_change[1] - (-4.55)) < 0.1  # ~4.55% decrease
    
    def test_rolling_statistics(self):
        """Test rolling statistics calculation."""
        data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        df = pd.DataFrame({'value': data})
        
        df['rolling_mean'] = df['value'].rolling(window=5).mean()
        df['rolling_std'] = df['value'].rolling(window=5).std()
        
        assert 'rolling_mean' in df.columns
        assert 'rolling_std' in df.columns
        # First 4 values should be NaN
        assert df['rolling_mean'].iloc[:4].isna().all()
        # 5th value should be mean of first 5
        assert abs(df['rolling_mean'].iloc[4] - 30.0) < 0.01


class TestStatisticalFunctions:
    """Test statistical calculation functions."""
    
    def test_sharpe_ratio_calculation(self):
        """Test Sharpe ratio calculation."""
        returns = [0.01, 0.02, -0.01, 0.015, 0.01]  # Sample returns
        mean_return = np.mean(returns)
        std_return = np.std(returns)
        
        # Annualized (assuming 252 trading days)
        annualized_return = mean_return * 252
        annualized_std = std_return * np.sqrt(252)
        
        sharpe_ratio = annualized_return / annualized_std if annualized_std > 0 else 0
        
        assert isinstance(sharpe_ratio, (int, float))
        assert not np.isnan(sharpe_ratio)
        assert not np.isinf(sharpe_ratio)
    
    def test_max_drawdown_calculation(self):
        """Test maximum drawdown calculation."""
        prices = [100, 110, 105, 120, 115, 130, 125, 140]
        df = pd.DataFrame({'Close': prices})
        
        # Calculate running maximum
        running_max = df['Close'].expanding().max()
        # Calculate drawdown
        drawdown = (df['Close'] / running_max) - 1
        max_drawdown = drawdown.min()
        
        assert max_drawdown <= 0  # Drawdown should be negative or zero
        assert abs(max_drawdown - (-0.0455)) < 0.01  # Approximately -4.55%


if __name__ == '__main__':
    pytest.main([__file__])

