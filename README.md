# Apple (AAPL) Stock Data Analysis

This project involves the visualization and analysis of Apple (AAPL) stock data using Python and various data visualization libraries.

## Overview

The Python script in this project loads Apple stock data from a CSV file, preprocesses the data, and creates various visualizations to analyze different aspects of the stock prices and trading volume. Here's an overview of what the script does:

1. **Data Loading and Preprocessing:**
   - Imports necessary libraries such as Pandas, NumPy, Matplotlib, Seaborn, and Plotly.
   - Loads Apple stock data from the 'AAPL.csv' file into a Pandas DataFrame.
   - Converts the "Date" column to datetime format for time-based analysis.
   - Handles missing values and drops the "Adj Close" column.

2. **Visualizations:**
   - Creates interactive subplots for "Open," "High," and "Low" stock prices over the entire dataset.
   - Divides the dataset into three time periods: 1980-1999, 2000-2010, and 2011-2022, and visualizes the "Open," "High," and "Low" prices for each period.
   - Analyzes and visualizes the trading volume ("Hacim") for the overall dataset and each time period.


