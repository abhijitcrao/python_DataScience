#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 20:57:54 2023

@author: abhi
"""
import os
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
# Importing library for logistic regression
from sklearn.linear_model import LogisticRegression

# Importing performance metrics - accuracy score & confusion matrix
from sklearn.metrics import accuracy_score,confusion_matrix

import numpy as np

os.chdir("/Users/abhi/Documents/Data_Science")

data_train=pd.read_csv("ServiceTrain.csv")
data_test = pd.read_csv("ServiceTest.csv")

#function to provide info on variable 
data_train.describe()

#function to provide data about categorial variables
data_train.describe(include="O")

# to check frequency of the categorial variable 

data_train["Service"].value_counts()

# we need to check for unique values under the categorical variable 

print(np.unique(data_train["Service"]))

# checking info from dataframe
data_train.info()

## checking for null values in the dataframe
data_train.isnull().sum()

# let's find out the missing column 
missing = data_train[data_train.isnull().any(axis=1)]
print(missing)

# find out correlation between the independent variables

corr = data_train.corr()

# get the column names

data_train.columns

# lets find out the cor between two variable specially the categorical variables vs independent variable

server_req = pd.crosstab(columns= data_train["OilQual"], index =data_train["Service"],margins=True,normalize='index')
print(server_req)

# make a copy of dataframe to avoid overwritting of the data
data_train_copy = data_train.copy()

# Categorical data needs to be mapped to 0 or 1 for processing
# before mapping let's find out the correct values to avoid NAN 
print(np.unique(data_train["Service"]))

data_train_copy['Service'] = data_train_copy['Service'].map({'Yes':1,'No':0})
data_test['Service'] = data_test['Service'].map({'Yes':1,'No':0})

column_list=list(data_train_copy.columns)
print(column_list)

#seperate the feature or input variable
features=list(set(column_list)-set(['Service']))
print(features)

#store output value into y

train_y=data_train_copy['Service'].values

#store values of features into x

train_x=data_train_copy[features].values

#####
## seperate the test information into x and y
#####

column_list=list(data_test.columns)
print(column_list)

#seperate the feature or input variable
features=list(set(column_list)-set(['Service']))
print(features)

#store output value into y

test_y=data_train_copy['Service'].values

#store values of features into x

test_x=data_train_copy[features].values





### now logistic Regression model

logistic = LogisticRegression()

# fitting the value of x and y
logistic.fit(train_x, train_y)
logistic.coef_
logistic.intercept_

prediction = logistic.predict(test_x)

confusion_matrix = confusion_matrix(test_y,prediction)

print(confusion_matrix)

accuracy_score=accuracy_score(test_y, prediction)
print(accuracy_score)

print('Misclassified samples: %d' % (test_y != prediction).sum())



## Improvising the train and test data to see effect

X_train, X_test, y_train, y_test = train_test_split(train_x, train_y, random_state = 0)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

logistic.fit(X_train, y_train)
logistic.coef_
logistic.intercept_

prediction = logistic.predict(X_test)

confusion_matrix = confusion_matrix(y_test,prediction)

print(confusion_matrix)


accuracy_score=accuracy_score(y_test, prediction)
print(accuracy_score)

print('Misclassified samples: %d' % (y_test != prediction).sum())


