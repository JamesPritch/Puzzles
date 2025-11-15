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

current_day = math.floor(time.time()/(24*60*60))


## Functions
# Read file
def read_file(current_day):
    sensor_outputs = np.loadtxt(('/Users/jpritch/Documents/Other/Puzzles/'
                                'DTC//sensor_outputs/sensor_output_'
                                +str(current_day)+'.csv'),
    			            	delimiter=',', dtype=float)
    return sensor_outputs

# A graphing function
def graph(sensor_outputs, titles, xlabel, ylabels):
    # Extracting individual readings from sensor output
    # Time
    x = sensor_outputs[:,0]/(60*60)
    # Temperature, Humidity, Pressure, Air Quality
    y = [sensor_outputs[:,1], sensor_outputs[:,2], 
         sensor_outputs[:,3], sensor_outputs[:,4]]
    # Loop to graph all four variables against time
    for i in range(0,4):
        # Change resolution of and label graph
        plt.figure(dpi=500)
        plt.title(titles[i] + ' on ' + time.strftime("%d %B %Y", 
                     time.gmtime(current_day*24*60*60)))
        plt.xlabel(xlabel)
        plt.ylabel(ylabels[i])
        # Scatter plot variable
        plt.scatter(x, y[i], c='black', marker = '.', s = 2)
        # Line of best fit
        best_fit = np.poly1d(np.polyfit(x, y[i], 5))
        xp = np.linspace(x[0], x[-1], 50)
        plt.plot(xp, best_fit(xp), '--', c='red')
        plt.show()


## Operations
sensor_outputs = read_file(current_day)
graph(sensor_outputs, titles, xlabel, ylabels)
