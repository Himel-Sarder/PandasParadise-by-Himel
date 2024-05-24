import pandas as pd

# Creating a sample Series
data = {'Alice': 85, 'Bob': 90, 'Charlie': 88, 'David': 92, 'Emily': 87}

s = pd.Series(data)

# Retrieve top 3 items with the largest values
top_3_largest = s.nlargest(3)
print("Top 3 items with the largest values:")
print(top_3_largest)

# Retrieve top 2 items with the smallest values
top_2_smallest = s.nsmallest(2)
print("\nTop 2 items with the smallest values:")
print(top_2_smallest)
