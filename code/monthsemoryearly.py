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
y_data=[]
ip_required = '136.159.16.16'
path = path+"/"+dirname
dirs = os.listdir(path)  #list all the dir in path
print (dirs)
flag=0
for dir in dirs:
	print dir
	if(os.path.isdir(path+'/'+dir)):
		if(dir[0] == '.'):
			pass
		else:
			files=os.listdir(path+'/'+dir)
			newpath = path+'/'+dir
			print path
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
							#print numLine



							line = line.strip('\n')            #remove the '\n' at the end of each line
							boxrecord.append(list(filter(None,line.split(' '))))  #set the split as "\t"
							#print boxrecord[numLine][0]
							#print boxrecord[numLine][1]
							if(ip_required == boxrecord[numLine][1]):
								y_data.append(boxrecord[numLine][0])
								flag=1
							numLine = numLine + 1
						if(flag==0):
							y_data.append(0)
						#print "Totle amount of file is: "+str(numLine)
						f_temp.close()
						flag=0





#print y_data

#print "Total amount of file is: "+str(numLine)
plt.figure()
x_data = range(len(y_data))
plt.plot(x_data,y_data)
plt.grid=(True)
plt.show()

