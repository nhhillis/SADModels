
#This code calculates diversity and Evenness
#This code is in the beginning stages 
#Simpson's index = D = sum(ni[ni-1])/(N[N-1])
######Steps######
#Select each species as n, for each n multiply n * n-1
#sum all n(n-1) then divide by N(N-1)
#D = Simpson's Index
#SD = Simpson's index of Diversity
#Evns = Simpson's measure of Evenness

#def Simpson(my_data):
    
my_data = [1,2,3,4,10]
my_data1 = [float(i) for i in my_data]
d = []
N = sum(my_data1)
N1 = N*(N-1)

for i in my_data1:
    n = my_data1.pop()
    n1 = n * (n-1)
    d.append(n1)
        
n2 = sum(d)

D = n2/N1
SD = 1 - D
D1 = 1 / D
Evns = D1/len(my_data1)

print 'Simpson\'s Index---', D
print 'Simpson\'s Index of Diversity---', SD
print 'Simpson\'s Index Reciprocal---', D1
print 'Simpson\'s Measure of Evenness---',Evns