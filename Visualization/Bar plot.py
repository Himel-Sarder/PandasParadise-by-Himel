import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample DataFrame for basic and customized bar plot
data = {
    'Category': ['A', 'B', 'C', 'D', 'E', 'F'],
    'Value': [10, 20, 15, 25, 30, 5]
}

df = pd.DataFrame(data)

# Basic bar plot
df.plot(kind='bar', x='Category', y='Value')
plt.title('Basic Bar Plot')
plt.xlabel('Category')
plt.ylabel('Value')
plt.show()

# Customizing the bar plot
plt.figure(figsize=(8, 5))
plt.bar(df['Category'], df['Value'], color='skyblue')
plt.title('Customized Bar Plot')
plt.xlabel('Category')
plt.ylabel('Value')
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.show()

# Advanced bar plot using Seaborn
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x='Category', y='Value', palette='viridis')
plt.title('Advanced Bar Plot with Seaborn')
plt.xlabel('Category')
plt.ylabel('Value')
plt.show()