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
    
    
def get_MLEs(RAC, sample_size):
    
    sample = []
    while len(sample) < sample_size:
        RAC = pln.get_rad_from_obs(RAC, 'pln')
        sample.append(RAC)
        print 'MLEs:', len(sample)
    
   #plt.plot(sample)
    #plt.show()
    return sample
N = 300
S = 50
sample_size = 10
SLN = SimLogNorm(N, S, sample_size)
#print SLN

x = []
y = []
for RAC in SLN:
    y.extend(np.log(RAC))
    x.extend(range(len(RAC)))
    
MLE_RACs = get_MLEs(RAC, 20)
print MLE_RACs
'''N = 0
for lst in MLE_RACs:
    N, S = sum(MLE_RACs[0]), len(MLE_RACs[0])
    print N, S, lst, np.var(lst, ddof = 1)'''

fig = plt.figure()  # declare a figure object  
  
for RAC in MLE_RACs:
    plt.plot(np.log(RAC), color='0.3', lw=3, alpha = 0.6)

fig = PlotAvgShape(fig, RAC) 
    
plt.hexbin(x, y, mincnt=1, gridsize = 20, bins = 'log', cmap=plt.cm.jet)
    
plt.xlim(0, len(RAC))
plt.xlabel('Rank in abundance', fontsize=16)
plt.ylabel('log(abundance)', fontsize=16)

plt.savefig('/Users/Nathan_Hillis/SADModels/figures/Debug_Figs/Ploting_MLE_RACs/logNormal_MLEs_RACs_N='+str(N)+'_S='+str(S)+'.png', dpi=600, bbox_inches = 'tight', pad_inches=0.03)
plt.show()