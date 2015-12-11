#!/usr/bin/env python
#
# Demonstration of basic plotting on on multiple subplots
#
# ARCHER, 2015

# Uncomment the following two lines to save an image 
# without needing an available display
# import matplotlib
# matplotlib.use("Agg")

# Import the required functionality
from matplotlib import pyplot as plt
import numpy as np

# The whole figure
fig = plt.figure()

# First subplot with y-label
data1 = np.genfromtxt('random1.dat')
plt.subplot(2,1,1)
plt.plot(data1[:,0], data1[:,1], 'r+', label='random1')
plt.ylabel('Values')

# Add second set of data with y-label
data2 = np.genfromtxt('random2.dat')
plt.subplot(2,1,2)
plt.plot(data2[:,0], data2[:,1], 'bx', label='random2')
plt.ylabel('Values')

# x-axis label and title
plt.xlabel('Positions')
fig.suptitle('Random Data Plots')

# Show the plot on the disply. Uncomment this line if 
# you just want to save to a file
plt.show()

# Save as an image
fig.savefig('multiple.png')
