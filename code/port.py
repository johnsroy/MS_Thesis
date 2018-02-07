import os
import matplotlib.pyplot as plt
path1='/Users/roysourish/Desktop/'
filename1=path1+'port'
filename2=path1+'time1'
f_temp1=open(filename1, 'r')
#f_temp2=open(filename2, 'r')
lines1 = f_temp1.readlines()

listrecord = []
numList = 0
for line in lines1:
	line = line.strip('\n')
	listrecord.append(filter(None,line.split(' ')))
	f_temp2=open(filename2, 'r')
	list_temp=f_temp2.readlines()[numList]
	list_temp=list_temp.strip('\n')
	listrecord[numList].append(filter(None, list_temp.split(' ')))
	numList += 1
#	f_temp2.close()
f_temp1.close()
print listrecord

x_data= []
y_data=[]
for member in listrecord:
        x_data.append(member[0])
        y_data.append(member[1])


print y_data
#fig.suptitle('For wireless IP 136.159.49.122', fontsize=14, fontweight='bold')
f, ax = plt.subplots(figsize=(6, 6))
plt.scatter(y_data,x_data)
#ax.set_yscale('log')
#ax.set_xscale('log')
#plt.xlim([0,12])
#plt.ylim([1,80000])
plt.ylabel("TCP Source Port")
plt.xlabel("Duration")
ax.set_title('For IP 136.159.49.122')
plt.show()

