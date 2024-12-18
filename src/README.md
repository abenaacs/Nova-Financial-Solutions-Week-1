### **README for `src/` Folder**

This README focuses on the Python scripts, detailing their functionality and how they interconnect.

````markdown
# Source Code (`src/`)

The `src/` directory contains all the Python scripts used in the project. Each script handles a specific part of the pipeline.

## Directory Structure

src/
├── data_loader.py # Functions to load stock and analyst ratings data.
├── data_processing.py # Functions for merging, cleaning, and enriching data.
├── eda.py # Exploratory Data Analysis (EDA) functions.
├── correlation_analysis.py # Functions to calculate and visualize correlations.
├── feature_engineering.py # Adding technical indicators like SMA, RSI, and MACD.
├── sentimental_analysis.py # Sentiment analysis using TextBlob.
├── main.py # Main pipeline that ties everything together.

markdown
Copy code

## Key Functions

### `data_loader.py`

- `load_stock_data_from_folder`: Reads stock price data from CSV files in a folder.
- `load_analyst_ratings`: Loads analyst ratings data and preprocesses it.

### `data_processing.py`

- `merge_stock_and_ratings`: Combines stock data and analyst ratings for analysis.

### `eda.py`

- `plot_stock_prices`: Visualizes closing prices for stocks.
- `analyst_ratings_summary`: Summarizes and visualizes analyst ratings.
- `analyze_sentiment`: Performs sentiment analysis on analyst headlines.
- `perform_topic_modeling`: Extracts topics using LDA.

### `correlation_analysis.py`

- `calculate_correlation`: Calculates and visualizes correlation between sentiment and stock returns.

### `feature_engineering.py`

- `add_technical_indicators`: Adds SMA, RSI, and MACD indicators to stock data.

### `sentimental_analysis.py`

- `add_sentiment_analysis`: Analyzes the sentiment of text headlines using TextBlob.

### `main.py`

The main script that executes the full pipeline:

1. Data Loading
2. Data Processing
3. Exploratory Analysis
4. Sentiment and Technical Analysis
5. Correlation Analysis
6. Saving Results

---

## How to Run

Run the pipeline using:

```bash
python main.py
---
```
````
