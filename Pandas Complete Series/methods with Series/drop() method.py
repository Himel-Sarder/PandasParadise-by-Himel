import pandas as p

list = [12, 13, 14, 15, 16, 17]

value = p.Series(list)

print(value.drop([1,3,5]))