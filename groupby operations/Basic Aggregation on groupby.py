import pandas as pd

# Creating a sample DataFrame
data = {'Category': ['A', 'B', 'A', 'B', 'A'],
        'Value': [10, 20, 30, 40, 50],
        'Count': [1, 2, 3, 4, 5]}

df = pd.DataFrame(data)

# Grouping by 'Category' and calculating
# the sum of 'Value' and 'Count'
result1 = df.groupby('Category').sum()
print(result1)

# Grouping by 'Category' and calculating
# the mean of 'Value' and 'Count'
result2 = df.groupby('Category').mean()
print(result2)

# Grouping by 'Category' and calculating
# the count of 'Value' and 'Count'
result3 = df.groupby('Category').count()
print(result3)
