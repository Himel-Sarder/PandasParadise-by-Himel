import pandas as pd

# Creating a sample DataFrame with time-series data
data = {'date': pd.date_range(start='2022-01-01', periods=10),
        'value': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]}

df = pd.DataFrame(data)




# 1. Expanding sum
expanding_sum = df['value'].expanding().sum()
print("Expanding Sum:")
print(expanding_sum)




# 2. Expanding mean
expanding_mean = df['value'].expanding().mean()
print("\nExpanding Mean:")
print(expanding_mean)




# 3. Expanding maximum
expanding_max = df['value'].expanding().max()
print("\nExpanding Maximum:")
print(expanding_max)




# 4. Expanding minimum
expanding_min = df['value'].expanding().min()
print("\nExpanding Minimum:")
print(expanding_min)



# 5. Expanding Standard Deviation
expanding_std = df['value'].expanding().std()
print("\nExpanding Standard Deviation:")
print(expanding_std)




# 6. Expanding Variance
expanding_var = df['value'].expanding().var()
print("\nExpanding Variance:")
print(expanding_var)




# 7. Expanding Count
expanding_count = df['value'].expanding().count()
print("\nExpanding Count:")
print(expanding_count)




# 8. Expanding Skewness
expanding_skew = df['value'].expanding().skew()
print("\nExpanding Skewness:")
print(expanding_skew)




# 9. Expanding Kurtosis
expanding_kurt = df['value'].expanding().kurt()
print("\nExpanding Kurtosis:")
print(expanding_kurt)




# 10. Custom Expanding Function
def custom_expanding_function(x):
    return x.max() - x.min()

expanding_custom = df['value'].expanding().apply(custom_expanding_function)
print("\nCustom Expanding Function (Max - Min):")
print(expanding_custom)