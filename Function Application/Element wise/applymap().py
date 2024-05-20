import pandas as pd

# Creating a sample DataFrame
data = {'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]}

df = pd.DataFrame(data)

def double(x):
    return x * 2

result = df.applymap(double)

print(result)