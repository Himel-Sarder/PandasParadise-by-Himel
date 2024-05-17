# Detecting Missing Data:
# isnull(): Returns a boolean DataFrame indicating missing values.
# notnull(): Returns the opposite of isnull(), indicating non-missing values.


import pandas as pd
import numpy as np

data = {'A': [1, None, 3, np.nan], 'B': [np.nan, 5, 6, None]}
df = pd.DataFrame(data)

print(df.isnull())

print(df.notnull)