import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

# Create a DataFrame
df = pd.DataFrame({'Value': data})

# Histogram using pandas
df.hist(bins=5, color='skyblue', edgecolor='black', linewidth=1.2)
plt.title('Histogram using Pandas')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# Histogram using Matplotlib
plt.figure(figsize=(8, 5))
plt.hist(df['Value'], bins=5, color='lightgreen', edgecolor='black', linewidth=1.2)
plt.title('Histogram using Matplotlib')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Histogram using Seaborn
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x='Value', bins=5, color='salmon', kde=False)
plt.title('Histogram using Seaborn')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
