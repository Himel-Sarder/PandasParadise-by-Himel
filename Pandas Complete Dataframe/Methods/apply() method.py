import pandas as pd

data = {'Name': ['Himel', 'Antu', 'Kabita'],
        'Math': [50, 75, 80],
        'English': [90, 58, 78]}

df = pd.DataFrame(data)

def calculator(row):
    return row['Math'] + row['English']

df['Total'] = df.apply(calculator, axis=1)

print(df)