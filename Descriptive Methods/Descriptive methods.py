import pandas as pd
import numpy as np

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 45],
    'Salary': [50000, 60000, 70000, 80000, 90000],
    'Score': [85, 90, 78, 88, 95]
}

df = pd.DataFrame(data)

# describe(): Generates descriptive statistics of the DataFrame.

print(df.describe())

# mean(): Calculates the mean of each numerical column.

print(df.mean())

# median(): Calculates the median of each numerical column.

print(df.median())

# mode(): Finds the mode of each column.

print(df.mode())

# std(): Calculates the standard deviation of each numerical column.

print(df.std())

# var(): Calculates the variance of each numerical column.

print(df.var())

# min(): Finds the minimum value for each numerical column.

print(df.min())

# max(): Finds the maximum value for each numerical column.

print(df.max())

# sum(): Calculates the sum of each numerical column.

print(df.sum())

# count(): Counts the number of non-null entries in each column.

print(df.count())

# quantile(): Calculates the quantiles of each numerical column.

print(df.quantile([0.25, 0.5, 0.75]))

# cumsum(): Calculates the cumulative sum of each numerical column.

print(df.cumsum())

# cumprod(): Calculates the cumulative product of each numerical column.

print(df.cumprod())

# skew(): Calculates the skewness of each numerical column.

print(df.skew())

# kurt(): Calculates the kurtosis of each numerical column.

print(df.kurt())

# mad(): Calculates the mean absolute deviation of each numerical column.

print(df.mad())

# prod(): Calculates the product of each numerical column.

print(df.prod())

# sem(): Calculates the standard error of the mean of each numerical column.

print(df.sem())

# nunique(): Counts the number of unique values in each column.

print(df.nunique())

# idxmin(): Finds the index of the first occurrence of the minimum value in each column.

print(df.idxmin())

# idxmax(): Finds the index of the first occurrence of the maximum value in each column.

print(df.idxmax())

# diff(): Calculates the difference between each element and its predecessor.

print(df.diff())

# pct_change(): Calculates the percentage change between each element and its predecessor.

print(df.pct_change())

# corr(): Calculates the correlation matrix of the DataFrame's numerical columns.

print(df.corr())

# cov(): Calculates the covariance matrix of the DataFrame's numerical columns.

print(df.cov())