from __future__ import division
import sys                                            
import numpy as np
from random import randrange
import math
import random

"""This script codes Broken Stick models """
    
# Simultaneous or Sequential? We should probably try to do both. -Ken

def SimBrokenStick(N, S, sample_size):
    """
    A function to generate random samples of the simultaneous Broken Stick Model
    of MacArthur 1957 or 1961. We need the actual citation.
    
    N  :  Total abundance, i.e., number of individuals
    S  :  Species richness, i.e., number of species
    sample_size  :  number of rank-abundance vectors to generate
    """    
    
    # Do some stuff
    
    return
     
#################  Notes 'N Stuff  #############################################
# Try to keep your lines under 80 or so characters. Something of a programming 
# convention to help readability. -Ken 
#
# Just some thoughts on how to make this work.  Create list of range of N, then 
# make S - 1 random divisions in range of N, repeat sample_size times. -Nathan
#
# Right, first we have to get our indices. Which you've figured out. -Ken
# Then, we can split a list of N 1's at those indices points. A few rules do 
# apply, e.g. 0 can't be one of the indices. -Ken

# Say your simultanesouly drawn indices are [2, 9, 5]. Here, simultaneous means
# those numbers were drawn without replacement, i.e., were not allowed to
# can't draw any number twice. Once you sort those numbers then you can...
# 
# Hint: Let N = 15, S = 4, and SortedIndices = [2, 5, 9]
# So: oo|ooo|oooo|oooooo  = [2, 3, 4, 6] -> N = 15 and S = 4
# 2-0 = 2  :  5-2 = 3  :  9-5 = 4  :  15-9 = 6
#
# i now have values that represent divisions in N not the number of individuals
# in each species -Nathan
# 
# You got on the right track very quickly. Nice job.
###########################  END  ############################################## 


N = 20
S = 4
sample_size = 10

n = range(N) # creates range of N 
print n
s = S-1 #number of divisions(species minus 1)

cuts = random.sample(set(n), s) #randomly selecting s number of items in range 
cuts.sort(reverse = True) #sorts numbers
print cuts #gives where the range is split 
