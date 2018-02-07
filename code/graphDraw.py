#!/bin/python

import json
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.ticker import FuncFormatter
import numpy as np
import urllib2
import os
from sharedMethods import *
import datetime



def getDates():
	start = datetime.date(2016, 03, 22)
	end = datetime.date(2016, 03, 22)
	daysRange = (end - start).days
	return [str(start + datetime.timedelta(days = i)) for i in range(daysRange + 1)]


def httpRequests_xHour_yTimes():
	if not os.path.exists("./httpInfo/httpRequests_xHour_yTimes"):
		os.makedirs("./httpInfo/httpRequests_xHour_yTimes")
	if not os.path.exists("./httpInfo/httpRequests_xHour_yTimesLog2"):
		os.makedirs("./httpInfo/httpRequests_xHour_yTimesLog2")

	httpRequests = readFromDict("./httpInfo/httpRequestTotalPerDay.json")
	dates = sorted(httpRequests.keys())
	for date in dates:
		# if date == "2014-12-02":
		day = sorted(httpRequests[date].items(), key = lambda x: x[0])
		fig = plt.figure(figsize = (15, 8))
		y = np.array([int(i[1].rstrip()) for i in day])
		x = np.arange(len(y))
		plt.bar(x, y, width = 0.5, color = 'r', align = 'center')
		plt.xlim([-1, x.size])
		xticksString = [i[0].split("-")[0] + "-\n" + i[0].split("-")[1] for i in day]
		plt.xticks(x, xticksString, rotation='vertical')
		plt.xlabel('Periods of Time')
		plt.ylabel('Number of Requests')
		plt.title(date)
		plt.subplots_adjust(bottom = 0.15)
		fig.savefig('./httpInfo/httpRequests_xHour_yTimes/' + date + '.eps', format = 'eps', dpi = fig.dpi)

		# fig = plt.figure(figsize = (15, 8))
		# y = getLogValue(y)
		# x = np.arange(len(y))
		# plt.bar(x, y, width = 0.5, color = 'r', align = 'center')
		# plt.xlim([-1, x.size])
		# xticksString = [i[0].split("-")[0] + "-\n" + i[0].split("-")[1] for i in day]
		# plt.xticks(x, xticksString, rotation='vertical')
		# plt.xlabel('Periods of Time')
		# plt.ylabel('Number of Requests, log_2')
		# plt.title(date)
		# plt.subplots_adjust(bottom = 0.15)
		# fig.savefig('./httpInfo/httpRequests_xHour_yTimesLog2/' + date + '.eps', format = 'eps', dpi = fig.dpi)

def millionsLabel(x, pos):
	return '%1.1fM' % (x*1e-6)


def kilosLabel(x, pos):
	return '%1.0fK' % (x*1e-3)


def httpRequests_xDay_yTimes():
	if not os.path.exists("./httpInfo/httpRequests_xDay_yTimes"):
		os.makedirs("./httpInfo/httpRequests_xDay_yTimes")
	if not os.path.exists("./httpInfo/httpRequests_xDay_yTimesLog2"):
		os.makedirs("./httpInfo/httpRequests_xDay_yTimesLog2")

	httpRequests = readFromDict("./httpInfo/httpRequestTotalPerDay.json")
	dates = sorted(httpRequests.keys())
	y = []
	for date in dates:
		y += [sum([int(i.rstrip()) for i in httpRequests[date].values()])]

	y = np.array(y)
	x = np.arange(len(y))
	fig = plt.figure(figsize = (15, 8))
	plt.bar(x, y, width = 0.5, color = 'r', align = 'center')
	plt.xlim([-1, x.size])
    #	xticksString = dates
    #	xticksString = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        xticksString = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
	plt.xticks([0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366], xticksString, fontsize = 10)
	plt.xlabel('Months')
	plt.ylabel('Number of Requests')
	plt.title("Typical d2l HTTP Traffic for the year of 2015")
	plt.subplots_adjust(bottom = 0.15)
	fig.savefig('./httpInfo/httpRequests_xDay_yTimes/' + dates[0] + " ~ " + dates[-1] + '.eps', format = 'eps', dpi = fig.dpi)
	
	# y = getLogValue(y)
	# x = np.arange(len(y))
	# fig = plt.figure(figsize = (15, 8))
	# plt.bar(x, y, width = 0.5, color = 'r', align = 'center')
	# plt.xlim([-1, x.size])
	# xticksString = dates
	# plt.xticks(x, xticksString, fontsize = 10, rotation='vertical')
	# plt.xlabel('Dates')
	# plt.ylabel('Number of Requests, log_2')
	# plt.title("Http Requests Total Per Day")
	# plt.subplots_adjust(bottom = 0.15)
	# fig.savefig('./httpInfo/httpRequests_xDay_yTimesLog2/' + dates[0] + " ~ " + dates[-1] + '.eps', format = 'eps', dpi = fig.dpi)


# def receiverIP():
# 	receiverIP = readFromDict("./ipInfo/receiverIP.json")
# 	receiverIP = receiverIP.items()
# 	ips = [i[0] for i in receiverIP]
# 	total = sum([i[1] for i in receiverIP])
# 	sizes = [i[1]/float(total) for i in receiverIP]
# 	colors = plt.cm.jet(np.linspace(0.8, 0., len(sizes)))
# 	explode = [i*0.15 for i in range(0, len(sizes))]
# 	fig = plt.figure(figsize = (15, 8))
# 	patches, texts, autotexts = plt.pie(sizes, explode = explode, colors = colors, autopct = '%1.1f%%')
# 	plt.axis('equal')
# 	labels = ['{0} - {1:1.2f} %'.format(i, j*100) for i, j in zip(ips, sizes)]
# 	plt.legend(patches, labels, loc='upper right', fontsize = 10)
# 	fig.savefig('./ipInfo/receiverIPPieGraph' + '.eps', format = 'eps', dpi = fig.dpi)

