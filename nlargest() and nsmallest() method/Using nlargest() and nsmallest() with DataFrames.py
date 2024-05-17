import pandas as pd

# Creating a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
        'Age': [25, 30, 35, 40, 35],
        'Score': [85, 90, 88, 92, 87]}

df = pd.DataFrame(data)

# Retrieve top 3 rows with the largest values in the 'Score' column
top_3_scores = df.nlargest(3, 'Score')
print("Top 3 rows with the largest scores:")
print(top_3_scores)

# Retrieve top 2 rows with the smallest values in the 'Age' column
top_2_youngest = df.nsmallest(2, 'Age')
print("\nTop 2 rows with the smallest ages:")
print(top_2_youngest)
