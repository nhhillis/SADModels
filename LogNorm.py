import numpy as np
import random
from random import randrange, seed
import matplotlib.pyplot as plt
import sys

sys.path.append('/Users/lisalocey/Desktop/RareBio/global/GenAnalysis/tools/')
import macroeco_distributions
import pln


def SimLogNorm(N, S, sample_size, integer=False):
    
    sample = []
    
    for i in range(sample_size): 
        RAC = [0.75*N, 0.25*N]
        
        while len(RAC) < S:
            ind = randrange(len(RAC))
            v = RAC.pop(ind)
            v1, v2 = [0.75 * v, v - 0.75 * v]
            RAC.extend([v1, v2])       
                        
        if integer == True:    
            if sum(RAC) !=N or len(RAC) != S:
                print 'Incorrect N and S: N=',sum(RAC),' S=', len(RAC)
                sys.exit()
        elif integer == False:
            if len(RAC) != S:
                print 'Incorrect S:', len(RAC)
                sys.exit()
        else: 
            print 'Integer values need to be either \'False\' or \'True\''
            sys.exit()
       
        RAC.sort()
        RAC.reverse()
        sample.append(RAC)
    
    return sample




fig = plt.figure()
ax = plt.subplot(1,1,1)

S = 500
RAD = np.random.logseries(0.99, S)
RAD.tolist()

RAD = pln.get_rad_from_obs(RAD, 'pln')
print sum(RAD), len(RAD) 
RADs = SimLogNorm(sum(RAD), len(RAD), 10000)
print sum(RADs[0]), len(RADs[0]) 

x = []
y = []

for RAD in RADs:
    seed()
    y.extend(np.log(RAD))
    x.extend(range(len(RAD)))

plt.hexbin(x, y, mincnt=1, bins = 'log', cmap=plt.cm.jet)
plt.plot(np.log(RAD), color='k', lw=4)
plt.xlim(0, S)

plt.xlabel('Rank in abundance', fontsize=16)
plt.ylabel('log(abundance)', fontsize=16)

plt.savefig('/Users/lisalocey/Desktop/logNormal2.png', dpi=600, bbox_inches = 'tight', pad_inches=0.03)
plt.show()