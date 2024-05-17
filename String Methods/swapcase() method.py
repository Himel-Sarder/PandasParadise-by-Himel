import pandas as pd

# Creating a sample Series
s = pd.Series(['Hello World',
               'Python Programming',
               'PYTHon PanDAS'])

# Swap the case of each character in the strings

print(s.str.swapcase())