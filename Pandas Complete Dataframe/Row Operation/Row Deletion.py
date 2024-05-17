import pandas as pd

# Create a DataFrame
data = {
    'Name': ['Himel', 'Abonti', 'Kabita'],
    'Marks': [100, 200, 300],
    'Grade': ['A+', 'A-', 'A']
}

df = pd.DataFrame(data)


df.drop(index=2, inplace=True)

print(df)