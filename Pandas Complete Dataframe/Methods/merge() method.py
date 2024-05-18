# Creating two sample DataFrames
import pandas as pd

data1 = {'Name': ['Alice', 'Bob', 'Charlie'],
         'Age': [25, 30, 35]}
df1 = pd.DataFrame(data1)

data2 = {'Name': ['Bob', 'Charlie', 'David'],
         'Score': [85, 90, 88]}
df2 = pd.DataFrame(data2)

# Merging two DataFrames based on 'Name' column
merged_df = pd.merge(df1, df2, on='Name', how='inner')
print("Merged DataFrame:")
print(merged_df)
