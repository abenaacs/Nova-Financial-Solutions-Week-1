import os
import glob
import pandas as pd
from data_load import (
    load_analyst_data,
    load_financial_data,
    merge_data,
    analyze_missing_values,
    save_processed_data,
)
from descriptive_statistics import (
    headline_length_analysis,
    articles_per_publisher,
    publication_date_trends,
)
from text_analysis import sentiment_analysis
from topic_model import topic_modeling
from time_series_analysis import time_series_analysis
from publisher_analysis import correlation_analysis


if __name__ == "__main__":
    # Load Financial Data
    current_dir = os.getcwd()
    financial_data_path = os.path.join(current_dir, "./data/yfinance_data")
    all_files = glob.glob(os.path.join(financial_data_path, "*.csv"))
    # Load Raw Analyst Data
    raw_data_analyst = os.path.join(
        current_dir, "./data/raw_analyst_ratings/raw_analyst_ratings.csv"
    )
    financial_data = load_financial_data(financial_data_path)
    analyst_data = load_analyst_data(raw_data_analyst)
    merged_data = merge_data(analyst_data, financial_data)

    analyze_missing_values(merged_data)
    headline_length_analysis(merged_data)
    articles_per_publisher(merged_data)
    publication_date_trends(merged_data)
    sentiment_analysis(merged_data)
    topic_modeling(merged_data)
    time_series_analysis(merged_data)
    correlation_analysis(merged_data)
    save_processed_data(merged_data)
