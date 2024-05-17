import pandas as pd

# Create a DataFrame
data = {
    'Name': ['Himel', 'Abonti', 'Kabita'],
    'Marks': [100, 200, 300],
    'Grade': ['A', 'B', 'C']
}

df = pd.DataFrame(data)

# Delete the 'Grade' column
df.drop('Grade', axis=1, inplace=True)

print(df)
