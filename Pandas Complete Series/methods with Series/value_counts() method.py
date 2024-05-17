import pandas as p

list = [12, 13, 14, 15, 16, 17]

valueCount = p.Series(list)

print(valueCount.value_counts())