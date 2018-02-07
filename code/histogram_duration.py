#!/bin/python
#python script used to draw a CDF to illstrate the duriation distribution of session with D2l
#using data from conn.log

import os
import numpy as np
import matplotlib.pyplot as plt
skip= False

i=0
index=0
counter=0
cumcount=0
counthist = []
total=0.0
obs = 0.0
num = 0.0
numbuckets = 100
startvalue=0.0
endvalue=500.0
stepsize=0.0

path='/Users/roysourish/Desktop/'  
dirname='hstgram_duration_records'
boxRecord = []
numList = 0
path=path+'/'+dirname
dirs=os.listdir(path)
#print(files)
for subdirname in dirs:
	#print filename
	if(subdirname[0]=='.'):
		pass
	elif(os.path.isdir(path+'/'+subdirname)):
		newpath=path+'/'+subdirname
		files=os.listdir(newpath)
		for filename in files:
			if(filename[0] == '.'):
				continue
			if(os.path.isfile(newpath+'/'+filename)):
				f_temp=open(newpath+'/'+filename,'r')
				lines=f_temp.readlines()
				for line in lines:
					line=line.strip('\n')
					boxRecord.append(filter(None,line.split(' ')))
					numList += 1
				f_temp.close()
print boxRecord

#need input here

if(startvalue > endvalue):
	num=startvalue
	startvalue=endvalue
	endvalue=num

stepsize=float((endvalue-startvalue)/numbuckets)

for i in range(0,numbuckets):
	counthist.append(0)
#print counthist

total = 0
counter = 0

for value in range(0,numList):
	if boxRecord[value][0] == '-':
		boxRecord[value][0] = 0
	#print boxRecord[value][0]
	obs = float(boxRecord[value][0])
	#print obs
	if obs > endvalue:
		counthist[numbuckets-1] += 1
		total += 1
		#print 'a'
		continue
	if obs < startvalue:
		counthist[0] += 1
		total += 1
		#print 'b'
		continue
	num = startvalue
	index = 0

	while num<obs:
		num += stepsize
		if(num<obs):
			index += 1
	counthist[index] += 1
	total += 1

x_Data = []
y_Data = []
#print counthist
print total
comcount = 0

for i in range(0,numbuckets):
	count = counthist[i];
	comcount += count;
	#print str(float(count)/float(total))+"\t"+str(float(comcount)/float(total))
	y_Data.append(float(comcount)/float(total))
		

newrecord=[]
for records in boxRecord:
	print records
	newrecord.append(float(records[0]))
print newrecord
x_Data = []
x_Data=range(int(startvalue),int(endvalue),int(stepsize))

fig = plt.figure()
fig.suptitle('Histogram-duration-Feb 1st- 12 to 1 am', fontsize=14, fontweight='bold')
#ax = fig.add_subplot(111)
#fig.subplots_adjust(top=0.85)
#ax.set_title('D2L-duration')
plt.xlabel("duration [s]")
plt.ylabel("PDF")
plt.grid(True)

#plt.hist(x_Data,y_Data)
ax = fig.add_subplot(111)
#ax.axis([0,200,0,650000])
#plt.test(2,2,'sdfasdfa')
ax.hist(newrecord,range=(0,200),bins=200)
#n, bins, patches = ax.hist(x_Data, bins=50, normed=1, facecolor='green')
plt.show()

