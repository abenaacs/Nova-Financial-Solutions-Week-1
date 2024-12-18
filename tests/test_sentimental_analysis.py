import pytest
from src.sentimental_analysis import (
    add_sentiment_analysis,
)
import pandas as pd


@pytest.fixture
def sample_headlines():
    """Fixture to return sample headlines for testing sentiment analysis"""
    data = {
        "headline": [
            "Stock market is up today!",
            "A major crash is predicted next week.",
            "Stocks are steady, no big changes.",
        ]
    }
    return pd.DataFrame(data)


def test_add_sentiment_analysis(sample_headlines):
    # Run the sentiment analysis function
    df = add_sentiment_analysis(sample_headlines)

    # Ensure that the sentiment column is created
    assert "sentiment" in df.columns, "Sentiment column not found in the DataFrame"
    assert df["sentiment"].dtype == float, "Sentiment column should be of type float"

    # Check that the sentiment category exists
    assert "sentiment_category" in df.columns, "Sentiment category column not found"
    assert set(df["sentiment_category"]).issubset(
        {"positive", "negative", "neutral"}
    ), "Sentiment category values should be 'positive', 'negative', or 'neutral'"
