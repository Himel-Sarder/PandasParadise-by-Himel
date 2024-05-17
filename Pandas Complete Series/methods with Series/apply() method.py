import pandas as p

list = [12, 13, 14, 15, 16, 17]

value = p.Series(list)

def MulByThree(x):
    result = x * 3
    return result

print(value.apply(MulByThree))