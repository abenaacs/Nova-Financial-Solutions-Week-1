import pandas as pd
import matplotlib.pyplot as plt
import os
from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation


def plot_stock_prices(stock_data_dict):
    """
    Plot closing prices for all stocks.

    Args:
        stock_data_dict (dict): Dictionary containing stock dataframes.
    """
    for stock, df in stock_data_dict.items():
        plt.figure(figsize=(10, 5))
        plt.plot(df["Date"], df["Close"], label="Close Price", color="blue")
        plt.title(f"{stock} Closing Prices Over Time")
        plt.xlabel("Date")
        plt.ylabel("Close Price (USD)")
        plt.legend()
        plt.grid()
        plt.show()


def analyst_ratings_summary(analyst_ratings_df, symbol_column="Symbol"):
    """
    Summarize the analyst ratings data.

    Args:
        analyst_ratings_df (pd.DataFrame): Analyst ratings dataframe.
        symbol_column (str): Column containing stock symbols.

    Returns:
        pd.DataFrame: Summary table for ratings count per stock.
    """
    if symbol_column in analyst_ratings_df.columns:
        summary = analyst_ratings_df[symbol_column].value_counts().reset_index()
        summary.columns = ["Stock", "Ratings Count"]
        print("Analyst Ratings Summary:")
        print(summary)
        return summary
    else:
        print(f"Column '{symbol_column}' not found in the dataframe.")
        return pd.DataFrame()


# Descriptive Statistics: Textual Length and Article Frequency
def analyze_text_length_and_frequency(df):
    """
    Analyze the length of headlines and the frequency of articles per publisher.
    """
    # Headline Length Analysis
    df["headline_length"] = df["headline"].apply(lambda x: len(str(x)))
    print("\nHeadline Length Statistics:")
    print(df["headline_length"].describe())

    # Articles per Publisher
    articles_per_publisher = df.groupby("publisher").size().sort_values(ascending=False)
    print("\nArticles per Publisher:")
    print(articles_per_publisher)


# Sentiment Analysis on Headlines
def analyze_sentiment(df):
    """
    Perform sentiment analysis on headlines.
    """
    df["sentiment"] = df["headline"].apply(
        lambda x: TextBlob(str(x)).sentiment.polarity
    )
    df["sentiment_category"] = df["sentiment"].apply(
        lambda x: "positive" if x > 0 else ("negative" if x < 0 else "neutral")
    )

    sentiment_counts = df["sentiment_category"].value_counts()
    print("\nSentiment Analysis:")
    print(sentiment_counts)


# Topic Modeling on Headlines
def perform_topic_modeling(df):
    """
    Perform topic modeling using LDA.
    """
    vectorizer = TfidfVectorizer(stop_words="english")
    X = vectorizer.fit_transform(df["headline"])

    lda = LatentDirichletAllocation(n_components=5, random_state=42)
    lda.fit(X)

    print("\nTopic Modeling:")
    for index, topic in enumerate(lda.components_):
        print(f"Topic {index}:")
        print(
            [
                vectorizer.get_feature_names_out()[i]
                for i in topic.argsort()[: -10 - 1 : -1]
            ]
        )


# Analysis of Publishing Times
def analyze_publishing_times(df):
    """
    Analyze the time of publication for articles.
    """
    df["publication_date"] = pd.to_datetime(df["publication_date"])
    df["publication_time"] = df["publication_date"].dt.hour

    articles_per_hour = df.groupby("publication_time").size()
    articles_per_hour.plot(kind="bar", title="Articles Published Per Hour")
    plt.show()


# Publisher Domain Analysis
def analyze_publisher_domains(df):
    """
    Analyze publisher domains for frequency.
    """
    df["publisher_domain"] = df["publisher"].str.split("@").str[-1]
    articles_per_domain = (
        df.groupby("publisher_domain").size().sort_values(ascending=False)
    )
    print("\nPublisher Domains:")
    print(articles_per_domain)


def plot_with_indicators(df, stock_name):
    """
    Plot stock closing prices with SMA, RSI, and MACD.

    Args:
        df (pd.DataFrame): Stock price data with indicators.
        stock_name (str): Name of the stock.
    """
    plt.figure(figsize=(12, 6))

    # Closing Price with SMAs
    plt.plot(df["Date"], df["Close"], label="Close Price", color="blue")
    plt.plot(df["Date"], df["SMA_20"], label="SMA 20", color="orange")
    plt.plot(df["Date"], df["SMA_50"], label="SMA 50", color="red")
    plt.title(f"{stock_name} Closing Price with SMA")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.show()

    # RSI
    plt.figure(figsize=(12, 3))
    plt.plot(df["Date"], df["RSI"], color="green")
    plt.axhline(70, color="red", linestyle="--", label="Overbought")
    plt.axhline(30, color="blue", linestyle="--", label="Oversold")
    plt.title(f"{stock_name} RSI")
    plt.xlabel("Date")
    plt.ylabel("RSI")
    plt.legend()
    plt.show()

    # MACD
    plt.figure(figsize=(12, 3))
    plt.plot(df["Date"], df["MACD"], label="MACD", color="purple")
    plt.plot(df["Date"], df["MACD_signal"], label="Signal Line", color="orange")
    plt.title(f"{stock_name} MACD")
    plt.xlabel("Date")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    from data_loader import load_stock_data_from_folder, load_analyst_ratings
    from data_processing import merge_stock_and_ratings

    current_dir = os.getcwd()
    # Paths
    yfinance_folder = os.path.join(current_dir, "./data/yfinance_data")
    analyst_ratings_file = os.path.join(
        current_dir, "./data/raw_analyst_ratings/raw_analyst_ratings.csv"
    )

    # Load and merge data
    stock_data = load_stock_data_from_folder(yfinance_folder)
    analyst_ratings = load_analyst_ratings(analyst_ratings_file)
    merged_data = merge_stock_and_ratings(stock_data, analyst_ratings)

    # Plot stock prices
    print("Visualizing Stock Prices...")
    plot_stock_prices(stock_data)

    # Summarize analyst ratings
    print("Generating Analyst Ratings Summary...")
    analyst_ratings_summary(analyst_ratings)

    # Perform additional EDA
    # For the sake of example, assuming your main dataset is 'df'
    df = merged_data  # or replace with your actual data

    # Descriptive statistics for textual lengths and articles per publisher
    analyze_text_length_and_frequency(df)

    # Sentiment Analysis
    analyze_sentiment(df)

    # Topic Modeling
    perform_topic_modeling(df)

    # Analyze Publishing Times
    analyze_publishing_times(df)

    # Analyze Publisher Domains
    analyze_publisher_domains(df)
