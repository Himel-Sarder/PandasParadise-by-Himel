import pandas as pd

# Create a DataFrame
data = {
    'Name': ['Himel', 'Abonti', 'Kabita'],
    'Marks': [100, 200, 300],
    'Grade': ['A+', 'A-', 'A'],
    'Subject': ['CSE', 'EEE', 'Math']
}

df = pd.DataFrame(data)

df["Marks"] =df["Marks"] / 100

print(df)






# Create two DataFrames
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = pd.DataFrame({'A': [10, 20, 30], 'B': [40, 50, 60]})

# Perform addition
result = df1 / df2

print(result)
