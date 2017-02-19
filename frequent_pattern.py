# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 22:30:55 2017

@author: Satheesh
"""
import numpy as np
import pandas as pd

database_animals = pd.read_csv('database.csv', header =0)

#create a dictionary for counting frequency
transaction_dictionary = dict()
for i in database_animals.itertuples():
    if i[1] in transaction_dictionary:
        transaction_dictionary[i[1]].append(i[2])
    else:
        transaction_dictionary[i[1]] = [i[2]]

print(transaction_dictionary)

#Count the number of unique instances first
itemlist = pd.Series(database_animals['ITEM'].unique())
print("The number of unique elements is " + str(len(itemlist)))

print(itemlist)

#Calculate the frequency of 1 item list
frequency_1_item_list = pd.Series([0] * len(itemlist))

for i in database_animals['ITEM']:
    frequency_1_item_list[itemlist[itemlist == i].index[0]] += 1

#Define minimum support and filter elements less than min support from itemlist_1
minimum_support = 2

min_support_pass_list = itemlist[frequency_1_item_list >= 2]

print("Number of elements having support >= 2")
print(min_support_pass_list)

#convert 1 item set to two item set
itemlist_2 = []
for i in min_support_pass_list:
    for j in min_support_pass_list:
        if i != j and min_support_pass_list[min_support_pass_list == i].index[0] < min_support_pass_list[min_support_pass_list== j].index[0]:
            itemlist_2.append([i,j])
            
print(itemlist_2)
itemlist_2 = pd.Series(itemlist_2)

#to find frequency of the 2 itemlist
frequency_2_item_list = pd.Series([0] * len(itemlist_2))

for index, i in enumerate(itemlist_2):
    for key, value in transaction_dictionary.items():
       if i[0] in value and i[1] in value:
           frequency_2_item_list[index] += 1


print(frequency_2_item_list)

#filter itemlist_2 with minimum support
itemlist_2 = itemlist_2[frequency_2_item_list >= 2]
print(itemlist_2)
print(type(itemlist_2))
       