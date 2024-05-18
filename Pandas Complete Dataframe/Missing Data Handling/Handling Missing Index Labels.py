# reindex(): Reindexes the DataFrame with missing index labels, optionally filling missing values.
# df.reindex(new_index)  # Reindex with new index labels
# df.reindex(new_index, fill_value=0)  # Fill missing values with a specified value


import pandas as pd

# Create a DataFrame
data = {'A': [1, 2, 3]}
df = pd.DataFrame(data)

# Reindex with new index labels
new_index = [0, 1, 2, 3]
df_reindexed = df.reindex(new_index)
print("DataFrame after reindexing without fill_value:")
print(df_reindexed)

# Reindex with new index labels and fill missing values with 0
df_reindexed_fill = df.reindex(new_index, fill_value=0)
print("\nDataFrame after reindexing with fill_value=0:")
print(df_reindexed_fill)
