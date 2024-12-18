import pandas as pd


def merge_stock_and_ratings(stock_data, analyst_ratings_sentiment):
    """
    Merge stock data with analyst ratings.

    Args:
        stock_data (dict): Dictionary of stock data DataFrames (one for each stock).
        analyst_ratings (pd.DataFrame): Analyst ratings DataFrame with columns like 'date', 'headline'.

    Returns:
        pd.DataFrame: A merged DataFrame containing stock data and corresponding analyst ratings.
    """
    merged_data = []

    for stock_name, stock_df in stock_data.items():
        print(f"Merging data for stock: {stock_name}...")
        ratings_for_stock = analyst_ratings_sentiment[
            analyst_ratings_sentiment["stock"].str.upper() == stock_name.upper()
        ]

        if ratings_for_stock.empty:
            print(f"No matching analyst ratings for stock: {stock_name}. Skipping...")
            continue
        stock_df["date"] = pd.to_datetime(stock_df["date"])
        ratings_for_stock.loc[:, "date"] = pd.to_datetime(
            ratings_for_stock["date"]
        ).dt.date
        merged_stock_data = pd.merge(
            stock_df,
            ratings_for_stock,
            on=["date"],
            how="inner",
        )
        merged_stock_data["stock_name"] = stock_name
        merged_data.append(merged_stock_data)
    merged_data = (
        pd.concat(merged_data, ignore_index=True) if merged_data else pd.DataFrame()
    )
    return merged_data
