# Aggregation operations in Pandas allow you to compute summary statistics or aggregate values based on rows or columns in a DataFrame. These operations provide insights into the distribution and characteristics of the data. Here are some common aggregation operations you can perform:

# Sum: Compute the sum of values in each column or row.

sum_by_column = df.sum()
sum_by_row = df.sum(axis=2)

print(sum_by_row)
print(sum_by_column)

# Mean: Compute the arithmetic mean (average) of values in each column or row.

mean_by_column = df.mean()
mean_by_row = df.mean(axis=1)


# Median: Compute the median of values in each column or row.

median_by_column = df.median()
median_by_row = df.median(axis=1)


# Minimum: Find the minimum value in each column or row.

min_by_column = df.min()
min_by_row = df.min(axis=1)


# Maximum: Find the maximum value in each column or row.

max_by_column = df.max()
max_by_row = df.max(axis=1)


# Count: Count the number of non-null values in each column or row.

count_by_column = df.count()
count_by_row = df.count(axis=1)


# Standard Deviation: Compute the standard deviation of values in each column or row.

std_by_column = df.std()
std_by_row = df.std(axis=1)


# Variance: Compute the variance of values in each column or row.

var_by_column = df.var()
var_by_row = df.var(axis=1)


# Summarize with describe(): Generate summary statistics for numeric columns.

summary_stats = df.describe()