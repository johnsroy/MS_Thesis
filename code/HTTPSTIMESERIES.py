#!/bin/python

import os
import matplotlib.pyplot as plt
import numpy as np
import pylab as pl

x_label = []
y = []

#this is taken out of the folder d2l4monthshttps from conn logs
with open("/Users/roysourish/Desktop/2016-01-01", "r") as data:
    for line in data:
        x_label.append(line.strip().split("\t")[0])
        y.append(int(line.strip().split("\t")[1]))
print x_label, y

fig = plt.figure(figsize = (15, 8))
fig.suptitle("HTTPS Traffic", fontsize=14, fontweight='bold')
ax=fig.add_subplot(111)
fig.subplots_adjust(top=0.85)
plt.xlabel("time in hours")
plt.ylabel("# of requests to D2L")
x = np.arange(len(x_label))

ax.bar(x, y, width = 0.5, color = 'r')
#plt.xlim([-1, x.size])
plt.xticks(x, x_label, rotation='vertical')
#plt.rcParams.update({'font.yticks': 2})

#rcParams['fig.figsize'] = 5, 10

#plt.plot(x,y)
#ax.axis([0,180,0,140000])
plt.subplots_adjust(bottom = 0.3)
plt.show()



'''
httpRequests = readFromDict("./httpInfo/httpRequestTotalPerDay.json")
    dates = sorted(httpRequests.keys())
        y = []
        for date in dates:
            y += [sum([int(i.rstrip()) for i in httpRequests[date].values()])]

'''