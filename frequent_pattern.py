# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 22:30:55 2017

@author: Satheesh
"""
import numpy as np
import pandas as pd

database_animals = pd.read_csv('database.csv', header =0)

#Count the number of unique instances first
itemlist = pd.Series(database_animals['ITEM'].unique())
print("The number of unique elements is " + str(len(itemlist)))

print(itemlist)

#Calculate the frequency of 1 item list
frequency_1_item_list = pd.Series([0] * len(itemlist))

for i in database_animals['ITEM']:
    frequency_1_item_list[itemlist[itemlist == i].index[0]] += 1

#Define minimum support
minimum_support = 2

min_support_pass_list = itemlist[frequency_1_item_list >= 2]

print("Number of elements having support >= 2")
print(min_support_pass_list)

#convert 1 item set to two item set
itemlist_2 = []
for i in itemlist:
    for j in itemlist:
        if i != j:
            itemlist_2.append([i,j])
            
print(itemlist_2)

