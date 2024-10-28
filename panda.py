import pandas as pd
a = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
data = pd.read_csv('data.csv')
# data.dtypes = data.astype(float)

# print(data.iloc[:3,:2])
# data['Duration'] = data['Duration'].apply(lambda x: x+10)
# print(data.Calories.mean())

age_12 = pd.Series([None,2.0,4.0,2.0,4.0,2.0])
age_teen = pd.Series([None,7.0,None,14.0,None,7.0])
pclass = pd.Series([3,2,3,3,2,3])
pas = pd.DataFrame()
pas = pd.concat([age_12,age_teen,pclass],axis=1)
pas.columns = ['Age_Teen','Age_12','Pclass']
pas.index = [1,3,5,0,10,22]
# print(pas.iloc[:3,:3])
# iloc enables access with index number regardless of label
# print(pas.groupby(['Age_12']).Pclass.median())

# print(data.iloc[0].mode())