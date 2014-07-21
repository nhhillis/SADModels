from __future__ import division                                        
import numpy as np
import sys  
sys.path.append('/users/Nathan_Hillis/SADModels/models') 

#Working on code to find the average RAC 

def avg(sample):
    x = np.array(sample)
    mean = sum(x)/float(len(x))
    return mean






