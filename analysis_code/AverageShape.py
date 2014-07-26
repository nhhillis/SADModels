from __future__ import division                                        
import numpy as np
#Working on code to find the average RAC shape


def AvgAbun(sample): #Total abundance / Species
    x = np.array(sample)
    return np.mean(x)  # this = average abundance
   
#To find the average shape of the SAD:
# - Find average difference of ranks between 2 RACs (for all combinations 
# - of RACs).  Find RAC with smallest avg difference.  
'''Still struggling to make the logic work'''

RACs = [[5,3,1,1],[6,2,1,1],[4,3,2,1], [7,1,1,1]]

def AvgShape(sample):
    avg1 = [] # stores the mean differences between ranks 
    var1 = [] #stores the variances
    
    for RAC in sample: 
        
        for rank in RAC: #Find diffence of ranks pairwise and average
            RAC1sum = 0
            x = sample[RAC][rank] - sample[RAC][rank]
            RAC1sum += x
            print RAC1sum
                
   
print AvgShape(RACs)     

    