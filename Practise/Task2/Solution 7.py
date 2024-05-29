import pandas as pd
df = pd.read_csv("D:\\Python\\Articles\\pandas\\automobile-dataset\\Automobile_data.csv")
car_Manufacturers = df.groupby('company')
mileageDf = car_Manufacturers['company','average-mileage'].mean()
print(mileageDf)