import pandas as p

list = [12, 13, 14, 15, 16, 17, 12, 14, 16]

uni = p.Series(list)

print(uni.unique())