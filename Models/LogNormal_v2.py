import numpy as np
from random import randrange, seed
import matplotlib.pyplot as plt
import sys

sys.path.append('/Users/Nathan_Hillis/SADModels/tools/')

import macroeco_distributions  # code that provides maximum likelihood 
# predictions for SAD models
import pln # importing the Poisson Lognormal from macroeco_distributions


#from macroeco_distributions import pln # code that provides maximum likelihood 
# predictions for SADs. Import the Poisson Lognormal from macroeco_distributions


def SimLogNorm(N, S, sample_size):
    '''Working to fix bug @ 'if v1 < 1...' trying to create list of broken RACs
    to then determine their effect.'''
    #N = 
    #S = 
    sample = []
    
    while len(sample) < sample_size:
        RAC = [0.75*N, 0.25*N] #Initial N is split 75:25
       
        
        while len(RAC) < S:
            ind = randrange(len(RAC)) 
            v = RAC.pop(ind) # Removes randomly selected number from list RAC
            v1, v2 = int(round(0.75 * v)), v - int(round(0.75 * v)) # forcing all abundance, rounding 
                                                                    # values to be integers
            
            if v1 < 1 or v2 < 1: break
                                            
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
        sample.append(np.var(RAC, ddof = 1))
        print 'MLEs:', len(sample)
    
    plt.plot(sample)
    #plt.show()
    return sample


fig = plt.figure()  # declare a figure object
ax = plt.subplot(1,1,1) # declare an axis object

S = 20  # Number of species, i.e., species richness
#RAC = [15, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
RAC = np.random.logseries(0.99, S) # a random draw from the log-series. Note,
# we are only constraining S here. We aren't telling it to give us a certain
# number of individuals. Then, convert the numpy array to a Python list...
RAC = RAC.tolist()
RAC.sort()
RAC.reverse()

""" Why did we make a random draw from the log-series when we are actually
interested in the lognormal?  Unlike other models, the lognormal will not give a
prediction for the SAD based on N and S. Instead, it needs the average abundance
and variance. So, we make a random draw from a log-series distribution to 
generate a random SAD. This could actually be from any of various statistical
distributions or SAD models. 

Once we have a random RAD we 1.) feed the mean and variance into our log-normal
maximum likelihood expectation (MLE) function, and then 2.) feed the N and S of
that log-normal into our log-normal random fraction function. 

So, while the log-normal random fraction function is based on 75/25 random
fractions, the MLE function is based on the average abundance and the variance. 
Consequently, it is impressive if they match up. """


MLE_RACs = get_MLEs(RAC, 50)
N = 0
for lst in MLE_RACs:
    N, S = sum(MLE_RACs[0]), len(MLE_RACs[0])
    print N, S, lst, np.var(lst, ddof = 1)
    # because the PLN only takes the avg
    # abundance and variance, the resulting expected form will have a different N
    # and S than the log-series RAC that provided the starting average abundance and 
    # variance.
    
#sys.exit()

RACs = SimLogNorm(N, S, 20) # Use the random fraction function
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

plt.savefig('/Users/Nathan_Hillis/SADModels/figures/Debug_Figs/logNormal_N='+str(N)+'_S='+str(S)+'.png',
                    dpi=600, bbox_inches = 'tight', pad_inches=0.03)
plt.close()

plt.show()