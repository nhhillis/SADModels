import numpy as np
import matplotlib.pyplot as plt
#Three plots, one for random fraction, BRkstk, LogNorm

def RACHeatMap(fig, RACs):
    
    ab = [] # y in RAC heat map
    ranks = [] # x in RAC heat map
    for RAC in RACs:
        
        RAC.sort(reverse = True)
        RAC = np.log(RAC).tolist()
        ab.extend(RAC)
        ranks.extend(range(len(RAC)))
    
    plt.hexbin(ranks, ab, gridsize = 20, bins = 'log', cmap=plt.cm.jet)
    
    return fig