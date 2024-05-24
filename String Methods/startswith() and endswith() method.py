import pandas as pd

# Creating a sample Series
s = pd.Series(['apple', 'banana', 'cherry'])

# Check if each string starts with 'a'
result = s.str.startswith('a')
print(result)

# Check if each string starts with 'b'
print(s.str.startswith('b'))

# Check if each string ends with 'e'
print(s.str.endswith('e'))

# Check if each string ends with 'y'
print(s.str.endswith('y'))
