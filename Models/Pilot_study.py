import csv
import numpy as np
from random import randrange
import matplotlib.pyplot as plt
import math
import sys
import os
mydir = os.path.expanduser("~Nathan_Hillis/SADModels/")
sys.path.append(mydir + "Analysis")
from AverageShape import AvgShape

'''Comparing Obsd SADs to simlognorm'''

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
    
def read_csv(filepath):
    SADs = []
    with open(filepath, 'U') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:  
            SAD = [int(i) for i in row]
            SADs.append(SAD)
    return SADs



def get_predx(SADs):
    
    for sad in SADs:
        
        sad.reverse()
        print sad
        N = sum(sad)
        S = len(sad)
        sample_size = 100
        
        prdSAD = AvgShape(SimLogNorm(N, S, sample_size))
        print prdSAD
        
    return prdSAD
    return sad

def graph_SAD(SADs):
    for sad in SADs:
        rank = range(len(sad))
        sad = np.log(sad)
        plt.plot(rank, sad) 
    plt.show()
    
SADs = read_csv('/Users/Nathan_Hillis/Dropbox/Nathan_Hillis/Data/Sample_data.csv')
RACs = get_predx(SADs)
graph_SAD(SADs)

'''print len(RACs[0])

x1 = len(RACs[0])
x2 = len(RACs[1])
x3 = len(RACs[2])
x4 = len(RACs[3])
x5 = len(RACs[4])
x6 = len(RACs[5])

y1 = sum(RACs[0])
y2 = sum(RACs[1])
y3 = sum(RACs[2])
y4 = sum(RACs[3])
y5 = sum(RACs[4])
y6 = sum(RACs[5])

plt.subplot(6, 1, 1)
plt.plot(x1, y1, 'yo-')
plt.title('A tale of 2 subplots')
plt.ylabel('Damped oscillation')

plt.subplot(6, 1, 2)
plt.plot(x2, y2, 'r.-')
plt.xlabel('time (s)')
plt.ylabel('Undamped')

plt.subplot(6, 1, 3)
plt.plot(x3, y3, 'r.-')
plt.xlabel('')
plt.ylabel('')

plt.subplot(6, 2, 1)
plt.plot(x2, y2, 'r.-')
plt.xlabel('time (s)')
plt.ylabel('Undamped')

plt.subplot(6, 2, 2)
plt.plot(x2, y2, 'r.-')
plt.xlabel('time (s)')
plt.ylabel('Undamped')

plt.subplot(6, 2, 3)
plt.plot(x2, y2, 'r.-')
plt.xlabel('time (s)')
plt.ylabel('Undamped')
plt.show()'''


    
