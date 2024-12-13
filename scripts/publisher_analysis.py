def correlation_analysis(data):
    """Analyze the correlation between sentiment and price change."""
    data["price_change"] = data["Close"] - data["Open"]
    sentiment_correlation = data[["sentiment", "price_change"]].corr()
    print("\nCorrelation Between Sentiment and Price Change:\n", sentiment_correlation)
