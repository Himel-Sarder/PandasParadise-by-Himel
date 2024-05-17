import pandas as pd

# Creating a sample Series
s = pd.Series(['personal land',
               'himel the coderr',
               'dark chocolate'])

# Convert the first character of
# each word to uppercase
print(s.str.title())


# Capitalize the first character of each string
print(s.str.capitalize())
