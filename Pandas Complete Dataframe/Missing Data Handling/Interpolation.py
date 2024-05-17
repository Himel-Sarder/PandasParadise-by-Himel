# interpolate(): Interpolates missing values based on the surrounding values.

# print(df.interpolate())  # Linear interpolation by default


import pandas as pd

data = {'A': [1, None, 3, None, 5], 'B': [3, 6, None, 12, None]}
df = pd.DataFrame(data)

print(df.interpolate())