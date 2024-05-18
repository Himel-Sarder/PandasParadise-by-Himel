import pandas as pd

# Create a DataFrame
data = {
    'Name': ['Himel', 'Abonti', 'Kabita'],
    'Marks': [100, 200, 300],
    'Grade': ['A+', 'A-', 'A']
}

df = pd.DataFrame(data)

NewRow = {'Name': 'Bibhuti', 'Marks': 400, "Grade": "B+"}
df = df.append(NewRow, ignore_index=True)

print(df)