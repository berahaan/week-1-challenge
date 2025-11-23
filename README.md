# Financial News Sentiment Analysis - Week 1 Challenge

## Project Overview

This project focuses on analyzing financial news data to discover correlations between news sentiment and stock market movements. The analysis includes sentiment analysis, technical indicators, and correlation analysis between news sentiment and daily stock returns.

## Business Objective

Nova Financial Solutions aims to enhance its predictive analytics capabilities to significantly boost financial forecasting accuracy and operational efficiency through advanced data analysis. The primary tasks include:

1. **Sentiment Analysis**: Perform sentiment analysis on news headlines to quantify tone and sentiment
2. **Correlation Analysis**: Establish statistical correlations between news sentiment and stock price movements

## Project Structure

```
├── .vscode/
│   └── settings.json          # VS Code settings for Python development
├── .github/
│   └── workflows/
│       └── unittests.yml      # CI/CD workflow for automated testing
├── .gitignore                 # Git ignore patterns
├── requirements.txt           # Python dependencies
├── README.md                  # This file
├── src/                       # Source code modules
│   └── __init__.py
├── notebooks/                 # Jupyter notebooks for analysis
│   ├── __init__.py
│   ├── README.md
│   └── task1_eda.ipynb        # Task 1: Exploratory Data Analysis
├── tests/                     # Unit tests
│   └── __init__.py
├── scripts/                   # Utility scripts
│   ├── __init__.py
│   └── README.md
└── data/                      # Dataset files
    ├── raw_analyst_ratings.csv
    └── [stock_symbol].csv     # Stock price data files
```

## Tasks

### Task 1: Git and GitHub + EDA ✅
- [x] Set up Python environment
- [x] Git version control setup
- [x] CI/CD workflow configuration
- [x] Exploratory Data Analysis (EDA)
  - Descriptive Statistics
  - Text Analysis and Topic Modeling
  - Time Series Analysis
  - Publisher Analysis

### Task 2: Quantitative Analysis ✅
- [x] Load and prepare stock price data
- [x] Technical indicators using TA-Lib (MA, RSI, MACD, Bollinger Bands, ATR)
- [x] Financial metrics using PyNance/pandas (Returns, Volatility, Sharpe Ratio)
- [x] Data visualization (Price charts, RSI, MACD, Bollinger Bands, Comparisons)

### Task 3: Correlation Analysis (Pending)
- Sentiment analysis on headlines
- Correlation between news sentiment and stock movements

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd kifiya_week_1
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Jupyter Notebook**
   ```bash
   jupyter notebook
   ```

## Key Dependencies

- pandas: Data manipulation and analysis
- numpy: Numerical computing
- matplotlib & seaborn: Data visualization
- nltk & textblob: Natural language processing
- wordcloud: Word cloud generation
- jupyter: Interactive notebook environment

## Git Workflow

1. Create a new branch for each task:
   ```bash
   git checkout -b task-1
   ```

2. Commit changes regularly with descriptive messages:
   ```bash
   git add .
   git commit -m "Descriptive commit message"
   ```

3. Push to remote and create Pull Request when ready

## Contact

For questions or support, please reach out through the Slack channel: #all-week1