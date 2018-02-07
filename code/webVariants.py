import os
import datetime
from sharedMethods import *
import subprocess
import glob

if not os.path.exists("./httpRequests/"):
	import matplotlib.pyplot as plt
	import matplotlib
	import numpy as np

	font = {'size': 40}

	matplotlib.rc('font', **font)
	matplotlib.rc('lines', lw=5)
	matplotlib.rc('legend', fontsize=20)
	# 15
	matplotlib.rcParams['xtick.major.pad'] = 15
	matplotlib.rcParams['ytick.major.pad'] = 15
	matplotlib.rcParams['savefig.bbox'] = 'tight'

CONST_REQS = 1583339.0
CONST_VOL = 8483.0


def getDates():
	start = datetime.date(2016, 02, 01)
	end = datetime.date(2016, 02, 29)
	daysRange = (end - start).days
	return [str(start + datetime.timedelta(days = i)) for i in range(daysRange + 1)]


def distinctRequests():
	url = {}
	dates = getDates()
	for date in dates:
		if os.path.exists("./fileInfo/fileBookPerDay/" + date + ".json"):
			fileBookPerDay = readFromDict("./fileInfo/fileBookPerDay/" + date + ".json")
			for i in fileBookPerDay:
				if i not in url:
					url[i] = fileBookPerDay[i]
				else:
					url[i][0] += fileBookPerDay[i][0]
					url[i][1] += fileBookPerDay[i][1]
	distReqsCount = 0
	distReqsVolume = 0
	totalFilesCount = len(url)
	totalFilesVolume = 0
	for i in url:
		if url[i][0] == 1:
			distReqsCount += 1
			distReqsVolume += url[i][1]
		totalFilesVolume += float(url[i][1]) / url[i][0]
	distFilesCount = distReqsCount
	distFilesVolume = distReqsVolume
	print "distReqsCount:", distReqsCount
	print "distReqsVolume:", distReqsVolume
	print "totalFilesCount:", totalFilesCount
	print "totalFilesVolume:", totalFilesVolume
	print "distFilesCount:", distFilesCount
	print "distFilesVolume:", distFilesVolume


def fileSizeDistribution():
	url = {}
	dates = getDates()
	for date in dates:
		if os.path.exists("./fileInfo/fileBookPerDay/" + date + ".json"):
			fileBookPerDay = readFromDict("./fileInfo/fileBookPerDay/" + date + ".json")
			for i in fileBookPerDay:
				newURL = i
				if newURL not in url:
					url[newURL] = fileBookPerDay[i]
				else:
					url[newURL][0] += fileBookPerDay[i][0]
					url[newURL][1] += fileBookPerDay[i][1]
	fileSizeList = []
	for i in url:
		fileSizeList.append([url[i][0], url[i][1] / url[i][0]])
	writeToFile(fileSizeList, "./fileInfo/fileSizeList.json", "wb")


def displayFileSizeDistribution():
	fileSizeList = readFromList("./fileInfo/fileSizeList.json")
	fig = plt.figure(figsize = (16, 9))
	newList = []
	for i in fileSizeList:
		newList += [i[1]]
	# print sorted(fileSizeList, key = lambda x: x[0], reverse = True)[0: 100]
	plt.hist(newList, bins = 100, linewidth=0, rwidth=0.8, normed=1, cumulative=True)
	# plt.xscale('log')
	plt.xlabel("File Size (Byte)")
	plt.ylabel("Frequency")
	plt.show()
	#fig.savefig('../figures/D2L-fileSizeDistribution.eps', format = 'eps', dpi = fig.dpi)


def referenceConcentration():
	fileBook = readFromDict("./fileInfo/fileBook.json")
	fileBook = fileBook.values()
	topRecords = sorted(fileBook, key = lambda x: x[0], reverse = True)[0: (len(fileBook) / 10)]
	print "10% URL numbers: ", len(topRecords)
	print "Request Concentraton: ", sum([i[0] for i in topRecords]) / CONST_REQS
	print "Volume Concentraton: ", sum([i[1] for i in topRecords]) / 1024.0 / 1024 / 1024 / CONST_VOL


def wideAreaUsage():
	ipBook = readFromDict("./ipInfo/ipBook.json")
	ipBookValues = sorted(ipBook.values(), reverse = True)
	ipBookValues = ipBookValues[0: (len(ipBookValues) / 10)]
	reqsSum = sum(ipBookValues)
	print "Wide Area Usage:", reqsSum / CONST_REQS


