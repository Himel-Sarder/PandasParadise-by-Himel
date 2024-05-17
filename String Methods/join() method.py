import pandas as pd

# Creating a sample Series
s = pd.Series(['Web Development ',
               'Python Developer ',
               'Competitive programmer'])

# Joining elements of the
# Series with a separator
result = '|'.join(s)
result2 = '*'.join(s)
result3 = '#'.join(s)
print(result)
print(result2)
print(result3)
