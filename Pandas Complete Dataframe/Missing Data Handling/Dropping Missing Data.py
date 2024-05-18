# dropna(): Drops rows or columns containing missing values.

# df.dropna()  # Drop rows with any missing value
# df.dropna(axis=1)  # Drop columns with any missing value
# df.dropna(thresh=2)  # Drop rows with at least 2 non-null values


import pandas as pd
import numpy as np

data = {'A': [1, np.nan, 3], 'B': [4, None, 6], 'C' : [1, 2, 3]}
df = pd.DataFrame(data)

print(df.dropna())  # Drop rows with any missing value
print(df.dropna(axis=1))  # Drop columns with any missing value
print(df.dropna(thresh=2)) # Drop rows with at least 2 non-null values
