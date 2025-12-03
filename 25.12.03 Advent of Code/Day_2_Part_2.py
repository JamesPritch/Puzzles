#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  3 18:32:30 2025

@author: jpritch
"""

with open('Day_2.txt') as f:
    lines = f.readline()
IDs=lines.split(',')

sumIDs = []


for i in range(len(IDs)):
    ID = IDs[i].split('-')
    start = int(ID[0])
    end = int(ID[1])+1
    for j in range(start,end):
        check = str(j)
        length = len(check)
        if length%2 == 0:
            if check[0:int(length/2)] == check[int(length/2):int(length)]:
                sumIDs.append(int(check[0:int(length/2)]*2))
        if length%3 == 0:
            if check[0:int(length/3)] == check[int(length/3):int(2*length/3)] == check[int(2*length/3):length]:
                sumIDs.append(int(check[0:int(length/3)]*3))
        if length%5 == 0:
            if check[0:int(length/5)] == check[int(length/5):int(2*length/5)] == check[int(2*length/5):int(3*length/5)] == check[int(3*length/5):int(4*length/5)] == check[int(4*length/5):length]:
                sumIDs.append(int(check[0:int(length/5)]*5))
        if length%7 == 0:
            if check[0:int(length/7)] == check[int(length/7):int(2*length/7)] == check[int(2*length/7):int(3*length/7)] == check[int(3*length/7):int(4*length/7)] == check[int(4*length/7):int(5*length/7)] == check[int(5*length/7):int(6*length/7)] == check[int(6*length/7):length]:
                sumIDs.append(int(check[0:int(length/7)]*7))



sumIDs = sum(list(set(sumIDs)))
print(sumIDs)
#47477053982