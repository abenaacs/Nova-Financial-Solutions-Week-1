import pandas as pd


def merge_stock_and_ratings(stock_data_dict, analyst_ratings_df, symbol_column="stock"):
    """
    Merge stock data and analyst ratings based on stock symbols.

    Args:
        stock_data_dict (dict): Dictionary containing stock price dataframes.
        analyst_ratings_df (pd.DataFrame): Analyst ratings dataframe.
        symbol_column (str): Column name in analyst ratings dataframe containing stock symbols.

    Returns:
        dict: Updated stock data dictionary with merged analyst ratings where applicable.
    """
    merged_data = {}

    for stock, stock_df in stock_data_dict.items():
        # Filter analyst ratings for the current stock symbol
        if symbol_column in analyst_ratings_df.columns:
            stock_ratings = analyst_ratings_df[
                analyst_ratings_df[symbol_column] == stock
            ]

            # Merge ratings with stock data on 'Date'
            merged_df = pd.merge(
                stock_df,
                stock_ratings,
                on="Date",
                how="left",  # Left join to retain all stock data
            )
            merged_data[stock] = merged_df
        else:
            print(f"Symbol column '{symbol_column}' not found in analyst ratings data.")
            merged_data[stock] = stock_df

    return merged_data


if __name__ == "__main__":
    from data_loader import load_stock_data_from_folder, load_analyst_ratings

    # Paths
    yfinance_folder = "yfinance_data"
    analyst_ratings_file = "raw_analyst_ratings/raw_analyst_ratings.csv"

    # Load data
    stock_data = load_stock_data_from_folder(yfinance_folder)
    analyst_ratings = load_analyst_ratings(analyst_ratings_file)

    # Merge data
    print("Merging Stock Data with Analyst Ratings...")
    merged_data = merge_stock_and_ratings(stock_data, analyst_ratings)

    # Display merged data
    for stock, df in merged_data.items():
        print(f"{stock} - Merged Data Sample:")
        print(df.head(), "\n")
