from __future__ import division                                        
import numpy as np
#Working on code to find the average RAC shape


def avg(sample):
    x = np.array(sample)
    mean = sum(x)/float(len(x))
    return mean
