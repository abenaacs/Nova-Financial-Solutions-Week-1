import os
import logging
from data_loader import load_stock_data_from_folder, load_analyst_ratings
from data_processing import merge_stock_and_ratings
from eda import plot_stock_prices, analyst_ratings_summary
from correlation_analysis import calculate_correlation
from feature_engineering import add_technical_indicators
from sentimental_analysis import add_sentiment_analysis

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def main():
    try:
        current_dir = os.getcwd()
        yfinance_folder = os.path.join(current_dir, "./data/yfinance_data")
        analyst_ratings_file = os.path.join(
            current_dir, "./data/raw_analyst_ratings/raw_analyst_ratings.csv"
        )

        logging.info("Starting data loading...")
        stock_data = load_stock_data_from_folder(yfinance_folder)
        analyst_ratings = load_analyst_ratings(analyst_ratings_file)

        logging.info("Performing sentiment analysis on analyst ratings...")
        analyst_ratings_sentiment = add_sentiment_analysis(
            analyst_ratings, text_column="headline"
        )

        # Exploratory Data Analysis
        plot_stock_prices(stock_data)
        analyst_ratings_summary(analyst_ratings_sentiment)

        logging.info("Enriching stock data with technical indicators...")
        enriched_data = add_technical_indicators(stock_data)

        logging.info("Merging stock data and analyst ratings...")
        merged_data = merge_stock_and_ratings(enriched_data, analyst_ratings_sentiment)

        logging.info("Performing correlation analysis...")
        calculate_correlation(merged_data)

        # Save processed data
        output_dir = "processed_data"
        os.makedirs(output_dir, exist_ok=True)
        for stock, df in merged_data.items():
            df.to_csv(f"{output_dir}/{stock}_processed.csv", index=False)

        logging.info("Pipeline completed successfully. Processed data saved.")
    except Exception as e:
        logging.error(f"Pipeline execution failed: {e}")


if __name__ == "__main__":
    main()
