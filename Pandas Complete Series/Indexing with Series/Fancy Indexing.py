import pandas as pd

# Create a Pandas Series
series = pd.Series([10, 20, 30, 40])

# Fancy indexing with numeric indices
print(series[[0, 2]])     # Select elements at positions 0 and 2

# Fancy indexing with correct labels
# Assuming labels 'A' and 'C' are present in the Series
series.index = ['A', 'B', 'C', 'D']
print(series[['A', 'C']])  # Select elements with labels 'A' and 'C'


'''
0    10
2    30
dtype: int64
A    10
C    30
dtype: int64
'''