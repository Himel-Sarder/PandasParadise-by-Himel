import pandas as pd

# Creating a sample Series
s = pd.Series(['java', 'Python', 'PANDAS'])

# Convert all strings to uppercase
print(s.str.upper())

# Convert all strings to lowercase
print(s.str.lower())
