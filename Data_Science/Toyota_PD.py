# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print("Hello World")
a= 10
b= a*   10
print(b)    


X=300 
Y= 17
X%=Y
print(X)

x=4
y=7
z=x//y
print(z)
    
num1='100'
num2='200'
print(num1+num2)
print(num1*num2)

num1=int(num1)
num2=int(num2)
print(num1+num2)

result= 12-4 * (16//2**4)+32
print(result)

print((16//2**4))

print(2**4)

print("a\nb\nc")

print("Good",end="")
print("Day")

print("Number is %i"%result)

x=3
y=6

x,y=y,x
print(x,y)

arrSample = range(1,9,4)
for x in arrSample: print(x)
print(arrSample)
print(arrSample[1:])
for x in arrSample: print(x)

lstSample=[1,2,3,'R','p']
print(lstSample)
lstSample=lstSample+['Py']
print(lstSample)


tupSample =(1,2,3,4,5,'a','r',1)
print(tupSample)
tupSample[2]=9
lstSample[2]=9
print(lstSample)

lstSample[2]
print(lstSample)
lstSample[3]

lstSample[3]*=2

a='gOOd moRning'
print(a)
a.title()

lstSet=[1,2,3,4,5]
print(lstSet)
lstSet.clear()


Product = ['Pencil', 'Pen', 'Eraser', 'Pencil Box', 'Scale']
Price= [5, 10, 2, 20, 12]  
Brand = ['Camlin', 'Rotomac', 'Nataraj', 'Camel', 'Apsara']
Stationery = [Product, Price, Brand]

print(Stationery[0][1])
Stationery[0][1]='Notebook'
print(Stationery)

Stationery[0].append('Note')
print(Stationery)

Stationery[0].insert(0, 'Book')

print(Stationery)      

Stationery[0][0]='Mobile'
print(Stationery)     




print(Product)
Product.index('Note')

import numpy as np


mat = np.matrix("5,9,10;2,5,4;1,9,8;2,6,8")
mat1 = np.matrix("1,2,3,4")
mat2 = np.insert(mat, 1, mat1, axis=1)
print(mat2)
print(mat1.ndim)
print(mat2.ndim)
print(mat2.shape)

#c = np.arange(start = 1, stop = 20, step = 3). What is c[5]?

c = np.arange(start=1, stop=7).reshape(2,3)
print(c)
print(c[1][0])

import os
import pandas as pd
import numpy as np

b = [True,2,3.0,np.nan,"String"]
[type(i) for i in b]

import os
import pandas as pd
import numpy as np

os.chdir("/Users/abhi/Documents/Data_Science")
pd_car = pd.read_csv("mtcars.csv")
pd_car.describe

pd_car[['model']]
pd_car.loc[:,['model']]
pd_car.iloc[:,1]

pd_car_op = pd_car[pd_car.model == 'Volvo 142E']
print(pd_car_op)

pd_car_op = pd_car.loc[pd_car.model.isin(['Volvo 142E'])]
print(pd_car_op)

pd_car_op = pd_car.model.loc[pd_car.isin(['Volvo 142E'])]
print(pd_car_op)

import os
import pandas as pd
import numpy as np

os.chdir("/Users/abhi/Documents/Data_Science")
cars_data=pd.read_csv("Toyota.csv",index_col=0,na_values=['??','????'])
cars_data

np.unique(cars_data['HP'])
np.unique(cars_data['Doors'])
np.unique(cars_data['MetColor'])
cars_data['MetColor']=cars_data['MetColor'].astype('object')
np.unique(cars_data['Automatic'])
cars_data['Automatic']=cars_data['Automatic'].astype('object')
print(cars_data.columns)
cars_data.info()

cars_data['Doors'].replace('three',3,inplace=True)
cars_data['Doors'].replace('four',4,inplace=True)
cars_data['Doors'].replace('five',5,inplace=True)
cars_data['Doors']=cars_data['Doors'].astype('int64')

np.unique(cars_data['Doors'])

cars_data.isnull().sum()
np.where()

def c_convert_round(val1):
    ren_val=round(val1,1)
    return[ren_val]

def c_convert(val1,val2):
    val_converted=val1/12
    ratio=val2/val1
    return[val_converted,ratio]

cars_data.insert(10,"Age_Convered",0)
cars_data.insert(11,"KM_Per_Month",0)

cars_data["Age_Converted"],cars_data["KM_Per_Month"]=c_convert(cars_data["Age"], cars_data["KM"])

cars_data.info
cars_data.describe
np.unique(cars_data["KM_Per_Month"])
cars_data["KM_Per_Month"]=round(cars_data["KM_Per_Month"],1)
print(cars_data["KM_Per_Month"])

cars_data["Age_Converted"]=round(cars_data["Age_Converted"],1)

cars_data.to_csv("Toyota1.csv")
    




        



      