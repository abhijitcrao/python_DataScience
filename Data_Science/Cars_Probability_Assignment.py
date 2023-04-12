#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 18:15:47 2023

@author: abhi
"""

import os
import pandas as pd

cars_data=pd.read_csv("Toyota.csv",index_col=0,na_values=["??",'????'])
print(cars_data)

cars_data2=cars_data.copy()

