import pandas as pd

# Creating a sample DataFrame
data = {'Category': ['A', 'B', 'A', 'C', 'B', 'C', 'A'],
        'Value': [10, 20, 30, 40, 50, 60, 70],
        'Type': ['X', 'Y', 'X', 'Y', 'X', 'Y', 'X']}

df = pd.DataFrame(data)
df['Category'] = df['Category'].astype('category')
df['Type'] = df['Type'].astype('category')

# Display the data types of the DataFrame
print("\nData Types after Conversion:")
print(df.dtypes)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# You can access properties
# specific to categorical data using
# the cat accessor.


# Accessing the categories
print("\nCategories of 'Category' Column:")
print(df['Category'].cat.categories)

# Accessing the codes
print("\nCodes of 'Category' Column:")
print(df['Category'].cat.codes)


