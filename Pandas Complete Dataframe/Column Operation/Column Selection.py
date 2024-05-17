import pandas as pd

# Create a DataFrame
data = {
    'Name': ['Himel', 'Abonti', 'Kabita'],
    'Marks': [100, 200, 300]
}

df = pd.DataFrame(data)

# Using bracket notation
name_column = df['Name']
print(name_column)

# Using dot notation (only works if column names don't have spaces or special characters)
marks_column = df.Marks
print(marks_column)
