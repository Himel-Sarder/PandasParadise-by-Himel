import pandas as pd

# Creating a sample DataFrame
data = {'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]}

df = pd.DataFrame(data)

# Define a function to calculate the sum of each row
def sum_row(row):
    return row.sum()

# Apply the function row-wise (along axis=1)
row_sum = df.apply(sum_row, axis=1)

print("Sum of each row:")
print(row_sum)

# Define a function to calculate the sum of each column
def sum_column(column):
    return column.sum()

# Apply the function column-wise (along axis=0)
column_sum = df.apply(sum_column, axis=0)

print("\nSum of each column:")
print(column_sum)
