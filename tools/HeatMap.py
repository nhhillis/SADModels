from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
#Three plots, one for random fraction, BRkstk, LogNorm

def RACHeatMap(fig, RACs):
    
    ab = [] # y in RAC heat map
    ranks = [] # x in RAC heat map
    grdsize = int(len(RACs[0])/2)
    for RAC in RACs:
        
        RAC.sort(reverse = True)
        RAC = np.log(RAC).tolist()
        ab.extend(RAC)
        ranks.extend(range(len(RAC)))
    
    plt.hexbin(ranks, ab, mincnt=1, gridsize = grdsize, bins = 'log', cmap=plt.cm.jet)
    
    return fig