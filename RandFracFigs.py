from __future__ import division
import sys
import Models 
sys.path.append('/Users/Nathan_Hillis/SADModels/tools/')

sys.path.append('/Users/lisalocey/Desktop/SADModels/tools/')

import HeatMap
import matplotlib.pyplot as plt



N = 1000
S = 50
sample_size = 200

fig = plt.figure()

ax = fig.add_subplot(3, 3, 1)
BrkStk = Models.SimBrokenStick(N, S, sample_size)
fig = HeatMap.RACHeatMap(fig, BrkStk)
plt.title('Broken Stick', fontsize = 10)
plt.xlabel(...
plt.ylabel(...

print 'finished broken stick'

#ax = fig.add_subplot(3, 2, 2)  # Debug me
#DPI = Models.DomPreInt(N, S, sample_size)
#fig = HeatMap.RACHeatMap(fig, DPI)
#print 'finished dominance preemption (integers)'

ax = fig.add_subplot(3, 3, 4)
DPF = Models.DomPreFloat(N, S, sample_size)
fig = HeatMap.RACHeatMap(fig, DPF)
print 'finished dominance preemption (decimals)'

ax = fig.add_subplot(3, 3, 5)
SLN = Models.SimLogNorm(N, S, sample_size)
fig = HeatMap.RACHeatMap(fig, SLN)
print 'finished lognormal'

ax = fig.add_subplot(3, 3, 7)
SP = Models.SimPareto(N, S, sample_size, integer=False)
fig = HeatMap.RACHeatMap(fig, SP)
print 'finished Pareto'

ax = fig.add_subplot(3, 3, 8)
SRF = Models.Sample_SimpleRandomFraction(N, S, sample_size)
fig = HeatMap.RACHeatMap(fig, SRF)
print 'finished simple random fraction'

plt.subplots_adjust(wspace=0.4, hspace=0.4)
plt.savefig(...
plt.show()