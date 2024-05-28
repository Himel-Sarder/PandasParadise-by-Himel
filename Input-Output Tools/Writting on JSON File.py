import pandas as pd
import json

# Create a sample DataFrame
data = {
    'Name': ['John', 'Alice', 'Bob'],
    'Age': [30, 25, 28],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# Convert DataFrame to JSON string
json_str = df.to_json(orient='records', indent=4)

# Path to the JSON file where you want to write the data
output_path = "Output/output3.json"

# Write JSON string to file
with open(output_path, 'w') as file:
    file.write(json_str)

print(f"DataFrame written to {output_path}")
