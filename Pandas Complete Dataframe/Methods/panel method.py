import pandas as pd
import numpy as np
# Using MultiIndex DataFrame instead of Panel
index = pd.MultiIndex.from_product([[2019, 2020], ['Q1', 'Q2']],
                                   names=['Year', 'Quarter'])
columns = ['A', 'B', 'C']
data = np.random.randn(4, 3)

df = pd.DataFrame(data, index=index, columns=columns)

print(df)
