#!/bin/python

import os
import matplotlib.pyplot as plt
import numpy as np
import pylab as pl

x_label = []
y = []
total = []
dict = {}
path = '/Users/roysourish/Desktop/'
dirname = 'd2l4monthshttps'
flag1=0
path= path + "/"+ dirname
dirs= os.listdir(path)
#this is taken out of the folder d2l4monthshttps from conn logs
for dir in dirs:
    #print dir
    if(os.path.isdir(path+'/'+dir)):
        #t = 0
        if(dir[0] == '.'):
            pass
        else:
            files=os.listdir(path+'/'+dir)
            #t=0
            newpath = path+'/'+dir
                        #print path
            for firstFile in files:  #in the first loop, open each monthly dir
                            #print firstFile
                            #print newpath
                            #t=0
                    if(os.path.isfile(newpath+'/'+firstFile)):  #if it is a dir
                               #print "Is file"
                            if(firstFile[0] == '.'):           #if it is an uninvisible dir, pass
                                pass
                            else:
                                            #print newpath+'/'+firstFile
                                f_temp = open(newpath+'/'+firstFile,'r')
                                #with open(newpath+'/'+firstFile,'r') as data:
                                lines=f_temp.readlines()
                                
                                for line in lines:
                                    #print line
                                    x_label.append(line.strip().split("\t")[0])
                                    y.append(int(line.strip().split("\t")[1]))
                                    print len(y)
                                #t = sum(y)
                            
#total.append(t)

total= [sum(y[x:x+24]) for x in range(0, len(x_label), 24)]
print total
