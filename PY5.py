#Visualizations

#first check that you have installed packages pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt
from PY4 import stocks_covid

#plot line time series of all
fig, ax = plt.subplots(5,figsize = (15,12))
stock_columns = stocks_covid.columns[2::]
i=0
r=0
c=0
for x in stock_columns:
  ax[r].plot(stocks_covid.index, stocks_covid[x], label=x)
  ax[r].legend(bbox_to_anchor = (1,0.3))
  ax[r].set_ylabel('Price ($)')
  if i%2 != 0:
    r+=1
  i+=1
fig.suptitle('Stock Daily High/Low over Time')
fig.tight_layout()
plt.show()

