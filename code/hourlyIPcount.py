#/bin/python

import os
import matplotlib.pyplot as plt
import numpy as np

path='/Users/roysourish/Desktop'
dirname='d2l'
boxrecord = []
dirList = []
fileList = []
numLine = 0
x_data=[]
y_data = []
y_count = 0
path = path+"/"+dirname
dirs = os.listdir(path)  #list all the dir in path
#print (dirs)
flag=0
for dir in dirs:
#	print dir
	if(os.path.isdir(path+'/'+dir)):
		if(dir[0] == '.'):
			pass
		else:
			files=os.listdir(path+'/'+dir)
			newpath = path+'/'+dir
			#print path
			for firstFile in files:  #in the first loop, open each monthly dir
				#print firstFile
				#print newpath
				if(firstFile[0] == '.'):
					continue
				f_temp = open(newpath+'/'+firstFile)
				lines = f_temp.readlines()
				y_data.append(0)
				for line in lines:
#					print line
					y_data[y_count] += 1
				print y_data[y_count]			
				y_count += 1


fig = plt.figure()
ax = fig.add_subplot(111)
x_data = range(len(y_data))
print max(y_data)
print len(y_data)
print y_data
#print x_data
plt.plot(x_data,y_data)
#plt.xlim([2900,1])
#plt.ylim([1000,1])
plt.show()
