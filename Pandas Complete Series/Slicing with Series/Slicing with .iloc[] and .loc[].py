import pandas as pd

# Create a Pandas Series with custom index labels
series = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])

# Positional slicing using .iloc[]
print(series.iloc[1:3])  # Select elements from index 1 to index 2 (exclusive)

# Label-based slicing using .loc[]
print(series.loc['b':'d'])  # Select elements from index label 'b' to 'd' (inclusive)
