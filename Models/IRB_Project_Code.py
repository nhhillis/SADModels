import numpy as np
from random import randrange
import matplotlib.pyplot as plt
import sys

sys.path.append('/Users/Nathan_Hillis/')



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
   
'''import csv
ObsRAC = []
with open('/Users/Nathan_Hillis/Desktop/IRB_Project/1_site_97.csv', 'r') as RAC:
    reader = csv.reader(RAC, delimiter = ',' , quoting = csv.QUOTE_NONE)
    for values in RAC:
        ObsRAC.append(values)

print ObsRAC
sys.exit()'''

ObsRAC = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,4,4,4,5,5,5,6,6,8,10,10,10,12,13,15,16,16,23,25,25,25,25,30,30,34,35,37,40,41,51,52,60,96,100,111,120,142,152,155,156,1000,2300]
ObsRAC.reverse()

                  
N = sum(ObsRAC)
S = len(ObsRAC)
sample_size = 50

SLN = SimLogNorm(N, S, sample_size)


x = []
y = []

for RAC in SLN: #Placing SLN RAC values into lists
    y.extend(np.log(RAC))
    x.extend(range(len(RAC)))
    



plt.plot(np.log(ObsRAC), color='0.3', lw=3, alpha = 0.6)

plt.hexbin(x, y, mincnt=1, gridsize = 20, bins = 'log', cmap=plt.cm.jet) #Generating Heat Map for SLN RAC
    
plt.xlim(0, S + 5)
plt.xlabel('Rank in abundance', fontsize=16)
plt.ylabel('log(abundance)', fontsize=16)

plt.savefig('/Users/Nathan_Hillis/Desktop/IRB_Project/Three_Site_N='+str(N)+'_S='+str(S)+'.png', dpi=600, bbox_inches = 'tight', pad_inches=0.03)
plt.show()