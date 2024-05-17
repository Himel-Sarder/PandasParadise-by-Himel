import pandas as pd

# Create a Pandas Series with custom index labels
series = pd.Series([10, 20, 30, 40], index=['A', 'B', 'C', 'D'])

print(series)
# Accessing elements by label
print(series['A'])      # Access element with label 'A'
print(series[['B', 'C']])  # Access elements with labels 'B' and 'C'


'''
A    10
B    20
C    30
D    40
dtype: int64
10
B    20
C    30
dtype: int64
'''