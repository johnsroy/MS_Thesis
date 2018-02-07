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
numbuckets = 370000
startvalue=0.0
endvalue=370000.0
stepsize=0.0

path='/Users/roysourish/Desktop/'
dirname2='d'
dirname1='inout_histogram_data'
listrecord = []
numList = 0
numList1=0
path1=path+'/'+dirname1
path2=path+'/'+dirname2
dirs1=os.listdir(path1)
dirs2=os.listdir(path2)
#print(files)
for subdirname in dirs1 :
        #print filename
        if(subdirname[0]=='.'):
                pass
        elif(os.path.isdir(path1+'/'+subdirname)):
                newpath1=path1+'/'+subdirname
                sondirs=os.listdir(newpath1)
                for sondir in sondirs:
                        #print newpath+sondir
                        if(sondir[0] == '.'):
                                pass
                        elif(os.path.isdir(newpath1+'/'+sondir)):
                                newsonpath1=newpath1+'/'+sondir
                                files1=os.listdir(newsonpath1)
                                print files1
                                for filename in files1:
                                        f_temp1=open(newsonpath1+'/'+filename,'r')
                                        lines1=f_temp1.readlines()
for subdirname1 in dirs2:
	if(subdirname[0]=='.'):
                pass
	elif(os.path.isdir(path2+'/'+subdirname1)):
                newpath2=path2+'/'+subdirname1
                sondirs1=os.listdir(newpath2)
                for sondir in sondirs1:
                        #print newpath+sondir
                        if(sondir[0] == '.'):
                                pass
                        elif(os.path.isdir(newpath2+'/'+sondir)):
                                newsonpath2=newpath2+'/'+sondir
                                files2=os.listdir(newsonpath2)
                                print files2
                                for filename in files2:
                                        f_temp2=open(newsonpath2+'/'+filename,'r')
                                        lines2=f_temp2.readlines()

listrecord = []
numList = 0
	
for line in lines2:
	line = line.strip('\n')
	listrecord.append(filter(None,line.split(' ')))
	list_temp = lines1[numList]
	#print list_temp
	list_temp = list_temp.strip('\n')
	listrecord[numList].append(filter(None, list_temp.split(' '))[0])
	numList += 1
	f_temp2.close()
f_temp1.close()
print listrecord

z_data=[]
a_data=[]
i=0
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

while(i<5001):
	z_data.append(float(y_data[i])/float(x_data[i]))
	i= i+1

if(startvalue > endvalue):
        num=startvalue
        startvalue=endvalue
        endvalue=num

stepsize=float((endvalue-startvalue)/numbuckets)

for i in range(0,numbuckets):
        counthist.append(0)

total = 0
counter = 0

for value in range(0,5001):
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
        print str(float(count)/float(total))+"\t"+str(float(comcount)/float(total))
        m_Data.append(float(comcount)/float(total))

n_Data=range(int(startvalue),int(endvalue),int(stepsize))

fig = plt.figure()
fig.suptitle('CDF-ADR(Outbound)', fontsize=14, fontweight='bold')
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

