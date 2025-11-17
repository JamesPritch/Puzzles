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
# T is the length of one cycle of readings, i.e. the number of seconds in a day
T = 24*60*60


## Functions
# Generate readings
def generate_readings(sensor_outputs, t, T, i):
    # Current values of Time, Temperature, Humidity, Pressure, and Air Quality
    curr_time = round(time.time())%(24*60*60)
    temp = generate_temp(t, T)
    humi = generate_humi(t, T)
    pres = generate_pres(t, T, i)
    airQ = generate_airQ(t, T, i) 
    # Update sensor_outputs
    sensor_outputs = np.append(sensor_outputs, 
                              [[curr_time, temp, humi, pres, airQ]], axis=0)
    return sensor_outputs

def generate_temp(t, T):
    # Equation for temperature is 22.5+10sin(2pi*t/T)
    temp = 22.5 + 10*math.sin(2*math.pi*(t)/T) 
    # Add randomness from Normal distribution with mu=0, omega=1
    temp += float(np.random.normal(0, 1, 1))
    return round(temp, 1)

def generate_humi(t, T):
    # Equation for humidity is 45.2+10sin(pit*/T)
    humi = 45.2 + 10*math.sin(math.pi*(t)/T) 
    # Add randomness from Normal distribution with mu=0, omega=0.5
    humi += float(np.random.normal(0, 0.5, 1))
    return round(humi, 1)

def generate_pres(t, T, i):
    if i/T < 1/3:
        # Linearly drop by 50 hPa
        pres = 1013.2 - 50*(t)/(T/3)
    else:
        # Equation for pressure is 963.2+e^(1.5ln(51)t/T)-1
        pres = 963.2 + math.exp((1.5*math.log(51, math.e))*(t-(T/3))/T)-1
    # Add randomness from Normal distribution with mu=0, omega=2
    pres += float(np.random.normal(0, 2, 1))
    return round(pres, 1)

def generate_airQ(t, T, i):
    if i/T < 2/3:
        # Equation for air quality is 12+(30/ln(43/3))ln(20(t+1)/T)
        airQ = 12 + (30/math.log(43/3, math.e))*math.log((20*(t+1)/T), math.e)
    else:
        # Linearly return to initial air quality
        airQ = 42 - 30*(t-T*2/3)/(T/3)
    # Add randomness from Normal distribution with mu=0, omega=1.5
    airQ += float(np.random.normal(0, 1.5, 1))
    return round(airQ, 0)

# Store readings in a CSV file
def store_readings(sensor_outputs, current_day):
    rows = ["{},{},{},{},{}".format(i, j, k, l, m) for 
            i, j, k, l, m in sensor_outputs]
    text = "\n".join(rows)
    # Write readings in a CSV file with the current day in the name
    with open('sensor_outputs/sensor_output_'+str(current_day)+'.csv', 'w') as f:
        f.write(text)


## Operations
while True: # This could be improved to break yearly
    current_day = math.floor(time.time()/(24*60*60))
    # Wait for the next whole second
    time.sleep(1.0 - (time.time()-math.floor(time.time())))
    # Initialise sensor_outputs and starttime
    t_0 = time.time()%(24*60*60)
    temp_0 = generate_temp(t_0, T)
    humi_0 = generate_humi(t_0, T)
    pres_0 = generate_pres(t_0, T, t_0)
    airQ_0 = generate_airQ(t_0, T, t_0) 
    sensor_outputs = np.array([[round(time.time())%(24*60*60), 
                                temp_0, humi_0, pres_0, airQ_0]])
    starttime = time.time() - time.time()%(24*60*60)
    # Wait for the next whole second
    time.sleep(1.0 - (time.time()-math.floor(time.time())))
    #for i in range(0,60):
    while round(time.time())%(24*60*60) != 0:
        t = time.time()-starttime
        i = time.time()%(24*60*60)
        sensor_outputs = generate_readings(sensor_outputs, t, T, i)
        time.sleep(1 - (t % 1))
    store_readings(sensor_outputs, current_day)

