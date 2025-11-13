#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 12 16:37:11 2025

@author: jpritch
"""

## Imports
import time
import numpy as np


## Variable definitions
# Initial sensor output example (as given)
init_time = round(time.time())
sensor_output = np.array([[round(time.time()) - init_time+0, 22.5, 45.2, 1013.2, 12],
                          [round(time.time()) - init_time+1, 22.6, 45.1, 1013.1, 14],
                          [round(time.time()) - init_time+2, 22.7, 45.3, 1013.0, 13],
                          [round(time.time()) - init_time+3, 22.8, 45.5, 1012.9, 16],
                          [round(time.time()) - init_time+4, 22.6, 45.4, 1012.8, 15]])

## Generate readings


## Store readings

# Test sensor_output is correct
#print(sensor_output)

# Save sensor readings in a CSV file
rows = ["{},{},{},{},{}".format(i, j, k, l, m) for 
        i, j, k, l, m in sensor_output]
text = "\n".join(rows)

with open('sensor_output.csv', 'w') as f:
    f.write(text)
