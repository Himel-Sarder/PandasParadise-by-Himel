import pandas as pd

# Read the CSV file
data = pd.read_csv("2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")

# Count squirrels based on their primary fur color
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

# Print the counts
print(grey_squirrels_count)
print(cinnamon_squirrels_count)
print(black_squirrels_count)

# Create a dictionary with the fur color counts
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data_dict)

# Save the DataFrame to a CSV file
df.to_csv("squirrel_count.csv", index=False)
