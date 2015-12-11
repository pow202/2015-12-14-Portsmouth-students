#!/usr/bin/env python
#
# Publication-quality plots
#
# ARCHER, 2015

# Uncomment the following two lines to save an image 
# without needing an available display
# import matplotlib
# matplotlib.use("Agg")
import sys
from matplotlib import rc_file
import numpy as np
from matplotlib import pyplot as plt

def main(argv):
    # Get the custom options
    rc_file("matplotlibrc.custom")

    # Set up the figure with the computed dimensions
    fig = plt.figure(figsize=figdims(500, 0.7))
    
    # Read the data and plot it
    data1 = np.genfromtxt('/Users/nbanglawala/Desktop/Work/ARCHER_CSE/CSE_Training/ScientificPython_NB/Exercises/matplotlib/code/random1.dat')
    plt.subplot(1,1,1)
    plt.plot(data1[:,0], data1[:,1], 'kx--', label='random1')

    # Axis labels
    plt.xlabel('Positions')
    plt.ylabel('Values')

    # Save in a nice format
    fig.tight_layout(pad=0.1)
    fig.savefig("publish.pdf", dpi=600)

# Compute the figure dimenstions based on width (in pts) and
# a scale factor
def figdims(width, factor):
    widthpt  = width * factor
    inperpt = 1.0 / 72.27
    golden_ratio  = (np.sqrt(5) - 1.0) / 2.0  # because it looks good

    widthin  = widthpt * inperpt
    heightin = widthin * golden_ratio
    return [widthin, heightin] # Dimensions as list 


# Function to create tidy way to have main method
if __name__ == "__main__":
        main(sys.argv[1:])

