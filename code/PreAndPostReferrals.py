#/bin/python

import os
import matplotlib.pyplot as plt
import numpy as np
path1='/Users/roysourish/Desktop/fileInfo/'
filename1=path1+'postreferer_March_MonthofMarch_2016.txt'
#To accepts any of \r, \n, \r\n as a newline you could use 'U' (universal newline) file mode:
file = open(filename1, 'r')
lines = file.readlines()
#print lines
result = {}
x=[]
y=[]
for line in lines:
	course,count,size = line.lstrip().rstrip('\n').split('\t')
    #course,count = line.lstrip().rstrip('\n').split('\t\t')
	if course not in result:
		result[course] = int(count)
	else:
		result[course] += int(count)
file.close()

frequency = sorted(result.items(), key = lambda i: i[1], reverse= True)
# (rank, frequency)
#print frequency
x=[]
y=[]
i=0
for element in frequency:
	x.append(element[0])
	y.append(element[1])

#print x
#plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)))
#m,b = np.polyfit(x, y)
#print b
#print m
z=[]
z=np.arange(len(x))
slope, intercept = np.polyfit(log(z),log(y), 1)
abline_values = [slope * i + intercept for i in z]
print(slope)
plt.loglog(z, y, '--')
plt.plot(z,abline_values,'b')
plt.title(slope)
plt.show()
#abline_values = [slope * i + intercept for i in z]
