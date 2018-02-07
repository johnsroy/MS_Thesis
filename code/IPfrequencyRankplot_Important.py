#/bin/python

import os
import matplotlib.pyplot as plt
import numpy as np
path1='/Users/roysourish/Desktop/'
filename1=path1+'IPFreq2'
file = open(filename1, 'r')
lines = file.readlines()
result = {}
for line in lines:
	count, ip = line.rstrip().lstrip().split(' ')
	if ip not in result:
		result[ip] = int(count)
	else:
		result[ip] += int(count)
file.close()

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
plt.xlabel("IPs")
plt.ylabel("Rank")
ax.set_title('IP Frequency Rank Plot')
plt.show()

