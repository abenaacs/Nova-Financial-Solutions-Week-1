import pandas as pd
import os


def load_stock_data_from_folder(folder_path):
    """
    Load all stock price CSV files from a folder into a dictionary.

    Args:
        folder_path (str): Path to the folder containing stock price CSV files.

    Returns:
        dict: A dictionary where keys are file names without extensions,
              and values are pandas DataFrames.
    """
    stock_data = {}

    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"The folder '{folder_path}' does not exist!")
    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            filepath = os.path.join(folder_path, filename)
            stock_name = filename.replace("_historical_data.csv", "")
            stock_df = pd.read_csv(filepath)
            required_cols = {"Date", "Open", "High", "Low", "Close", "Volume"}
            if not required_cols.issubset(stock_df.columns):
                print(f"Warning: {filename} is missing required columns. Skipping...")
                continue

            stock_df["Date"] = pd.to_datetime(stock_df["Date"])
            stock_df.columns = stock_df.columns.str.lower()
            stock_df.sort_values("date", inplace=True)
            stock_data[stock_name] = stock_df

    return stock_data


def load_analyst_ratings(filepath):
    """
    Load and preprocess raw analyst ratings data.

    Args:
        filepath (str): Path to the analyst ratings CSV file.

    Returns:
        pd.DataFrame: Cleaned analyst ratings dataframe.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"{filepath} does not exist!")
    ratings_df = pd.read_csv(filepath)
    ratings_df["date"] = pd.to_datetime(
        ratings_df["date"], errors="coerce"
    ).dt.tz_localize(None)
    ratings_df.dropna(inplace=True)
    ratings_df.drop_duplicates(inplace=True)

    return ratings_df
