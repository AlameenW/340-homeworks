import pandas as pd
a = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
data = pd.read_csv('data.csv')
data.dtypes = data.astype(float)
# print(data.iloc[:5])
# data['Kcal'] = data['Duration']*data['Calories']
# data.Duration.apply(lambda x: x.replace('Time: x'))
data['Duration'] = data['Duration'].apply(lambda x: x+10)
# print(data.iloc[:5,-3:])
print(data.Calories.mean())
