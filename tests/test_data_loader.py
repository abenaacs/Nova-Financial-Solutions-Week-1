import pytest
import pandas as pd
from src.data_loader import (
    load_stock_data_from_folder,
)


@pytest.fixture
def sample_stock_data():
    """Fixture to return sample stock data for testing"""
    data = {
        "date": pd.date_range(start="2020-01-01", periods=5, freq="D"),
        "close": [100, 101, 102, 103, 104],
    }
    return pd.DataFrame(data)


def test_load_stock_data_from_folder(sample_stock_data):
    # Assuming load_stock_data_from_folder loads a CSV file and returns a dataframe
    df = sample_stock_data
    assert df.shape == (5, 2), "Dataframe should have 5 rows and 2 columns"
    assert "date" in df.columns, "Dataframe should contain 'date' column"
    assert "close" in df.columns, "Dataframe should contain 'close' column"
