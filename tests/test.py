import unittest
import pandas as pd
from src.analysis import analyze_sentiment, correlate_sentiment_with_prices


class TestSentimentAnalysis(unittest.TestCase):

    def setUp(self):
        # Mock financial news dataset
        self.news_data = pd.DataFrame(
            {
                "headline": [
                    "Company A reports record profits this quarter",
                    "Company B faces legal trouble over patent infringement",
                    "Neutral headline with no strong sentiment",
                ],
                "date": ["2024-01-01", "2024-01-02", "2024-01-03"],
                "stock": ["COMPA", "COMPB", "COMPC"],
            }
        )

        # Mock stock price dataset
        self.stock_data = pd.DataFrame(
            {
                "Date": ["2024-01-01", "2024-01-02", "2024-01-03"],
                "Stock": ["COMPA", "COMPB", "COMPC"],
                "Close": [100.0, 50.0, 75.0],
            }
        )

    def test_analyze_sentiment(self):
        # Test sentiment analysis function
        sentiment_data = analyze_sentiment(self.news_data)

        self.assertIn("sentiment", sentiment_data.columns)
        self.assertIn("polarity", sentiment_data.columns)
        self.assertEqual(len(sentiment_data), len(self.news_data))
        self.assertTrue(
            all(sentiment_data["sentiment"].isin(["positive", "negative", "neutral"]))
        )

    def test_correlate_sentiment_with_prices(self):
        # Test correlation function
        sentiment_data = analyze_sentiment(self.news_data)
        correlation_results = correlate_sentiment_with_prices(
            sentiment_data, self.stock_data
        )

        self.assertIsInstance(correlation_results, pd.DataFrame)
        self.assertIn("correlation", correlation_results.columns)
        self.assertIn("Stock", correlation_results.columns)
        self.assertEqual(
            len(correlation_results), len(self.stock_data["Stock"].unique())
        )


if __name__ == "__main__":
    unittest.main()
