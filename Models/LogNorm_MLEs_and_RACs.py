import numpy as np
from random import randrange
import matplotlib.pyplot as plt
import sys
import os

mydir = os.path.expanduser("~/Desktop/repos/SADModels/") # put the path to the repo here (e.g. Ken's desktop has a directory named "repos")

sys.path.append(mydir + "tools") # put a more explicit path here
import pln

sys.path.append(mydir + 'Analysis')
from AverageShape import AvgShape



"""
    Plotting SimLogNorm and MLEs:

    The intended order of operations (!BUT THIS IS STILL INCORRECT!):
    1. Draw a random RAC from any desired distribution (e.g. log-series, log-normal, geometric, etc.)
    2. Find the maximum likelihood expectation (MLE) for the log-normal, using the random RAC as an input 
    3. Get N and S from the log-normal MLE
    4. Get a random sample of simulated forms of the log-normal, using N and S as inputs
    5. Find the "average shape" from the random sample.
    
    What you (nathan) were doing:
    1. Picking N and S
    2. Get a random sample of simulated forms of the log-normal, using N and S as inputs
    3. Find the maximum likelihood expectation (MLE) for the log-normal, using the **last generated random RAC** as an input 
    4. plot the MLE and the heat map
    
    I realized that you were:
        1.) using only the last randomly generated RAC as the input for the log-normal MLE
        2.) getting the log-normal MLE after your random sample, meaning that the N of the MLE would probably not agree with the N of any RAC in your random sample
    
    
    
    ACTUAL ANSWER TO COMPARING SIMULATED LOG-NORMAL AND MLE FOR THE LOG-NORMAL:
    
    First, the Mistake: By iterating the log-normal on itself to stabilize the variance, I think that we were actually
    making it converge to (or approximate) the canonical form of the log-normal (which is usually defined by a
    mean and variance). I noticed that if S was, say, 20, that the MLE always ended up with a variance near 12.
    This is not what we want, and really, I can't be exactly sure what it actually achieved. That is, by trying
    to make the variance 'settle down', we ended up finding some sort of log-normal-like expectation for S. That
    would be neat, but as I said, I'm not it's what we actually achieved.
    
    And now, the answer:
    1. Choose N, S, and sample size
    2. Run SimLogNorm, then get average shape (RAC)
    3. Run get_LogNormMLE using RAC as the input
    4. Get N and S from the log-normal MLE (might not match that in #1)
    5. Repeat #2, using N and S from #4
    6. plot
    
    See Below or run this code 
    
    

"""

def SimLogNorm(N, S, sample_size):
    
    RACs = []  # 'sample' is a function. You don't want to give variables the same name as a function 
    
    while len(RACs) < sample_size:
        RAC = [N] #Initial 
        
        while len(RAC) < S:
            ind = randrange(len(RAC))
            v = RAC.pop(ind) # Removes randomly selected number from list RAC
            v1 = int(round(0.75 * v)) # split 75:25
            v2 = v - v1  # force all abundances to be integers 
            
            if v1 < 1 or v2 < 1: break # force min(RAC) to be > 1
                                            
            RAC.extend([v1, v2]) # add new values to RAC, increaseing len(RAC) by 1
            
        if len(RAC) == S and sum(RAC) == N: # When conditions are met sort and append
            RAC.sort()
            RAC.reverse()
            RACs.append(RAC)
            print len(RACs)
            
    return RACs
   
    
    
def get_LogNormMLE(RAC):
    varlst = [1, 2, 3] 
    
    VarOfVars = 1
    
    while VarOfVars > 0.01: # while the variance of varlst is greater than zero
        
        RAC = pln.get_rad_from_obs(RAC, 'pln') #get RAC from pln
        varlst.append(np.var(RAC, ddof =1)) # add the variance of the end RAC to the list
        varlst.pop(0) # remove the first number in the varlst 
        
        print varlst
        VarOfVars = np.var(varlst, ddof=1)
        break
        
    return RAC
    
    
sample_size = 100
N = 200
S = 20
RACs = SimLogNorm(N, S, sample_size)
RAC = AvgShape(RACs) # you (nathan) were leaving this out

MLE = get_LogNormMLE(RAC) #Finding MLE for log-normal for a given N and S (does not return N)

N = sum(MLE)
print 'N =',N,', S =', S

sample_size = 100
RACs = SimLogNorm(N, S, sample_size)

SimLogNorm = AvgShape(RACs) # you (nathan) were leaving this out

x = []
y = []

for RAC in RACs: #Placing SLN RAC values into lists
    y.extend(np.log(RAC))
    x.extend(range(len(RAC)))
    

print len(MLE), sum(MLE), len(RAC), sum(RAC)

plt.hexbin(x, y, mincnt=1, gridsize = 20, bins = 'log', cmap=plt.cm.jet) # Generating Heat Map

plt.plot(np.log(MLE), color='0.3', lw=3, label='MLE: N='+str(N)+', S='+str(S)) # Plot the MLE 

plt.plot(np.log(SimLogNorm), color='Lime', lw=3, label='Simulated N='+str(N)+', S='+str(S)) # Plot the simulated form

leg = plt.legend(loc=1,prop={'size':13}) # plot a legend
leg.draw_frame(False) # don't plot the legend's frame
    

plt.xlim(0, S + 5)
plt.xlabel('Rank in abundance', fontsize=16)
plt.ylabel('log(abundance)', fontsize=16)

#plt.savefig('/Users/Nathan_Hillis/SADModels/figures/Debug_Figs/Ploting_MLE_RACs/logNormal_MLEs_RACs_N='+str(N)+'_S='+str(S)+'.png', dpi=600, bbox_inches = 'tight', pad_inches=0.03)
plt.show()