import pandas as pd

# Creating a sample DataFrame
data = {'Category': ['A', 'B', 'A', 'C', 'B', 'C', 'A'],
        'Value': [10, 20, 30, 40, 50, 60, 70],
        'Type': ['X', 'Y', 'X', 'Y', 'X', 'Y', 'X']}

df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Sorting the DataFrame by the 'Category' column
df_sorted = df.sort_values(by='Category')

print(df_sorted)

# Sorting the DataFrame by the 'Value' column
df_sorted2 = df.sort_values(by='Value')

print(df_sorted2)