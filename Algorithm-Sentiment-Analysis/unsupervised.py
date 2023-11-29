from statsmodels.regression.rolling import RollingOLS
import pandas_datareader.data as web
import matplotlib.pyplot as pit
import statsmodels.api as sm
import pandas as pd
import numpy as np
import datetime as dt       
import yfinance as yf 
import pandas_ta 
import warnings 
warnings.filterwarnings('ignore')

data = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]
data['Symbol'] = data['Symbol'].str.replace('.', '-')

data_symbols = data['Symbol'].unique().tolist()

end_date = input("Enter the end date (YYYY-MM-DD): ")
start_date = pd.to_datetime(end_date)-pd.DateOffset(years=8)

failed_download = []
finance_data = pd.DataFrame()
for symbol in data_symbols:
    try:
        historical_data = yf.download(tickers=symbol, start=start_date, end=end_date)
        finance_data = pd.concat([finance_data, historical_data], axis=1)
    except Exception as e:
        print("Failed to download data for {symbol}: {e}")
        failed_download.append(symbol)
    
print("\nFailed downloads:", failed_download)
print("\nFinancial data")
print(finance_data.head())


