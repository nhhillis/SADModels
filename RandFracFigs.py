from __future__ import division
import sys
import Models 
sys.path.append('/Users/Nathan_Hillis/SADModels/tools/')

sys.path.append('/Users/lisalocey/Desktop/SADModels/tools/')

import HeatMap
import matplotlib.pyplot as plt



N = 10000000
S = 20
sample_size = 1

fig = plt.figure()
""" The Broken Stick Model constrained by N and S """
ax = fig.add_subplot(3, 3, 1)
BrkStk = Models.SimBrokenStick(N, S, sample_size)
fig = HeatMap.RACHeatMap(fig, BrkStk)
plt.title('Broken Stick', fontsize = 13)
plt.xlabel('Rank')
plt.ylabel('Abundance')

print 'finished broken stick'

'''"""The Dominance Preemption constrained by N and S, excluding decimals """
ax = fig.add_subplot(3, 3, 2)  # Debug me
DPI = Models.DomPreInt(N, S, sample_size)
fig = HeatMap.RACHeatMap(fig, DPI)
plt.title('Dominance Preemption (Integer)', fontsize = 13)
plt.xlabel('Rank')
plt.ylabel('Abundance')
print 'finished dominance preemption (integers)' '''

""" The Dominance Preemption constrained by N and S, allowing decimals """
ax = fig.add_subplot(3, 3, 4)
DPF = Models.DomPreFloat(N, S, sample_size)
fig = HeatMap.RACHeatMap(fig, DPF)
plt.title('Dominance Preemption (Float)', fontsize = 13)
plt.xlabel('Rank')
plt.ylabel('Abundance')
print 'finished dominance preemption (decimals)' 

""" The Log-normal (75/25) constrained by N and S """
ax = fig.add_subplot(3, 3, 5)
SLN = Models.SimLogNorm(N, S, sample_size)
fig = HeatMap.RACHeatMap(fig, SLN)
plt.title('Log Normal', fontsize = 13)
plt.xlabel('Rank')
plt.ylabel('Abundance')
print 'finished lognormal'

""" Pareto (80/20) constrained by N and S """
ax = fig.add_subplot(3, 3, 7)
SP = Models.SimPareto(N, S, sample_size, integer=False)
fig = HeatMap.RACHeatMap(fig, SP)
plt.title('Pareto', fontsize = 13)
plt.xlabel('Rank')
plt.ylabel('Abundance')
print 'finished Pareto'

""" Simple random fraction constrained by N and S """
ax = fig.add_subplot(3, 3, 8)
SRF = Models.Sample_SimpleRandomFraction(N, S, sample_size)
fig = HeatMap.RACHeatMap(fig, SRF)
plt.title('Simple Random Fraction', fontsize = 13)
plt.xlabel('Rank')
plt.ylabel('Abundance')
print 'finished simple random fraction'

ax = fig.add_subplot(3, 3, 8)
DDF = Models.DomFloat(N, S, sample_size)
fig = HeatMap.RACHeatMap(fig, DDF)
plt.title('Dominance Decay (float)', fontsize = 13)
plt.xlabel('Rank')
plt.ylabel('Abundance')
print 'finished Dominance decay float'

plt.subplots_adjust(wspace=0.8, hspace=0.8)
plt.savefig('/Users/Nathan_Hillis/SADModels/Results/Figure')
plt.show()