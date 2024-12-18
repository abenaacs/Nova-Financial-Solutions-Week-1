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
        plt.plot(df["date"], df["close"], label="Close Price", color="blue")
        plt.title(f"{stock} Closing Prices Over Time")
        plt.xlabel("Date")
        plt.ylabel("Close Price (USD)")
        plt.legend()
        plt.grid()
        plt.show()


def analyst_ratings_summary(analyst_ratings_df, symbol_column="Symbol"):
    """
    Summarize the analyst ratings data and visualize it.

    Args:
        analyst_ratings_df (pd.DataFrame): Analyst ratings dataframe.
        symbol_column (str): Column containing stock symbols.

    Returns:
        pd.DataFrame: Summary table for ratings count per stock.
    """
    if symbol_column in analyst_ratings_df.columns:
        summary = analyst_ratings_df[symbol_column].value_counts().reset_index()
        summary.columns = ["Stock", "Ratings Count"]

        # Bar Chart for Ratings Count
        plt.figure(figsize=(10, 6))
        plt.bar(summary["Stock"], summary["Ratings Count"], color="skyblue")
        plt.title("Analyst Ratings Count by Stock")
        plt.xlabel("Stock")
        plt.ylabel("Ratings Count")
        plt.xticks(rotation=45)
        plt.show()

        return summary
    else:
        print(f"Column '{symbol_column}' not found in the dataframe.")
        return pd.DataFrame()


def analyze_text_length_and_frequency(df):
    """
    Analyze the length of headlines and the frequency of articles per publisher.
    """
    # Headline Length Analysis
    df["headline_length"] = df["headline"].apply(lambda x: len(str(x)))

    # Histogram for Headline Length
    plt.figure(figsize=(10, 6))
    plt.hist(df["headline_length"], bins=30, color="skyblue", edgecolor="black")
    plt.title("Distribution of Headline Lengths")
    plt.xlabel("Headline Length")
    plt.ylabel("Frequency")
    plt.grid()
    plt.show()


def analyze_article_per_publisher(df):
    articles_per_publisher = df.groupby("publisher").size().sort_values(ascending=False)
    print("\nArticles per Publisher:")
    print(articles_per_publisher)

    articles_per_publisher.plot(kind="bar", figsize=(12, 6), color="orange")
    plt.title("Number of Articles per Publisher")
    plt.xlabel("Publisher")
    plt.ylabel("Article Count")
    plt.xticks(rotation=45)
    plt.show()


def analyze_sentiment(df):
    """
    Perform sentiment analysis on headlines and visualize the results.
    """
    df["sentiment"] = df["headline"].apply(
        lambda x: TextBlob(str(x)).sentiment.polarity
    )
    df["sentiment_category"] = df["sentiment"].apply(
        lambda x: "positive" if x > 0 else ("negative" if x < 0 else "neutral")
    )

    sentiment_counts = df["sentiment_category"].value_counts()

    # Pie Chart for Sentiment
    plt.figure(figsize=(8, 6))
    plt.pie(
        sentiment_counts,
        labels=sentiment_counts.index,
        autopct="%1.1f%%",
        startangle=140,
        colors=["lightgreen", "salmon", "lightgray"],
    )
    plt.title("Sentiment Distribution")
    plt.show()


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


def plot_with_indicators(df, stock_name):
    """
    Plot stock closing prices with SMA, RSI, and MACD.

    Args:
        df (pd.DataFrame): Stock price data with indicators.
        stock_name (str): Name of the stock.
    """
    plt.figure(figsize=(12, 6))

    # Closing Price with SMAs
    plt.plot(df["date"], df["close"], label="Close Price", color="blue")
    plt.plot(df["date"], df["SMA_20"], label="SMA 20", color="orange")
    plt.plot(df["date"], df["SMA_50"], label="SMA 50", color="red")
    plt.title(f"{stock_name} Closing Price with SMA")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.show()

    # RSI
    plt.figure(figsize=(12, 3))
    plt.plot(df["date"], df["RSI"], color="green")
    plt.axhline(70, color="red", linestyle="--", label="Overbought")
    plt.axhline(30, color="blue", linestyle="--", label="Oversold")
    plt.title(f"{stock_name} RSI")
    plt.xlabel("Date")
    plt.ylabel("RSI")
    plt.legend()
    plt.show()

    # MACD
    plt.figure(figsize=(12, 3))
    plt.plot(df["date"], df["MACD"], label="MACD", color="purple")
    plt.plot(df["date"], df["MACD_signal"], label="Signal Line", color="orange")
    plt.title(f"{stock_name} MACD")
    plt.xlabel("Date")
    plt.legend()
    plt.show()
