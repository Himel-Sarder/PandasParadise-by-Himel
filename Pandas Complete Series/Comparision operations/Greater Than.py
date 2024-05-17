import pandas as pd

# Create Pandas Series
series1 = pd.Series([1, 2, 3])
series2 = pd.Series([2, 2, 2])

# Check if series1 elements are greater than series2 elements
result = series1 > series2

print(result)