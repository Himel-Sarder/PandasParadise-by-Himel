import pandas as pd

# Create a Pandas Series with custom index labels
series = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])

# Positional indexing using .iloc[]
print(series.iloc[0])    # Access the first element
print(series.iloc[1:3])  # Access a slice of elements

# Label-based indexing using .loc[]
print(series.loc['a'])      # Access element with label 'a'
print(series.loc[['b', 'c']])  # Access elements with labels 'b' and 'c'
