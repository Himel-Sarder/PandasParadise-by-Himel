import pandas as pd

# Creating a sample DataFrame with time-series data
data = {'date': pd.date_range(start='2022-01-01', periods=10),
        'value': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]}

df = pd.DataFrame(data)

# Applying a rolling window operation to calculate the rolling mean
window_size = 3
rolling_mean = df['value'].rolling(window=window_size).mean()

# Adding the rolling mean as a new column in the DataFrame
df['rolling_mean'] = rolling_mean

print(df)
