import pandas as pd
import os
import glob


def load_financial_data(financial_data_path):
    """Load financial data from multiple CSV files in the specified directory."""
    all_files = glob.glob(os.path.join(financial_data_path, "*.csv"))

    financial_dfs = []
    for file in all_files:
        try:
            df = pd.read_csv(file)
            if not df.empty:  # Only add non-empty DataFrames
                df.rename(columns=str.lower, inplace=True)
                df["date"] = pd.to_datetime(df["date"], errors="coerce").dt.tz_localize(
                    None
                )
                financial_dfs.append(df)
            else:
                print(f"Warning: {file} is empty and will not be included.")
            stock_name = os.path.basename(file).split(".")[0]
            df["stock"] = stock_name
            financial_dfs.append(df)
        except Exception as e:
            print(f"Error reading {file}: {e}")
    financial_data = pd.concat(financial_dfs, ignore_index=True)
    # Preprocess Financial Data

    # Calculate Price Change Percentages
    financial_data["price_change_pct"] = (
        (financial_data["close"] - financial_data["open"]) / financial_data["open"]
    ) * 100
    print(financial_data[["date"]].head())
    return financial_data


def load_analyst_data(analyst_data_path):
    """Load analyst data from a CSV file."""
    analyst_data = pd.read_csv(analyst_data_path)
    analyst_data.rename(columns=str.lower, inplace=True)
    analyst_data["date"] = pd.to_datetime(
        analyst_data["date"], errors="coerce"
    ).dt.tz_localize(None)
    # Check the first few rows to verify the conversion
    print(analyst_data[["date"]].head())

    return analyst_data


def merge_data(analyst_data, financial_data):
    """Merge analyst data with financial data."""
    # Merge the data again after ensuring 'date' columns are in datetime format
    merged_data = pd.merge(
        analyst_data,
        financial_data,
        left_on=["stock", "date"],
        right_on=["stock", "date"],
        how="inner",
    )
    print(merged_data.head())
    print(merged_data.columns)

    return merged_data


def analyze_missing_values(data):
    """Print missing values in the dataset."""
    missing_values = data.isnull().sum()
    return missing_values


def save_processed_data(data, output_path):
    """Save the processed data to a CSV file."""
    data.to_csv(output_path, index=False)
