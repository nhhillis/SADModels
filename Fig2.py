from __future__ import division
import sys
import numpy as np
import matplotlib.pyplot as plt

sys.path.append('Models/')
import Models
sys.path.append('tools/')
import Indices


""" Github commands
    
    1. git pull: pull = fetch + merge
    2. You would change some code
    3. git add --all: this adds your changes to your local repo (i.e. master)
    4. git commit -m "I did some stuff -NH"
    5. git push: this 'pushes' the changes to your online repo
    
"""



rel = True
fig = plt.figure()
title = 'log(%N)'


""" This chunk of code generates the first column. N will stay constant. S 
    will change. """

N = 3000
Ss = [4, 16, 32, 64, 128, 256, 512, 1024, 2042]

N = 1000
Ss = [10, 20, 40, 80, 160, 320, 640]


# S = 50
# Ns = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]



sample_size = 4

BSsample = []
LNsample = []
Psample = []
DDsample = []
DPsample = []
RFsample = []

BS_AvgDominance = []
BS_AvgDiversity = []

LN_AvgDominance = []
LN_AvgDiversity = []

P_AvgDominance = []
P_AvgDiversity = []

RF_AvgDominance = []
RF_AvgDiversity = []

DD_AvgDominance = []
DD_AvgDiversity = []

DP_AvgDominance = []
DP_AvgDiversity = []


ax = fig.add_subplot(3, 3, 1)
# this for loop also generates RAC samples for N across all S, and generates all needed index values
for S in Ss:
#for N in Ns:
        
    """ Get RAC samples from each model """
    BSsample = Models.SimBrokenStick(N, S, sample_size, rel)
    BS_AvgEv = Indices.GetAvgEvenness(BSsample)
    BS_AvgDominance.append(Indices.GetAvgDominance(BSsample))
    BS_AvgDiversity.append(Indices.GetAvgDiversity(BSsample))
    if S == min(Ss): plt.scatter([S],[BS_AvgEv], color='Lime', label='Broken Stick') 
    plt.scatter([S],[BS_AvgEv], color='Lime')
    print 'finished broken stick'
    
    LNsample = Models.SimLogNormFloat(N, S, sample_size, rel)
    LN_AvgEv = Indices.GetAvgEvenness(LNsample)
    LN_AvgDominance.append(Indices.GetAvgDominance(LNsample))
    LN_AvgDiversity.append(Indices.GetAvgDiversity(LNsample))
    if S == min(Ss): plt.scatter([S],[LN_AvgEv], color='Cyan', label='Log-normal')
    plt.scatter([S],[LN_AvgEv], color='Cyan')
    print 'finished log normal'
    
    Psample = Models.SimParetoFloat(N, S, sample_size, rel)
    P_AvgEv = Indices.GetAvgEvenness(Psample)
    P_AvgDominance.append(Indices.GetAvgDominance(Psample))
    P_AvgDiversity.append(Indices.GetAvgDiversity(Psample))
    if S == min(Ss): plt.scatter([S],[P_AvgEv], color= 'SpringGreen', label='Pareto')
    plt.scatter([S],[P_AvgEv], color= 'SpringGreen')
    print 'finished Pareto'
    
    DDsample = Models.DomDecayFloat(N, S, sample_size, rel)
    DD_AvgEv = Indices.GetAvgEvenness(DDsample)
    DD_AvgDominance.append(Indices.GetAvgDominance(DDsample))
    DD_AvgDiversity.append(Indices.GetAvgDiversity(DDsample))
    if S == min(Ss): plt.scatter([S],[DD_AvgEv], color='Magenta', label='Dominance Decay')
    plt.scatter([S],[DD_AvgEv], color='Magenta')
    print 'finished Dominance Decay'
    
    DPsample = Models.DomPreFloat(N, S, sample_size, rel)
    DP_AvgEv = Indices.GetAvgEvenness(DPsample)
    DP_AvgDominance.append(Indices.GetAvgDominance(DPsample))
    DP_AvgDiversity.append(Indices.GetAvgDiversity(DPsample))
    if S == min(Ss): plt.scatter([S],[DP_AvgEv], color='DeepSkyBlue', label='Dominance Preemption')
    plt.scatter([S],[DP_AvgEv], color='DeepSkyBlue')
    print 'finished Dominance Preemption'
    
    RFsample = Models.Sample_SimpleRandomFraction(N, S, sample_size, rel)
    RF_AvgEv = Indices.GetAvgEvenness(RFsample)
    RF_AvgDominance.append(Indices.GetAvgDominance(RFsample))
    RF_AvgDiversity.append(Indices.GetAvgDiversity(RFsample))
    if S == min(Ss): plt.scatter([S],[RF_AvgEv], color='Maroon', label='Random Fraction', alpha=0.9)
    plt.scatter([S],[RF_AvgEv], color='Maroon', alpha=0.9)
    print 'finished random fraction'
    
    

