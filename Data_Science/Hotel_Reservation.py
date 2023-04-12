#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 23:19:39 2023

@author: abhi
"""

import os
import pandas as pd
import numpy as np

os.chdir("/Users/abhi/Documents/Data_Science")
data_hotel=pd.read_csv("hotel_bookings.csv",index_col=0,na_values=['??','????'])

data_hotel.describe
data_hotel.columns
pd.unique(data_hotel["reservation_status"])
pd.unique(data_hotel["is_canceled"])
pd.unique(data_hotel["arrival_date_year"])

pd.crosstab(index=data_hotel["is_canceled"], columns =data_hotel["arrival_date_year"], 
            dropna=True)

data_hotel2 = data_hotel[data_hotel["arrival_date_year"] == 2017]
data_hotel2.describe
data_hotel.describe
data_hotel2.columns

pd.unique(data_hotel2["arrival_date_month"])

pd.crosstab(index=data_hotel2["is_canceled"], columns =data_hotel2["arrival_date_month"], 
            dropna=True)