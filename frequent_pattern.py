# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 22:30:55 2017

@author: Satheesh
"""
import numpy as np
import pandas as pd

database_animals = pd.read_csv('database.csv', header =0)

#Count the number of unique instances first
df_itemlist = database_animals['ITEM'].unique()

print("The number of unique elements is " + str(len(df_itemlist)))