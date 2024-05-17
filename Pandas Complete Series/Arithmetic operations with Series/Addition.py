import pandas as pd

A1 = [10, 11, 12, 13, 14]
A2 = [1, 2, 3, 4, 5]

S1 = pd.Series(A1)
S2 = pd.Series(A2)
Add = S1.add(S2)

print(Add)