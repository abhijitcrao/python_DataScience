#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 20:45:54 2023

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

data_train=pd.read_csv("GHI_Report.csv")

data_train.describe()

#to know the categorical variable info

data_train.describe(include='O')
# this gives error as therea are no categorical variables

# know the coloumns

col_list= data_train.columns

# Separating input and output features
x1=data_train.drop(['H_Score'],axis='columns', inplace=False)
y1=data_train['H_Score']

# H_Score
sns.distplot(data_train['H_Score'])
sns.boxplot(y=data_train['H_Score'])

x_train,x_test,y_train,y_test = train_test_split(x1,y1,test_size=0.3,random_state=1)

print(x_train.shape,y_train.shape,x_test.shape,y_test.shape)

## now we need to baseline the prediction 

from sklearn.metrics import mean_squared_error

base_pred=np.mean(y_test)
print(base_pred)

# Repeating same value till length of test data
base_pred = np.repeat(base_pred, len(y_test))

base_root_mean_square_error = np.sqrt(mean_squared_error(y_test, base_pred))

print(base_root_mean_square_error)


