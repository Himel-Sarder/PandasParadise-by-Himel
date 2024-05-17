import pandas as pd

# Creating a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Score': [85, 90, 88]}

df = pd.DataFrame(data)

# Iterate over the rows of the DataFrame using
# itertuples()

for row in df.itertuples():
    print("Index: ", row.Index)
    print("Name : ", row.Name)
    print("Age :", row.Age)
    print("Score : ", row.Score)
    print()