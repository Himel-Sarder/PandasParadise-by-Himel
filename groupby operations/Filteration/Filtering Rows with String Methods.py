import pandas as pd

# Creating a sample DataFrame
data = {'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
        'Value': [10, 20, 30, 40, 50, 60],
        'Count': [1, 2, 3, 4, 5, 6]}

df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Filter rows where the Category
# starts with 'A'.

filtered_df = df[df['Category'].str.startswith('A')]

print(filtered_df)