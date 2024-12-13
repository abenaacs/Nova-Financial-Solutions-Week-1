# Financial News Sentiment Analysis and Correlation Project

## Overview

This project aims to enhance predictive analytics by analyzing financial news headlines and correlating sentiment with stock price movements. The insights from this analysis can inform investment strategies by leveraging the relationship between news sentiment and stock performance trends.

## Project Objectives

1. **Sentiment Analysis**: Perform sentiment analysis on financial news headlines to quantify the tone (positive, negative, neutral).
2. **Correlation Analysis**: Investigate the statistical correlation between news sentiment and corresponding stock price changes.
3. **Actionable Insights**: Provide investment recommendations based on the relationship between sentiment and market behavior.

## Dataset

### Financial News Dataset

- Contains columns: `headline`, `url`, `publisher`, `date`, `stock`

### Stock Price Dataset

- Contains columns: `Date`, `Open`, `High`, `Low`, `Close`, `Adj Close`, `Volume`, `Dividends`, `Stock Splits`

## Folder Structure

```
├── .vscode/
│   └── settings.json
├── .github/
│   └── workflows/
│       └── unittests.yml
├── data/
│   ├── financial_news.csv
│   └── stock_prices.csv
├── notebooks/
│   ├── eda_and_sentiment_analysis.ipynb
│   └── README.md
├── src/
│   ├── __init__.py
│   └── analysis.py
├── tests/
│   ├── __init__.py
│   └── test_analysis.py
├── scripts/
│   ├── __init__.py
│   └── run_analysis.py
├── processed/
│   └── processed_financial_news.csv
├── requirements.txt
├── README.md
└── LICENSE
```

## Methodology

### 1. Exploratory Data Analysis (EDA)

- **Descriptive Statistics**: Analyzed headline lengths, article frequency by publisher, and publication trends.
- **Visualization**: Created histograms, line plots, and bar charts to explore data patterns.

### 2. Sentiment Analysis

- Used **TextBlob** for polarity scoring of headlines.
- Categorized sentiments into `positive`, `neutral`, and `negative` for distribution analysis.

### 3. Topic Modeling

- Applied **TF-IDF Vectorization** and **Latent Dirichlet Allocation (LDA)** to identify prevalent topics in headlines.

### 4. Correlation Analysis

- Merged news sentiment with stock price data.
- Analyzed the correlation between sentiment polarity and daily stock price changes.

## CI/CD Workflow

To ensure the reliability and maintainability of the project, a CI/CD pipeline is set up using GitHub Actions:

- **Location**: The pipeline configuration file is located in the `.github/workflows/unittests.yml` directory.
- **Key Features**:
  - **Automated Testing**: Runs unit tests defined in the `tests/` directory whenever new code is pushed or a pull request is created.
  - **Dependency Check**: Validates that all dependencies listed in `requirements.txt` are installed and compatible.
  - **Continuous Deployment**: Ensures that new code integrates smoothly without breaking the existing functionality.
  - **Notifications**: Sends alerts for test failures or build errors to facilitate quick debugging.

Developers can contribute with confidence, knowing that the CI/CD pipeline ensures code quality and prevents regression issues.

## Key Findings (Interim)

- Headline lengths follow a normal distribution.
- Most articles are published during trading hours, with peaks observed near market open and close.
- Sentiment distribution leans neutral, with fewer extreme positive or negative headlines.
- Preliminary correlation analysis suggests weak positive correlation between sentiment and stock price changes.

## Challenges

- Missing values in the dataset required preprocessing.
- Merging datasets involved aligning dates and stock symbols, which highlighted data inconsistencies.

## Requirements

Install project dependencies by running:

```
pip install -r requirements.txt
```

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/username/financial-news-analysis.git
   ```
2. Navigate to the project directory:
   ```bash
   cd financial-news-analysis
   ```
3. Run the main analysis script:
   ```bash
   python scripts/run_analysis.py
   ```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing

Feel free to fork this repository and create pull requests for improvements or additional features.
