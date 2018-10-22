import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression
from scipy.stats import mode

df_train = pd.read_csv('Train.csv')
df_test = pd.read_csv('Test.csv')
headers = ['Item_Identifier','Item_Weight','Item_Fat_Content','Item_Visibility','Item_Type','Item_MRP','Outlet_Identifier','Outlet_Establishment_Year','Outlet_Size','Outlet_Location_Type','Outlet_Type','Item_Outlet_Sales']
df_train.columns = headers
df_test.columns = headers[:11]


df_train['source'] = 'Train'
df_test['source'] = 'Test'

df = pd.concat([df_train,df_test],ignore_index=True,sort=False)

df['Item_Visibility'].replace(0,df['Item_Visibility'].mean(),inplace=True)
df['Item_Weight'].fillna(df['Item_Weight'].mean(),inplace=True)

df['Item_Fat_Content'].replace('reg','Regular',inplace=True)
df['Item_Fat_Content'].replace('low fat','Low Fat',inplace=True)
df['Item_Fat_Content'].replace('LF','Low Fat',inplace=True)

#Finding Outlet Size using Mode

outlet_size_mode = df.pivot_table(values='Outlet_Size',columns='Outlet_Type',aggfunc=(lambda x: x.mode().iat[0]))
miss_bool = df['Outlet_Size'].isnull()
df.loc[miss_bool,'Outlet_Size'] = df.loc[miss_bool,'Outlet_Type'].apply(lambda x: outlet_size_mode[x])

# building model

dummies = ['Item_Fat_Content','Item_Type','Outlet_Location_Type','Outlet_Size','Outlet_Type']

df = pd.get_dummies(df,columns=dummies)


df.drop(['Outlet_Identifier','Item_Identifier'],axis=1,inplace=True)


Train = df.loc[df['source']=='Train']
Test = df.loc[df['source']=='Test']

Train.drop('source',axis=1,inplace=True)
Test.drop('source',axis=1,inplace=True)

x_train = Train.drop(['Item_Outlet_Sales'],axis=1)
x_test = Test.drop(['Item_Outlet_Sales'],axis=1)
y_train = Train['Item_Outlet_Sales']

model = LinearRegression()
model.fit(x_train,y_train)

y_predict = model.predict(x_test)
print(y_predict)