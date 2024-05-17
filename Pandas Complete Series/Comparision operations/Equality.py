import pandas as pd

# Create Pandas Series
series1 = pd.Series([1, 2, 3])
series2 = pd.Series([1, 4, 3])

# Check for equality
result = series1 == series2

print(result)