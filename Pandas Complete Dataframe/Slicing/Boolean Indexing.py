import pandas as pd

# Create a DataFrame
data = {
    'Name': ['Himel', 'Abonti', 'Kabita'],
    'Marks': [100, 200, 300],
    'Grade': ['A+', 'A-', 'A'],
    'Subject': ['CSE', 'EEE', 'Math']
}

df = pd.DataFrame(data)

# Boolean indexing to filter rows based on a condition
filtered_rows = df[df['Marks'] > 200]

print(filtered_rows)
