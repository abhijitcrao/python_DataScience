#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 19:32:24 2023

@author: abhi
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

os.chdir("/Users/abhi/Documents/Data_Science")
cars_data=pd.read_csv("Toyota.csv",index_col=0,na_values=["??",'????'])
print(cars_data)

cars_data.dropna(axis=0,inplace=True)

plt.scatter(cars_data['Age'],cars_data['Price'],c='red')
plt.title('Scatter plot of Price vs Age of the cars')
plt.xlabel('Age -> ')
plt.ylabel('Price ->')
plt.show()

plt.hist(cars_data["KM"],color='green',edgecolor='white',bins=5)
plt.xlabel('Kilometer')
plt.ylabel('Frequency')
plt.show()

cars_data.columns
cars_data.loc[:cars_data["FuelType"] == "Petrol"].count()

cars_data.describe()

cars_data['FuelType'].value_counts().index[0]

cars_data['FuelType'].isna().sum()

cars_data['MetColor'].mode()

cars_data.isnull().sum()
     