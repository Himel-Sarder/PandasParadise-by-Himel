import pandas as pd

# Creating a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Score': [85, 90, 88]}

df = pd.DataFrame(data)

# Iterate over the rows of the DataFrame
for index, row in df.iterrows():
    print("Index:", index)
    print("Row data:")
    print(row)
    print()
