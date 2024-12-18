import os
from data_loader import load_stock_data_from_folder, load_analyst_ratings
from data_processing import merge_stock_and_ratings
from eda import (
    plot_stock_prices,
    analyst_ratings_summary,
    analyze_sentiment,
    analyze_text_length_and_frequency,
    analyze_article_per_publisher,
    perform_topic_modeling,
)
from correlation_analysis import calculate_correlation
from feature_engineering import add_technical_indicators
from sentimental_analysis import add_sentiment_analysis


def main():
    current_dir = os.getcwd()
    yfinance_folder = os.path.join(current_dir, "./data/yfinance_data")
    analyst_ratings_file = os.path.join(
        current_dir, "./data/raw_analyst_ratings/raw_analyst_ratings.csv"
    )
    print("Loading data...")
    stock_data = load_stock_data_from_folder(yfinance_folder)
    analyst_ratings = load_analyst_ratings(analyst_ratings_file)
    print("Performing sentiment analysis on analyst ratings...")
    analyst_ratings_sentiment = add_sentiment_analysis(
        analyst_ratings, text_column="headline"
    )
    plot_stock_prices(stock_data)
    analyst_ratings_summary(analyst_ratings)
    analyze_text_length_and_frequency(analyst_ratings)
    analyze_article_per_publisher(analyst_ratings)
    analyze_sentiment(analyst_ratings)
    perform_topic_modeling(analyst_ratings)
    enriched_data = add_technical_indicators(stock_data)
    merged_data = merge_stock_and_ratings(enriched_data, analyst_ratings_sentiment)
    calculate_correlation(merged_data)

    output_dir = "processed_data"
    os.makedirs(output_dir, exist_ok=True)

    for stock, df in merged_data.items():
        df.to_csv(f"{output_dir}/{stock}_processed.csv", index=False)


if __name__ == "__main__":
    main()