def interReferenceTimes():
	dates = getDates()
	interReferenceTimes = {}
	for date in dates:
		if os.path.exists("./httpRequests/" + date):
			fileDataPerDay = subprocess.check_output("zcat ./httpRequests/" + date + "/http.*.gz" + " | gawk 'BEGIN {RS=\"\\\\\\\\n\"; FS=\"\\\\\\\\t\"} {print $10 \"\\t\" $28}'", shell = True).rsplit("\n")
			for i in fileDataPerDay:
				i = i.split("\t")
				if (i[0] != "-") and (i[0] != "") and (i[1] != "-") and (i[1] != ""):
					if (i[0] not in interReferenceTimes):
						interReferenceTimes[i[0]] = [float(i[1])]
					else:
						interReferenceTimes[i[0]].append(float(i[1]))
	writeToFile(interReferenceTimes, "./fileInfo/interReferenceTimes.json", "wb")


def interReferenceValues():
	interReferenceTimes = readFromDict("./fileInfo/interReferenceTimes.json")
	print "interReferenceTimes length: ", len(interReferenceTimes)
	interReferenceValues = []
	for fileName in interReferenceTimes:
		requestTimes = sorted(interReferenceTimes[fileName])
		for i in range(len(requestTimes) - 1):
			interReferenceValues.append(round(requestTimes[i + 1] - requestTimes[i], 3))
	writeToFile(interReferenceValues, "./fileInfo/interReferenceValues.json", "wb")


def displayInterReference():
	interReferenceValues = readFromList("./fileInfo/interReferenceValues.json")
	fig = plt.figure(figsize = (16, 9))
	# plt.xscale('log')
	plt.xlabel('Seconds')
	plt.ylabel('Cumulative Frequency')
	values, base = np.histogram(interReferenceValues, bins=1000, density=True)
	values = values / values.sum()
	cumulative = np.cumsum(values)
	plt.plot(base[:-1], cumulative)
	plt.gca().set_ylim(bottom = 0)
	plt.gca().set_xlim(left = 0)
	plt.show()
	fig.savefig('../figures/D2L-interReferenceTimes.eps', format = 'eps', dpi = fig.dpi)


def fileTypes():
	fileType = {}
	dates = getDates()
	for date in dates:
		for files in glob.glob("./httpRequests/" + date + "/http.*.txt.gz"):
			result = subprocess.check_output("zcat " + files + " | gawk 'BEGIN {RS=\"\\\\\\\\n\"; FS=\"\\\\\\\\t\"} // {print $33 \"\\t\" $14}'", shell = True).rsplit("\n")
			for record in result:
				record = record.split("\t")
				if record[0] != "":
					if record[0] not in fileType:
						fileType[record[0]] = [1, int(record[1])]
					else:
						fileType[record[0]][0] += 1
						fileType[record[0]][1] += int(record[1])
	writeToFile(fileType, "./fileInfo/fileType.json", "wb")
	tableString = "{:<80}\t{:>25}\t{:>25}\t{:>25}\t{:>25}\t{:>25}\t{:>25}\n".format("File Type", "Rank (by Count)", "Count", "Percentage (by Count)", "Rank (by Volume)", "Volume (GB)", "Percentage (by Volume)")
	countTotal = float(sum([fileType[i][0] for i in fileType]))
	volumeTotal = float(sum([fileType[i][1] for i in fileType]))
	sortByCount = sorted(fileType.items(), key = lambda x: x[1][0], reverse = True)
	rankByCount = {}
	for i in sortByCount:
		rankByCount[i[0]] = sortByCount.index(i) + 1
	sortByVolume = sorted(fileType.items(), key = lambda x: x[1][1], reverse = True)
	rankByVolume = {}
	for i in sortByVolume:
		rankByVolume[i[0]] = sortByVolume.index(i) + 1
	for i in sortByCount:
		typeName = i[0]
		tableString += "{:<80}\t{:>25}\t{:>25}\t{:>25.2%}\t{:>25}\t{:>25}\t{:>25.2%}\n".format(
			typeName,
			rankByCount[typeName], fileType[typeName][0], fileType[typeName][0] / countTotal,
			rankByVolume[typeName], fileType[typeName][1] / 1073741824.0, fileType[typeName][1] / volumeTotal,
			)
	writeToTxt(tableString, "./fileInfo/fileTypeSummary.txt", "wb")

#distinctRequests()
#fileSizeDistribution()
#referenceConcentration()
#wideAreaUsage()
#interReferenceTimes()
#interReferenceValues()
#fileTypes()
#Display Figure
displayFileSizeDistribution()
#displayInterReference()

