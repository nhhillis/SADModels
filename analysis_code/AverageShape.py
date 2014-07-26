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
# - OR do you just find which SAD has the most ranks in common with the
#     others?
SADs = [[5,3,1,1],[6,2,1,1],[4,3,2,1], [7,1,1,1]]

def AvgShape(sample):
    return [rank for rank in sample[0] if rank in sample[1]]
    
            
print AvgShape(SADs)     
    