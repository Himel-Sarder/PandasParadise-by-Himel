import pandas as pd

# Creating a sample DataFrame
data = {'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]}

df = pd.DataFrame(data)


def add_one(df):
    return df + 1

def multiply_by_two(df):
    return df * 2

# Chain the custom functions using pipe()
result = df.pipe(add_one).pipe(multiply_by_two)

print("Result after chaining custom functions:")
print(result)