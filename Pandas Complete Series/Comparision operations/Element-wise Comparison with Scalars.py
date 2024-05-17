import pandas as pd

# Create a Pandas Series
series = pd.Series([1, 2, 3])

# Compare each element with a scalar value
result = series > 2

print(result)