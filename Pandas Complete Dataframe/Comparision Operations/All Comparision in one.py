# 1. Element-wise Equality (`==`):

   # result = df1 == df2


# 2. Element-wise Inequality (`!=`):

   # result = df1 != df2


# 3. Element-wise Greater Than (`>`):

   # result = df1 > df2


# 4. Element-wise Greater Than or Equal To (`>=`):

   # result = df1 >= df2


# 5. Element-wise Less Than (`<`):

   # result = df1 < df2


# 6. Element-wise Less Than or Equal To (`<=`):

   # result = df1 <= df2


# 7. Element-wise Operations with Scalars:

   # result = df > scalar_value

import pandas as pd

# Create a DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# Perform comparison with a scalar value
result = df > 2

print(result)
