#housing data set, trying to create a model to predict housing prices based off of existing features.

#First Step Imports

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#import the excel/csv file to analyse
df = pd.read_csv('C:/Users/sganesh/Downloads/Py_DS_ML_Bootcamp-master/Refactored_Py_DS_ML_Bootcamp-master/11-Linear-Regression/USA_Housing.csv')
print(df.head())

#understanding the dataset
df.describe()
#fetching the column namesm 
df.columns
# sns.pairplot(df)
sns.distplot(df['Price'])
sns.heatmap(df.corr())


x = df[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
       'Avg. Area Number of Bedrooms', 'Area Population']]

y = df['Price']

x_train, x_test,y_train,y_test = train_test_split(x,y,test_size=0.4,random_state=101)


lm = LinearRegression()
lm.fit(x_train,y_train)
print(lm.coef_)
print(lm.intercept_)

cdf = pd.DataFrame(lm.coef_,X.columns,columns=['Coeff'])

predictions = lm.predict(X_test)

plt.scatter(y_test,predictions)

sns.distplot((y_test-predictions))

from sklearn import metrics
metrics.mean_absolute_error(y_test,predictions)
metrics.mean_squared_error(y_test,predictions)
np.sqrt(metrics.mean_squared_error(y_test,predictions))

