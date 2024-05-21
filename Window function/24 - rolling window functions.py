import pandas as pd

# Creating a sample DataFrame with time-series data
data = {'date': pd.date_range(start='2022-01-01', periods=10),
        'value': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]}

df = pd.DataFrame(data)




# 1. Rolling Sum
rolling_sum = df['value'].rolling(window=3).sum()
print("Rolling Sum:")
print(rolling_sum)




# 2. Rolling Mean
rolling_mean = df['value'].rolling(window=3).mean()
print("\nRolling Mean:")
print(rolling_mean)




# 3. Rolling Median
rolling_median = df['value'].rolling(window=3).median()
print("\nRolling Median:")
print(rolling_median)




# 4. Rolling Minimum
rolling_min = df['value'].rolling(window=3).min()
print("\nRolling Minimum:")
print(rolling_min)




# 5. Rolling Maximum
rolling_max = df['value'].rolling(window=3).max()
print("\nRolling Maximum:")
print(rolling_max)




# 6. Rolling Variance
rolling_variance = df['value'].rolling(window=3).var()
print("\nRolling Variance:")
print(rolling_variance)




# 7. Rolling Standard Deviation
rolling_std = df['value'].rolling(window=3).std()
print("\nRolling Standard Deviation:")
print(rolling_std)




# 8. Apply Custom Function
def custom_function(x):
    return x.max() - x.min()

rolling_custom = df['value'].rolling(window=3).apply(custom_function)
print("\nRolling Custom Function (Max - Min):")
print(rolling_custom)




# 9. Exponential Moving Average (EMA)
ema = df['value'].ewm(span=3, adjust=False).mean()
print("\nExponential Moving Average (EMA):")
print(ema)




# 10. Rolling Count
rolling_count = df['value'].rolling(window=3).count()
print("Rolling Count:")
print(rolling_count)




# 11. Rolling Skewness
rolling_skew = df['value'].rolling(window=3).skew()
print("\nRolling Skewness:")
print(rolling_skew)




# 12. Rolling Kurtosis
rolling_kurtosis = df['value'].rolling(window=3).kurt()
print("\nRolling Kurtosis:")
print(rolling_kurtosis)




# 13. Rolling Covariance
rolling_covariance = df['value'].rolling(window=3).cov(df['value'].shift(-1))
print("\nRolling Covariance:")
print(rolling_covariance)




# 14. Rolling Correlation
rolling_correlation = df['value'].rolling(window=3).corr(df['value'].shift(-1))
print("\nRolling Correlation:")
print(rolling_correlation)




# 15. Rolling Apply with a Custom Function (e.g., Moving Average)
rolling_ma = df['value'].rolling(window=3).apply(lambda x: x.mean())
print("\nRolling Moving Average:")
print(rolling_ma)




# 16. Rolling Quantile
rolling_quantile = df['value'].rolling(window=3).quantile(0.5)  # 50th percentile
print("\nRolling Quantile (50th Percentile):")
print(rolling_quantile)




# 17. Rolling Exponential Weighted Mean (EWMA)
ewma = df['value'].ewm(span=3).mean()
print("\nExponential Weighted Moving Average (EWMA):")
print(ewma)




# 18. Rolling Sum of Squares
rolling_sum_sq = df['value'].rolling(window=3).apply(lambda x: (x**2).sum())
print("Rolling Sum of Squares:")
print(rolling_sum_sq)




# 19. Rolling Exponential Weighted Covariance
rolling_ewm_cov = df['value'].ewm(span=3).cov(df['value'].shift(-1))
print("\nRolling Exponential Weighted Covariance:")
print(rolling_ewm_cov)




# 20. Rolling Exponential Weighted Correlation
rolling_ewm_corr = df['value'].ewm(span=3).corr(df['value'].shift(-1))
print("\nRolling Exponential Weighted Correlation:")
print(rolling_ewm_corr)




# 21. Rolling Quantile with Custom Quantile Values
rolling_custom_quantile = df['value'].rolling(window=3).quantile([0.25, 0.75])  # 25th and 75th percentiles
print("\nRolling Custom Quantiles (25th and 75th Percentiles):")
print(rolling_custom_quantile)




# 22. Rolling Exponential Weighted Standard Deviation
rolling_ewm_std = df['value'].ewm(span=3).std()
print("\nRolling Exponential Weighted Standard Deviation:")
print(rolling_ewm_std)




# 23. Rolling Exponential Weighted Variance
rolling_ewm_var = df['value'].ewm(span=3).var()
print("\nRolling Exponential Weighted Variance:")
print(rolling_ewm_var)




# 24. Rolling Quantile with Custom Quantile Function
def custom_quantile(x):
    return x.quantile(0.25)

rolling_custom_quantile_func = df['value'].rolling(window=3).apply(custom_quantile)
print("\nRolling Quantile with Custom Quantile Function (25th Percentile):")
print(rolling_custom_quantile_func)