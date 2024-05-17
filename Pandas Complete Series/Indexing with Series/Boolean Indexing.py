import pandas as pd

# Create a Pandas Series
series = pd.Series([10, 20, 30, 40, 5, 50])

# Boolean indexing
print(series[series > 20])  # Select elements greater than 20


'''
2    30
3    40
5    50
dtype: int64
'''