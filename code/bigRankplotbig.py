#/bin/python

import os
import matplotlib.pyplot as plt
import numpy as np
path='/Users/roysourish/Desktop'
dirname='d2l'
result={}
dirList = []
fileList = []
numLine = 0
x=[]
y=[]
z=[]
path = path+"/"+dirname
dirs = os.listdir(path)  #list all the dir in path
print (dirs)
for dir in dirs:
        #print dir
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
                                if(os.path.isfile(newpath+'/'+firstFile)):  #if it is a dir
                                        #print "Is file"
                                        if(firstFile[0] == '.'):           #if it is an uninvisible dir, pass
                                                pass
                                        else:
                                                #print newpath+'/'+firstFile
                                                f_temp = open(newpath+'/'+firstFile,'r')  #open the file in f_temp
                                                lines=f_temp.readlines()
                                                for line in lines:                     #append every lines to boxrecord
                                                        count, ip = line.rstrip().lstrip().split(' ')
                                                        #print count, ip
                                                        if ip not in result:
                                                                result[ip] = int(count)
                                                        else:
                                                                result[ip] += int(count)
                                                f_temp.close()

frequency = sorted(result.items(), key = lambda i: i[1], reverse = True)
#frequencyRank = list(enumerate(frequency, start = 1))
# (rank, frequency)
#print frequency

x=[]
y=[]
i=0
for element in frequency:
	x.append(element[0])
	y.append(element[1])
	
for i in range(len(x)):
	print x[i],y[i]
z=[]
fig=plt.figure()
ax = fig.add_subplot(111)
z=range(len(x))
plt.plot(z,y)
ax.set_yscale('log')
ax.set_xscale('log')
plt.xlabel("Rank")
plt.ylabel("Frequency")
#Also used it for jan and feb
ax.set_title('HTTPS IP Frequency Rank Plot Fall 2016')
plt.show()

