#/bin/python

import os
import matplotlib.pyplot as plt
import numpy as np
path1='/Users/roysourish/Desktop/'
filename1=path1+'testingContent.txt'
#To accepts any of \r, \n, \r\n as a newline you could use 'U' (universal newline) file mode:
file = open(filename1, 'U')
lines = file.readlines()
#print lines
result = {}
for line in lines:
	count, course = line.lstrip().rstrip('\n').split('\t')
	if course not in result:
		result[course] = int(count)
	else:
		result[course] += int(count)
file.close()

frequency = sorted(result.items(), key = lambda i: i[1], reverse= True)
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
z=np.arange(len(x))
plt.bar(z, y, width = 0.5, color = 'r', align = 'center')
#ax.set_yscale('log')
#ax.set_xscale('log'a)
xticksString = [i for i in x]
plt.xlim([-1, z.size])
plt.xticks(z, xticksString, rotation='vertical')
plt.xlabel("Course")
plt.ylabel("Popularity")
ax.set_title('Course Popularity for 4 months(Winter 2016)')
plt.show()


