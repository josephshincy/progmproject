
from PY1 import deaths_df, confirmed_cases_df
import pandas as pd
confirmed_cases = confirmed_cases_df.drop(columns=['Province/State','Country/Region','Lat','Long'])
print(confirmed_cases)
confirmed_cases = pd.DataFrame.transpose(confirmed_cases)
print(confirmed_cases)
confirmed_cases = pd.DataFrame(confirmed_cases.sum(axis=1), columns=['confirmed_cases'])
confirmed_cases.index.name='Date'
#confirmed_cases.columns = ['confirmed_cases']
confirmed_cases.index =pd.to_datetime(confirmed_cases.index)
deaths_df = deaths_df.drop(columns=['Province/State','Country/Region','Lat','Long'])
print(deaths_df)
covid_deaths = pd.DataFrame.transpose(deaths_df)
print(covid_deaths)
covid_deaths = pd.DataFrame(covid_deaths.sum(axis=1), columns=['covid_deaths'])
covid_deaths.index.name='Date'
#deaths_cases.columns = ['covid_deaths']
print(covid_deaths)
covid_deaths.index =pd.to_datetime(covid_deaths.index)
print(covid_deaths)
covid_data = pd.concat ([confirmed_cases, covid_deaths], axis = 1)
print (covid_data)