# 	receiverIP = readFromDict("./ipInfo/receiverIP.json")
# 	result = "IP\tCount\n"
# 	receiverIP = showTopKResults(receiverIP, len(receiverIP))
# 	for i in receiverIP:
# 		result += i[0] + "\t" + str(i[1]) + "\n"
# 	writeToTxt(result, "./ipInfo/receiverIP.txt", "wb+")


def ipRank():
	ipBook = readFromDict("./ipInfo/ipBook.json")
	ipBookID = readFromDict("./ipInfo/ipBookID.json")
	result = "{:<5}\t{:<15}\t{:<15}\t{:<20}\t{:<20}\t{:<20}\t{:<20}\n".format(
		"Rank", "IP", "Count", "Country", "Region", "City", "ISP")
	ipBookRank = showTopKResults(ipBook, len(ipBook))
	rankFlag = 1
	for i in ipBookRank:
		ip = i[0]
		country = ipBookID[ip]["country"]
		times = ipBookID[ip]["times"]
		if "region" in ipBookID[ip]:
			region = ipBookID[ip]["region"]
		else:
			region = "NA"
		if "city" in ipBookID[ip]:
			city = ipBookID[ip]["city"]
		else:
			city = "NA"
		if "isp" in ipBookID[ip]:
			isp = ipBookID[ip]["isp"]
		else:
			isp = "NA"
		result += "{:<5}\t{:<15}\t{:<15,}\t{:<20}\t{:<20}\t{:<20}\t{:<20}\n".format(
			rankFlag, ip, times, country, region, city, isp)
		rankFlag += 1
	writeToTxt(result, "./ipInfo/ipRank.txt", "wb+")


def ipBookID():
	ipBookID = {}
	ipBook = readFromDict("./ipInfo/ipBook.json")
	flag = 1
	for ip in ipBook:
		times = ipBook[ip]
		#url = "http://freegeoip.net/json/" + ip
                #url = "http://geoip.nekudo.com/api/199.30.181.42/" +ip
                #url = "http://api.myiponline.net/ip?ip=199.30.181.42&sort=geo/" + ip
                url = "http://api.petabyet.com/geoip/" + ip
		response = {}
		try:
			response = json.loads(urllib2.urlopen(url).read(), object_hook = decodeDict)
			print str(flag) + ". " + ip
			flag += 1
		except Exception as msg:
			print "some error: " + msg.message + " " + ip
		response.update({"times": times})
		ipBookID[ip] = response
	writeToFile(ipBookID, "./ipInfo/ipBookID.json", "wb+")


def ipBookIDCheck():
	ipBookID = readFromDict("./ipInfo/ipBookID.json")
	for ip in ipBookID:
		if "longitude" not in ipBookID[ip]:
			url = "http://www.telize.com/geoip/" + ip
			response = {}
			try:
				response = json.loads(urllib2.urlopen(url).read(), object_hook = decodeDict)
				print ip
			except Exception as msg:
				print "some error: " + msg.message + " " + ip
			ipBookID[ip].update(response)
	writeToFile(ipBookID, "./ipInfo/ipBookID2.json", "wb+")


def ipLabel():
	if not os.path.exists("./ipInfo/ipLabel"):
		os.makedirs("./ipInfo/ipLabel")
	ipBookID = readFromDict("./ipInfo/ipBookID.json")

	def ipStatFig(figName, figSize, label = None, drawFig = True, rank = 0, textNumber = 0, dist = 0.15, bboxToAnchor = False):
		data = {}
		for i in ipBookID:
			if figName in ipBookID[i]:
				if label is None:
					if ipBookID[i][figName] not in data:
						data[ipBookID[i][figName]] = ipBookID[i]["times"]
					else:
						data[ipBookID[i][figName]] += ipBookID[i]["times"]
				else:
					if label[0] in ipBookID[i]:
						if ipBookID[i][label[0]] == label[1]:
							if ipBookID[i][figName] not in data:
								data[ipBookID[i][figName]] = ipBookID[i]["times"]
							else:
								data[ipBookID[i][figName]] += ipBookID[i]["times"]
		if drawFig:
			if label is None:
				drawPieFigure(data, "./ipInfo/ipLabel/" + figName + ".eps", figSize, rank, textNumber, dist, bboxToAnchor)
			else:
				label[1] = label[1].replace("/", "-")
				if not os.path.exists("./ipInfo/ipLabel/" + label[0] + "-" + figName):
					os.makedirs("./ipInfo/ipLabel/" + label[0] + "-" + figName)
				drawPieFigure(data, "./ipInfo/ipLabel/" + label[0] + "-" + figName + "/" + label[1] + ".eps", figSize, rank, textNumber, dist, bboxToAnchor)
		return data

	## Get country distribution
	#ip_country = ipStatFig("country", (16, 9), rank = 5, textNumber = 3)

	## Get region in country distribution
	#ipStatFig("region", (16, 9), ["country", "Canada"], rank = 5, textNumber = 3, dist = 0.15)
	#ipStatFig("region", (16, 9), ["country", "United States"], rank = 5, dist = 0, bboxToAnchor = [1.1, 1])

	## Get city in Canada, US distribution
	canada_region = ipStatFig("region", (15, 15), ["country", "Canada"], False)
	ipStatFig("city", (16, 9), ["region", "Alberta"])
	#, rank = 5)
	# us_region = ipStatFig("region", (15, 15), ["country", "United States"], False)
	# for i in us_region:
	# 	ipStatFig("city", (15, 15), ["region", i])
        ipStatFig("region", (15, 25), ["country", "Canada"])
	## Get ISP in Canada, US distrubtion
	ipStatFig("isp", (15, 25), ["country", "Canada"])
	#ipStatFig("isp", (15, 25), ["country", "United States"])


