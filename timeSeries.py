# Convert a series of date-strings to a timeseries
import pandas as pd

def convert_to_timeseries(date_strings):
    return pd.to_datetime(date_strings)
# Example usage
date_strings = ['2021-01-01', '2021-02-01', '2021-03-01']
timeseries = convert_to_timeseries(date_strings)
print(timeseries)