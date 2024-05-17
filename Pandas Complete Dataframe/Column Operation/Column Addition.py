import pandas as pd

# Create a DataFrame
data = {
    'Name': ['Himel', 'Abonti', 'Kabita'],
    'Marks': [100, 200, 300]
}

df = pd.DataFrame(data)

# Add a new column called 'Grade'
df['Grade'] = ['A', 'B', 'C']

print(df)
