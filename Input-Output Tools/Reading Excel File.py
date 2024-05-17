import pandas as pd

path = "Samples/Test3.xlsx"

df = pd.read_excel(path,
                   sheet_name="Employee Sample Data")

print(df.head())
