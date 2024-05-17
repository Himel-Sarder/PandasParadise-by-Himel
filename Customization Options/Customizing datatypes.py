import pandas as pd

# Creating a sample DataFrame
data = {'A': ['1', '2', '3'],
        'B': [4.5, 5.6, 6.7]}

df = pd.DataFrame(data)

# Converting column 'A' to integers
df['A'] = df['A'].astype(int)

# Converting column 'B' to integers
df['B'] = df['B'].astype(int)

print(df.dtypes)






# Converting column 'A' to integers using pd.to_numeric()
df['A'] = pd.to_numeric(df['A'])

print(df.dtypes)






# Creating a sample Series with dates as strings
dates = pd.Series(['2022-01-01', '2022-02-01', '2022-03-01'])

# Converting strings to datetime objects
dates = pd.to_datetime(dates)

print(dates)