leg = plt.legend(loc=1, prop={'size':5})
leg.draw_frame(False)
        
leg.get_frame().set_alpha(0.0)
for text in leg.get_texts():
    text.set_color('k')

plt.title('N = 1000', fontsize=14)     
plt.xlabel('S')
plt.ylabel('Evenness')  
plt.tick_params(axis='both', which='major', labelsize=5)
#plt.show()

####################### Plot 2 ############   
ax = fig.add_subplot(3, 3, 4)

""" Get Average Evenness (Simpsons) from each model """
plt.scatter(Ss, BS_AvgDominance, color='Lime', label='Broken Stick') 
    
plt.scatter(Ss, LN_AvgDominance, color='Cyan', label='Log-normal')
    
plt.scatter(Ss, P_AvgDominance, color= 'SpringGreen', label='Pareto')

plt.scatter(Ss, DD_AvgDominance, color='Magenta', label='Dominance Decay')

plt.scatter(Ss, DP_AvgDominance, color='DeepSkyBlue', label='Dominance Preemption')

plt.scatter(Ss, RF_AvgDominance, color='Maroon', label='Random Fraction', alpha=0.9)

plt.xlabel('S')
plt.ylabel('Dominance')
plt.tick_params(axis='both', which='major', labelsize=5)
plt.subplots_adjust(wspace=0.4, hspace=0.4)
#plt.show()
                        
            
####################### Plot 3 ############   
ax = fig.add_subplot(3, 3, 7)

""" Get Average Diversity from each model """
plt.scatter(Ss, BS_AvgDiversity, color='Lime', label='Broken Stick') 
    
plt.scatter(Ss, LN_AvgDiversity, color='Cyan', label='Log-normal')
    
plt.scatter(Ss, P_AvgDiversity, color= 'SpringGreen', label='Pareto')

plt.scatter(Ss, DD_AvgDiversity, color='Magenta', label='Dominance Decay')

plt.scatter(Ss, DP_AvgDiversity, color='DeepSkyBlue', label='Dominance Preemption')

plt.scatter(Ss, RF_AvgDiversity, color='Maroon', label='Random Fraction', alpha=0.9)

plt.xlabel('S')
plt.ylabel('Diversity')
plt.tick_params(axis='both', which='major', labelsize=5)
plt.subplots_adjust(wspace=0.4, hspace=0.4)
#plt.show()   

############################################
           ####################### Plot 4 ############   
           

S = 50
Ns = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
sample_size = 4

BSsample = []
LNsample = []
Psample = []
DDsample = []
DPsample = []
RFsample = []

BS_AvgDominance = []
BS_AvgDiversity = []

LN_AvgDominance = []
LN_AvgDiversity = []

P_AvgDominance = []
P_AvgDiversity = []

RF_AvgDominance = []
RF_AvgDiversity = []

DD_AvgDominance = []
DD_AvgDiversity = []

DP_AvgDominance = []
DP_AvgDiversity = []


