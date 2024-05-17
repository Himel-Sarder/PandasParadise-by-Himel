import pandas as p

list = [12, 13, 14, 15, 16, 17]

D = p.Series(list)

print(D.describe())