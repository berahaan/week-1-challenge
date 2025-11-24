"""
Tests for technical indicator calculations.
"""
import pytest
import pandas as pd
import numpy as np


class TestMovingAverages:
    """Test moving average calculations."""
    
    def test_sma_calculation(self):
        """Test Simple Moving Average calculation."""
        dates = pd.date_range('2020-01-01', periods=30, freq='D')
        prices = np.random.rand(30) * 100 + 50
        df = pd.DataFrame({'Date': dates, 'Close': prices})
        df.set_index('Date', inplace=True)
        
        # Calculate SMA
        df['SMA_20'] = df['Close'].rolling(window=20).mean()
        
        assert 'SMA_20' in df.columns
        assert not df['SMA_20'].iloc[:19].notna().any()  # First 19 should be NaN
        assert df['SMA_20'].iloc[19:].notna().all()  # From index 19 onwards should have values
    
    def test_ema_calculation(self):
        """Test Exponential Moving Average calculation."""
        dates = pd.date_range('2020-01-01', periods=30, freq='D')
        prices = np.random.rand(30) * 100 + 50
        df = pd.DataFrame({'Date': dates, 'Close': prices})
        df.set_index('Date', inplace=True)
        
        # Calculate EMA
        df['EMA_12'] = df['Close'].ewm(span=12, adjust=False).mean()
        
        assert 'EMA_12' in df.columns
        assert df['EMA_12'].iloc[0] == df['Close'].iloc[0]  # First value should equal close
        assert df['EMA_12'].notna().all()  # All values should be non-null


class TestRSI:
    """Test Relative Strength Index calculation."""
    
    def test_rsi_calculation(self):
        """Test RSI calculation."""
        dates = pd.date_range('2020-01-01', periods=30, freq='D')
        # Create price series with some trend
        prices = 50 + np.cumsum(np.random.randn(30) * 2)
        df = pd.DataFrame({'Date': dates, 'Close': prices})
        df.set_index('Date', inplace=True)
        
        # Calculate RSI
        delta = df['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        df['RSI'] = 100 - (100 / (1 + rs))
        
        assert 'RSI' in df.columns
        # RSI should be between 0 and 100
        valid_rsi = df['RSI'].dropna()
        if len(valid_rsi) > 0:
            assert (valid_rsi >= 0).all()
            assert (valid_rsi <= 100).all()


class TestMACD:
    """Test MACD calculation."""
    
    def test_macd_calculation(self):
        """Test MACD calculation."""
        dates = pd.date_range('2020-01-01', periods=50, freq='D')
        prices = 50 + np.cumsum(np.random.randn(50) * 2)
        df = pd.DataFrame({'Date': dates, 'Close': prices})
        df.set_index('Date', inplace=True)
        
        # Calculate MACD
        ema_12 = df['Close'].ewm(span=12, adjust=False).mean()
        ema_26 = df['Close'].ewm(span=26, adjust=False).mean()
        df['MACD'] = ema_12 - ema_26
        df['MACD_signal'] = df['MACD'].ewm(span=9, adjust=False).mean()
        df['MACD_histogram'] = df['MACD'] - df['MACD_signal']
        
        assert 'MACD' in df.columns
        assert 'MACD_signal' in df.columns
        assert 'MACD_histogram' in df.columns
        # MACD should have values after enough data points
        assert df['MACD'].iloc[25:].notna().any()


class TestBollingerBands:
    """Test Bollinger Bands calculation."""
    
    def test_bollinger_bands_calculation(self):
        """Test Bollinger Bands calculation."""
        dates = pd.date_range('2020-01-01', periods=30, freq='D')
        prices = np.random.rand(30) * 100 + 50
        df = pd.DataFrame({'Date': dates, 'Close': prices})
        df.set_index('Date', inplace=True)
        
        # Calculate Bollinger Bands
        df['BB_middle'] = df['Close'].rolling(window=20).mean()
        std = df['Close'].rolling(window=20).std()
        df['BB_upper'] = df['BB_middle'] + (std * 2)
        df['BB_lower'] = df['BB_middle'] - (std * 2)
        
        assert 'BB_upper' in df.columns
        assert 'BB_middle' in df.columns
        assert 'BB_lower' in df.columns
        # Upper band should be above middle, lower should be below
        valid_data = df[['BB_upper', 'BB_middle', 'BB_lower']].dropna()
        if len(valid_data) > 0:
            assert (valid_data['BB_upper'] >= valid_data['BB_middle']).all()
            assert (valid_data['BB_lower'] <= valid_data['BB_middle']).all()


class TestFinancialMetrics:
    """Test financial metrics calculations."""
    
    def test_daily_returns(self):
        """Test daily returns calculation."""
        dates = pd.date_range('2020-01-01', periods=10, freq='D')
        prices = [100, 102, 101, 103, 105, 104, 106, 107, 108, 110]
        df = pd.DataFrame({'Date': dates, 'Close': prices})
        df.set_index('Date', inplace=True)
        
        df['Daily_Return'] = df['Close'].pct_change()
        
        assert 'Daily_Return' in df.columns
        assert pd.isna(df['Daily_Return'].iloc[0])  # First value should be NaN
        assert not pd.isna(df['Daily_Return'].iloc[1:]).all()  # Others should have values
    
    def test_cumulative_returns(self):
        """Test cumulative returns calculation."""
        dates = pd.date_range('2020-01-01', periods=10, freq='D')
        prices = [100, 102, 101, 103, 105, 104, 106, 107, 108, 110]
        df = pd.DataFrame({'Date': dates, 'Close': prices})
        df.set_index('Date', inplace=True)
        
        df['Daily_Return'] = df['Close'].pct_change()
        df['Cumulative_Return'] = (1 + df['Daily_Return']).cumprod() - 1
        
        assert 'Cumulative_Return' in df.columns
        # Final cumulative return should match price change
        final_return = (df['Close'].iloc[-1] / df['Close'].iloc[0]) - 1
        assert abs(df['Cumulative_Return'].iloc[-1] - final_return) < 0.01
    
    def test_volatility_calculation(self):
        """Test volatility calculation."""
        dates = pd.date_range('2020-01-01', periods=50, freq='D')
        returns = np.random.randn(50) * 0.02  # 2% daily volatility
        df = pd.DataFrame({'Date': dates, 'Daily_Return': returns})
        df.set_index('Date', inplace=True)
        
        df['Volatility'] = df['Daily_Return'].rolling(window=30).std() * np.sqrt(252)
        
        assert 'Volatility' in df.columns
        valid_vol = df['Volatility'].dropna()
        if len(valid_vol) > 0:
            assert (valid_vol >= 0).all()  # Volatility should be non-negative


if __name__ == '__main__':
    pytest.main([__file__])

