from __future__ import division
import sys
import Models 
sys.path.append('/Users/Nathan_Hillis/SADModels/tools/')

sys.path.append('/Users/lisalocey/Desktop/SADModels/tools/')

import HeatMap
import matplotlib.pyplot as plt



N = 1000
S = 50
sample_size = 120

fig = plt.figure()

ax = fig.add_subplot(3, 3, 1)
BrkStk = Models.SimBrokenStick(N, S, sample_size)
fig = HeatMap.RACHeatMap(fig, BrkStk)
plt.title('Broken Stick', fontsize = 13)
plt.xlabel('Rank')
plt.ylabel('Abundance')

print 'finished broken stick'

ax = fig.add_subplot(3, 2, 2)  # Debug me
DPI = Models.DomPreInt(N, S, sample_size)
fig = HeatMap.RACHeatMap(fig, DPI)
plt.title('Dominance Preemption (Integer)', fontsize = 10)
plt.xlabel('Rank')
plt.ylabel('Abundance')
print 'finished dominance preemption (integers)' 

ax = fig.add_subplot(3, 3, 4)
DPF = Models.DomPreFloat(N, S, sample_size)
fig = HeatMap.RACHeatMap(fig, DPF)
plt.title('Dominance Preemption (Float)', fontsize = 13)
plt.xlabel('Rank')
plt.ylabel('Abundance')
print 'finished dominance preemption (decimals)'

ax = fig.add_subplot(3, 3, 5)
SLN = Models.SimLogNorm(N, S, sample_size)
fig = HeatMap.RACHeatMap(fig, SLN)
plt.title('Log Noramal', fontsize = 13)
plt.xlabel('Rank')
plt.ylabel('Abundance')
print 'finished lognormal'

ax = fig.add_subplot(3, 3, 7)
SP = Models.SimPareto(N, S, sample_size, integer=False)
fig = HeatMap.RACHeatMap(fig, SP)
plt.title('Pareto', fontsize = 13)
plt.xlabel('Rank')
plt.ylabel('Abundance')
print 'finished Pareto'

ax = fig.add_subplot(3, 3, 8)
SRF = Models.Sample_SimpleRandomFraction(N, S, sample_size)
fig = HeatMap.RACHeatMap(fig, SRF)
plt.title('Simple Random Fraction', fontsize = 13)
plt.xlabel('Rank')
plt.ylabel('Abundance')
print 'finished simple random fraction'

plt.subplots_adjust(wspace=0.8, hspace=0.8)
plt.savefig('Figure_1')
plt.show()