import os
from data_loader import load_stock_data_from_folder, load_analyst_ratings
from data_processing import merge_stock_and_ratings
from eda import (
    plot_stock_prices,
    analyst_ratings_summary,
    analyze_publisher_domains,
    analyze_publishing_times,
    analyze_sentiment,
    analyze_text_length_and_frequency,
    perform_topic_modeling,
)
from feature_engineering import add_technical_indicators
from feature_engineering import add_moving_averages
from sentimental_analysis import add_sentiment_analysis


def main():
    # Paths
    current_dir = os.getcwd()
    yfinance_folder = os.path.join(current_dir, "./data/yfinance_data")
    analyst_ratings_file = os.path.join(
        current_dir, "./data/raw_analyst_ratings/raw_analyst_ratings.csv"
    )

    # Step 1: Load data
    print("Loading data...")
    stock_data = load_stock_data_from_folder(yfinance_folder)
    analyst_ratings = load_analyst_ratings(analyst_ratings_file)

    # Step 2: Sentiment analysis on analyst ratings
    print("Performing sentiment analysis on analyst ratings...")
    analyst_ratings = add_sentiment_analysis(analyst_ratings, text_column="Comments")

    # Step 3: Merge data
    print("Merging stock data with analyst ratings...")
    merged_data = merge_stock_and_ratings(stock_data, analyst_ratings)

    # Step 4: Feature Engineering
    print("Adding moving averages...")
    merged_data = add_moving_averages(merged_data)

    # Step 5: EDA
    print("Performing Exploratory Data Analysis...")
    plot_stock_prices(merged_data)
    analyst_ratings_summary(analyst_ratings)
    # Perform additional EDA
    # Descriptive statistics for textual lengths and articles per publisher
    analyze_text_length_and_frequency(analyst_ratings)

    # Sentiment Analysis
    analyze_sentiment(analyst_ratings)

    # Topic Modeling
    perform_topic_modeling(analyst_ratings)

    # Analyze Publishing Times
    analyze_publishing_times(analyst_ratings)

    # Analyze Publisher Domains
    analyze_publisher_domains(analyst_ratings)
    # Ensure the output directory exists

    print("Calculating technical indicators...")
    for stock, df in stock_data.items():
        df = add_technical_indicators(df)
        stock_data[stock] = df

    # Step 3: Visualization
    print("Visualizing stock data with indicators...")
    for stock, df in stock_data.items():
        plot_with_indicators(df, stock_name=stock)
    output_dir = "processed_data"
    os.makedirs(output_dir, exist_ok=True)  # Create the directory if it doesn't exist

    for stock, df in merged_data.items():
        df.to_csv(f"{output_dir}/{stock}_processed.csv", index=False)


if __name__ == "__main__":
    main()
