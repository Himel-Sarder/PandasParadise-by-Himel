import pandas as pd

# Create a Pandas Series with monotonically increasing values
series_inc = pd.Series([1, 2, 3, 4, 5])

# Check if the values are monotonically increasing
is_monotonic_inc = series_inc.is_monotonic

print(is_monotonic_inc)

# Create a Pandas Series with monotonically decreasing values
series_dec = pd.Series([5, 4, 3, 2, 1])

# Check if the values are monotonically decreasing
is_monotonic_dec = series_dec.is_monotonic

print(is_monotonic_dec)