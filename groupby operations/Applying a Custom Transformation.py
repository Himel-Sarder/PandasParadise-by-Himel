import pandas as pd

# Creating a sample DataFrame
data = {'Category': ['A', 'B', 'A', 'B', 'A'],
        'Value': [10, 20, 30, 40, 50],
        'Count': [1, 2, 3, 4, 5]}

df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Custom transformation:
# Range (max - min) within each group
df['Range'] = \
    (df.groupby('Category')['Value']
     .transform(lambda x: x.max() - x.min()))
print("\nCustom Transformation (Range):")
print(df)
