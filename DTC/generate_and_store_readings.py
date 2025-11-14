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
current_day = math.floor(time.time()/(24*60*60))


## Functions
# Generate readings
def generate_readings():
    # Wait for the next whole second
    time.sleep(1.0 - (time.monotonic()-math.floor(time.monotonic())))
    # Initialise sensor_outputs
    sensor_outputs = np.array([[round(time.time())%(24*60*60), 22.5, 45.2, 1013.2, 12]])
    # Wait for the next whole second
    time.sleep(1.0 - (time.monotonic()-math.floor(time.monotonic())))
    starttime = time.monotonic()
    for i in range(0,100):
    #while round(time.time())%(24*60*60) != 0:
        # Current values of Time, Temperature, Humidity, Pressure, and Air Quality
        curr_time = round(time.time())%(24*60*60)
        temp = round(22.5 + float(np.random.normal(0, 1, 1)), 1)
        humi = round(45.2 + float(np.random.normal(0, 1, 1)), 1)
        pres = round(1013.2 + float(np.random.normal(0, 1, 1)), 1)
        airQ = round(12 + float(np.random.normal(0, 1, 1)), 0)
        # Update sensor_outputs
        sensor_outputs = np.append(sensor_outputs, 
                                  [[curr_time, temp, humi, pres, airQ]], axis=0)
        time.sleep(1 - ((time.monotonic() - starttime) % 1))
    return sensor_outputs

# Store readings in a CSV file
def store_readings(sensor_outputs, current_day):
    rows = ["{},{},{},{},{}".format(i, j, k, l, m) for 
            i, j, k, l, m in sensor_outputs]
    text = "\n".join(rows)
    
    with open('sensor_outputs/sensor_output_'+str(current_day)+'.csv', 'w') as f:
        f.write(text)


## Operations
#while True: # This could be improved to break yearly
sensor_outputs = generate_readings()
store_readings(sensor_outputs, current_day)

