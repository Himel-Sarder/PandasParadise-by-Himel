import pandas as pd

# Creating a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Score': [85, 90, 88]}

df = pd.DataFrame(data)

# Descriptive statistics methods in pandas are used to analyze and summarize the data in a DataFrame or Series. These methods provide insights into the distribution, central tendency, and variability of the data. Here are some common descriptive statistics methods in pandas:

# mean(): Calculates the arithmetic mean of numeric data.

df.mean()
# median(): Computes the median of numeric data.

df.median()
# mode(): Finds the mode(s) of each element along the specified axis.

df.mode()
# std(): Computes the standard deviation of numeric data.

df.std()
# var(): Calculates the variance of numeric data.

df.var()
# describe(): Generates descriptive statistics that summarize the central tendency, dispersion, and shape of the dataset's distribution.

df.describe()
# count(): Counts the number of non-null values in each column.

df.count()
# min(): Returns the minimum value in each column.

df.min()
# max(): Returns the maximum value in each column.

df.max()
# quantile(): Computes sample quantiles of the data.

df.quantile(0.25)  # For the first quartile (25th percentile)
# These methods can be applied to both entire DataFrames or individual Series within a DataFrame. They provide valuable insights into the characteristics of your dataset, helping you understand its distribution, central tendency, and variability.