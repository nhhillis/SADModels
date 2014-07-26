from __future__ import division                                        
import numpy as np
#Working on code to find the average RAC shape


def AvgAbun(sample): #Total abundance / Species
    x = np.array(sample)
    return np.mean(x)  # this = average abundance
   
#To find the average shape of the SAD:
# - compare each SAD to each other SAD and find which one is 
#   most similar to the others
# - compare S in list to the average of the other Ss in other lists
# - 
SADs = [[6,3,1],[5,4,1],[6,2,2]]


def AvgShape(sample):
    avg1 = (sample[1][0] + sample[2][0]) / (len(sample) -1)# need loop to generate
    avg2 = (sample[1][1] + sample[2][1]) / (len(sample) -1)# avg S's for each SAD
    avg3 = (sample[1][2] + sample[2][2]) / (len(sample) -1)
    print avg1, avg2, avg3
    x1 = abs(sample[0][0] - avg1) # this will need to be a loop for each 
    x2 = abs(sample[0][1] - avg2) # SAD in sample
    x3 = abs(sample[0][2] - avg3)
    print x1, x2, x3
     
print AvgShape(SADs)     
    