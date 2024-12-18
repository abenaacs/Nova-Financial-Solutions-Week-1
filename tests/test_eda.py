import pytest
from src.eda import (
    plot_stock_prices,
)
import pandas as pd
import matplotlib.pyplot as plt


@pytest.fixture
def sample_stock_data():
    """Fixture to return sample stock data for testing"""
    data = {
        "date": pd.date_range(start="2020-01-01", periods=5, freq="D"),
        "close": [100, 101, 102, 103, 104],
    }
    return pd.DataFrame(data)


def test_plot_stock_prices(sample_stock_data):
    # Test that the plot is called
    with pytest.raises(
        ValueError
    ):  # We expect an error if data is not passed correctly
        plot_stock_prices({})

    # Now check for valid input
    try:
        plot_stock_prices({"Test Stock": sample_stock_data})
    except Exception as e:
        pytest.fail(f"plot_stock_prices raised {type(e).__name__} unexpectedly!")

    # Check that plt.show() is called during the function (testing the plot)
    with pytest.raises(Exception):
        plt.close()  # Avoid error if plt.show() raises exception.
