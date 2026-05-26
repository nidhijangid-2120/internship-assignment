# Practise Pandas Series
# Create a Pandas Series from Dictionary 
# Create a Pandas Series from Lists 
# Access the elements of a Series in Pandas
import pandas as pd
# Create a Pandas Series from Dictionary
data = {'a': 1, 'b': 2, 'c': 3}
series_from_dict = pd.Series(data)
print("Pandas Series from Dictionary:")
print(series_from_dict)
# Create a Pandas Series from Lists
data_list = [10, 20, 30, 40, 50]
series_from_list = pd.Series(data_list)
print("\nPandas Series from List:")
print(series_from_list)
# Access the elements of a Series in Pandas
print("\nAccessing elements of the Series:")
print("Element at index 0:", series_from_list[0])
print("Element at index 2:", series_from_list[2])
print("Element at index 4:", series_from_list[4])