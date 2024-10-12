import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df['calories'])


df = pd.read_csv('data.csv')
print(df.head(10))
# print(df.tail())
# print(df.info())
print(df.loc[range(0,6),'Calories'])