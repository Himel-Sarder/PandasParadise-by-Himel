import pandas as p

Data = (["Himel", 100, "CSE"],["Abonti", 200, "Physics"], ["Kabita", 300, "EEE"])

col = ["Name", "Marks", "Department"]

DataF = p.DataFrame(Data, columns=col)

print(DataF)

'''
     Name  Marks Department
0   Himel    100        CSE
1  Abonti    200    Physics
2  Kabita    300        EEE
'''