import pandas as pd

# Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# Access a single column by label
name_column = df['Name']
print(name_column
      )
# Access a single row by label
row_bob = df.loc[1]
print(row_bob)

# Access a subset of rows by labels
rows_bob_charlie = df.loc[1:2]

# Access a subset of rows and specific columns by labels
subset = df.loc[1:2, ['Name', 'Age']]

print(subset)