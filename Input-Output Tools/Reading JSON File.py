import pandas as pd

# Read JSON file
with open("Samples/Test4.json", 'r') as file:
    data = file.read()
    df = pd.read_json(data)

# Display the DataFrame
print(df.head())
