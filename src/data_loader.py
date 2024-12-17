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

    # Iterate through each file in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            filepath = os.path.join(folder_path, filename)
            stock_name = filename.replace(
                "_historical_data.csv", ""
            )  # Extract stock name
            stock_df = pd.read_csv(filepath)

            # Check if necessary columns exist
            required_cols = {"Date", "Open", "High", "Low", "Close", "Volume"}
            if not required_cols.issubset(stock_df.columns):
                print(f"Warning: {filename} is missing required columns. Skipping...")
                continue

            # Convert 'Date' column to datetime format
            stock_df["Date"] = pd.to_datetime(stock_df["Date"])
            stock_df.sort_values("Date", inplace=True)

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

    # Load analyst ratings data
    ratings_df = pd.read_csv(filepath)

    # Drop null values and duplicates
    ratings_df.dropna(inplace=True)
    ratings_df.drop_duplicates(inplace=True)

    return ratings_df


if __name__ == "__main__":
    # Example usage
    # Path to the folders
    yfinance_folder = "yfinance_data"
    analyst_ratings_file = "raw_analyst_ratings/raw_analyst_ratings.csv"

    print("Loading Stock Data...")
    stock_data_dict = load_stock_data_from_folder(yfinance_folder)
    for stock, data in stock_data_dict.items():
        print(f"Loaded {stock} data. Sample:")
        print(data.head())

    print("\nLoading Analyst Ratings Data...")
    analyst_ratings = load_analyst_ratings(analyst_ratings_file)
    print("Analyst Ratings Data Sample:")
    print(analyst_ratings.head())
