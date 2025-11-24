"""
Tests for data loading and preprocessing functions.
"""
import pytest
import pandas as pd
import numpy as np
from datetime import datetime


class TestDataLoading:
    """Test data loading functionality."""
    
    def test_load_stock_data_structure(self):
        """Test that stock data has correct structure."""
        # Sample stock data structure
        dates = pd.date_range('2020-01-01', periods=10, freq='D')
        data = {
            'Date': dates,
            'Open': np.random.rand(10) * 100,
            'High': np.random.rand(10) * 100,
            'Low': np.random.rand(10) * 100,
            'Close': np.random.rand(10) * 100,
            'Volume': np.random.randint(1000000, 10000000, 10)
        }
        df = pd.DataFrame(data)
        
        assert 'Date' in df.columns
        assert 'Open' in df.columns
        assert 'High' in df.columns
        assert 'Low' in df.columns
        assert 'Close' in df.columns
        assert 'Volume' in df.columns
    
    def test_date_conversion(self):
        """Test date column conversion to datetime."""
        dates = ['2020-01-01', '2020-01-02', '2020-01-03']
        df = pd.DataFrame({'date': dates})
        df['date'] = pd.to_datetime(df['date'])
        
        assert df['date'].dtype == 'datetime64[ns]'
        assert isinstance(df['date'].iloc[0], pd.Timestamp)
    
    def test_mixed_date_formats(self):
        """Test handling of mixed date formats."""
        dates = [
            '2020-01-01 10:30:54-04:00',
            '2020-01-02 00:00:00',
            '2020-01-03 15:45:20-04:00'
        ]
        df = pd.DataFrame({'date': dates})
        df['date'] = pd.to_datetime(df['date'], format='mixed', errors='coerce', utc=True)
        df['date'] = df['date'].dt.tz_localize(None)
        
        assert not df['date'].isna().any()
        assert df['date'].dtype == 'datetime64[ns]'
    
    def test_numeric_columns(self):
        """Test that numeric columns are properly converted."""
        df = pd.DataFrame({
            'Close': ['100.5', '101.2', '99.8'],
            'Volume': ['1000000', '2000000', '1500000']
        })
        
        df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
        df['Volume'] = pd.to_numeric(df['Volume'], errors='coerce')
        
        assert df['Close'].dtype in ['float64', 'float32']
        assert df['Volume'].dtype in ['int64', 'int32', 'float64']


class TestDataPreprocessing:
    """Test data preprocessing functions."""
    
    def test_drop_unnamed_column(self):
        """Test dropping Unnamed: 0 column."""
        df = pd.DataFrame({
            'Unnamed: 0': range(5),
            'headline': ['Test'] * 5,
            'date': pd.date_range('2020-01-01', periods=5)
        })
        
        if 'Unnamed: 0' in df.columns:
            df = df.drop('Unnamed: 0', axis=1)
        
        assert 'Unnamed: 0' not in df.columns
    
    def test_extract_date_components(self):
        """Test extraction of date components."""
        dates = pd.date_range('2020-01-01', periods=10, freq='D')
        df = pd.DataFrame({'date': dates})
        
        df['year'] = df['date'].dt.year
        df['month'] = df['date'].dt.month
        df['day_of_week'] = df['date'].dt.day_name()
        df['hour'] = df['date'].dt.hour
        
        assert 'year' in df.columns
        assert 'month' in df.columns
        assert 'day_of_week' in df.columns
        assert 'hour' in df.columns
        assert df['year'].iloc[0] == 2020


if __name__ == '__main__':
    pytest.main([__file__])

