import pandas as pd

# Load the CSV file with specified values treated as NaN
df = pd.read_csv("Automobile_data.csv", na_values={
    'price': ["?", "n.a"],
    'stroke': ["?", "n.a"],
    'horsepower': ["?", "n.a"],
    'peak-rpm': ["?", "n.a"],
    'average-mileage': ["?", "n.a"]
})

# Print the DataFrame to inspect it
print(df)

# Fill NaN values with an empty string or a specific value
df.fillna('', inplace=True)

# Save the cleaned DataFrame to a CSV file in the specified directory
output_dir = "All_Outputs"
output_file = "Output_Exercise_2.csv"
output_path = f"{output_dir}/{output_file}"

# Ensure the output directory exists
import os
os.makedirs(output_dir, exist_ok=True)

# Save the DataFrame to a CSV file
df.to_csv(output_path, index=False)

print(f"Cleaned data saved to {output_path}")
