from __future__ import division                                        
import numpy as np
#Working on code to find the average RAC shape


def AvgAbun(sample): #Total abundance / Species
    x = np.array(sample)
    return np.mean(x)  # this = average abundance
   
