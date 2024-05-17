import pandas as p

list = [16, 11, 14, 12, 15, 13]

Sortvalue = p.Series(list)

print(Sortvalue.sort_values())



list = [16, 11, 14, 12, 15, 13]

Sortvalue2 = p.Series(list)

print(Sortvalue2.sort_values(ascending=False))