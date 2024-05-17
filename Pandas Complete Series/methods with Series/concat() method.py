import pandas as p
list1 = [16, 11, 14, 12, 15, 13]
list2 = [12, 11, 14, 11, 10, 16]

value1 = p.Series(list1)
value2 = p.Series(list2)

new = p.concat([value1, value2], ignore_index=True)
print(new)