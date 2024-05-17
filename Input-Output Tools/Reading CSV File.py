import pandas as pd

df = pd.read_csv('Samples/Test.csv')

print(df.head(3))
print(df.tail())
print(df.describe())
print(df['Grade'])
