import os
import numpy as np
from random import randrange, seed
import matplotlib.pyplot as plt
import sys
sys.path.append('/Users/Nathan_Hillis/SADModels/tools/')

import macroeco_distributions  # code that provides maximum likelihood 
# predictions for SAD models
import pln # importing the Poisson Lognormal from macroeco_distributions

sys.path.append('/Users/Nathan_Hillis/SADModels/Models/')
import LogNormal_v2



def RADfigs(a, S):
    fig = plt.figure()  # declare a figure object
    ax = plt.subplot(1,1,1) # declare an axis object

    
    lsRAC = np.random.logseries(a, S) # a random draw from the log-series. Note,
    # we are only constraining S here. We aren't telling it to give us a certain
    # number of individuals. Then, convert the numpy array to a Python list...
    lsRAC = lsRAC.tolist()
    lsRAC.sort()
    lsRAC.reverse()
    
    
    MLE_RACs = LogNormal_v2.get_MLEs(lsRAC, 2)
    N, S = sum(MLE_RACs[0]), len(MLE_RACs[0]) # because the PLN only takes the avg
    # abundance and variance, the resulting expected form will have a different N
    # and S than the log-series RAC that provided the starting average abundance and 
    # variance.
    print N, S , min(MLE_RACs[0]) # The N and S of the log-normal MLEs
    
    
    RACs = LogNormal_v2.SimLogNorm(N, S, 100) # Use the random fraction function
    # to generate 10K random RACs
    print sum(RACs[0]), len(RACs[0]), min(RACs[0]) # N & S of the first RAC
    
    
    x = []
    y = []
    for RAC in RACs:
        y.extend(np.log(RAC))
        x.extend(range(len(RAC)))
    
    plt.hexbin(x, y, mincnt=1, gridsize = 20, bins = 'log', cmap=plt.cm.jet)
    
    for RAC in MLE_RACs:
        plt.plot(np.log(RAC), color='0.3', lw=3, alpha = 0.6)
    
    plt.xlim(0, len(RAC))
    
    plt.xlabel('Rank in abundance', fontsize=16)
    plt.ylabel('log(abundance)', fontsize=16)
    
    plt.savefig('/Users/Nathan_Hillis/SADModels/figures/Debug_Figs/logNormal_N='+str(N)+'_S='+str(S)+'.png', # insert mydir
                        dpi=600, bbox_inches = 'tight', pad_inches=0.03)
    plt.close()
    
    return
    plt.show()
    

a_s = [0.5, 0.6, 0.7, 0.8, 0.9, 0.99]
Ss = [4, 8, 16, 32]

for a in a_s:
    for S in Ss:
           RADfigs(a , S)
           
           
            
                