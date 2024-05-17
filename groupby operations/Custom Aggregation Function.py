import pandas as pd

# Creating a sample DataFrame
data = {'Category': ['A', 'B', 'A', 'B', 'A'],
        'Value': [10, 20, 30, 40, 50],
        'Count': [1, 2, 3, 4, 5]}

df = pd.DataFrame(data)
# Custom aggregation function to
# calculate the range (max - min)
def value_range(x):
    return x.max() -x.min()

result = df.groupby('Category').agg({
    'Value': value_range,
    'Count': 'sum'
})
print(result)