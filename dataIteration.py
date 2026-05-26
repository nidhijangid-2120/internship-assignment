# Data iteration
# Different ways to iterate over rows in Pandas Dataframe 
# Selecting rows in pandas DataFrame based on conditions 
# Select any row from a Dataframe using iloc[]
# Limited rows selection with given column
# Drop rows from the dataframe based on certain condition
import pandas as pd
# Create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 30, 35, 40, 45],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']}
df = pd.DataFrame(data)
# Different ways to iterate over rows in Pandas DataFrame
print("Iterating over rows using iterrows():")
for index, row in df.iterrows():
    print(f"Index: {index}, Name: {row['Name']}, Age: {row['Age']}, City: {row['City']}")
# Selecting rows in pandas DataFrame based on conditions
print("\nSelecting rows where Age > 30:")
age_condition = df[df['Age'] > 30]
print(age_condition)
# Select any row from a DataFrame using iloc[]
print("\nSelecting the second row using iloc[]:")
second_row = df.iloc[1]
print(second_row)
# Limited rows selection with given column
print("\nSelecting the 'Name' column for the first three rows:")
name_column = df.loc[:2, 'Name']
print(name_column)
# Drop rows from the DataFrame based on certain condition
print("\nDropping rows where Age < 30:")
df_filtered = df[df['Age'] >= 30]
print(df_filtered)
