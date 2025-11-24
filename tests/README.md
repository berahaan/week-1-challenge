# Tests Directory

This directory contains unit tests for the Financial News Sentiment Analysis project.

## Test Structure

### Test Files

- **`test_data_loading.py`**: Tests for data loading and preprocessing functions
  - Data structure validation
  - Date conversion and formatting
  - Numeric column conversion
  - Data preprocessing operations

- **`test_technical_indicators.py`**: Tests for technical indicator calculations
  - Moving Averages (SMA, EMA)
  - Relative Strength Index (RSI)
  - MACD (Moving Average Convergence Divergence)
  - Bollinger Bands
  - Financial metrics (returns, volatility)

- **`test_text_analysis.py`**: Tests for text analysis functions
  - Headline processing
  - Keyword extraction
  - Significant phrase detection
  - Publisher analysis
  - Temporal analysis

- **`test_utils.py`**: Tests for utility functions
  - Data validation
  - Data transformation
  - Statistical calculations (Sharpe ratio, drawdown)

- **`conftest.py`**: Pytest configuration and shared fixtures
  - Sample stock data fixture
  - Sample news data fixture
  - Sample returns fixture

## Running Tests

### Run all tests
```bash
pytest tests/
```

### Run specific test file
```bash
pytest tests/test_data_loading.py
```

### Run with coverage report
```bash
pytest tests/ --cov=. --cov-report=html
```

### Run with verbose output
```bash
pytest tests/ -v
```

### Run specific test class
```bash
pytest tests/test_technical_indicators.py::TestMovingAverages
```

### Run specific test function
```bash
pytest tests/test_data_loading.py::TestDataLoading::test_load_stock_data_structure
```

## Test Coverage

The tests cover:
- ✅ Data loading and preprocessing
- ✅ Technical indicator calculations
- ✅ Text analysis functions
- ✅ Financial metrics calculations
- ✅ Utility functions
- ✅ Data validation

## Continuous Integration

Tests are automatically run via GitHub Actions on:
- Push to main branch
- Pull requests
- Push to task branches (task-1, task-2, task-3)

See `.github/workflows/unittests.yml` for CI/CD configuration.

## Writing New Tests

When adding new functionality, follow these guidelines:

1. **Create test file**: Add a new `test_*.py` file in the tests directory
2. **Use fixtures**: Leverage fixtures from `conftest.py` for sample data
3. **Follow naming**: Use descriptive test function names starting with `test_`
4. **Assert clearly**: Use clear assertions that explain what is being tested
5. **Test edge cases**: Include tests for boundary conditions and error cases

### Example Test Structure

```python
import pytest
import pandas as pd

class TestNewFeature:
    """Test new feature functionality."""
    
    def test_basic_functionality(self):
        """Test basic functionality works."""
        # Arrange
        data = pd.DataFrame({'col': [1, 2, 3]})
        
        # Act
        result = your_function(data)
        
        # Assert
        assert result is not None
        assert len(result) == 3
```

## Dependencies

Tests require:
- pytest >= 8.3.4
- pytest-cov >= 6.0.0
- pandas
- numpy

All dependencies are listed in `requirements.txt`.

