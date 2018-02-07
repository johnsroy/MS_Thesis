#!/bin/python

import os
import matplotlib.pyplot as plt
path1='/Users/roysourish/Desktop/'
filename1=path1+'00'
path2='/Users/roysourish/Desktop/'
filename2=path2+'11'

f_temp1=open(filename1, 'r')
f_temp2=open(filename2, 'r')

lines1 = f_temp1.readlines()
#lines2 = f_temp2.readlines()
#print lines2

listrecord = []
numList = 0
for line in lines1:
	line = line.strip('\n')
	listrecord.append(filter(None,line.split(' ')))
	f_temp2=open(filename2, 'r')
	list_temp = f_temp2.readlines()[numList]
	#print list_temp
	list_temp = list_temp.strip('\n')
	listrecord[numList].append(filter(None, list_temp.split(' '))[0])
	numList += 1
	f_temp2.close()
f_temp1.close()
#f_temp2.close()
print listrecord
print max(listrecord[0])
print max(listrecord[1])
x_data = []
y_data = []
for member in listrecord:
	if(member[0] == '-'):
		continue
		member[0] = 0
	if(member[1] == '-'):
		continue
		member[1] = 0
	x_data.append(member[0])
	y_data.append(member[1])

#x_data = range(len(listrecord))
f, ax = plt.subplots(figsize=(6, 6))
plt.scatter(x_data, y_data)
plt.xlim([1,8000])
plt.ylim([1,10000000])


diag_line, = ax.plot(ax.get_xlim(), ax.get_ylim(), ls="--", c=".3")
def on_change(axes):
    # When this function is called it checks the current
    # values of xlim and ylim and modifies diag_line
    # accordingly.
    x_lims = ax.get_xlim()
    y_lims = ax.get_ylim()
    diag_line.set_data(x_lims, y_lims)

# Connect two callbacks to your axis instance.
# These will call the function "on_change" whenever
# xlim or ylim is changed.
ax.callbacks.connect('xlim_changed', on_change)
ax.callbacks.connect('ylim_changed', on_change)


ax.set_yscale('log')
ax.set_xscale('log')
plt.xlabel("Duration[s]")
plt.ylabel("Oubound Data Volume")
ax.set_title('Bandwidth of 1st Feb 1 to 2 am')


plt.show()

