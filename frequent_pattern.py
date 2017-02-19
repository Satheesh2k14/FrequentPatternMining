# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 22:30:55 2017

@author: Satheesh
"""
import numpy as np
import pandas as pd

database_animals = pd.read_csv('database.csv', header =0)

print(database_animals)
#Count the number of unique instances first
itemlist = pd.Series(database_animals['ITEM'].unique())
print("The number of unique elements is " + str(len(itemlist)))

frequency_1_item_list = [0] * len(itemlist)

for i in database_animals['ITEM']:
    frequency_1_item_list[itemlist[itemlist == i].index[0]] += 1

print(frequency_1_item_list)