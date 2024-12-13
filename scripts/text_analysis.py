import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob


def sentiment_analysis(data):
    """Perform sentiment analysis on headlines."""
    data["sentiment"] = data["headline"].apply(lambda x: TextBlob(x).sentiment.polarity)
    data["sentiment_category"] = pd.cut(
        data["sentiment"],
        bins=[-1, -0.01, 0.01, 1],
        labels=["negative", "neutral", "positive"],
    )

    sentiment_distribution = data["sentiment_category"].value_counts()
    print("\nSentiment Distribution:\n", sentiment_distribution)

    plt.figure(figsize=(8, 5))
    sentiment_distribution.plot(kind="bar", color="green", edgecolor="black")
    plt.title("Sentiment Distribution")
    plt.xlabel("Sentiment Category")
    plt.ylabel("Frequency")
    plt.show()
