import pandas as pd

# Create a Pandas Series
series = pd.Series([1, 2, None, 4, 5])

# Count the non-null elements
count_value = series.count()

print(count_value)