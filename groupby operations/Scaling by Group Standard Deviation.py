import pandas as pd

# Creating a sample DataFrame
data = {'Category': ['A', 'B', 'A', 'B', 'A'],
        'Value': [10, 20, 30, 40, 50],
        'Count': [1, 2, 3, 4, 5]}

df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Scaling by the standard deviation of each group
df['Value_scaled'] = \
        (df.groupby('Category')['Value']
         .transform(lambda x: x / x.std()))
print("\nScaled by Group Standard Deviation:")
print(df)
