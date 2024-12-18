import logging
import pandas as pd
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def load_stock_data_from_folder(folder_path):
    """
    Load all stock price CSV files from a folder into a dictionary.

    Args:
        folder_path (str): Path to the folder containing stock price CSV files.

    Returns:
        dict: A dictionary where keys are file names without extensions,
              and values are pandas DataFrames.

    Raises:
        FileNotFoundError: If the folder does not exist.
    """
    stock_data = {}
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"The folder '{folder_path}' does not exist!")

    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            filepath = os.path.join(folder_path, filename)
            stock_name = filename.replace("_historical_data.csv", "")
            try:
                stock_df = pd.read_csv(filepath)
                required_cols = {"Date", "Open", "High", "Low", "Close", "Volume"}
                if not required_cols.issubset(stock_df.columns):
                    logging.warning(
                        f"{filename} is missing required columns. Skipping..."
                    )
                    continue

                stock_df["Date"] = pd.to_datetime(stock_df["Date"], errors="coerce")
                stock_df.columns = stock_df.columns.str.lower()
                stock_df.dropna(subset=["date"], inplace=True)
                stock_df.sort_values("date", inplace=True)
                stock_data[stock_name] = stock_df
            except Exception as e:
                logging.error(f"Failed to process {filename}: {e}")

    logging.info(f"Loaded data for {len(stock_data)} stocks.")
    return stock_data


import logging
import pandas as pd
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def load_analyst_ratings(filepath):
    """
    Load and preprocess raw analyst ratings data.

    Args:
        filepath (str): Path to the analyst ratings CSV file.

    Returns:
        pd.DataFrame: Cleaned analyst ratings dataframe.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the required columns are missing in the file.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"The file '{filepath}' does not exist!")

    try:
        ratings_df = pd.read_csv(filepath)
        required_cols = {"date", "headline", "publisher", "symbol"}

        # Validate required columns
        if not required_cols.issubset(ratings_df.columns):
            raise ValueError(
                f"The file '{filepath}' is missing one or more required columns: {required_cols}"
            )

        # Process data
        ratings_df["date"] = pd.to_datetime(
            ratings_df["date"], errors="coerce"
        ).dt.tz_localize(None)
        ratings_df.dropna(subset=["date", "headline"], inplace=True)
        ratings_df.drop_duplicates(inplace=True)

        logging.info(
            f"Loaded and cleaned analyst ratings data. Total records: {len(ratings_df)}"
        )
        return ratings_df
    except Exception as e:
        logging.error(f"Error while loading or processing {filepath}: {e}")
        raise
