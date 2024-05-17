import pandas as pd

# Creating a sample DataFrame
data = {'A': [1.123456789, 2.987654321, 3.555555555, 4.7777777],
        'B': [4.123456789, 5.987654321, 6.555555555, 8.4444444],
        'C': [7.123456789, 8.987654321, 9.555555555, 3.2222222]}

df = pd.DataFrame(data)

# Setting display options
pd.set_option('display.max_rows', 3)  # Maximum number of rows to display
pd.set_option('display.max_columns', 2)  # Maximum number of columns to display
pd.set_option('display.width', 80)  # Maximum width of the display
pd.set_option('display.precision', 2)  # Number of digits of precision for floating-point numbers

# Displaying the DataFrame
print("DataFrame with customized display options:")
print(df)

# Resetting display options to default
pd.reset_option('display.max_rows')
pd.reset_option('display.max_columns')
pd.reset_option('display.width')
pd.reset_option('display.precision')

print(df)