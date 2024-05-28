import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Path to save the CSV file
file_path = 'output.csv'

# Write DataFrame to CSV file
df.to_csv(file_path, index=False)

print(f'DataFrame has been written to {file_path}')

