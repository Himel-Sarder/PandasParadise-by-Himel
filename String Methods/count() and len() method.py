import pandas as pd

# Creating a sample Series
s = pd.Series(['apple', 'banana', 'cherry'])

# Count the occurrences of 'a' in each string
print(s.str.count('a'))

# Calculate the length of each string
print(s.str.len())