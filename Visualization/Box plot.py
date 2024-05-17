# Sample data
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'Category': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
    'Value': [10, 15, 14, 22, 21, 20, 30, 35, 32]
}

df = pd.DataFrame(data)

# Basic box plot
df.boxplot(column='Value', by='Category')
plt.title('Basic Box Plot')
plt.suptitle('')  # Suppress the automatic title to make it cleaner
plt.xlabel('Category')
plt.ylabel('Value')
plt.show()

# Customizing the box plot
plt.figure(figsize=(10, 6))
df.boxplot(column='Value', by='Category', grid=False, patch_artist=True,
           boxprops=dict(facecolor='lightblue', color='blue'),
           medianprops=dict(color='red'))
plt.title('Customized Box Plot')
plt.suptitle('')
plt.xlabel('Category')
plt.ylabel('Value')
plt.show()

# Advanced box plot using Seaborn
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Category', y='Value', palette='Set3')
plt.title('Advanced Box Plot with Seaborn')
plt.xlabel('Category')
plt.ylabel('Value')
plt.show()