def senderVolume_xHour_yVolume():
	if not os.path.exists("./httpInfo/senderVolume_xHour_yVolume"):
		os.makedirs("./httpInfo/senderVolume_xHour_yVolume")

	senderVolume = readFromDict("./fileInfo/senderVolumePerDay.json")
	dates = sorted(senderVolume.keys())
	for date in dates:
		day = sorted(senderVolume[date].items(), key = lambda x: x[0])
		fig = plt.figure(figsize = (15, 8))
		y = np.array([int(i[1].rstrip()) / 1048576.0 for i in day])
		x = np.arange(len(y))
		plt.bar(x, y, width = 0.5, color = 'r', align = 'center')
		plt.xlim([-1, x.size])
		xticksString = [i[0].split("-")[0] + "-\n" + i[0].split("-")[1] for i in day]
		plt.xticks(x, xticksString, rotation='vertical')
		plt.xlabel('Periods of Time')
		plt.ylabel('Volume (MB)')
		plt.title(date)
		plt.subplots_adjust(bottom = 0.15)
		fig.savefig('./httpInfo/senderVolume_xHour_yVolume/' + date + '.eps', format = 'eps', dpi = fig.dpi)


def receiverVolume_xHour_yVolume():
	if not os.path.exists("./fileInfo/receiverVolume_xHour_yVolume"):
		os.makedirs("./fileInfo/receiverVolume_xHour_yVolume")

	receiverVolume = readFromDict("./fileInfo/receiverVolumePerDay.json")
	dates = sorted(receiverVolume.keys())
	for date in dates:
		day = sorted(receiverVolume[date].items(), key = lambda x: x[0])
		fig = plt.figure(figsize = (15, 8))
		y = np.array([int(i[1].rstrip()) / 1048576.0 for i in day])
		x = np.arange(len(y))
		plt.bar(x, y, width = 0.5, color = 'r', align = 'center')
		plt.xlim([-1, x.size])
		xticksString = [i[0].split("-")[0] + "-\n" + i[0].split("-")[1] for i in day]
		plt.xticks(x, xticksString, rotation='vertical')
		plt.xlabel('Periods of Time')
		plt.ylabel('Volume (MB)')
		plt.title(date)
		plt.subplots_adjust(bottom = 0.15)
		fig.savefig('./fileInfo/receiverVolume_xHour_yVolume/' + date + '.eps', format = 'eps', dpi = fig.dpi)

def IP_xRank_yFreq():
    fig = plt.figure(figsize = (16, 9))
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Rank', fontsize = 30)
    plt.ylabel('Frequency', fontsize = 30)
    ipBook = readFromDict("./month/ipInfo/ipInfo1day.json")
    ipBookValues = sorted(ipBook.values(), reverse=True)
    rankFreq = [(r, f) for r, f in enumerate(ipBookValues, start = 1)]
    rank, freq = zip(*rankFreq)
    plt.plot(rank, freq, 'k')
    fig.savefig('./month/1day-IPRankFreq.eps', format = 'eps', dpi = fig.dpi)



def senderVolume_xDay_yVolume():
	if not os.path.exists("./fileInfo/senderVolume_xDay_yVolume"):
		os.makedirs("./fileInfo/senderVolume_xDay_yVolume")

	senderVolume = readFromDict("./fileInfo/senderVolumePerDay.json")
	dates = sorted(senderVolume.keys())
	y = []
	for date in dates:
		y += [sum([int(i.rstrip()) for i in senderVolume[date]]) / 1048576.0]

	y = np.array(y)
	x = np.arange(len(y))
	fig = plt.figure(figsize = (15, 8))
	plt.bar(x, y, width = 0.5, color = 'r', align = 'center')
	plt.xlim([-1, x.size])
	xticksString = dates
	plt.xticks(x, xticksString, fontsize = 10, rotation='vertical')
	plt.xlabel('Dates')
	plt.ylabel('Volume (MB)')
	plt.title("Sender Volume Total Per Day")
	plt.subplots_adjust(bottom = 0.15)
	fig.savefig('./fileInfo/senderVolume_xDay_yVolume/' + dates[0] + " ~ " + dates[-1] + '.eps', format = 'eps', dpi = fig.dpi)


def receiverVolume_xDay_yVolume():
	if not os.path.exists("./fileInfo/receiverVolume_xDay_yVolume"):
		os.makedirs("./fileInfo/receiverVolume_xDay_yVolume")
	receiverVolume = readFromDict("./fileInfo/receiverVolumePerDay.json")
	dates = sorted(receiverVolume.keys())
	y = []
	for date in dates:
		y += [int(receiverVolume[date].rstrip()) / 1048576.0]
	y = np.array(y)
	x = np.arange(len(y))
	fig = plt.figure(figsize = (15, 8))
	plt.bar(x, y, width = 0.5, color = 'r', align = 'center')
	plt.xlim([-1, x.size])
	xticksString = dates
	plt.xticks(x, xticksString, fontsize = 10, rotation='vertical')
	plt.xlabel('Dates')
	plt.ylabel('Volume (MB)')
	plt.title("Receiver Volume Total Per Day")
	plt.subplots_adjust(bottom = 0.15)
	fig.savefig('./fileInfo/receiverVolume_xDay_yVolume/' + dates[0] + " ~ " + dates[-1] + '.eps', format = 'eps', dpi = fig.dpi)
	

