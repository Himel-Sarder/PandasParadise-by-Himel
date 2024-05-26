import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data
data = {
    'Year': [2000, 2001, 2002, 2003, 2004],
    'A': [1, 2, 3, 4, 5],
    'B': [2, 3, 4, 5, 6],
    'C': [3, 4, 5, 6, 7]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set 'Year' as the index
df.set_index('Year', inplace=True)

# Area plot using pandas
df.plot(kind='area', alpha=0.5)
plt.title('Area Plot using Pandas')
plt.xlabel('Year')
plt.ylabel('Values')
plt.show()

# Extracting data for Matplotlib plot
years = df.index
A = df['A']
B = df['B']
C = df['C']

# Area plot using Matplotlib
plt.figure(figsize=(8, 6))
plt.fill_between(years, A, color='skyblue', alpha=0.5, label='A')
plt.fill_between(years, B, color='lightgreen', alpha=0.5, label='B')
plt.fill_between(years, C, color='salmon', alpha=0.5, label='C')

# Add labels and title
plt.title('Area Plot using Matplotlib')
plt.xlabel('Year')
plt.ylabel('Values')
plt.legend()
plt.show()

# Area plot using Seaborn and Matplotlib
plt.figure(figsize=(8, 6))
sns.set_style("whitegrid")

# Create an area plot for each series
plt.fill_between(years, A, color='skyblue', alpha=0.5, label='A')
plt.fill_between(years, B, color='lightgreen', alpha=0.5, label='B')
plt.fill_between(years, C, color='salmon', alpha=0.5, label='C')

# Add labels and title
plt.title('Area Plot using Seaborn and Matplotlib')
plt.xlabel('Year')
plt.ylabel('Values')
plt.legend()
plt.show()
