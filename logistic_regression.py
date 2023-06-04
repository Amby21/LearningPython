#Logistic Regression on Titanic data

#Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

#Inporting the data file, in this case the titanic dataset
train = pd.read_csv('C:/Users/sganesh/Downloads/Py_DS_ML_Bootcamp-master/Refactored_Py_DS_ML_Bootcamp-master/13-Logistic-Regression/titanic_train.csv')

#displaying the first few records to check data.
train.head()

#Visulization to see survival

sns.countplot(x='Survived',hue='Pclass',data=train)

sns.distplot(train['Age'].dropna(),kde=False,bins=30)

sns.countplot(x='SibSp', data=train)

#To fill in missing data
#solving for missing data for age..

sns.boxplot(x='Pclass',y='Age',data=train)

#Imputing the average value for age as per passenger class
def impute_age(cols):
    Age = cols[0]
    Pclass = cols[1]

    if pd.isnull(Age):

        if Pclass == 1:
            return 37
        elif Pclass == 2:
            return 29
        else:
            return 24
    else:
        return Age

train['Age'] = train[['Age','Pclass']].apply(impute_age,axis=1)
sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')

train.drop('Cabin',axis=1,inplace=True)

#putting dummy variables for columns
sex = pd.get_dummies(train['Sex'],drop_first=True)

embark = pd.get_dummies(train['Embarked'],drop_first=True)

train = pd.concat([train,sex,embark],axis=1)

train.head(2)

train.drop(['Sex','Embarked','Name','Ticket'],axis=1,inplace=True)
train.head()

X = train.drop(['Survived'],axis=1)
y = train['Survived']

X_train,X_test,Y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=101)

from sklearn.linear_model import LogisticRegression

logmodel = LogisticRegression()

logmodel.fit(X_train,Y_train)

predictions = logmodel.predict(X_test)

from sklearn.metrics import classification_report

print(classification_report(y_test,predictions))