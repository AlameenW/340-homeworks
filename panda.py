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
pclass = pd.Series([4,2,3,3,2,3])
pas = pd.DataFrame()
pas = pd.concat([age_12,age_teen,pclass],axis=1)
pas.columns = ['Age_Teen','Age_12','Pclass']
pas.index = [1,3,5,0,10,22]
# pas.dropna(subset=['Age_Teen'],inplace=True)
# print(pas)
# iloc enables access with index number regardless of label
# print(pas.groupby(['Age_12']).Pclass.median())

# print(data.iloc[0].mode())

df = pd.DataFrame({
  'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob'],
  'City': ['New York', 'London', 'New York', 'London', 'Tokyo'],
  'Sales': [100, 200, 150, 120, 250]
})
grouped = df.groupby('City')
print(grouped.get_group('New York').Sales.mean())
for city,group in grouped:
  group['City'] = group['City'].apply(lambda x: x+('City'))
  group['City'] = group['City'].apply(lambda x: x.replace('City','.'))
  print(group)
# for city,group in grouped:
  
df = pd.DataFrame()
col1 = [x**2 for x in range(1,5)]
col2 = ['Red','Yellow','Blue','Green']
pd.concat([col1,col2],axis=1)
