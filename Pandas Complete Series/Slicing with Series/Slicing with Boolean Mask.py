import pandas as pd

# Create a Pandas Series
series = pd.Series([10, 20, 30, 40, 50, 60])

# Boolean masking for slicing
mask = [True, False, True, False, True, True]
print(series[mask])  # Select elements where mask is True
