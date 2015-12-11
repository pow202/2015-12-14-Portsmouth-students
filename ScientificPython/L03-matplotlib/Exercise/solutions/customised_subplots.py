#!/usr/bin/env python
#
# Demonstration of customised plotting on multiple subplots
#
# This script plots a column of 3 plots, a pie chart and 2 
# vertically stacked histograms
#
# ARCHER, 2015

# Uncomment the following two lines to save an image
# without needing an available display
# import matplotlib
# matplotlib.use("Agg")

# import pyplot, numpy as usual
import matplotlib.pyplot as plt
import numpy as np

## Generate random data for the histograms
# h1 = abs(np.random.randn(100));
# h2 = abs(np.random.randn(100));

## Save data in files
# np.savetxt('histogram1.dat',h1);
# np.savetxt('histogram2.dat',h2);

# Create subplot grid with handles for each subplot
(fig, ax) = plt.subplots(3,1); 

# Adjust the figure size
fig.set_size_inches(4,8);

# Set the figure title with suptitle
# Alternatively set the title of the topmost
# plot:
# plt.sca(ax[0]); plt.title('Customise subplots',loc='center');
#
fig.suptitle('Customised subplots');


# Set the current plotting area to the topmost plot, plot 1
plt.sca(ax[0]); 

# Pie chart parameters
pie_labels = 'A', 'B', 'C', 'D'
pie_sizes = [15, 30, 45, 10]
pie_colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
pie_radius = 1.1 # size of pie chart
pie_angle = 90   # orientation of pie chart
plt.axis('equal') # have both x, y axis equal

# Plot the pie chart
# The slices will be ordered and plotted counter-clockwise
plt.pie(np.random.random(4), labels=pie_labels, colors=pie_colors,
autopct='%1.1f%%', shadow=True, startangle=pie_angle, radius=pie_radius);

# Load the histogram data
h1 = np.loadtxt('histogram1.dat');
h2 = np.loadtxt('histogram2.dat');

# Set the number of bins
bins = 50

# Set the current axis to the middle plot, plot 2
plt.sca(ax[1]);

# Plot the histogram
plt.hist(h1, bins, color='m',label='hist 1');
plt.ylabel('Plot 2 y-axis');
plt.legend();

# Set the x-axis tick marks
plt.tick_params(
   axis='x',          # changes apply to the x-axis
   which='both',      # both major and minor ticks are affected
   bottom='on',       # ticks along the bottom edge are off
   top='on',          # ticks along the top edge are off
   labelbottom='off') # ticks labels along the bottom are off

# Set the y-axis ticks so that values will not
# overlap with y-axis of bottom plot
yt2=[2,4,6,8];
yt2L=['2','4','6','8'];
plt.yticks(yt2, yt2L);

# Set the current axis to the bottom plot, plot 3
plt.sca(ax[2]);
plt.hist(h2, bins, color='g', label='hist 2');
plt.ylabel('Plot 3 y-axis');
plt.xlabel('Plot 3 x-axis');
plt.legend();

# Set the y-axis tick marks, adjusting for any overlap
# with plot 2
yt3=[0,2,4,6,8];
yt3L=['0','2','4','6','8']; 
plt.yticks(yt3, yt3L);

# Want tick marks on the x-axis of the bottom plot
xt3=np.arange(0,4); 
xt3L=['0.','1.','2.','3.']; 

# Finally remove (though not completely) the space between the 
# two histograms so they appear to share the x-axis
plt.subplots_adjust(hspace=0.001);

# Save figure as a PNG image
plt.savefig('customised_subplots.png')

## Show figure
# plt.show()
