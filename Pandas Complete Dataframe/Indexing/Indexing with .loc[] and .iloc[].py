import pandas as pd

# Create a DataFrame
data = {
    'Name': ['Himel', 'Abonti', 'Kabita'],
    'Marks': [100, 200, 300],
    'Grade': ['A+', 'A-', 'A'],
    'Subject': ['CSE', 'EEE', 'Math']
}

df = pd.DataFrame(data)

# Using .loc[] for label-based indexing
abontiRow = df.loc[1]
subset = df.loc[1:2, ['Name', 'Marks']]

print(abontiRow)
print(subset)

# Using .iloc[] for integer-based indexing
kabitaRow = df.iloc[1]
subset = df.iloc[1:3, 0:2]  # Rows 1 and 2, columns 0 and 1

print(kabitaRow)
print(subset)