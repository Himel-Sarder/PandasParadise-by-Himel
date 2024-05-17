import pandas as pd

# Create two DataFrames
df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value': [1, 2, 3]})
df2 = pd.DataFrame({'key': ['B', 'C', 'D'], 'value': [4, 5, 6]})

# Merge DataFrames based on 'key' column with inner join
merged_inner = pd.merge(df1, df2, on='key', how='inner')

print(merged_inner)
