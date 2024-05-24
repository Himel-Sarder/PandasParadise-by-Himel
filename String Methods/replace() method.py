import pandas as pd

# Creating a sample Series
s = pd.Series(['apple', 'banana', 'pherry'])

# Replace 'a' with 'X' in each string of the Series
result = s.str.replace('a', 'X')
print(result)

# Replace 'p' with '_' in each string of the Series
result2 = s.str.replace('p', '_')
print(result2)