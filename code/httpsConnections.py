#!/bin/python

import os
import matplotlib.pyplot as plt
import numpy as np

path = '/Users/roysourish/Desktop/'
dirname= 'd2l4monthshttps'
boxRecord = []
dirList = []
fileList = []
numLine = 0
x_data=[]
y_data1 = []
y_data=[]
y_count = 0
path = path+"/"+dirname
dirs = os.listdir(path)  #list all the dir in path
files = os.listdir(path)  #list all the dir in path
print (files)
for firstFile in files:  #in the first loop, open each monthly dir
    #	print firstFile
    if(os.path.isdir(path+'/'+firstFile)):  #if it is a dir
        #		print "Is dir"
        if(firstFile[0] == '.'):           #if it is an uninvisible dir, pass
            pass
        else:
            newpath = path+'/'+firstFile   #new path used to loop daily files
                        #			print "new path is " + newpath
            newfiles = os.listdir(newpath)  #list all the files and directions
            for secondFile in newfiles:
                #print "second file is "+secondFile
                if(os.path.isfile(newpath+'/'+secondFile)):  #if it is a file rather than a dir
                                #					print "Is file"
                    if(secondFile[0] == '.'):        #skip invisible
                        pass
                    else:
                        print newpath+'/'+secondFile
                        f_temp = open(newpath+'/'+secondFile,'r')  #open the file in f_temp
                        lines=f_temp.readlines()
                        for line in lines:
                            line = line.strip('\n')
                            print line
                            boxRecord.append(filter(None,line.split('\t')))
                            #print boxRecord
                            for i in boxRecord:
                                y_data.append(i[1])
                            #y_data.append(int(boxRecord[1]))
                        #print y_data
                        #y_count = y_count + 1
                        f_temp.close()
'''
fig=plt.figure()
fig.suptitle("Overall Email Traffic", fontsize=14, fontweight='bold')
ax=fig.add_subplot(111)
#fig.subplots_adjust(top=0.85)
plt.xlabel("time in hours")
plt.ylabel("# of connetcions per hour")
x_data = range(len(y_data))
plt.plot(x_data,y_data)
#ax.axis([0,180,0,140000])
plt.show()
'''

