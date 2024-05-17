import pandas as pd

# Creating a sample DataFrame
data = {'Category': ['A', 'B', 'A', 'C', 'B', 'C', 'A'],
        'Value': [10, 20, 30, 40, 50, 60, 70],
        'Type': ['X', 'Y', 'X', 'Y', 'X', 'Y', 'X']}

df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

df['Category'] = df['Category'].astype('category')
df['Type'] = df['Type'].astype('category')

# Display the data types of the DataFrame
print("\nData Types after Conversion:")
print(df.dtypes)
