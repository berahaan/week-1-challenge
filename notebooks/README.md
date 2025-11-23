# Notebooks Directory

This directory contains Jupyter notebooks for data analysis and exploration.

## Notebooks

### task1_eda.ipynb
Comprehensive Exploratory Data Analysis (EDA) notebook covering:

1. **Descriptive Statistics**
   - Headline length analysis (character count, word count)
   - Articles per publisher
   - Publication date trends (year, month, day of week, hour)

2. **Text Analysis and Topic Modeling**
   - Common keywords extraction
   - Word cloud visualization
   - Significant financial phrases identification (FDA approval, price target, earnings, etc.)

3. **Time Series Analysis**
   - Daily publication frequency over time
   - Monthly aggregation
   - Publishing time patterns (hour of day, day of week)

4. **Publisher Analysis**
   - Publisher contribution statistics
   - Domain analysis (if email addresses are used)
   - Stock coverage by publisher
   - Publisher distribution visualizations

## Usage

To run the notebooks:

1. Ensure all dependencies are installed (see main README.md)
2. Start Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
3. Navigate to the notebooks directory and open the desired notebook
4. Run all cells or execute cells individually

## Notes

- The notebooks assume data files are located in the `../data/` directory
- Some cells may take time to execute depending on dataset size
- Visualizations are automatically displayed inline

