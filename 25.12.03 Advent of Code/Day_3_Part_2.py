#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 19:22:56 2025

@author: jpritch
"""

# Reading instructions from file
with open('Day_3.txt') as f:
    lines = f.readlines()
lines[-1] = lines[-1]+' '

# Variables
length = len(lines[0])
joltage_length = 12
joltages = []
values = [0] * joltage_length
indices = [[None] * joltage_length]
for i in range(len(lines)-1):
    indices.append([None] * joltage_length)


# Functions
def findmax(lines, i, j, values, indices):
    if j == 0:
        start = 0
    else:
        start = indices[i][j-1]+1
    for k in range(start, length - (joltage_length-j)):
        if int(lines[i][k]) > values[j]:
            values[j] = int(lines[i][k])
            indices[i][j] = k
    return indices


# Operations
for i in range(len(lines)):
    for j in range(joltage_length):
        indices = findmax(lines, i, j, values, indices)
    joltage = 0
    for j in range(joltage_length):
        joltage += int(lines[i][indices[i][j]]) * 10 ** (joltage_length-j-1)
    joltages.append(joltage)
    values = [0] * joltage_length



print(sum(joltages))
# 168798209663590