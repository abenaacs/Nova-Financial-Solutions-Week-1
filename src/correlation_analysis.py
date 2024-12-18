from scipy.stats import pearsonr
import matplotlib.pyplot as plt
import pandas as pd


def calculate_correlation(df):
    """
    Calculate and visualize the correlation between sentiment and stock returns.

    Args:
        df (pd.DataFrame): Merged DataFrame containing sentiment and stock data.

    Returns:
        None
    """
    try:
        required_columns = ["date", "Sentiment_Polarity", "Daily_Returns"]
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            print(f"Missing columns: {missing_columns}")
            return
        daily_sentiment = df.groupby("date")["Sentiment_Polarity"].mean().reset_index()
        daily_returns = df.groupby("date")["Daily_Returns"].mean().reset_index()
        analysis_data = pd.merge(daily_sentiment, daily_returns, on="date")
        print("Merged sentiment and returns data:\n", analysis_data.head())
        correlation, _ = pearsonr(
            analysis_data["Sentiment_Polarity"], analysis_data["Daily_Returns"]
        )
        print(f"Pearson Correlation Coefficient: {correlation:.4f}")
        plt.scatter(
            analysis_data["Sentiment_Polarity"],
            analysis_data["Daily_Returns"],
            color="blue",
            alpha=0.7,
            label=f"Correlation (ρ={correlation:.2f})",
        )
        plt.title("Correlation between Sentiment and Returns")
        plt.xlabel("Sentiment Score")
        plt.ylabel("Daily Returns")
        plt.legend()
        plt.show()

    except Exception as e:
        print(f"Error processing data: {e}")
