from __future__ import division
import sys                                            
import numpy as np
from random import randrange
import math
import random
import itertools
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path
import csv


reader = csv.reader(open("sample_RAC.csv", "rb"), quoting=csv.QUOTE_ALL) # Reading in sample_RAC.
for row in reader:
    print row #getting TypeError: float() argument must be a string or a number when I try and plot'''


out=open("sample_RAC.csv","rb")         #A way to open the sample csv files...but gives cannot convert error
data=csv.reader(out)
data=[row for row in data]
out.close()
print data

RAC_plot = plt.plot(reader)
plt.ylabel('RAC')
plt.show()