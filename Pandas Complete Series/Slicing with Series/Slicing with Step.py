import pandas as pd

# Create a Pandas Series
series = pd.Series([10, 20, 30, 40, 50])

# Slicing with step
print(series[::2])  # Select every second element
