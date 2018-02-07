#!/bin/python

import os
import matplotlib.pyplot as plt
import numpy as np

i=0
index=0
counter=0
cumcount=0
counthist = []
total=0.0
obs = 0.0
num = 0.0
numbuckets = 1500000
startvalue=0.0
endvalue=1500000.0
stepsize=0.0


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
#lines2 = f_temp2.readlines()
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
#print listrecord
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
print len(y_data)	
while(i<1025):
	z_data.append(float(y_data[i])/float(x_data[i]))
	i= i+1
print max(z_data)
if(startvalue > endvalue):
        num=startvalue
        startvalue=endvalue
        endvalue=num

stepsize=float((endvalue-startvalue)/numbuckets)

for i in range(0,numbuckets):
        counthist.append(0)

total = 0
counter = 0

for value in range(0,1025):
	obs = float(z_data[value])
        #print obs
        if obs > endvalue:
                counthist[numbuckets-1] += 1
                total += 1
                continue
        if obs < startvalue:
                counthist[0] += 1
		total += 1
                continue
        num = startvalue
        index = 0

        while num<obs:
                num += stepsize
		if(num<obs):
                        index += 1
        counthist[index] += 1
        total += 1


m_Data=[]
n_Data=[]

comcount = 0
for i in range(0,numbuckets):
        count = counthist[i];
        comcount += count;
        #print str(float(count)/float(total))+"\t"+str(float(comcount)/float(total))
        m_Data.append(float(comcount)/float(total))

n_Data=range(int(startvalue),int(endvalue),int(stepsize))

fig = plt.figure()
fig.suptitle('CDF-ADR(Inbound)', fontsize=14, fontweight='bold')
ax = fig.add_subplot(111)
fig.subplots_adjust(top=0.85)
ax.set_title('ADR in BPS')
plt.xlabel("bits per second")
plt.ylabel("CDF")
plt.grid(True)

ax.plot(n_Data,m_Data)
ax.axis([startvalue,endvalue,0,1])
#plt.test(2,2,'sdfasdfa')
plt.show()
