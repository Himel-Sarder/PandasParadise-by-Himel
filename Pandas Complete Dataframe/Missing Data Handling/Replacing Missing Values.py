# replace(): Replaces specified values with other values.
# df.replace(to_replace, value)

import pandas as pd
import numpy as np

data = {'A': [1, None, 3], 'B': [None, 5, 6]}
df = pd.DataFrame(data)

print(df.replace(np.nan, -1))  # Replace None with -1

