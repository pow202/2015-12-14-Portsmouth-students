#!/usr/bin/env python
#
# continuation of warm up exercise :
# now read ages from a input file 'years.txt'
# Note: have to create input file
#
# ARCHER, 2015

from random import randint;
import sys;
from ages import medianage;

# check function works
years = [1989, 1955, 2011, 1943, 1975];
medianage(years);

# using list comprehension
years = [randint(1950,2015) for x in range(9)]; 
print years;

# save years to file
outyears = open("years.txt",'w');
i=1
# output total number of years
outyears.write("{0:2d}\n".format(len(years)))
               
for y in years:
    outyears.write("{0:2d} {1:2d}\n".format(i, y));
    i+=1;
    
outyears.close();

# read file
inyears = open("years.txt","r");
line = inyears.readline()
# remove any newline characters
N=int(line);

ages=[];
yrs=[];
for i in range(N):
    line = inyears.readline()
    line = line.rstrip();
    tokens = line.split();
    yrs.append(int(tokens[1]));

inyears.close()

# check we have the correct input values
print yrs

# get median age
print medianage(yrs)


