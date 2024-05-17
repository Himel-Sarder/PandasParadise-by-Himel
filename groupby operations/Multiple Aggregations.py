import pandas as pd

# Creating a sample DataFrame
data = {'Category': ['A', 'B', 'A', 'B', 'A'],
        'Value': [10, 20, 30, 40, 50],
        'Count': [1, 2, 3, 4, 5]}

df = pd.DataFrame(data)

# Grouping by 'Category' and applying multiple
# aggregations to 'Value' and 'Count'
result = df.groupby('Category').agg({
    'Value': ['sum', 'mean', 'max'],
    'Count': ['count', 'min']
})
print("Multiple Aggregation: ")
print(result)