from __future__ import division                                        
import numpy as np
#Working on code to find the average RAC shape


def AvgAbun(sample): #Total abundance / Species
    x = np.array(sample)
    return np.mean(x)  # this = average abundance
   
#To find the average shape of the SAD:
# - Find average difference of ranks between 2 RACs (for all combinations 
# - of RACs).  Find RAC with smallest avg difference.  
RACs = [[5,3,1,1],[6,2,1,1],[4,3,2,1], [7,1,1,1]]

def AvgShape(sample):
    
    for RAC in sample:
    
        for rank in RAC: 
               return cmp(RAC[-1], RAC[-2])
               
print AvgShape(RACs)     
    