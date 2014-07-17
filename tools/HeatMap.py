import numpy as np
import matplotlib.pyplot as plt
#Three plots, one for random fraction, BRkstk, LogNorm


sample_size = 10000

s = 100
ab = []
ranks = []

for i in range(sample_size):
    
    RAC = np.random.logseries(0.9999, s).tolist()
    RAC.sort(reverse = True)

    ab.extend(RAC)
    ranks.extend(range(s))
    
fig = plt.figure()

plt.subplot(1,2,1)#Row, col, plot number
plt.hexbin(ranks, ab, bins = 'log', cmap=plt.cm.jet)

plt.subplot(1,2,2)
plt.hexbin(ranks,np.log(ab), bins ='log', cmap=plt.cm.jet)

plt.show()