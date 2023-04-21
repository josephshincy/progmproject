# Visualizations

# first check that you have installed packages pandas and matplotlib
import pandas as pd
import matplotlib as plt
from PY4 import stocks_covid

# plot line time series of all
fig, ax = plt.subplots(5, figsize=(15, 12))
stock_columns = stocks_covid.columns[2::]
i = 0
r = 0
c = 0
for x in stock_columns:
    ax[r].plot(stocks_covid.index, stocks_covid[x], label=x)
    ax[r].legend(bbox_to_anchor=(1, 0.3))
    ax[r].set_ylabel('Price ($)')
    if i % 2 != 0:
        r += 1
    i += 1
fig.suptitle('Stock Daily High/Low over Time')
fig.tight_layout()
plt.show()

#focused stock data plots on time around drop in 2020 (plot from 2020-01-01 to 2020-06-31)
stocks_covid_2020Drop = stocks_covid[(stocks_covid.index >= '2020-01-01') & (stocks_covid.index <= '2020-06-06')]
fig2, ax2 = plt.subplots(5,figsize = (15,12))
stock_columns2 = stocks_covid_2020Drop.columns[2::]
i2=0
r2=0
for x in stock_columns:
  ax2[r2].plot(stocks_covid_2020Drop.index, stocks_covid_2020Drop[x], label=x)
  ax2[r2].legend(bbox_to_anchor = (0.15,0.3))
  ax2[r2].set_ylabel('Price ($)')
  if i2%2 != 0:
    r2+=1
  i2+=1
fig2.suptitle('Stock Daily High/Low over Time (focused on Drop in 2020)')
fig2.tight_layout()
plt.show()