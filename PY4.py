# This file will append Stock Data to Covid Data
# first check that you have installed packages pandas, DateTime and yfinance

from PY2 import covid_data
from PY3 import stocks_high_low

import pandas as pd

# combine dataframes of covid data and stock data
stocks_covid = pd.concat([covid_data, stocks_high_low], axis=1)
# keep only data from 2018 onwards
stocks_covid = stocks_covid[(stocks_covid.index >= '2018-01-01')]
#print(stocks_covid)
