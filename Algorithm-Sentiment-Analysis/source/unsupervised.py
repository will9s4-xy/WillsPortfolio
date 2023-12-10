from statsmodels.regression.rolling import RollingOLS
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import statsmodels.api as sm
import pandas as pd
import numpy as np
import datetime as dt        
import yfinance as yf  
import pandas_ta  
import warnings  
warnings.filterwarnings('ignore')

class FinancialDataDownloader:
    def __init__(self):
        self.data = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]
        self.data['Symbol'] = self.data['Symbol'].str.replace('.', '-', regex=True)
        self.data_symbols = self.data['Symbol'].unique().tolist()
        self.failed_download = []
        self.finance_data = pd.DataFrame()

    def download_data(self, start_date, end_date):
        for symbol in self.data_symbols:
            try:
                historical_data = yf.download(tickers=symbol, start=start_date, end=end_date)
                self.finance_data = pd.concat([self.finance_data, historical_data], axis=1)
            except Exception as e:
                print(f"Failed to download data for {symbol}: {e}")
                self.failed_download.append(symbol)

    def display_results(self):
        print("\nFailed downloads:", self.failed_download)
        print("\nFinancial data")
        print(self.finance_data.head())
        print( best_underlyings )

    def predict_best_underlyings(self):
        #Get the data
        data = self.finance_data
        #Get the 5 best underlyings
        best_underlyings = data.iloc[:, 1:6].mean().sort_values(ascending=False).head(5).index.tolist()


    def main(self):
        end_date = input("Enter the end date (YYYY-MM-DD): ")
        start_date = pd.to_datetime(end_date) - pd.DateOffset(years=8)
        self.download_data(start_date, end_date)
        self.display_results()
        self.predict_best_underlyings()

# Instantiate the class and call the main method
if __name__ == "__main__":
    financial_downloader = FinancialDataDownloader()
    financial_downloader.main()
