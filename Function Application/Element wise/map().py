'''import pandas as pd

# Creating a sample Series
s = pd.Series(['apple', 'banana', 'cherry'])

# Define a mapping dictionary
mapping = {'apple': 'fruit', 'banana': 'fruit', 'cherry': 'fruit'}

# Using map with a dictionary
result_dict = s.map(mapping)
print("Using map with a dictionary:")
print(result_dict)
'''

import pandas as pd
# Define a function
s = pd.Series(['apple', 'banana', 'cherry'])

def classify(fruit):
    if fruit in ['apple', 'banana', 'mango']:
        return 'fruit'
    else:
        return 'Unknown'

result = s.map(classify)
print(result)
