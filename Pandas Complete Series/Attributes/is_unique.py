import pandas as pd

# Create a Pandas Series
series_unique1 = pd.Series([1, 2, 3, 4, 5])
series_unique2 = pd.Series([1, 2, 3, 3, 5])

# Check if all elements are unique
is_unique1 = series_unique1.is_unique
is_unique2 = series_unique2.is_unique

print(is_unique1)
print(is_unique2)