import pandas as pd
import numpy as np
url='Dia.csv'
df=pd.read_csv(url)
header=["Preg","Glucose","BP","SkinT","Insulin","BMI","DBfun","Age","Outcome"]
df.columns=header
print(df)

x=np.array(df.drop(['Outcome'],axis=1))
y=np.array(df['Outcome'])


#scaling

from sklearn.preprocessing import MinMaxScaler 
scaler=MinMaxScaler()
x_scaler=scaler.fit_transform(x)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x_scaler,y,test_size=0.2,random_state=0)


#classifier
from sklearn.naive_bayes import GaussianNB
classifier=GaussianNB()
classifier.fit(x_train,y_train)
y_predict=classifier.predict(x_test)

#validation using confusion matrix
from sklearn.metrics import confusion_matrix
c=confusion_matrix(y_test,y_predict)
print(c)


#accuracy

from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import accuracy_score
prfs=precision_recall_fscore_support(y_test,y_predict)
acc=accuracy_score(y_test,y_predict)
print(acc)
print("prec",prfs[0])