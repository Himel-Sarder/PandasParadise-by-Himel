import pandas as pd

# Create a Pandas Series
series = pd.Series([1, 2, 3, 4, 5])

# Assign a name to the Series
series.name = 'Himel Sarder'

# Get the name of the Series
name = series.name

print(name)