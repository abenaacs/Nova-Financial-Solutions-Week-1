# README for Notebooks

## Purpose

The notebook(s) included in this project focus on exploratory data analysis (EDA), sentiment analysis, and topic modeling. These steps help derive insights from financial news and explore correlations with stock price data.

## Key Notebook(s)

1. **eda_and_sentiment_analysis.ipynb**: Includes code for EDA, sentiment analysis, and topic modeling.

## Methodology

### Exploratory Data Analysis (EDA)

- **Descriptive Statistics**: Analyzed headline lengths, article frequency by publisher, and publication trends.
- **Visualization**: Created histograms, line plots, and bar charts to explore data patterns.

### Sentiment Analysis

- Used **TextBlob** for polarity scoring of headlines.
- Categorized sentiments into `positive`, `neutral`, and `negative` for distribution analysis.

### Topic Modeling

- Applied **TF-IDF Vectorization** and **Latent Dirichlet Allocation (LDA)** to identify prevalent topics in headlines.

### Correlation Analysis

- Merged news sentiment with stock price data.
- Analyzed the correlation between sentiment polarity and daily stock price changes.

## How to Run

- Open the `.ipynb` file in Jupyter Notebook or JupyterLab.
- Run each cell sequentially to replicate the analysis.
