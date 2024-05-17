import pandas as pd

# Create a Pandas Series with custom index labels
series = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])

# Slicing using index labels
print(series['b':'d'])  # Select elements from index label 'b' to 'd' (inclusive)
