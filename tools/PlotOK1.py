from __future__ import division
import matplotlib.pyplot as plt

import csv
import sys
sys.path.append('SADModels/Data')
'''This script is currently still being worked out.  Trying to import 
my data as a csv file.  Canopy is not finding my data file Oklahoma.csv'''

#with open('Oklahoma.csv', 'rb''') as csvfile:
  #   reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    # for row in reader:
      #  print(', '.join(row))

    
OK_1_13 = [38, 38, 29, 19, 17, 17, 15, 13, 12, 12, 11 ,10, 9, 9, 9, 8, 8, 8, 8, 6, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
OK_1_12a = [2, 1, 8, 4, 1, 4, 1, 4, 3, 4, 1, 1, 6, 3, 1, 1, 2, 5, 2, 5, 7, 2, 30, 3, 6, 6, 3, 2, 16, 3, 40, 5, 6, 7, 15, 3, 15, 38, 1, 6, 4, 3, 1, 1, 28, 4, 8, 2, 2, 7, 2, 2, 9, 14, 13, 8, 15, 3, 9]
OK_1_12 = OK_1_12a.sort(reverse = True)
OK_1_11 = [46, 42, 29, 18, 15, 13, 12, 11, 11, 10, 10, 10, 8, 6, 6, 6, 5, 5, 5, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

fig, ax = plt.subplots()
ax.plot(OK_1_13, label='2013')
ax.plot(OK_1_12a, label='2012')
ax.plot(OK_1_11, label='2011')

legend = ax.legend(loc='upper center', shadow=True)
frame  = legend.get_frame()
frame.set_facecolor('0.90')

for label in legend.get_texts():
    label.set_fontsize('large')

for label in legend.get_lines():
    label.set_linewidth(1.5)  # the legend line width
plt.xlabel('Rank')
plt.ylabel('Abundance')
plt.title('BBS OK Route_1')
plt.show()





