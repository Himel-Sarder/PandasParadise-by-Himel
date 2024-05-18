import pandas as pd

# Create a DataFrame
data = {
    'Name': ['Himel', 'Abonti', 'Kabita'],
    'Marks': [100, 200, 300],
    'Grade': ['A+', 'A-', 'A']
}

df = pd.DataFrame(data)

dfHimel = df.loc[0]
dfAbonti = df.loc[1]
dfKabita = df.loc[2]

print(dfHimel)
print(dfAbonti)
print(dfKabita)