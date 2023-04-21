#This will read covid confirmed cases and deaths into 2 dataframes
import pandas as pd

# URL for the confirmed cases data
confirmed_cases_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"

# Read the data into a DataFrame
confirmed_cases_df = pd.read_csv(confirmed_cases_url)

# URL for the deaths data
deaths_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"

# Read the data into a DataFrame
deaths_df = pd.read_csv(deaths_url)
print(confirmed_cases_df)
print(deaths_df)


