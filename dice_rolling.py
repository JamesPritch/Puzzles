#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  7 10:28:51 2026

@author: jpritch
"""

import random
import math

#rolls = [0,0,0,0,0,0]
rolls = []
roll56 = 0
roll66 = 0
roll5then6 = 0
roll6then6 = 0

def dieroll():
    roll = random.random() * 6
    return math.floor(roll) + 1
    
#for i in range(1000000):
#    roll = dieroll()
#    rolls[roll] += 1

for i in range(100000):
    for j in range(100):
        rolls.append(dieroll())
    for j in range(99):
        if rolls[j] == 5 and rolls[j+1] == 6:
            roll56 += 1
        if rolls[j] == 6 and rolls[j+1] == 6:
            roll66 += 1
    for j in range(99):
        if rolls[j] == 5 and rolls[j+1] == 6:
            roll5then6 += 1
            break
        elif rolls[j] == 6 and rolls[j+1] == 6:
            roll6then6 += 1
            break
            
    rolls = []



print('Rolls of 5 then 6 count', str(roll56) + ', and rolls of 6 then 6 count', str(roll66) + '.')
print('Percentage difference is', roll56/roll66 * 100 - 100)

print('5 then 6 happened first', roll5then6, 'times and 6 and 6 happened first', roll6then6, 'times.')
print('Percentage difference is', roll5then6/roll6then6 * 100 - 100)