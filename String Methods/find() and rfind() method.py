import pandas as pd

# Creating a sample Series
s = pd.Series(['apple', 'banana', 'cherry'])

# Find the index of the first
# occurrence of 'an' in each string
print(s.str.find('an'))

# Find the index of the last
# occurrence of 'e' in each string
print(s.str.rfind('e'))

