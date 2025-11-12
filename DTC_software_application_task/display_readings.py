#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 12 16:41:01 2025

@author: jpritch
"""

## Imports
import numpy as np
import matplotlib.pyplot as plt
import time


## Read file
sensor_output = np.loadtxt("/Users/jpritch/Documents/Other/Puzzles/DTC_software_application_task/sensor_output.csv",
				delimiter=",", dtype=float)


print(sensor_output[:,1])

xpoints = sensor_output[:,0]
ypoints = sensor_output[:,4]

plt.plot(xpoints, ypoints)
plt.show()