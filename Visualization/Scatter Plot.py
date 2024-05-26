import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample DataFrame for scatter plot
data = {
    'X': [1, 2, 3, 4, 5],
    'Y': [10, 15, 12, 18, 20]
}

df = pd.DataFrame(data)

# Scatter plot using pandas
df.plot(kind='scatter', x='X', y='Y', title='Scatter Plot using Pandas')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

# Scatter plot using Matplotlib
plt.figure(figsize=(8, 5))
plt.scatter(df['X'], df['Y'], color='red', label='Data Points')
plt.title('Scatter Plot using Matplotlib')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

# Scatter plot using Seaborn
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='X', y='Y')
plt.title('Scatter Plot using Seaborn')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
