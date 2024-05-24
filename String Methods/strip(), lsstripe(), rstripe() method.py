import pandas as pd

# Creating a sample Series
s = pd.Series(['  hello ', '  world', 'python  '])

# Remove leading and trailing whitespace
print(s.str.strip())


# Remove leading whitespace
print(s.str.lstrip())


# Remove trailing whitespace
print(s.str.rstrip())