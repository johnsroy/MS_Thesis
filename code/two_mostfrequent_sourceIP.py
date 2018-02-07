#/bin/python

import os
import matplotlib.pyplot as plt
import numpy as np

path='/Users/roysourish/Desktop/'
dirname='twographs'
boxrecord = []
dirList = []
fileList = []
numLine = 0
x_data=[]
y_data1=[]
y_data2=[]
path = path+'/'+dirname
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
#				print "second file is "+secondFile
				if(os.path.isfile(newpath+'/'+secondFile)):  #if it is a file rather than a dir
#					print "Is file"
					if(secondFile[0] == '.'):        #skip invisible
						pass 
					else:
						print newpath+'/'+secondFile
						f_temp = open(newpath+'/'+secondFile,'r')  #open the file in f_temp
						lines=f_temp.readlines()                
						for line in lines:                     #append every lines to boxrecord
#							print numLine
							line = line.strip('\n')            #remove the '\n' at the end of each line
							boxrecord.append(list(filter(None,line.split('\t'))))  #set the split as "\t"
							print boxrecord[numLine][2]
							if(boxrecord[numLine][2] is not None):
								y_data1.append(int(boxrecord[numLine][2]))
							if(boxrecord[numLine][1] is not None):
								y_data2.append(int(boxrecord[numLine][1]))
							numLine = numLine + 1
							#print "Totle amount of file is: "+str(numLine)
						f_temp.close()
print boxrecord
print "Totle amount of file is: "+str(numLine)
plt.figure()
x_data = range(len(y_data1))
plt.plot(x_data,y_data1)
plt.plot(x_data,y_data2)
plt.grid=(True)
plt.show()

