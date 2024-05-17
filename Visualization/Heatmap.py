import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = {
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8],
    'C': [9, 10, 11, 12],
    'D': [13, 14, 15, 16]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Heatmap using pandas (actually using Matplotlib via imshow)
plt.figure(figsize=(8, 5))
plt.imshow(df, cmap='viridis', aspect='auto')
plt.colorbar(label='Value')
plt.title('Heatmap using Matplotlib (via pandas)')
plt.xlabel('Columns')
plt.ylabel('Rows')
plt.xticks(range(len(df.columns)), df.columns)
plt.yticks(range(len(df)), df.index)
plt.show()

# Heatmap using Matplotlib directly
plt.figure(figsize=(8, 6))
plt.imshow(df.values, cmap='viridis', interpolation='nearest')
plt.colorbar(label='Value')
plt.title('Heatmap using Matplotlib')
plt.xlabel('Columns')
plt.ylabel('Rows')
plt.xticks(range(len(df.columns)), df.columns)
plt.yticks(range(len(df)), df.index)
plt.show()

# Heatmap using Seaborn
plt.figure(figsize=(8, 5))
sns.heatmap(df, cmap='viridis', annot=True, fmt="d")
plt.title('Heatmap using Seaborn')
plt.xlabel('Columns')
plt.ylabel('Rows')
plt.show()
