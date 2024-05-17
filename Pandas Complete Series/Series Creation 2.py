import pandas as pd

Dic = {"Name": "Himel", "Age": 22, "Profession": "Student", "Subject": "CSE"}
DicT = pd.Series(Dic)

print(DicT)

'''
Name            Himel
Age                22
Profession    Student
Subject           CSE
dtype: object
'''