from __future__ import division                                        
import numpy as np
import sys  
sys.path.append('/users/Nathan_Hillis/SADModels/models') 
import LogNormal as LN
import BrokenStick as BS

bs = BS.SimBrokenStick(100, 5, 5) #Just used for data to use
logn = LN.SimLogNorm(100, 5, 5)

BSSample = np.array(bs) #converted to numpy arrays 
LNSample = np.array(logn)

#Working on code to find the average RAC 

def avg(sample):
    mean = sum(sample)/float(len(sample))
    return mean
    