def fileBookRank():
    	#fileBook = readFromDict("./fileInfo/fileBook_MonthofMarch_2016.json")
    	fileBook = readFromDict("./fileInfo/post_URIs_referer_4months.json")
	fileBookCount = sorted(fileBook.items(), key = lambda x: x[1][0], reverse = True)
	fileBookSize = sorted(fileBook.items(), key = lambda x: x[1][1], reverse = True)
    #string1 = "URL\tTimes\tSize(GB)\n"
    	string1 = "URL\tTimes\n"
	for i in fileBookCount:
        	string1 += str(i[0]) + "\t" + str(i[1][0]) + "\n"
        #string1 += str(i[0]) + "\t" + str(i[1][0]) + "\t" + str(i[1][1]/1048576.0/1024) + "\n"
	string2 = "URL\tSize(GB)\tTimes\n"
	for i in fileBookSize:
		string2 += str(i[0]) + "\t" + str(i[1][1]/1048576.0/1024) + "\t" + str(i[1][0]) + "\n"
	writeToTxt(string1, "./fileInfo/postreferer_4months_Winter_2016.txt", "wb+")
    #writeToTxt(string2, "./fileInfo/fileBookSize_MonthofMarch_2016.txt.txt", "wb+")


def videoURL_xRank_yFreq():
	fig = plt.figure(figsize = (16, 9))
	plt.xscale('log')
	plt.yscale('log')
	plt.xlabel('Rank', fontsize = 30)
	plt.ylabel('Frequency', fontsize = 30)
	urlBook = readFromDict("fileInfo/fileBook.json")
	# for i in urlBook.items():
	# 	if (('mp4' in i[0]) and ('ASTR209' in i[0])):
	# 		print i[0]
	urlBookValues = sorted([i[1][0] for i in urlBook.items() if (('mov' in i[0]))], reverse=True)
	rankFreq = [(r, f) for r, f in enumerate(urlBookValues, start = 1)]
	rank, freq = zip(*rankFreq)
	plt.plot(rank, freq)
	fig.savefig('./fileInfo/urlRankFreqMov.eps', format = 'eps', dpi = fig.dpi)


def userAgent():
	userAgent = readFromDict("./httpInfo/userAgent.json")
	result = "UserAgent\tCount\n"
	userAgent = showTopKResults(userAgent, len(userAgent))
	for i in userAgent:
		result += i[0] + "\t" + str(i[1]) + "\n"
	writeToTxt(result, "./httpInfo/userAgentCountTop.txt", "wb+")


def userAgentID():
	# Should replace "#" with other characters, since the API gets error when sending it.
	userAgent = readFromDict("./httpInfo/userAgent.json")
	userAgentID = {}
	for i in userAgent:
		times = userAgent[i]
		url = "http://www.useragentstring.com/?uas=" + i + "&getJSON=all"
		url = url.replace(" ", "%20")
		response = {}
		try:
			response = json.loads(urllib2.urlopen(url).read(), object_hook = decodeDict)
		except Exception as msg:
			print "some error: " + msg.message + " " + i
		response.update({"times": times})
		userAgentID[i] = response
	writeToFile(userAgentID, "./httpInfo/userAgentID.json", "wb+")

def agentStatFig(figName, figSize, label = None, drawFig = True, rank = 0, textNumber = 0, dist = 0.15, bboxToAnchor = False):
	userAgentID = readFromDict("./httpInfo/userAgentID.json")
	for i in userAgentID:
		if "AppleCoreMedia" in i:
			userAgentID[i]["agent_name"] = "AppleCoreMedia"
			userAgentID[i]["agent_type"] = "AppleCoreMedia"
	data = {}
	for i in userAgentID:
        	if label is None:
            		if userAgentID[i][figName] not in data:
                		data[userAgentID[i][figName]] = userAgentID[i]["times"]
            		else:
                		data[userAgentID[i][figName]] += userAgentID[i]["times"]
        	else:
            		if userAgentID[i][label[0]] == label[1]:
                		data[userAgentID[i][figName]] = userAgentID[i]["times"]
            		else:
                		data[userAgentID[i][figName]] += userAgentID[i]["times"]

	if drawFig is True:
        	if label is None:
                	drawPieFigure(data, "./httpInfo/new/userAgentLabel/" + figName + ".eps", figSize, rank, textNumber, dist, bboxToAnchor)
            	else:
                	drawPieFigure(data, "./httpInfo/new/userAgentLabel/" + label[0] + "/" + label[1] + ".eps", figSize, rank, textNumber, dist, bboxToAnchor)
	return data
