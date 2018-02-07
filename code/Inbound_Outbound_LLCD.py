#!/bin/python
#python script used to draw a CDF test of inbound and outbound requests. 
#using data from conn.log


import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D


i=0
index=0
counter=0
cumcount=0
counthist_in = []
counthist_ou = []
mydata1=[]
mydata2=[]
total_in=0
total_ou = 0
obs = 0.0
num = 0.0
numbuckets = 110000
startvalue=0.0
endvalue=2200000000.0
stepsize=0.0

path='/Users/roysourish/Desktop/'  
dirname='inout_histogram_data'
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
		sondirs=os.listdir(newpath)
		for sondir in sondirs:
			#print newpath+sondir
			if(sondir[0] == '.'):
				pass
			elif(os.path.isdir(newpath+'/'+sondir)):
				newsonpath=newpath+'/'+sondir
				files=os.listdir(newsonpath)
				#print files
				for filename in files:
					f_temp=open(newsonpath+'/'+filename,'r')
					lines=f_temp.readlines()[1:]
					for line in lines:
						line=line.strip('\n')
						boxRecord.append(filter(None,line.split(' ')))
						numList += 1
					f_temp.close()


#if(startvalue > endvalue):
#	num=startvalue
#	startvalue=endvalue
#	endvalue=num

stepsize=float((endvalue-startvalue)/numbuckets)

for i in range(0,numbuckets):
	counthist_in.append(0)
	counthist_ou.append(0)
#for i in range(0,numbuckets):
#	counthist_ou.append(0)

#print counthist_in

total_in = 0
total_ou = 0
counter = 0
#======================================
for value in range(0,numList):
	if boxRecord[value][1] == '-':
		boxRecord[value][1] = 0
	obs = float(boxRecord[value][1])
	#print obs
	if obs > endvalue:
		counthist_in[numbuckets-1] += 1
		total_in += 1
		#print 'a'
		continue
	if obs < startvalue:
		counthist_in[0] += 1
		total_in += 1
		#print 'b'
		continue
	num = startvalue
	index = 0

	while num<obs:
		num += stepsize
		if(num<obs):
			index += 1
	counthist_in[index] += 1
	total_in += 1
#=========================================
for value in range(0,numList):
	if boxRecord[value][0] == '-':
		boxRecord[value][0] = 0
	obs = float(boxRecord[value][0])
	if obs > endvalue:
		counthist_ou[numbuckets-1] += 1
		total_ou += 1
		continue
	if obs < startvalue:
		counthist_ou[0] += 1
		total_ou += 1
		continue
	num = startvalue
	index = 0

	while num<obs:
		num += stepsize
		#print index
		if(num<obs):
			index += 1
	counthist_ou[index] += 1
	total_ou += 1
#=============================================
x_Data = []
y_Data_in = []
y_Data_ou = []
#print counthist_in
#print total
comcount = 0
print "total in is "+str(total_in)
print "total out is "+str(total_ou)
for i in range(0,numbuckets):
	count_in = counthist_in[i];
	comcount += count_in;
#	print str(float(count_in)/float(total_in))+"\t"+str(float(comcount)/float(total_in))
	y_Data_in.append(1-(float(comcount)/float(total_in)))
comcount = 0
for i in range(0,numbuckets):
	count_ou = counthist_ou[i];
	comcount += count_ou;
#	print str(float(count_ou)/float(total_ou))+"\t"+str(float(comcount)/float(total_ou))
	y_Data_ou.append(1-(float(comcount)/float(total_ou)))
		


x_Data = []
x_Data=range(int(startvalue),int(endvalue),int(stepsize))
#x_Data=range(int(startvalue),int(endvalue))


for i in boxRecord:
	mydata1.append(float(i[0]))
	mydata2.append(float(i[1]))

print max(mydata1)
print max(mydata2)


fig = plt.figure()
#fig= plt.histogram()
fig.suptitle('LLCD-size(Feb)', fontsize=14, fontweight='bold')
ax = fig.add_subplot(111)
#fig.subplots_adjust(top=0.85)
ax=plt.gca()
ax.set_title('d2l.ucalgary.ca-InOut_BoundData_size')
line1,=ax.plot(np.array(x_Data),np.array(y_Data_ou),label='outbound',linestyle='--',linewidth=2.0)
line2,=ax.plot(np.array(x_Data),np.array(y_Data_in),label='inbound',linewidth=2.0)

plt.xlabel("size [B]")
plt.ylabel("LLCD")
plt.grid(True)

plt.legend(loc = 1)
ax.set_yscale('log')
ax.set_xscale('log')
#plt.xlim([1,100000000])
#plt.ylim([-100000,1])
#ax.axis([1,30000000,-1000000,1])


plt.show()
