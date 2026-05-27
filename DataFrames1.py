# Create two DataFrames, df1 and df2, with a common column (e.g., 'ID'). 

# Perform an inner merge on this common column and display the resulting DataFrame.
# Perform a left join of df1 and df2 on the 'ID' column. Explain how missing values are handled in the resulting DataFrame. Right Join and Index-Based Join.
# Perform a right join using pd.merge() on a common column, then perform a join using df.join() based on the index. Compare the results. Merging with Multiple Keys.
import pandas as pd
# Create two DataFrames
df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie']
})

df2 = pd.DataFrame({
    'ID': [2, 3, 4],
    'Age': [25, 30, 35]
})
# Perform an inner merge on the 'ID' column
inner_merge = pd.merge(df1, df2, on='ID', how='inner')
print("Inner Merge Result:")
print(inner_merge)
# Perform a left join on the 'ID' column
left_join = pd.merge(df1, df2, on='ID', how='left')
print("\nLeft Join Result:")
print(left_join)
# Perform a right join on the 'ID' column
right_join = pd.merge(df1, df2, on='ID', how='right')
print("\nRight Join Result:")
print(right_join)
# Perform a join using df.join() based on the index
# First, set 'ID' as the index for both DataFrames  
df1.set_index('ID', inplace=True)
df2.set_index('ID', inplace=True)
index_join = df1.join(df2, how='inner')
print("\nIndex-Based Join Result:")
print(index_join)
# Merging with Multiple Keys
# Create two DataFrames with multiple keys  
df3 = pd.DataFrame({
    'ID': [1, 2, 3],
    'City': ['New York', 'Los Angeles', 'Chicago'],
    'Name': ['Alice', 'Bob', 'Charlie']
})
df4 = pd.DataFrame({
    'ID': [2, 3, 4],
    'City': ['Los Angeles', 'Chicago', 'Houston'],
    'Age': [25, 30, 35]
})
# Perform a merge on multiple keys ('ID' and 'City')
multi_key_merge = pd.merge(df3, df4, on=['ID', 'City'], how='inner')
print("\nMulti-Key Merge Result:")
print(multi_key_merge)