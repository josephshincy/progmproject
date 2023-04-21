#Get Stock daily high and low data and save in dataframe

#import required libraries
#first check that you have installed packages pandas and yfinance
#import required libraries
import pandas as pd
import DateTime as dt

import yfinance as yf

#Set your alpha_vantage API key Here
key = 'HK550L4D3IIB0IMZ'

#define a function that takes in the accepted ticker for the required stock and returns that stock's daily adjusted information from AlphaVantage
def getalpha(stock):
  alpha = pd.read_csv('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=' + stock + '&apikey=' + key + '&datatype=csv')
  return alpha

#define a function that takes in the accepted ticker for the required stock and returns that stock's daily adjusted information from yfinance
def getyahoo(stock):
  ydata = pd.DataFrame(yf.Ticker(stock).history(period="10y"))
  return ydata

#define stocks to gather data for
#Overall American Market (Dow Jones Industrial Average)
stock_a = '^DJI'
#Overall Canadian Market (S&P/TSX Composite index)
stock_b = '^GSPTSE'
#Travel Sector (Delta Air Lines)
stock_c = 'DAL'
#Real Estate Sector (Colliers International Group Inc.)
stock_d = 'CIGI'
#Precious Metals (Alamos Gold)
stock_e = 'AGI'

#Get stock data for selected stocks from AlphaVantage and yfinance
alpha_a = getyahoo(stock_a)
alpha_b = getyahoo(stock_b)
alpha_c = getyahoo(stock_c)
alpha_d = getyahoo(stock_d)
alpha_e = getyahoo(stock_e)

#isolate daily high and low values
a = alpha_a[['High','Low']]
a.columns = [f'{stock_a}_high',f'{stock_a}_low']
b = alpha_b[['High','Low']]
b.columns = [f'{stock_b}_high',f'{stock_b}_low']
c = alpha_c[['High','Low']]
c.columns = [f'{stock_c}_high',f'{stock_c}_low']
d = alpha_d[['High','Low']]
d.columns = [f'{stock_d}_high',f'{stock_d}_low']
e = alpha_e[['High','Low']]
e.columns = [f'{stock_e}_high',f'{stock_e}_low']

#combine into one dataframe with all high and low values for all stocks
stocks_high_low = pd.concat([a,b,c,d,e], axis = 1)
index_series = pd.DataFrame(stocks_high_low.index)
index_series['Date'] = index_series['Date'].dt.date
stocks_high_low.index = index_series['Date']
stocks_high_low.index = pd.to_datetime(stocks_high_low.index)

print(stocks_high_low.head(30))
print(stocks_high_low.index.dtype)