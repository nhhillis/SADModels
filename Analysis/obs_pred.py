'''This file will -
        1. Get empirical SADs
        2. Get predicted SADs
        3. Write empirical and predicted SADs to a file (obs_pred.txt)'''

#################################################################
#Working on importing txt. file but getting ValueError: invalid literal for int() with base 10: '' 

import os
import numpy as np

mydir = os.path.expanduser("/GitHub/SADModels/")
path = ('/Users/Nathan_Hillis/Desktop/Data')

datafile = path + ('/66_data.txt')
num_lines = sum(1 for line in open(datafile))


Data = open(datafile, 'r') 
SadData = [x.split("\t") for x in Data]

print SadData

SADs=[]
for line in SadData:
    SAD = map(int, line)
    SADs.append(SAD)

print SAD
