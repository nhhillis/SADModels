import numpy as np
from random import randrange
import matplotlib.pyplot as plt
import sys

sys.path.append('/Users/Nathan_Hillis/SADModels/tools/')
import HeatMap
import pln 

sys.path.append('/Users/Nathan_Hillis/SADModels/Analysis/')

from AverageShape import PlotAvgShape


"""Plotting SimLogNorm and MLEs"""
#Trying to pull AvgShape in but having issues

def SimLogNorm(N, S, sample_size):
    '''Working to fix bug @ 'if v1 < 1...' trying to create list of broken RACs
    to then determine their effect.'''
    sample = []
    
    while len(sample) < sample_size:
        RAC = [0.75*N, 0.25*N] #Initial N is split 75:25
       
        
        while len(RAC) < S:
            ind = randrange(len(RAC)) 
            v = RAC.pop(ind) # Removes randomly selected number from list RAC
            v1, v2 = int(round(0.75 * v)), v - int(round(0.75 * v)) # forcing all abundance, rounding 
                                                                    # values to be integers
            
            if v1 < 1 or v2 < 1: break# forcing smallest abundance to be greater than one
                #break  #Instead of Breaking Loop, Return to line 29? 
                #continue #Determining what will happen if we ignore this condition
                                            
            RAC.extend([v1, v2]) # Adds new values to RAC
            
            
        if len(RAC) == S and sum(RAC) == N: #When conditions are met sort and append
            RAC.sort()
            RAC.reverse()
            sample.append(RAC)
            print len(sample)
            
    return sample
    
    
def get_MLEs(RAC):
    '''Still not making this work at the moment.  MLE seems to be messing up'''
    varlst = [1, 2, 3]#I have been decreasing the number in this list. I think that having more numbers
    #is causing something to happen.  Not sure what, but it seems like that the more times that we
    # require the variances to be equal the less log normal the MLE becomes.
    
    while np.var(varlst, ddof = 1) > 0: # while the variance of varlst is greater than zero
        RAC = pln.get_rad_from_obs(RAC, 'pln') #get RAC from pln
        print RAC
        varlst.append(np.var(RAC, ddof =1)) # add the variance of the end RAC to the list
        varlst.pop(0) # remove the first number in the varlst 
        print np.var(varlst)
    
    print RAC    
    return RAC
    
    
N = 1000
S = 20
sample_size = 5

SLN = SimLogNorm(N, S, sample_size)


x = []
y = []

for RAC in SLN: #Placing SLN RAC values into lists
    y.extend(np.log(RAC))
    x.extend(range(len(RAC)))
    
MLE = get_MLEs(RAC) #Finding MLEs valus

plt.plot(np.log(MLE), color='0.3', lw=3, alpha = 0.6)

plt.hexbin(x, y, mincnt=1, gridsize = 20, bins = 'log', cmap=plt.cm.jet) #Generating Heat Map for SLN RAC
    
plt.xlim(0, S + 5)
plt.xlabel('Rank in abundance', fontsize=16)
plt.ylabel('log(abundance)', fontsize=16)

plt.savefig('/Users/Nathan_Hillis/SADModels/figures/Debug_Figs/Ploting_MLE_RACs/logNormal_MLEs_RACs_N='+str(N)+'_S='+str(S)+'.png', dpi=600, bbox_inches = 'tight', pad_inches=0.03)
plt.show()