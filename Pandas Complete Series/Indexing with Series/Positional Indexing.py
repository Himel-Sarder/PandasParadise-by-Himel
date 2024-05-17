import pandas as pd

# Create a Pandas Series
s = [11, 12, 13, 14, 15]
series = pd.Series(s)

# Accessing elements by position
print(series[0])    # Access the first element
print(series[1:4])  # Access a slice of elements


'''
11
1    12
2    13
3    14
dtype: int64
'''