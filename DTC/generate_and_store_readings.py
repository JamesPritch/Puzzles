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
    for i in range(0,60):
    #while round(time.time())%(24*60*60) != 0:
        # Current values of Time, Temperature, Humidity, Pressure, and Air Quality
        curr_time = round(time.time())%(24*60*60)
        temp = generate_temp(starttime)
        humi = generate_humi(starttime)
        pres = generate_pres(starttime, i)
        airQ = generate_airQ(starttime, i) 
        # Update sensor_outputs
        sensor_outputs = np.append(sensor_outputs, 
                                  [[curr_time, temp, humi, pres, airQ]], axis=0)
        time.sleep(1 - ((time.monotonic() - starttime) % 1))
    return sensor_outputs

def generate_temp(starttime):
    # Equation for temperature is 22.5+10sin(2pix/60), where x is time
    temp = 22.5 + 10*math.sin(2*math.pi*(time.monotonic()-starttime)/(60)) 
    # Add randomness from Normal distribution with mu=0, omega=2
    temp += float(np.random.normal(0, 2, 1))
    return round(temp, 1)

def generate_humi(starttime):
    # Equation for humidity is 45.2+10sin(pix/60), where x is time
    humi = 45.2 + 10*math.sin(math.pi*(time.monotonic()-starttime)/(60)) 
    # Add randomness from Normal distribution with mu=0, omega=1
    humi += float(np.random.normal(0, 1, 1))
    return round(humi, 1)

def generate_pres(starttime, i):
    if i/60 < 1/3:
        # Linearly drop to initial pressure
        pres = 1013.2 - 50*(time.monotonic()-starttime+1)/((60)/3)
    else:
        # Equation for pressure is 1013.2+10e^(x-1), where x is time
        pres = 962 + 10*(math.exp((time.monotonic()-starttime-((60)/3))/22)-1)
    # Add randomness from Normal distribution with mu=0, omega=4
    pres += float(np.random.normal(0, 4, 1))
    return round(pres, 1)

def generate_airQ(starttime, i):
    if i/60 < 2/3:
        # Equation for pressure is 1013.2+10ln(x+1), where x is time
        airQ = 12 + 10*math.log((time.monotonic()-starttime+2), math.e)
    else:
        # Linearly return to initial pressure
        airQ = 48 - 40*(time.monotonic()-starttime-40)/((60)/3)
    # Add randomness from Normal distribution with mu=0, omega=3
    airQ += float(np.random.normal(0, 3, 1))
    return round(airQ, 0)

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

