import numpy as np
from random import randrange
import matplotlib.pyplot as plt
import sys
import os

mydir = os.path.expanduser("~Nathan_Hillis/SADModels/") # put the path to the repo here (e.g. Ken's desktop has a directory named "repos")

sys.path.append(mydir + "tools") # put a more explicit path here
import pln

sys.path.append(mydir + "Analysis")
from AverageShape import AvgShape



"""Code to compare SimLogNorm to the NPLogNorm to determine if the SimLogNorm code
is biased.
Process
1. Use NP.random.ln to generate 500 RACs
2. Find Average shape and plot
3. Get N and S from NPLN
4. Use N and S to run through SimLogNorm (x500) then plot as heat map"""

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
            #print len(RAC)
            
    return RACs
    
    
''' Going from mean to S and N:
    e^(mean) = e^(log(n/s))
    e^(mean) = N/S
    e^(mean) * S = N'''

'''Working through this one.  Still working on converting the logAB to AB. Also 
npLogNorm does not seem to be passing to SimLogNorm'''

def npLogNorm(mean, sigma, S, sample_size):#will need to change log(ab) to ab
    RAClst = []
    while len(RAClst) < sample_size:
        a = np.random.lognormal(mean, sigma, S) #calling np.lgnm
        a = np.log(a)
        a = a.tolist()
        a.sort()
        a.reverse()
        #conditional statement to kick out neg lists
        '''for i in a:     #iterate through nln
            c = np.log(i)
            b.append(c)  #add to b
            b.sort()'''
       
        RAClst.append(a)    #append transformed RAC to RACs
        
    return RAClst  

#mean = 100
S = 15
sample_size = 50

iRAC = SimLogNorm(100,S, sample_size) # use to get a reasonable sigma
mean = float(np.mean(iRAC))
print 'Mean =', mean

sigma = float(np.std(iRAC))#find sigma(standard deviation), 
print 'Sigma =', sigma

RAClst = npLogNorm(mean, sigma, S, sample_size)#Call npLogNorm fuction


NPRAC = AvgShape(RAClst) #find Avg shape of NP log norm
#print len(NPRAC)

N= sum(AvgShape(RAClst))
RACs = SimLogNorm(N, S, sample_size) #call SLN function 
RAC = AvgShape(RACs) # you (nathan) were leaving this out

print 'N =',N,', S =', S

#RACs = SimLogNorm(N, S, sample_size) #obtain SLN RACs

SimLogNorm = AvgShape(RACs) # you (nathan) were leaving this out

x = []
y = []

for RAC in RACs: #Placing SLN RAC values into lists
    y.extend(np.log(RAC))
    x.extend(range(len(RAC)))
     
plt.hexbin(x, y, mincnt=1, gridsize = 20, bins = 'log', cmap=plt.cm.jet) # Generating Heat Map

ranks = (range(len(NPRAC)))
print 'Ranks', len(ranks)
print 'NPRAC', NPRAC

plt.plot(ranks, np.log(NPRAC), color='0.3', lw=3, label='NPLogN: N='+str(N)+', S='+str(S)) # Plot the MLE 
plt.plot(np.log(SimLogNorm), color='Lime', lw=3, label='Simulated N='+str(N)+', S='+str(S)) # Plot the simulated form


leg = plt.legend(loc=1,prop={'size':13}) # plot a legend
leg.draw_frame(False) # don't plot the legend's frame
    

plt.xlim(0, S + 5)
plt.xlabel('Rank in abundance', fontsize=16)
plt.ylabel('log(abundance)', fontsize=16)

plt.savefig('/Users/Nathan_Hillis/SADModels/figures/Debug_Figs/NPLN_v_SimLN/logNormal_NPLog_V_Sim_N='+str(N)+'_S='+str(S)+'.png', dpi=600, bbox_inches = 'tight', pad_inches=0.03)
plt.show()