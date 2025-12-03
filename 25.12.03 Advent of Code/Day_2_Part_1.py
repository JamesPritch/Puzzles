#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  3 18:15:36 2025

@author: jpritch
"""

with open('Day_2.txt') as f:
    lines = f.readline()
IDs=lines.split(',')

sumIDs = 0


for i in range(len(IDs)):
    ID = IDs[i].split('-')
    start = int(ID[0])
    end = int(ID[1])+1
    for j in range(start,end):
        check = str(j)
        length = len(check)
        if length%2 == 0:
            if check[0:int(length/2)] == check[int(length/2):int(length)]:
                sumIDs += int(check[0:int(length/2)]*2)
            
            
print(sumIDs)
#37314786486