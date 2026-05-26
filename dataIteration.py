# Data iteration
# Different ways to iterate over rows in Pandas Dataframe 
# Selecting rows in pandas DataFrame based on conditions 
# Select any row from a Dataframe using iloc[]
# Limited rows selection with given column
# Drop rows from the dataframe based on certain condition applied on a column 
# Insert row at given position in Pandas Dataframe 
# Create a list from rows in Pandas dataframe
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
# Insert row at given position in Pandas DataFrame
print("\nInserting a new row at index 2:")
new_row = {'Name': 'Frank', 'Age': 28, 'City': 'San Francisco'}
df = pd.concat([df.iloc[:2], pd.DataFrame([new_row]), df.iloc[2:]]).reset_index(drop=True)
print(df)
# Create a list from rows in Pandas DataFrame
print("\nCreating a list from the 'Name' column:")
name_list = df['Name'].tolist()
print(name_list)
