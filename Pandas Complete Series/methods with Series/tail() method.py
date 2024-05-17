import pandas as p

list = [12, 13, 14, 15, 16, 17]

T = p.Series(list)

print(T.tail(3))