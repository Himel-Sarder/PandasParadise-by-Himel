import pandas as pd

# Creating a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily', 'Frank', 'Grace'],
        'Age': [25, 30, 35, 40, 28, 33, 38],
        'Score': [85, 90, 88, 92, 87, 85, 89]}

df = pd.DataFrame(data)

# Using head() to view the first few rows (default is 5 rows)
print("First few rows:")
print(df.head())

# Using tail() to view the last few rows (default is 5 rows)
print("\nLast few rows:")
print(df.tail())
