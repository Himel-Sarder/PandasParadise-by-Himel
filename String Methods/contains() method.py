import pandas as pd

# Creating a sample Series
s = pd.Series(['apple', 'banana', 'chbrry'])

# Check if each string contains 'an'
result = s.str.contains('an')
print(result)

# Check if each string contains a vowel
result2 = s.str.contains('[aeiou]')
print(result2)
