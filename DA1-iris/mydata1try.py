import pandas as pd
import matplotlib.pyplot as plt 
from pandas.plotting import scatter_matrix
url='iris.csv'
df=pd.read_csv(url)

header=["sepal_length","sepal_width","petal_length","petal_width","class"]
df.columns=header
print(df)

df.hist()
plt.show()

df.boxplot()
plt.show()

scatter_matrix(df)
plt.show()