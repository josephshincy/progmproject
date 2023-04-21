# This file will append Stock Data to Covid Data
from PY2 import covid_data
from PY3 import stocks_high_low

#combine dataframes of covid data and stock data
stocks_covid = pd.concat([covid_data,stocks_high_low], axis = 1)
