import pandas as pd
import numpy as np

# Creating a sample DataFrame with missing values
data = {'Name': ['Alice', 'Bob', np.nan, 'David'],
        'Age': [25, np.nan, 35, 40],
        'Score': [85, 90, np.nan, np.nan]}

df = pd.DataFrame(data)

# Filling missing values with a specified value
df_filled = df.fillna(value=0)  # Fill NaN with 0
print("DataFrame after filling missing values:")
print(df_filled)
