# Create three DataFrames. Vertically concatenate two of them using pd.concat(), then merge the resulting DataFrame with the third DataFrame on a common key. T Understand join() vs. merge().

# Also Explain the primary differences between df.join() and pd.merge()
import pandas as pd
# Create three DataFrames
df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie']
})

df2 = pd.DataFrame({
    'ID': [4, 5, 6],
    'Name': ['David', 'Eve', 'Frank']
})

df3 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Age': [25, 30, 35]
})
# Vertically concatenate df1 and df2 using pd.concat()
concatenated_df = pd.concat([df1, df2], ignore_index=True)
print("Concatenated DataFrame:")
print(concatenated_df)

# Merge the concatenated DataFrame with df3 on the 'ID' column
merged_df = pd.merge(concatenated_df, df3, on='ID', how='inner')
print("\nMerged DataFrame:")
print(merged_df)
# Explanation of df.join() vs. pd.merge()
# df.join() is primarily used for joining DataFrames based on their index. It is a convenient method for combining DataFrames when the index is the key. It can perform left, right, and inner joins based on the index.
# pd.merge() is a more flexible function that allows you to merge DataFrames based on one or more keys (columns). It can perform various types of joins (inner, left, right, outer) and is not limited to index-based merging. It is suitable for merging DataFrames with different structures or when the key is not the index.    