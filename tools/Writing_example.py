bla = [[0,1,2,3,4,5],[6,7,8,9,10,11]]

with open('bla2.txt', 'w+') as text:
    for item in bla:
  	for i in item:
  	     text.write("%s\n" % i)