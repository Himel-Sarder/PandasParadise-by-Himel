import pandas as pd
import numpy as np

# Creating a sample DataFrame with missing values
data = {'Name': ['Alice', 'Bob', np.nan, 'David'],
        'Age': [25, np.nan, 35, 40],
        'Score': [85, 90, np.nan, np.nan]}

df = pd.DataFrame(data)

# Displaying the original DataFrame
print("Original DataFrame:")
print(df)

# Dropping rows with any NaN values
df_without_nan_rows = df.dropna()
print("\nDataFrame after dropping rows with NaN values:")
print(df_without_nan_rows)

# Dropping columns with any NaN values
df_without_nan_cols = df.dropna(axis=1)
print("\nDataFrame after dropping columns with NaN values:")
print(df_without_nan_cols)
