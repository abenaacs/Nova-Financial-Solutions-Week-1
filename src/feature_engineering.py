import talib
import pynance as pn
import talib
import pandas as pd


def add_technical_indicators(stock_data):
    """
    Adds technical indicators (SMA, RSI, MACD) and daily returns to stock data.

    Parameters:
    stock_data (dict): A dictionary where keys are stock tickers and values are DataFrames.

    Returns:
    dict: Updated dictionary with technical indicators added.
    """
    for ticker, df in stock_data.items():
        try:
            if "close" not in df.columns or "date" not in df.columns:
                print(f"Skipping {ticker}: Missing 'close' or 'date' column.")
                continue
            df = df.sort_values(by="date")
            df["SMA_20"] = talib.SMA(df["close"], timeperiod=20)
            df["SMA_50"] = talib.SMA(df["close"], timeperiod=50)
            df["RSI"] = talib.RSI(df["close"], timeperiod=14)
            df["MACD"], df["Signal"], df["Hist"] = talib.MACD(
                df["close"], fastperiod=12, slowperiod=26, signalperiod=9
            )
            df["Daily_Returns"] = df["close"].pct_change()
            stock_data[ticker] = df
            print(f"Technical indicators added for {ticker}:")
            print(
                df[
                    [
                        "date",
                        "close",
                        "SMA_20",
                        "SMA_50",
                        "RSI",
                        "MACD",
                        "Signal",
                        "Daily_Returns",
                    ]
                ].head()
            )

        except Exception as e:
            print(f"Error processing {ticker}: {e}")

    return stock_data