'''
def agentStatFig(figName, figSize, label = None, drawFig = True, rank = 0, textNumber = 0, dist = 0.15, bboxToAnchor = False):
	userAgentID = readFromDict("./httpInfo/userAgentID.json")
    
    #for i in userAgentID:
    #	if "AppleCoreMedia" in i:
    #		userAgentID[i]["agent_name"] = "AppleCoreMedia"
    #		userAgentID[i]["agent_type"] = "AppleCoreMedia"
	data = {}
	for i in userAgentID:
		if label is None:
			if userAgentID[i][figName] not in data:
				data[userAgentID[i][figName]] = userAgentID[i]["times"]
			else:
				data[userAgentID[i][figName]] += userAgentID[i]["times"]
		else:
			if userAgentID[i][label[0]] == label[1]:
				if userAgentID[i][figName] not in data:
					data[userAgentID[i][figName]] = userAgentID[i]["times"]
				else:
					data[userAgentID[i][figName]] += userAgentID[i]["times"]
    	print data
	if drawFig is True:
		if label is None:
			drawPieFigure(data, "./httpInfo/new/userAgentLabel/" + figName + ".eps", figSize, rank, textNumber, dist, bboxToAnchor)
        else:
			drawPieFigure(data, "./httpInfo/new/userAgentLabel/" + label[0] + "/" + label[1] + ".eps", figSize, rank, textNumber, dist, bboxToAnchor)
	return data

def userAgentLabel():
	if not os.path.exists("./httpInfo/new/userAgentLabel"):
		os.makedirs("./httpInfo/new/userAgentLabel")
            #agentStatFig("agent_name", (15, 9), rank = 8, textNumber = 8, dist = 0.05, bboxToAnchor = [1.18, 1])
	## Get agent_type distribution
    	agent_type = agentStatFig("agent_type", (15, 9))
	## Get agent_name distribution
    	agent_name = agentStatFig("agent_name", (15, 9), rank = 8, textNumber = 8, dist = 0.05, bboxToAnchor = [1.18, 1])
	# ## Get os_type distribution
        os_type = agentStatFig("os_type", (15, 8), rank = 6, textNumber = 4, dist = 0.2, bboxToAnchor = [0.95, 1])
	# ## Get os_name distribution
        os_name = agentStatFig("os_name", (15, 8))
	## Get agent_name distribution
        if not os.path.exists("./httpInfo/new/userAgentLabel/agent_type"):
            os.makedirs("./httpInfo/new/userAgentLabel/agent_type")
        for i in agent_type:
            agentStatFig("agent_name", (15, 9), ["agent_type", "Browser"], rank = 5, dist = 0.05, bboxToAnchor = [1.18, 1])

	# ## Get agent_version distribution
        if not os.path.exists("./httpInfo/new/userAgentLabel/agent_name"):
            os.makedirs("./httpInfo/new/userAgentLabel/agent_name")
        for i in agent_name:
            agentStatFig("agent_version", (15, 15), ["agent_name", i])

	# ## Get os_name distribution
        if not os.path.exists("./httpInfo/new/userAgentLabel/os_type"):
            os.makedirs("./httpInfo/new/userAgentLabel/os_type")
        for i in os_type:
            agentStatFig("os_name", (15, 15), ["os_type", i])

	
	# ## Get os_versionNumber distribution
        if not os.path.exists("./httpInfo/new/userAgentLabel/os_name"):
            os.makedirs("./httpInfo/new/userAgentLabel/os_name")
        for i in os_name:
            agentStatFig("os_versionNumber", (15, 15), ["os_name", i])

	# Test!!!!!!!!!!!!!!
	userAgentID = readFromDict("./httpInfo/userAgentID.json")
	total = 0
	for i in userAgentID:
        	if "AppleWebKit" in i:
            		total += userAgentID[i]["times"]
            		print userAgentID[i]["times"], i
	print total
    
def drawPieFigure(inputDict, fileName, figsize, rank = 0, textNumber = 0, dist = 0.15, bboxToAnchor = False):
	if textNumber == 0:
		textNumber = rank
	matplotlib.rcParams['font.size'] = 15
	matplotlib.rcParams['savefig.bbox'] = 'tight'
	plt.rcParams['patch.edgecolor'] = 'white'
	inputDict = sorted(inputDict.items(), key = lambda x: x[1], reverse = True)
	if rank != 0:
		inputDict = inputDict[0: rank] + [("others", sum([i[1] for i in inputDict[rank:]]))]
	inputTypes = [i[0].replace('\xc3\xa9', 'e') for i in inputDict]
	inputValues = [i[1] for i in inputDict]
	total = sum([i[1] for i in inputDict])
	sizes = [i[1]/float(total) for i in inputDict]
	colors = plt.cm.jet(np.linspace(0.8, 0.2, len(sizes)))
	explode = [i * dist for i in range(0, len(sizes))]
	fig = plt.figure(figsize = figsize)
	patches, texts, autotexts = plt.pie(sizes, explode = explode, labels = inputTypes[0:textNumber] + [""]*(len(inputTypes) - textNumber - 1) + ["others"], colors = colors, autopct = '%1.1f%%')
	plt.axis('equal')
	labels = ['{0} - {1:1.2f}% - {2}'.format(i, j*100, k) for i, j, k in zip(inputTypes, sizes, inputValues)]
	if bboxToAnchor is False:
		plt.legend(patches, labels, loc='upper right', fontsize = 10)
	else:
		plt.legend(patches, labels, loc='upper right', fontsize = 10, bbox_to_anchor = bboxToAnchor)
	fig.savefig(fileName, format = 'eps', dpi = fig.dpi)


def httpMethod(dataset):
        httpMethod = readFromDict("./" + dataset + "/httpInfo/httpMethod.json")
        dates = getDates()
        y_get = [0] * len(dates)
        y_head = [0] * len(dates)
	y_post = [0] * len(dates)
        for date in dates:
        	position = dates.index(date)
            	for i in httpMethod[date]:
                	if "GET" in httpMethod[date][i]:
                 		y_get[position] += httpMethod[date][i]["GET"]
			if "POST" in httpMethod[date][i]:
                                y_post[position] += httpMethod[date][i]["POST"]
                        if "HEAD" in httpMethod[date][i]:
                            	y_head[position] += httpMethod[date][i]["HEAD"]
        x = np.arange(len(dates))
        fig = plt.figure(figsize = (16, 9))
        plt.gca().set_color_cycle(['green', 'black'])
       	#plt.plot(x, y_get)
	plt.plot(x, y_post)
        #plt.plot(x, y_head, '--')
        xticksString = ["Jan", "Feb", "Mar", "Apr"]
        plt.xticks([0, 31, 59, 90], xticksString)
        plt.ylabel('Count')
	'''
        if dataset == 'http_dataset':
            y_format = FuncFormatter(millionsLabel)
        else:
            y_format = FuncFormatter(kilosLabel)
        plt.gca().yaxis.set_major_formatter(y_format)
        plt.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(prune = 'lower'))
        '''
	plt.title("NUMBER OF HTTP POST REQUESTS FOR THE WINTER 2016 TERM")
	#plt.ylim([0,65])
	#plt.legend(['GET', 'HEAD'], loc='upper right', ncol=2)
    	fig.savefig('./http_dataset/' + dataset + 'POST.eps', format = 'eps', dpi = fig.dpi)
'''
def httpStatusCode():
	httpStatusCode = readFromDict("./" + "/httpInfo/httpStatusCode_All.json")
	dates = getDates()
	statusCodes = {}
	for date in dates:
		for i in httpStatusCode[date]:
			for statusCode in httpStatusCode[date][i]:
				if statusCode not in statusCodes:
					statusCodes[statusCode] = httpStatusCode[date][i][statusCode]
				else:
					statusCodes[statusCode] += httpStatusCode[date][i][statusCode]
	statusCodes = sorted(statusCodes.items(), key = lambda x: x[1], reverse = True)
	statusValues = [i[1] for i in statusCodes]
	print statusCodes
	print "Sum: ", sum(statusValues)
	print "Ave: ", ["{:.2}".format(float(i) / len(dates)) for i in statusValues]
	print "Pct: ", ["{:.2%}".format(float(i) / sum(statusValues)) for i in statusValues]
	# Draw line graph.
	statusNames = [k[0] for k in statusCodes][0: 14]
	y = [[0] * len(dates) for i in range(len(statusNames))]
	for date in dates:
		for i in httpStatusCode[date]:
			for j in httpStatusCode[date][i]:
				try:
					if j not in ['-', '301', '416', '400']:
						position = statusNames.index(j)
						y[position][dates.index(date)] += httpStatusCode[date][i][j]
				except Exception as Error:
					print Error
	x = np.arange(len(dates))
	fig = plt.figure(figsize = (16, 9))
	colors = ['black', 'darkred', 'darkblue', 'darkseagreen','darkcyan','darkgoldenrod', 'darkgray', 'darkkhaki', 'darkorange', 'darkseagreen', 'deeppink', 'firebrick','violet', 'steelblue']
	plt.gca().set_color_cycle(colors)
	lines = iter(["-", "--", "-.", "-","-", "--", "-.", "-","-", "--", "-" , "--", "-.","])
	for i in y:
		plt.plot(x, i[:100] + [0] + i[101:], linestyle = next(lines))
	xticksString = ["Jan", "Feb", "Mar", "Apr"]
	plt.xticks([0, 31, 59, 90], xticksString)
	plt.ylabel('Count')
	plt.yscale('log')
	# y_format = FuncFormatter(kilosLabel)
	# plt.gca().yaxis.set_major_formatter(y_format)
	# plt.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(prune = 'lower'))
	plt.legend(statusNames, loc='upper right', ncol=2)
	fig.savefig('./httpInfo/D2L_httpStatusCode_All.eps', format = 'eps', dpi = fig.dpi)
    
def fileBookRank():
    fileBook = readFromDict("./fileInfo/refererBookTotal.json")
        fileBookCount = sorted(fileBook.items(), key = lambda x: x[1][0], reverse = True)
        #fileBookSize = sorted(fileBook.items(), key = lambda x: x[1][1], reverse = True)
        string1 = "URL\tTimes\n"
        for i in fileBookCount:
        	string1 += str(i[0]) + "\t" + str(i[1][0]) + "\n"
    #string2 = "URL\tSize(GB)\tTimes\n"
    #for i in fileBookSize:
    #string2 += str(i[0]) + "\t" + str(i[1][1]/1048576.0/1024) + "\t" + str(i[1][0]) + "\n"
    	writeToTxt(string1, "./fileInfo/new2.txt", "wb+")
#writeToTxt(string2, "./fileInfo/fileBookSize_MonthofMarch_2016.txt.txt", "wb+")



def refererTopK(k):
	refererBook = readFromDict("./fileInfo/refererBookTotal.json")
	refererTime = sorted(refererBook.items(), key = lambda x: x[1][0], reverse = True)[0: k]
	refererSize = sorted(refererBook.items(), key = lambda x: x[1][1], reverse = True)[0: k]
	refererTimeTxt = "Referer" + "\t\t" + "Times" + "\n"
    	refererSizeTxt = "Referer" + "\t\t" + "Size (GB)" + "\t\tTimes\n"
	for i in range(k):
            #refererTimeTxt += refererTime[i][0] + "\t\t" + str(refererTime[i][1][0]) + "\n"
            refererTimeTxt += refererTime[i][0] + "\t\t" + str(refererTime[i][1][0]) + "\t\t" + str(refererTime[i][1][1] / 1073741824.0) + "\n"
            #refererSizeTxt += refererSize[i][0] + "\t\t" + str(refererSize[i][1][1]) + "\t\t" + str(refererSize[i][1][0]) + "\n"
	writeToTxt(refererTimeTxt, "./fileInfo/refererTime.txt", "wb+")
    #writeToTxt(refererSizeTxt, "./fileInfo/refererSize.txt", "wb+")



def sslEncryptionCode():
	httpStatusCode = readFromDict("./" + "/sslinfo/httpMethod.json")
	dates = getDates()
	statusCodes = {}
	for date in dates:
		for i in httpStatusCode[date]:
			for statusCode in httpStatusCode[date][i]:
				if statusCode not in statusCodes:
					statusCodes[statusCode] = httpStatusCode[date][i][statusCode]
				else:
					statusCodes[statusCode] += httpStatusCode[date][i][statusCode]
	statusCodes = sorted(statusCodes.items(), key = lambda x: x[1], reverse = True)
	statusValues = [i[1] for i in statusCodes]
	print statusCodes
	print "Sum: ", sum(statusValues)
	print "Ave: ", ["{:.2}".format(float(i) / len(dates)) for i in statusValues]
	print "Pct: ", ["{:.2%}".format(float(i) / sum(statusValues)) for i in statusValues]
	# Draw line graph.
	statusNames = [k[0] for k in statusCodes][0: 10]
        print "Status Names"
        print statusNames
	y = [[0] * len(dates) for i in range(len(statusNames))]
	for date in dates:
		for i in httpStatusCode[date]:
			for j in httpStatusCode[date][i]:
				try:
                                        if j not in ['-']:
                                                position = statusNames.index(j)
                                                y[position][dates.index(date)] += httpStatusCode[date][i][j]
                                except Exception as Error:
                                        print Error
    	print "this is y"
    	print y

	x = np.arange(len(dates))
	fig = plt.figure(figsize=(21,11))
	colors = ['black', 'red', 'blue', 'darkgreen','yellow','white','cyan','darkviolet','grey','darkorange']
	plt.gca().set_color_cycle(colors)
	lines = iter(["-", "--", "-", "-","-","--","-","--","-","--"])
	#plot(x, y, linewidth=width)
	for i in y:
		plt.plot(x, i[:100] + [0] + i[101:], linestyle = next(lines), linewidth= 2)
	xticksString = ["Jan", "Feb", "Mar", "Apr"]
	plt.xticks([0, 31, 59, 90], xticksString)
	plt.ylabel('Count')
	plt.yscale('log')
	# y_format = FuncFormatter(kilosLabel)
	# plt.gca().yaxis.set_major_formatter(y_format)
	# plt.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(prune = 'lower'))
	plt.legend(statusNames, loc='upper right', ncol=2)
	fig.savefig('./sslinfo/ssl_Encryption_Code.eps', format = 'eps', dpi = fig.dpi)

def userAgentTrace():
	userAgentTrace = readFromDict("./httpInfo/userAgentTrace.json")
	userAgentID = readFromDict("./httpInfo/userAgentID.json")
	osNames = ['OS X', 'iPhone OS', 'Android', 'Chrome OS']
	osTrace = {}
	for osName in osNames:
		osTrace[osName] = {}
		for ip in userAgentTrace:
			osTrace[osName][ip] = []
			for userAgent in sorted(userAgentTrace[ip].items(), key = lambda x: x[1]):
				userAgent = userAgent[0]
				if userAgentID[userAgent]['os_name'] == osName:
					if userAgentID[userAgent]['os_versionNumber'] not in osTrace[osName][ip]:
						osTrace[osName][ip].append(userAgentID[userAgent]['os_versionNumber'])
	
	for osName in osNames:
		print "os_name: " + osName
		total_user = 0
		update_user = 0
		for i in osTrace[osName]:
			if len(osTrace[osName][i]) > 0:
				total_user += 1
			if len(osTrace[osName][i]) > 1:
				update_user += 1
		print "total users: ", total_user
		print "update_user: ", update_user
		print "percentage: ", '{:.3%}'.format(update_user / float(total_user)), "\n"

	agentNames = agentStatFig("agent_name", (15, 15), drawFig = False)
	agentTrace = {}
	for agentName in agentNames:
		agentTrace[agentName] = {}
		for ip in userAgentTrace:
			agentTrace[agentName][ip] = []
			for userAgent in sorted(userAgentTrace[ip].items(), key = lambda x: x[1]):
				userAgent = userAgent[0]
				if userAgentID[userAgent]['agent_name'] == agentName:
					if userAgentID[userAgent]['agent_version'] not in agentTrace[agentName][ip]:
						agentTrace[agentName][ip].append(userAgentID[userAgent]['agent_version'])
	
	for agentName in agentNames:
		print "agent_name: " + agentName
		total_user = 0
		update_user = 0
		for i in agentTrace[agentName]:
			if len(agentTrace[agentName][i]) > 0:
				total_user += 1
			if len(agentTrace[agentName][i]) > 1:
				update_user += 1
		print "total users: ", total_user
		print "update_user: ", update_user
		if total_user > 0:
			print "percentage: ", '{:.3%}'.format(update_user / float(total_user)), "\n"
		else:
			print "percentage: ", '{:.3%}'.format(float(0)), "\n"


def courseRelatedURL():
	courseRelatedURL = readFromDict("fileInfo/courseRelatedURL.json")
	dates = getDates()
	string1 = "{:<100}{:<10}{:<15}\n".format("URL", "Count", "Size (GB)")
	string2 = "{:<100}{:<15}{:<10}\n".format("URL", "Size (GB)", "Count")
	for date in dates:
	 	timePeriods = sorted(courseRelatedURL[date].keys())
	 	for timePeriod in timePeriods:
	 		URLsCount = sorted(courseRelatedURL[date][timePeriod].items(), key = lambda x: x[1][0], reverse = True)
	 		URLsSize = sorted(courseRelatedURL[date][timePeriod].items(), key = lambda x: x[1][1], reverse = True)
	 		string1 += "Date: " + date + "    " + "Period: " + timePeriod + "\n"
	 		string2 += "Date: " + date + "    " + "Period: " + timePeriod + "\n"
	 		for i in URLsCount:
	 			string1 += "{:<100}{:<10,}{:<15,.2f}\n".format(i[0], i[1][0], i[1][1]/1048576.0/1024)
	 		for i in URLsSize:
	 			string2 += "{:<100}{:<15,.2f}{:<10,}\n".format(i[0], i[1][1]/1048576.0/1024, i[1][0])
	 		string1 += "\n"
	 		string2 += "\n"
	 writeToTxt(string1, "./fileInfo/courseRelatedURLCount.txt", "wb+")
	 writeToTxt(string2, "./fileInfo/courseRelatedURLSize.txt", "wb+")

	homework = []
	for date in dates:
		for timePeriod in courseRelatedURL[date]:
			shortURL = {"Video": [0, 0], "Course Note": [0, 0], "Homework": [0, 0], "Midterm": [0, 0], "Outline": [0, 0], "Final": [0, 0]}
			for url in courseRelatedURL[date][timePeriod]:
				if ("mp4" in url) or ("mov" in url):
					shortURL["Video"][0] += courseRelatedURL[date][timePeriod][url][0]
					shortURL["Video"][1] += courseRelatedURL[date][timePeriod][url][1]
				elif "Homework" in url:
					shortURL["Homework"][0] += courseRelatedURL[date][timePeriod][url][0]
					shortURL["Homework"][1] += courseRelatedURL[date][timePeriod][url][1]
				elif "Course_Notes" in url:
					shortURL["Course Note"][0] += courseRelatedURL[date][timePeriod][url][0]
					shortURL["Course Note"][1] += courseRelatedURL[date][timePeriod][url][1]
				elif "Outline" in url:
					shortURL["Outline"][0] += courseRelatedURL[date][timePeriod][url][0]
					shortURL["Outline"][1] += courseRelatedURL[date][timePeriod][url][1]
				elif ("Midterm" in url) or ("midterm" in url):
					shortURL["Midterm"][0] += courseRelatedURL[date][timePeriod][url][0]
					shortURL["Midterm"][1] += courseRelatedURL[date][timePeriod][url][1]
				elif ("Final" in url) or ("final" in url):
					shortURL["Final"][0] += courseRelatedURL[date][timePeriod][url][0]
					shortURL["Final"][1] += courseRelatedURL[date][timePeriod][url][1]
			courseRelatedURL[date][timePeriod] = shortURL
		homework += [sum([courseRelatedURL[date][i]["Final"][0] for i in courseRelatedURL[date]])]

	string1 = "{:<100}{:<10}{:<15}\n".format("URL Group", "Count", "Size (GB)")
	string2 = "{:<100}{:<15}{:<10}\n".format("URL Group", "Size (GB)", "Count")
	for date in dates:
		timePeriods = sorted(courseRelatedURL[date].keys())
		for timePeriod in timePeriods:
			URLsCount = sorted(courseRelatedURL[date][timePeriod].items(), key = lambda x: x[1][0], reverse = True)
			URLsSize = sorted(courseRelatedURL[date][timePeriod].items(), key = lambda x: x[1][1], reverse = True)
			string1 += "Date: " + date + "    " + "Period: " + timePeriod + "\n"
			string2 += "Date: " + date + "    " + "Period: " + timePeriod + "\n"
			for i in URLsCount:
				string1 += "{:<100}{:<10,}{:<15,.2f}\n".format(i[0], i[1][0], i[1][1]/1048576.0/1024)
			for i in URLsSize:
				string2 += "{:<100}{:<15,.2f}{:<10,}\n".format(i[0], i[1][1]/1048576.0/1024, i[1][0])
			string1 += "\n"
			string2 += "\n"
	writeToTxt(string1, "./fileInfo/shortURLCount.txt", "wb+")
	writeToTxt(string2, "./fileInfo/shortURLSize.txt", "wb+")

	y = np.array(homework)
	x = np.arange(len(y))
	fig = plt.figure(figsize = (16, 9))
	plt.plot(x, y, 'k')
	xticksString = ["Jan", "Feb", "Mar", "Apr"]
	plt.xticks([0, 31, 59, 90], xticksString)
	plt.ylabel('Number of Requests')
	fig.savefig('./fileInfo/course.eps', format = 'eps', dpi = fig.dpi)
	
	httpRequests = readFromDict("./httpInfo/videoCountPerDay.json")
	dates = getDates()
	y = []
	for date in dates:
		y += [sum([int(str(i)) for i in httpRequests[date].values()])]
	print sum(y)

refererTopK(1001)
httpRequests_xHour_yTimes()
httpRequests_xDay_yTimes()
httpStatusCode()
sslEncryptionCode()
httpMethod('http_dataset')
#senderVolume_xHour_yVolume()
#receiverVolume_xHour_yVolume()
#senderVolume_xDay_yVolume()
#receiverVolume_xDay_yVolume()
#fileBookRank()
#userAgent()
#httpMethod()
#ipBookID()
#ipBookIDCheck()
#ipLabel()
#ipRank()
#userAgentID()
#userAgentLabel()
IP_xRank_yFreq()
#fileBookRank2()
#videoURL_xRank_yFreq()
#userAgentTrace()
#courseRelatedURL()
