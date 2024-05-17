import pandas as pd

# Sample data
data = {
    'Name': ['John', 'Alice', 'Bob', 'Emma'],
    'Age': [23, 30, 25, 22],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

# Create a DataFrame
df = pd.DataFrame(data)

path = "Output/output2.xlsx"

df.to_excel(path, sheet_name="Sheet2", index=False)

print("Completed....")