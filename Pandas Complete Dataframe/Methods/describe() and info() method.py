import pandas as pd

# Creating a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily', 'Frank', 'Grace'],
        'Age': [25, 30, 35, 40, 28, 33, 38],
        'Score': [85, 90, 88, 92, 87, 85, 89]}

df = pd.DataFrame(data)

# Using info() to get details about the DataFrame
print("DataFrame Info:")
print(df.info())

# Using describe() to get descriptive statistics about the DataFrame's columns
print("\nDataFrame Descriptive Statistics:")
print(df.describe())