ax = fig.add_subplot(3, 3, 2)
# this for loop also generates RAC samples for N across all S, and generates all needed index values
for N in Ns:
#for N in Ns:
        
    """ Get RAC samples from each model """
    BSsample = Models.SimBrokenStick(N, S, sample_size, rel)
    BS_AvgEv = Indices.GetAvgEvenness(BSsample)
    BS_AvgDominance.append(Indices.GetAvgDominance(BSsample))
    BS_AvgDiversity.append(Indices.GetAvgDiversity(BSsample))
    if N == min(Ns): plt.scatter([N],[BS_AvgEv], color='Lime', label='Broken Stick') 
    plt.scatter([N],[BS_AvgEv], color='Lime')
    print 'finished broken stick'
    
    LNsample = Models.SimLogNormFloat(N, S, sample_size, rel)
    LN_AvgEv = Indices.GetAvgEvenness(LNsample)
    LN_AvgDominance.append(Indices.GetAvgDominance(LNsample))
    LN_AvgDiversity.append(Indices.GetAvgDiversity(LNsample))
    if N == min(Ns): plt.scatter([N],[LN_AvgEv], color='Cyan', label='Log-normal')
    plt.scatter([N],[LN_AvgEv], color='Cyan')
    print 'finished log normal'
    
    Psample = Models.SimParetoFloat(N, S, sample_size, rel)
    P_AvgEv = Indices.GetAvgEvenness(Psample)
    P_AvgDominance.append(Indices.GetAvgDominance(Psample))
    P_AvgDiversity.append(Indices.GetAvgDiversity(Psample))
    if N == min(Ns): plt.scatter([N],[P_AvgEv], color= 'SpringGreen', label='Pareto')
    plt.scatter([N],[P_AvgEv], color= 'SpringGreen')
    print 'finished Pareto'
    
    DDsample = Models.DomDecayFloat(N, S, sample_size, rel)
    DD_AvgEv = Indices.GetAvgEvenness(DDsample)
    DD_AvgDominance.append(Indices.GetAvgDominance(DDsample))
    DD_AvgDiversity.append(Indices.GetAvgDiversity(DDsample))
    if N == min(Ns): plt.scatter([N],[DD_AvgEv], color='Magenta', label='Dominance Decay')
    plt.scatter([N],[DD_AvgEv], color='Magenta')
    print 'finished Dominance Decay'
    
    DPsample = Models.DomPreFloat(N, S, sample_size, rel)
    DP_AvgEv = Indices.GetAvgEvenness(DPsample)
    DP_AvgDominance.append(Indices.GetAvgDominance(DPsample))
    DP_AvgDiversity.append(Indices.GetAvgDiversity(DPsample))
    if N == min(Ns): plt.scatter([N],[DP_AvgEv], color='DeepSkyBlue', label='Dominance Preemption')
    plt.scatter([N],[DP_AvgEv], color='DeepSkyBlue')
    print 'finished Dominance Preemption'
    
    RFsample = Models.Sample_SimpleRandomFraction(N, S, sample_size, rel)
    RF_AvgEv = Indices.GetAvgEvenness(RFsample)
    RF_AvgDominance.append(Indices.GetAvgDominance(RFsample))
    RF_AvgDiversity.append(Indices.GetAvgDiversity(RFsample))
    if N == min(Ns): plt.scatter([N],[RF_AvgEv], color='Maroon', label='Random Fraction', alpha=0.9)
    plt.scatter([N],[RF_AvgEv], color='Maroon', alpha=0.9)
    print 'finished random fraction'
    
    

leg = plt.legend(loc=1, prop={'size':5})
leg.draw_frame(False)
        
leg.get_frame().set_alpha(0.0)
for text in leg.get_texts():
    text.set_color('k')

plt.title('S = 50', fontsize=14)     
plt.xlabel('N')
plt.ylabel('Evenness')  
plt.tick_params(axis='both', which='major', labelsize=5)
#plt.show()         

            
####################### Plot 5 ############   
ax = fig.add_subplot(3, 3, 5)

""" Get Average Evenness (Simpsons) from each model """
plt.scatter(Ns, BS_AvgDominance, color='Lime', label='Broken Stick') 
    
plt.scatter(Ns, LN_AvgDominance, color='Cyan', label='Log-normal')
    
plt.scatter(Ns, P_AvgDominance, color= 'SpringGreen', label='Pareto')

plt.scatter(Ns, DD_AvgDominance, color='Magenta', label='Dominance Decay')

plt.scatter(Ns, DP_AvgDominance, color='DeepSkyBlue', label='Dominance Preemption')

plt.scatter(Ns, RF_AvgDominance, color='Maroon', label='Random Fraction', alpha=0.9)

plt.xlabel('N')
plt.ylabel('Dominance')
plt.tick_params(axis='both', which='major', labelsize=5)
plt.subplots_adjust(wspace=0.4, hspace=0.4)
#plt.show()


           
 ####################### Plot 6############   
ax = fig.add_subplot(3, 3, 8)

""" Get Average Diversity from each model """
plt.scatter(Ns, BS_AvgDiversity, color='Lime', label='Broken Stick') 
    
plt.scatter(Ns, LN_AvgDiversity, color='Cyan', label='Log-normal')
    
plt.scatter(Ns, P_AvgDiversity, color= 'SpringGreen', label='Pareto')

plt.scatter(Ns, DD_AvgDiversity, color='Magenta', label='Dominance Decay')

plt.scatter(Ns, DP_AvgDiversity, color='DeepSkyBlue', label='Dominance Preemption')

plt.scatter(Ns, RF_AvgDiversity, color='Maroon', label='Random Fraction', alpha=0.9)

plt.xlabel('N')
plt.ylabel('Diversity')
plt.tick_params(axis='both', which='major', labelsize=5)
plt.subplots_adjust(wspace=0.4, hspace=0.4)
plt.show()   
                        
            
                       