import pandas as p

List = [12, None, None, 15, 16, None]

value = p.Series(List)

print(value.fillna("Himel"))