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


## Extracting individual readings from sensor output
# Time
xpoints = sensor_output[:,0]
# Temperature, Humidity, Pressure, Air Quality
ypoints_temperature = sensor_output[:,1]
ypoints_humidity = sensor_output[:,2]
ypoints_pressure = sensor_output[:,3]
ypoints_airQuality = sensor_output[:,4]

# Graph Titles
title_temperature = 'Temperature against Time'
title_humidity = 'Humidity against Time'
title_pressure = 'Pressure against time'
title_airQuality = 'Air Quality against Time'

# Axis labels
xlabel = 'Time (seconds)'
ylabel_temperature = 'Temperature (°C)'
ylabel_humidity = 'Humidity (%)'
ylabel_pressure = 'Pressure (hPa)'
ylabel_airQuality = 'Air Quality (Index)'


## A function to graph
def graph(x,y, title, xlab, ylab):
    plt.figure(dpi=300)
    plt.scatter(x, y, c='black', marker = '.')
    plt.title(title)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.show()




graph(xpoints, ypoints_temperature, title_temperature, xlabel, ylabel_temperature)
graph(xpoints, ypoints_humidity, title_humidity, xlabel, ylabel_humidity)
graph(xpoints, ypoints_pressure, title_pressure, xlabel, ylabel_pressure)
graph(xpoints, ypoints_airQuality, title_airQuality, xlabel, ylabel_airQuality)