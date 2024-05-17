import pandas as pd

# Path to the HTML file
input_path = "Samples/Test5.html"

# Read HTML file into a list of DataFrames
dataframes = pd.read_html(input_path)

# Display the first DataFrame (assuming the HTML file contains tables)
df = dataframes[0]
print(df)
