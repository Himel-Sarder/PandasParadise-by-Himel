import pandas as pd
import matplotlib.pyplot as plt


data = {
    'Category': ['A', 'B', 'A', 'C', 'B', 'C', 'A'],
    'Value': [10, 40, 25, 65, 35, 25, 70],
    'Count': [1, 2, 3, 4, 5, 6, 7]
}

df = pd.DataFrame(data)

df.plot(x='Count', y='Value', kind='line', marker='o')
plt.title('Value Trend Over Count')
plt.xlabel('Count')
plt.ylabel('Value')
plt.grid(True)
plt.show()

# Customizing the line plot
plt.figure(figsize=(10,6))
plt.plot(df['Count'], df['Value'], marker='o',linestyle='-', color='r', label='Value')
plt.title('Customized Line Plot of Value Trend Over Count')
plt.xlabel('Count')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()