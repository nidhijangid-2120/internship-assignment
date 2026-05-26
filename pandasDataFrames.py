# DataFrames
# Make a Pandas DataFrame with a two-dimensional Python list 
# Create DataFrame from Python dict 
# Create Pandas dataframe using list of lists 
# Create a Pandas dataframe using list of tuples 
# Create a Pandas DataFrame from List of Dicts
import pandas as pd
# Make a Pandas DataFrame with a two-dimensional Python list
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
df = pd.DataFrame(data) 
print("DataFrame from 2D list:")
print(df)
# Create DataFrame from Python dict
data_dict = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35], 'City': ['New York', 'Los Angeles', 'Chicago']}
df_dict = pd.DataFrame(data_dict)
print("\nDataFrame from Dictionary:")
print(df_dict)
# Create Pandas dataframe using list of lists
data_list_of_lists = [['Alice', 25, 'New York'], ['Bob', 30, 'Los Angeles'], ['Charlie', 35, 'Chicago']]
df_list_of_lists = pd.DataFrame(data_list_of_lists, columns=['Name', 'Age', 'City'])
print("\nDataFrame from List of Lists:")
print(df_list_of_lists)
# Create a Pandas dataframe using list of tuples
data_list_of_tuples = [('Alice', 25, 'New York'), ('Bob', 30, 'Los Angeles'), ('Charlie', 35, 'Chicago')]
df_list_of_tuples = pd.DataFrame(data_list_of_tuples, columns=['Name', 'Age', 'City'])
print("\nDataFrame from List of Tuples:")
print(df_list_of_tuples)
# Create a Pandas DataFrame from List of Dicts  
data_list_of_dicts = [{'Name': 'Alice', 'Age': 25, 'City': 'New York'}, {'Name': 'Bob', 'Age': 30, 'City': 'Los Angeles'}, {'Name': 'Charlie', 'Age': 35, 'City': 'Chicago'}]
df_list_of_dicts = pd.DataFrame(data_list_of_dicts)
print("\nDataFrame from List of Dicts:")
print(df_list_of_dicts)