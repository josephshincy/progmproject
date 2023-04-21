from PY1 import deaths_df, confirmed_cases_df
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
global_confirmed_cases = confirmed_cases_df.iloc[:, -1].sum()
global_deaths = deaths_df.iloc[:, -1].sum()

# Create a dataframe with the global totals
global_totals_df = pd.DataFrame({
    "Confirmed Cases": [global_confirmed_cases]

