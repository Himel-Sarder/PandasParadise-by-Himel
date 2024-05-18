# Create a DataFrame
import pandas as pd
data = {
    'Name': ['Himel', 'Abonti', 'Kabita'],
    'Marks': [100, 200, 300],
    'Grade': ['A+', 'A-', 'A'],
    'Subject': ['CSE', 'EEE', 'Math']
}

df = pd.DataFrame(data)

# Slice rows by positional indices
subset_rows = df[1:3]

print(subset_rows)