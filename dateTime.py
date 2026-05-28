# 2) Explore more datetime function and uses in pandas 
import pandas as pd
# Create a sample DataFrame with datetime data
data = {
    'date': ['2023-01-01', '2023-01-02', '2023-01-03'],
    'value': [1, 2, 3]
}
df = pd.DataFrame(data)
df['date'] = pd.to_datetime(df['date'])
# Extracting year, month, and day from the date column
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
print(df)
# Filtering data based on date
df_filtered = df[df['date'] == '2023-01-02']
print(df_filtered)
# Adding a new column with the day of the week
df['day_of_week'] = df['date'].dt.day_name()
print(df)
# Resampling data by month and calculating the sum of values
df.set_index('date', inplace=True)
df_resampled = df.resample('M').sum()
print(df_resampled)
