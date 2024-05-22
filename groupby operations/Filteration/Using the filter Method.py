import pandas as pd

# Creating a sample DataFrame
data = {'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
        'Value': [10, 20, 30, 40, 50, 60],
        'Count': [1, 2, 3, 4, 5, 6]}

df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

filtered_df = df.filter(items=['Category', 'Count'])

print(filtered_df)

