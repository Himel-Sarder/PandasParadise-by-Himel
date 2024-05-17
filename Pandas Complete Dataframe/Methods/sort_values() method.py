import pandas as pd

# Creating a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'Score': [85, 90, 88, 92]}

df = pd.DataFrame(data)

# Sorting by a single column
df_sorted_by_age = df.sort_values(by='Age')  # Sort by Age column
print("Sorted by Age:")
print(df_sorted_by_age)

# Sorting by multiple columns
df_sorted_by_multiple = df.sort_values(by=['Age', 'Score'], ascending=[True, False])
# Sort by Age in ascending order, then by Score in descending order
print("\nSorted by Age and Score:")
print(df_sorted_by_multiple)
