# In pandas, the query() method is used to filter rows from a DataFrame based on a specified condition expressed as a string.
# This method provides a convenient way to select rows that meet certain criteria without needing to use traditional boolean indexing. Here's how you can use the query() method:

import pandas as pd

# Creating a sample DataFrame
data = {'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50],
        'C': ['a', 'b', 'c', 'd', 'e']}

df = pd.DataFrame(data)

# Using query method to filter rows
result = df.query('A > 2')  # Select rows where column 'A' is greater than 2
print("Rows where A > 2:")
print(result)

'''
Output:

Rows where A > 2:
   A   B  C
2  3  30  c
3  4  40  d
4  5  50  e

# In this example, the query() method is used to filter rows where the values in column 'A' are greater than 2. 
The query expression 'A > 2' is provided as a string, and the method returns a DataFrame containing only the rows that satisfy the condition.

# You can use various operators and logical expressions in the query string, such as >, <, >=, <=, ==, !=, and, or, not, in, not in, etc., to express 
different filtering conditions. The query() method is particularly useful when dealing with large datasets or complex filtering conditions.
'''

# import pandas as pd

# Creating a sample DataFrame
data = {'Product': ['A', 'B', 'C', 'D', 'E'],
        'Price': [100, 150, 200, 250, 300],
        'Quantity': [50, 60, 70, 80, 90]}

df = pd.DataFrame(data)

# Using query method to filter rows
result = df.query('Price > 150 and Quantity < 80')  # Select rows where Price > 150 and Quantity < 80
print("Rows where Price > 150 and Quantity < 80:")
print(result)

'''
Output:

Rows where Price > 150 and Quantity < 80:
  Product  Price  Quantity
3       D    250        80

In this example, we're filtering rows where the price is greater than 150 and the quantity is less than 80. 
The query string 'Price > 150 and Quantity < 80' expresses this condition, and the query() method returns a DataFrame containing only the rows that satisfy both conditions.
'''