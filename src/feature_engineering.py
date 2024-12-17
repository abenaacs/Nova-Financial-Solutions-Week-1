from pynance.ind import indicators
import talib


def add_moving_averages(stock_data_dict, windows=[7, 30]):
    """
    Add moving averages to each stock dataframe.

    Args:
        stock_data_dict (dict): Dictionary containing stock dataframes.
        windows (list): List of window sizes for moving averages.

    Returns:
        dict: Updated stock data dictionary with moving averages.
    """
    for stock, df in stock_data_dict.items():
        for window in windows:
            df[f"MA_{window}"] = df["Close"].rolling(window=window).mean()
        stock_data_dict[stock] = df
    return stock_data_dict


def calculate_technical_indicators(df):
    """
    Calculate basic technical indicators using TA-Lib.

    Args:
        df (pd.DataFrame): Stock price data with columns 'Open', 'High', 'Low', 'Close', 'Volume'.

    Returns:
        pd.DataFrame: DataFrame with added technical indicators.
    """
    # Simple Moving Average (SMA)
    df["SMA_50"] = talib.SMA(df["Close"], timeperiod=50)
    df["SMA_200"] = talib.SMA(df["Close"], timeperiod=200)

    # Exponential Moving Average (EMA)
    df["EMA_50"] = talib.EMA(df["Close"], timeperiod=50)

    # Relative Strength Index (RSI)
    df["RSI"] = talib.RSI(df["Close"], timeperiod=14)

    # MACD (Moving Average Convergence Divergence)
    df["MACD"], df["MACD_signal"], df["MACD_hist"] = talib.MACD(
        df["Close"], fastperiod=12, slowperiod=26, signalperiod=9
    )

    print("Technical indicators calculated successfully.")
    return df


def calculate_pynance_metrics(df):
    """
    Calculate additional financial metrics using PyNance.

    Args:
        df (pd.DataFrame): Stock price data with columns 'Open', 'High', 'Low', 'Close', 'Volume'.

    Returns:
        pd.DataFrame: DataFrame with added financial metrics.
    """
    # Example: Add metrics like cumulative returns
    df["Cumulative_Returns"] = indicators.cumulative_returns(df["Close"])
    print("Financial metrics calculated using PyNance.")
    return df
