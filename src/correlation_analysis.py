from scipy.stats import pearsonr
import matplotlib.pyplot as plt
import pandas as pd
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def calculate_correlation(
    df, sentiment_col="Sentiment_Polarity", returns_col="Daily_Returns"
):
    """
    Calculate and visualize the correlation between sentiment and stock returns.

    Args:
        df (pd.DataFrame): Merged DataFrame containing sentiment and stock data.
        sentiment_col (str): Name of the sentiment column.
        returns_col (str): Name of the daily returns column.

    Returns:
        float: Pearson correlation coefficient.
    """
    try:
        # Check required columns
        required_columns = {"date", sentiment_col, returns_col}
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            raise ValueError(f"Missing columns in the DataFrame: {missing_columns}")

        # Group sentiment and returns by date
        daily_sentiment = df.groupby("date")[sentiment_col].mean().reset_index()
        daily_returns = df.groupby("date")[returns_col].mean().reset_index()

        # Merge sentiment and returns data
        analysis_data = pd.merge(daily_sentiment, daily_returns, on="date")
        if analysis_data.empty:
            raise ValueError(
                "No data available for correlation analysis after merging."
            )

        # Compute Pearson Correlation
        correlation, _ = pearsonr(
            analysis_data[sentiment_col], analysis_data[returns_col]
        )
        logging.info(f"Pearson Correlation Coefficient: {correlation:.4f}")

        # Visualization
        plt.figure(figsize=(8, 6))
        plt.scatter(
            analysis_data[sentiment_col],
            analysis_data[returns_col],
            color="blue",
            alpha=0.7,
            label=f"Correlation (ρ={correlation:.2f})",
        )
        plt.title("Correlation between Sentiment and Returns")
        plt.xlabel("Sentiment Score")
        plt.ylabel("Daily Returns")
        plt.legend()
        plt.grid()
        plt.show()

        return correlation
    except Exception as e:
        logging.error(f"Error during correlation calculation: {e}")
        raise
