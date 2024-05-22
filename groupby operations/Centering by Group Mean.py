import pandas as pd

# Creating a sample DataFrame
data = {'Category': ['A', 'B', 'A', 'B', 'A'],
        'Value': [10, 20, 30, 40, 50],
        'Count': [1, 2, 3, 4, 5]}

df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Subtracting the mean of each group from
# the group's values
df['Value_centered'] = (df.groupby('Category')['Value'].transform(lambda x: x - x.mean()))
print("\nCentered by Group Mean:")
print(df)
