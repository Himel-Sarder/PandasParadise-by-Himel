import pandas as pd

# Create a dictionary of Series
data = {
    'Name': pd.Series(['Himel', 'Abonti', 'Kabita']),
    'Marks': pd.Series([100, 200, 300])
}

# Create a DataFrame from the dictionary
data_frame = pd.DataFrame(data)

print(data_frame)
