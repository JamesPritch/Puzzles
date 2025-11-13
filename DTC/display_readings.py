#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 12 16:41:01 2025

@author: jpritch
"""

## Imports
import time
import math
import numpy as np
import matplotlib.pyplot as plt

## Variables
# Graph Titles
titles = ['Temperature against Time', 'Humidity against Time', 
         'Pressure against time', 'Air Quality against Time']
# Axis labels
xlabel = 'Time (hours past midnight)'
ylabels = ['Temperature (°C)', 'Humidity (%)', 
          'Pressure (hPa)', 'Air Quality (Index)']

current_day = math.floor(time.time()/(24*60*60))-3


## Functions
# Read file
def read_file():
    sensor_output = np.loadtxt(('/Users/jpritch/Documents/Other/Puzzles/'
                                'DTC//sensor_outputs/sensor_output_'
                                +str(current_day)+'.csv'),
    			            	delimiter=',', dtype=float)
    return sensor_output

# A graphing function
def graph(sensor, titles, xlab, ylabs):
    # Extracting individual readings from sensor output
    # Time
    x = sensor[:,0]/(60*60)
    # Temperature, Humidity, Pressure, Air Quality
    y = [sensor[:,1], sensor[:,2], sensor[:,3], sensor[:,4]]
    # Loop to graph all four variables against time
    for i in range(0,4):
        # Change resolution of and label graph
        plt.figure(dpi=300)
        plt.title(titles[i] + ' on ' + time.strftime("%d %B %Y", 
                     time.gmtime(current_day*24*60*60)))
        plt.xlabel(xlab)
        plt.ylabel(ylabs[i])
        # Scatter plot variable
        plt.scatter(x, y[i], c='black', marker = '.')
        # Line of best fit
        best_fit = np.poly1d(np.polyfit(x, y[i], 3))
        xp = np.linspace(x[0], x[-1], 50)
        plt.plot(xp, best_fit(xp), '--', c='red')
        plt.show()


## Operations
sensor_output = read_file()
graph(sensor_output, titles, xlabel, ylabels)
