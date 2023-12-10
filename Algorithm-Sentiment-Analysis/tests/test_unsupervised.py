import pytest
from unittest.mock import patch
import sys
sys.path.append(r"C:\Users\William Sanefski\OneDrive\Documents\Will's Portfolio\Algorithm-Sentiment-Analysis")
import pandas as pd
from source.unsupervised import FinancialDataDownloader

@pytest.fixture
def financial_downloader():
    return FinancialDataDownloader()

@pytest.mark.parametrize("start_date, end_date", [("2022-01-01", "2023-01-01"), ("2021-01-01", "2022-01-01")])
def test_download_data(financial_downloader, start_date, end_date):
    with patch("yfinance.download") as mock_download:
        mock_download.return_value = pd.DataFrame({"Adj Close": [1, 2, 3]})
        financial_downloader.download_data(start_date, end_date)
        assert not financial_downloader.failed_download
        assert not financial_downloader.finance_data.empty




