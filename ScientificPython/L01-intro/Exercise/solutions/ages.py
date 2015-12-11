# function to calculate the median age and 
# its two neighbours from a random list of 
# years. Note, years is of length N, where
# N is odd and N > 3
#
# ARCHER, 2015
#
import numpy as np

def medianage(years):
    ages=[];
    for y in years:
        ages.append(2015-y);

    # need to sort list
    ages.sort()

    N = len(ages);
    mid = N/2;

    # return the median and its neighbours
    return ages[mid-1:mid+2];
