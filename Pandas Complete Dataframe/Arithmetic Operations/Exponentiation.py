import pandas as pd

# Create a DataFrame
data = {
    'Name': ['Himel', 'Abonti', 'Kabita'],
    'Marks': [5, 2, 300],
    'Grade': ['A+', 'A-', 'A'],
    'Subject': ['CSE', 'EEE', 'Math']
}

df = pd.DataFrame(data)

df["Marks"] =df["Marks"] ** 5

print(df)


import pandas as pd

# Create two DataFrames
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# Perform addition
result = df1 ** df2

print(result)
