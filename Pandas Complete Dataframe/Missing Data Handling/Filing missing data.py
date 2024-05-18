# fillna(): Fills missing values with specified values.

# df.fillna(value)  # Fill missing values with a scalar or a dictionary
# df.fillna(method='ffill')  # Forward fill missing values
# df.fillna(method='bfill')  # Backward fill missing values


import pandas as pd

data = {'A': [1, None, 3], 'B': [None, 5, 6]}
df = pd.DataFrame(data)

print(df.fillna(0))  # Fill missing values with a scalar
print(df.fillna({'A': 0, 'B': 1}))  # Fill missing values with a dictionary
print(df.fillna(method='ffill'))
print(df.fillna(method='bfill'))
print(df.fillna(method='pad'))