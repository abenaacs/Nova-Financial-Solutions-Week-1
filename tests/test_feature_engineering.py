import pytest
from src.feature_engineering import (
    add_technical_indicators,
)
import pandas as pd


@pytest.fixture
def sample_stock_data():
    """Fixture to return sample stock data for testing"""
    data = {
        "date": pd.date_range(start="2020-01-01", periods=5, freq="D"),
        "close": [100, 101, 102, 103, 104],
    }
    return pd.DataFrame(data)


def test_add_sma(sample_stock_data):
    # Test if Simple Moving Average (SMA) is added correctly
    df = add_technical_indicators(sample_stock_data)

    # Check if SMA columns exist
    assert "SMA_20" in df.columns, "SMA_20 column not found"
    assert "SMA_50" in df.columns, "SMA_50 column not found"

    # Check if SMA columns are numeric
    assert df["SMA_20"].dtype == float, "SMA_20 column should be float"
    assert df["SMA_50"].dtype == float, "SMA_50 column should be float"
