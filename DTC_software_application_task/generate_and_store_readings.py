#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 12 16:37:11 2025

@author: jpritch
"""

## Imports
import time
import math
import numpy as np


## Variable definitions
# Initial sensor output example (as given)
current_day = math.floor(time.time()/(24*60*60))
sensor_output = np.array([[round(time.time())%(24*60*60)+0, 22.5, 45.2, 1013.2, 12],
                          [round(time.time())%(24*60*60)+1, 22.6, 45.1, 1013.1, 14],
                          [round(time.time())%(24*60*60)+2, 22.7, 45.3, 1013.0, 13],
                          [round(time.time())%(24*60*60)+3, 22.8, 45.5, 1012.9, 16],
                          [round(time.time())%(24*60*60)+4, 22.6, 45.4, 1012.8, 15]])

## Generate readings



## Store readings in a CSV file
rows = ["{},{},{},{},{}".format(i, j, k, l, m) for 
        i, j, k, l, m in sensor_output]
text = "\n".join(rows)

with open('sensor_output_'+str(current_day)+'.csv', 'w') as f:
    f.write(text)
