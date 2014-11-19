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
with open('/Users/Nathan_Hillis/Desktop/IRB_Project/All_sites_97.csv', 'r') as RAC:
    reader = csv.reader(RAC, delimiter = ',' , quoting = csv.QUOTE_NONE)
    for values in RAC:
        ObsRAC.append(values)

print ObsRAC
sys.exit()'''

ObsRAC = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,4,4,4,5,5,5,5,6,7,7,8,8,8,8,9,9,9,9,9,10,10,11,12,12,13,14,14,15,15,17,18,18,18,20,20,23,23,24,25,26,27,28,31,34,35,37,38,38,39,40,44,47,47,48,50,50,56,61,61,63,63,66,67,67,69,81,84,87,90,99,100,105,106,106,120,136,140,142,149,152,155,161,181,205,208,219,220,253,269,306,315,330,348,365,383,394,394,420,420,428,447,459,462,487,500,518,539,574,586,614,644,675,713,737,739,744,854,918,1000,1035,1043,1044,1044,1052,1074,1124,1176,1212,1255,1305,1323,1465,1469,1501,1765,1910,1965,2094,2342,2367,2373,2526,2610,2877,3060,3296,3453,3495,3826,4592,4608,6434,6489,9015,9345,10673,11905,14266,15092,24258,45770,64560,72225,440821]
print len(ObsRAC), sum(ObsRAC)
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

plt.savefig('/Users/Nathan_Hillis/Desktop/IRB_Project/All_Site_N='+str(N)+'_S='+str(S)+'.png', dpi=600, bbox_inches = 'tight', pad_inches=0.03)
plt.show()