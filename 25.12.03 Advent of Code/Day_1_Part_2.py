#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  3 16:58:11 2025

@author: jpritch
"""

# Reading instructions from file
with open('Day_1.txt') as f:
    lines = f.readlines()
lines[-1] = lines[-1]+' '
    
dial = 50
password = 0


for i in range(len(lines)):
    instruction = lines[i]
    if instruction[0] == 'L':
        for j in range(int(instruction[1:-1])):
            dial -= 1
            if dial < 0:
                dial += 100
            if dial == 0:
                password += 1
    elif instruction[0] == 'R':
        for j in range(int(instruction[1:-1])):
            dial += 1
            if dial >= 100:
                dial -= 100
            if dial == 0:
                password += 1


        

#print(password)
# 6166