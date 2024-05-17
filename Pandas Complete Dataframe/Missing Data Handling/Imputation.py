# Fill missing values with estimated values (e.g., mean, median, mode) based on other observations.

import pandas as pd

data = {'A': [1, None, 3], 'B': [4, None, 6], 'C' : [None, 2, 3]}
df = pd.DataFrame(data)

print(df.fillna(df.mean()))  # Fill missing values with mean of each column
