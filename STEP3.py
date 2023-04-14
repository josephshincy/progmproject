import pandas as pd
# read data from csv file
covid_data = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/"
                         "csse_covid_19_time_series/time_series_covid19_confirmed_global.csv")

# select columns with dates only
dates = covid_data.columns[4:]

# sum data by date to get global confirmed cases
global_confirmed = covid_data[dates].sum(axis=0)

# repeat the above steps to get global deaths
covid_data = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/"
                         "csse_covid_19_time_series/time_series_covid19_deaths_global.csv")
global_deaths = covid_data[dates].sum(axis=0)

# create a new dataframe with global confirmed cases and deaths
global_data = pd.DataFrame({"Confirmed": global_confirmed, "Deaths": global_deaths})

print(global_data)