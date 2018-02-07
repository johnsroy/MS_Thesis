#!/bin/python

import os
import matplotlib.pyplot as plt
import numpy as np
path1='/Users/roysourish/Desktop/'
filename1=path1+'00'
path2='/Users/roysourish/Desktop/'
filename2=path2+'11'
z_data=[]
a_data=[]
i=0
f_temp1=open(filename1, 'r')
f_temp2=open(filename2, 'r')

lines1 = f_temp1.readlines()
lines2 = f_temp2.readlines()
#print lines2

listrecord = []
numList = 0
for line in lines1:
	line = line.strip('\n')
	listrecord.append(filter(None,line.split(' ')))
	f_temp2=open(filename2, 'r')
	list_temp = f_temp2.readlines()[numList]
	#print list_temp
	list_temp = list_temp.strip('\n')
	listrecord[numList].append(filter(None, list_temp.split(' '))[1])
	numList += 1
	f_temp2.close()
f_temp1.close()
#f_temp2.close()
 
print listrecord
print max(listrecord[0])
print max(listrecord[1])
x_data = []
y_data = []
for member in listrecord:
	if(member[0] == '-'):
		continue
		member[0] = 0
	if(member[1] == '-'):
		continue
		member[1] = 0
	x_data.append(member[0])
	y_data.append(member[1])

y_data= (np.array(y_data, dtype=int)*8)
	

while(i<1025):
	z_data.append(float(y_data[i])/float(x_data[i]))
	i= i+1

#print z_data
a_data=range(len(z_data))
fig = plt.figure()
plt.plot(a_data,z_data)
plt.ylabel('Bits/sec')
plt.xlabel('Rate')
fig.suptitle('Average Data Rate for Inbound connections(bps)',fontsize=10, fontweight='bold')
plt.show()	
