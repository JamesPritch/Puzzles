#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  3 16:11:27 2025

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
        dial = dial - int(instruction[1:-1])
    elif instruction[0] == 'R':
        dial = dial + int(instruction[1:-1])
    while dial >= 100:
        dial = dial - 100
    while dial < 0:
        dial = dial + 100
    if dial == 0:
        password += 1
        

print(password)
# 1034
