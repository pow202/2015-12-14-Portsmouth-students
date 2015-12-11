#!/usr/bin/env python
#
# Demonstration of basic plotting on on a single subplots
#
# ARCHER, 2015

# Uncomment the following two lines to save an image 
# without needing an available display
# import matplotlib
# matplotlib.use("Agg")

# Import the required functionality
from matplotlib import pyplot as plt
import numpy as np

# Read in the data
data1 = np.genfromtxt('random1.dat')

# Print the data
print data1

# Simple plot
fig = plt.figure()
plt.subplot(1,1,1)
plt.plot(data1[:,0], data1[:,1], 'r+', label='random1')

# Add second set of data
data2 = np.genfromtxt('random2.dat')
plt.plot(data2[:,0], data2[:,1], 'go-', label='random2')

# Axis labels and title
plt.xlabel('Positions')
plt.ylabel('Values')
fig.suptitle(‘Random Data Plot’)

# Add a legend
plt.legend()

# Show the plot on the disply. Uncomment this line if 
# you just want to save to a file
plt.show()

# Save as an image
fig.savefig('simple.png')
