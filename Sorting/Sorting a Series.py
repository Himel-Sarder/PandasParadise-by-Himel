import pandas as pd

# Creating a sample Series
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35]}

s = pd.Series(data['Age'], index=data['Name'])

# Sort Series by values
sorted_values = s.sort_values()
print("Sorted Series by values:")
print(sorted_values)

# Sort Series by index
sorted_index = s.sort_index()
print("\nSorted Series by index:")
print(sorted_index)
