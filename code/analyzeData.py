import os
import subprocess
import glob
from sharedMethods import *
import datetime


class AnalyzeData:
	rootDir = "/home/sourish/http"

	def __init__(self):
		os.chdir(self.rootDir)
		if not os.path.exists("./httpInfo"):
			os.makedirs("./httpInfo")
		if not os.path.exists("./ipInfo"):
			os.makedirs("./ipInfo")
		if not os.path.exists("./fileInfo"):
			os.makedirs("./fileInfo")
		self.httpRequestTotalPerDay()
		self.ipInfo()
		self.httpMethod()
		self.httpStatusCode()
		self.checkUserAgent()
		self.fileBookPerDay()
		self.fileBook()
		self.ipBookPerDay()
		self.senderVolumePerDay()
		self.receiverVolumePerDay()
		self.contentInfo()
		self.userAgentTrace()
		self.videoRecords()
		self.videoCountPerDay()
		self.videoVolumePerDay()
		self.courseRelatedURL()
		self.fileSizeDistribution("/d2l.ucalgary.ca/d2l/home/", 'Topic0_GeneralInfo.json')
		self.courseRequests()
		self.courseVolume()
		self.videoConnDuration()
		self.videoResponseSize()

	def __getDateList(self):
		"""This function returns a list of strings, of all the dates.
		"""
		start = datetime.date(2016, 01, 01)
		end = datetime.date(2016, 04, 30)
		daysRange = (end - start).days
		return [str(start + datetime.timedelta(days = i)) for i in range(daysRange + 1)]


	def checkUserAgent(self):
                        userAgent = {}
                        dates = self.__getDateList()
                        for date in dates:
                                methodsPerDay = subprocess.check_output("zcat /data4/" + date + "/http.*.gz" + " | gawk 'BEGIN {RS=\"\\\\\\\\n\"; FS=\"\\\\\\\\t\"} $3~/199.30.181.42/ {print $12}'", shell = True).rsplit('\n')
                                for i in methodsPerDay:
                                        if i != "":
                                                if i not in userAgent.keys():
                                                        userAgent[i] = 1
                                                else:
                                                        userAgent[i] += 1
                        writeToFile(userAgent, "./httpInfo/userAgent.json", "wb+")
        def fileSizeDistribution(self, url, savedName):
		url = url.replace('/', '\\/').replace('.', '\\.')
		fileSizeValues = []
		for date in ["2015-02-18", "2015-02-19", "2015-02-20", "2015-02-21", "2015-02-22", "2015-02-23", "2015-02-24"]:
			for files in glob.glob("./httpRequests/" + date + "/http.*.txt.gz"):
				result = subprocess.check_output(
					"zcat " + files + " | gawk 'BEGIN {RS=\"\\\\\\\\n\"; FS=\"\\\\\\\\t\"} ($10~/" + url + "/) && ($5~/199.30.181.42/) {print $1 \"\\t\" $14}'",
					shell = True
					).rsplit('\n')
				for i in result[1: -1]:
					i = i.split("\t")
					fileSizeValues += [(int(float(i[0])), int(i[1]))]
		writeToFile(fileSizeValues, './fileInfo/' + savedName, 'wb')
		print "fileSizeDistribution " + savedName + " : Done"


	def httpRequestTotalPerDay(self):
		#This function returns a dictionary containing the total number of requests per hour per day.
		#E.g. {'2014-12-01': {'00...-01...': '1000\n', '01...-02...': '23423\n'} ...}
		#Also the dictionary is written to ISM/httpInfo/httpRequestTotalPerDay.json file.
                httpRequestTotalPerDay = {}
		dates = self.__getDateList()
		for date in dates:
			httpRequestTotalPerDay[date] = {}
			for files in glob.glob("./httpRequests/" + date + "/http.*.txt.gz"):
				httpRequestTotalPerDay[date][files.split("/")[-1].split(".")[1]] = subprocess.check_output("zcat " + files + " | gawk 'BEGIN {i=0; RS=\"\\\\\\\\n\"; FS=\"\\\\\\\\t\"} $5~/199.30.181.42/ {i++} END {print i}'", shell = True)
		writeToFile(httpRequestTotalPerDay, "./httpInfo/httpRequestTotalPerDay.json", "wb+")


	def ipInfo(self):
		ipBook = {}
		dates = self.__getDateList()
		for date in dates:
			ipBookPerDay = subprocess.check_output("zcat ./httpRequests/" + date + "/http.*.gz" + " | gawk 'BEGIN {RS=\"\\\\\\\\n\"; FS=\"\\\\\\\\t\"} $5~/199.30.181.42/ {print $3}'", shell = True).rsplit('\n')
			for i in ipBookPerDay:
				if i not in ipBook:
					ipBook[i] = 1
				else:
					ipBook[i] += 1
		writeToFile(ipBook, "./ipInfo/ipBook.json", "wb+")


	def ipBookPerDay(self):
		#This function uses the data in httpRequests, output a dictionary to the ipInfo/ipBookPerDay folder.
		if not os.path.exists("./ipInfo/ipBookPerDay/"):
			os.makedirs("./ipInfo/ipBookPerDay/")
		dates = self.__getDateList()
		for date in dates:
			if os.path.exists("./httpRequests/" + date):
				ipBookPerDay = {}
				ipDataPerDay = subprocess.check_output("zcat ./httpRequests/" + date + "/http.*.gz" + " | gawk 'BEGIN {RS=\"\\\\\\\\n\"; FS=\"\\\\\\\\t\"} $5~/199.30.181.42/ {print $3}'", shell = True).rsplit('\n')
				for i in ipDataPerDay:
					if i not in ipBookPerDay:
						ipBookPerDay[i] = 1
					else:
						ipBookPerDay[i] += 1
			writeToFile(ipBookPerDay, "./ipInfo/ipBookPerDay/" + date + ".json", "wb+")


	def httpMethod(self):
		httpMethod = {}
		dates = self.__getDateList()
		for date in dates:
			httpMethod[date] = {}
			if os.path.exists("./httpRequests/" + date):
				for files in glob.glob("./httpRequests/" + date + "/http.*.txt.gz"):
					time = files.split("/")[-1].split(".")[1]
					httpMethod[date][time] = {}
					result = subprocess.check_output("zcat " + files + " | gawk 'BEGIN {RS=\"\\\\\\\\n\"; FS=\"\\\\\\\\t\"} $5~/199.30.181.42/ {print $8}'", shell = True).rsplit("\n")
					for record in result:
						if record != "":
							if record not in httpMethod[date][time]:
								httpMethod[date][time][record] = 1
							else:
								httpMethod[date][time][record] += 1
		writeToFile(httpMethod, "./httpInfo/httpMethod.json", "wb+")



	def httpStatusCode(self):
		httpStatusCode = {}
		dates = self.__getDateList()
		for date in dates:
			httpStatusCode[date] = {}
			if os.path.exists("./httpRequests/" + date):
				for files in glob.glob("./httpRequests/" + date + "/http.*.txt.gz"):
					time = files.split("/")[-1].split(".")[1]
					httpStatusCode[date][time] = {}
					result = subprocess.check_output("zcat " + files + " | gawk 'BEGIN {RS=\"\\\\\\\\n\"; FS=\"\\\\\\\\t\"} $5~/199.30.181.42/ {print $15}'", shell = True).rsplit("\n")
					for record in result:
						if record != "":
							if record not in httpStatusCode[date][time]:
								httpStatusCode[date][time][record] = 1
							else:
								httpStatusCode[date][time][record] += 1
		writeToFile(httpStatusCode, "./httpInfo/httpStatusCode.json", "wb+")


analyze = AnalyzeData()


####################################################
	# These functions need the servers site contentInfo folder support.
	def userAgentTrace(self):
		userAgentTrace = {}
		for date in self.__getDateList():
			data = readFromDict("./httpInfo/contentInfo/" + date + ".json")
			for hour in sorted(data.keys()):
				for order in range(1, len(data[hour]) + 1):
					order = str(order)
					ip = data[hour][order][0]
					userAgent = data[hour][order][4]
					time = date + ";" + hour
					if ip not in userAgentTrace:
						userAgentTrace[ip] = {userAgent: time}
					else:
						if userAgent not in userAgentTrace[ip]:
							userAgentTrace[ip].update({userAgent: time})
		writeToFile(userAgentTrace, "./httpInfo/userAgentTrace.json", "wb+")


	def videoRecords(self):
		result = ""
		for date in self.__getDateList():
			data = readFromDict("./httpInfo/contentInfo/" + date + ".json")
			for hour in sorted(data.keys()):
				for order in range(1, len(data[hour]) + 1):
					order = str(order)
					ip = data[hour][order][0]
					http_method = data[hour][order][1]
					url = data[hour][order][2]
					response_volume = data[hour][order][5]
					http_status = data[hour][order][6]
					if ('mov' in url or 'mp4' in url) and (http_status != '404'):
						result += date + " " + hour + "\t" + order + "\t" + ip + "\t" + http_method + "\t" + url + "\t" + str(float(response_volume) / 1048576) + "\t" + http_status + "\n"
		writeToTxt(result, "./fileInfo/videoRecords.txt", 'wb+')
	####################################################               

	


	def videoCountPerDay(self):
		videoCountPerDay = {}
		dates = self.__getDateList()
		for date in dates:
			videoCountPerDay[date] = {}
			for files in glob.glob("./httpRequests/" + date + "/http.*.txt.gz"):
				videoCountPerDay[date][files.split("/")[-1].split(".")[1]] = int(subprocess.check_output(
					"zcat " + files + " | gawk 'BEGIN {i=0; RS=\"\\\\\\\\n\"; FS=\"\\\\\\\\t\"} ($5~/136.159.55.130/) && (($10~/mp4/) || ($10~/mov/)) {i++} END {print i}'",
					shell = True
					).rsplit('\n')[0])
		writeToFile(videoCountPerDay, "./httpInfo/videoCountPerDay.json", "wb+")


	def videoVolumePerDay(self):
		videoVolumePerDay = {}
		dates = self.__getDateList()
		for date in dates:
			videoVolumePerDay[date] = {}
			for files in glob.glob("./httpRequests/" + date + "/http.*.txt.gz"):
				videoVolumePerDay[date][files.split("/")[-1].split(".")[1]] = int(subprocess.check_output(
					"zcat " + files + " | gawk 'BEGIN {RS=\"\\\\\\\\n\"; FS=\"\\\\\\\\t\"; i = 0;} ($5~/136.159.55.130/) && (($10~/mp4/) || ($10~/mov/)) {i += int($14);} END {print i}'",
					shell = True
					).rsplit('\n')[0])
		writeToFile(videoVolumePerDay, "./fileInfo/videoVolumePerDay.json", "wb+")


	def fileBookPerDay(self):
		if not os.path.exists("./fileInfo/fileBookPerDay/"):
			os.makedirs("./fileInfo/fileBookPerDay/")
		dates = self.__getDateList()
		for date in dates:
			fileBookPerDay = {}
			if os.path.exists("./httpRequests/" + date):
				fileDataPerDay = subprocess.check_output("zcat ./httpRequests/" + date + "/http.*.gz" + " | gawk 'BEGIN {RS=\"\\\\\\\\n\"; FS=\"\\\\\\\\t\"} $5~/136.159.55.130/ {print $10 \"\\t\" $14}'", shell = True).rsplit("\n")
				for i in fileDataPerDay:
					i = i.split("\t")
					if (i[0] != "-") and (i[0] != "") and (i[1] != "-") and (i[1] != ""):
						if (i[0] not in fileBookPerDay):
							fileBookPerDay[i[0]] = [1, int(i[1])]
						else:
							fileBookPerDay[i[0]][0] += 1
							fileBookPerDay[i[0]][1] += int(i[1])
			writeToFile(fileBookPerDay, "./fileInfo/fileBookPerDay/" + date + ".json", "wb+")


	def fileBook(self):
		dates = self.__getDateList()
		fileBook = {}
		for date in dates:
			if os.path.exists("./fileInfo/fileBookPerDay/" + date + ".json"):
				fileBookPerDay = readFromDict("./fileInfo/fileBookPerDay/" + date + ".json")
				for url in fileBookPerDay:
					if url not in fileBook:
						fileBook[url] = fileBookPerDay[url]
					else:
						fileBook[url][0] += fileBookPerDay[url][0]
						fileBook[url][1] += fileBookPerDay[url][1]
		writeToFile(fileBook, "./fileInfo/fileBook.json", "wb+")


	def senderVolumePerDay(self):
		senderVolumePerDay = {}
		dates = self.__getDateList()
		for date in dates:
			senderVolumePerDay[date] = subprocess.check_output("zcat ./httpRequests/" + date + "/http.*.gz" + " | gawk 'BEGIN {RS=\"\\\\\\\\n\"; FS=\"\\\\\\\\t\"; i = 0;} $5~/136.159.55.130/ {i += int($13);} END {print i}'", shell = True).rsplit()[0]
		writeToFile(senderVolumePerDay, "./fileInfo/senderVolumePerDay.json", "wb+")


	def receiverVolumePerDay(self):
		receiverVolumePerDay = {}
		dates = self.__getDateList()
		for date in dates:
			receiverVolumePerDay[date] = subprocess.check_output("zcat ./httpRequests/" + date + "/http.*.gz" + " | gawk 'BEGIN {RS=\"\\\\\\\\n\"; FS=\"\\\\\\\\t\"; i = 0;} $5~/136.159.55.130/ {i += int($14);} END {print i}'", shell = True).rsplit()[0]
		writeToFile(receiverVolumePerDay, "./fileInfo/receiverVolumePerDay.json", "wb+")


	def contentInfo(self):
		#Extracting useful information including sender_IP (FS 3), http_method (FS 8), url (FS 10),
		#referer (FS 11), user_agent(FS 12), response_volume (FS 14), http_status (FS 15),
		if not os.path.exists("./httpInfo/contentInfo/"):
			os.makedirs("./httpInfo/contentInfo/")
		# period1 = [str(datetime.date(2015, 02, 15) + datetime.timedelta(days = i)) for i in range(10)]
		# period2 = [str(datetime.date(2015, 03, 15) + datetime.timedelta(days = i)) for i in range(10)]
		# period3 = [str(datetime.date(2015, 04, 15) + datetime.timedelta(days = i)) for i in range(7)]
		for date in self.__getDateList():
			contentInfo = {}
			for files in glob.glob("./httpRequests/" + date + "/http.*.txt.gz"):
				result = subprocess.check_output(
					"zcat " + files + " | gawk 'BEGIN {RS=\"\\\\\\\\n\"; FS=\"\\\\\\\\t\"} $5~/136.159.55.130/ {print $3 \"\\t\" $8 \"\\t\" $10 \"\\t\" $11 \"\\t\" $12 \"\\t\" $14 \"\\t\" $15}'", shell = True
				).rsplit("\n")
				contentInfo[files.split("/")[-1].split(".")[1]] = {}
				order = 1
				for i in result[0: -1]:
					i = i.split("\t")
					# sender_IP = i[0]
					# http_method = i[1]
					# url = i[2]
					# referer = i[3]
					# user_agent = i[4]
					# response_volume = i[5]
					# http_status = i[6]
					contentInfo[files.split("/")[-1].split(".")[1]].update({order: i})
					order += 1
			writeToFile(contentInfo, "./httpInfo/contentInfo/" + date + ".json", "wb+")


	def courseRelatedURL(self):
		courseRelatedURL = {}
		dates = self.__getDateList()
		for date in dates:
			courseRelatedURL[date] = {}
			for files in glob.glob("./httpRequests/" + date + "/http.*.txt.gz"):
				timePeriod = files.split("/")[-1].split(".")[1]
				courseRelatedURL[date][timePeriod] = {}
				courseRelatedURLPerDay = subprocess.check_output(
					"zcat " + files + " | gawk 'BEGIN {RS=\"\\\\\\\\n\"; FS=\"\\\\\\\\t\"} ($5~/136.159.55.130/) && (($10~/mp4/) || ($10~/mov/) || ($10~/pdf/)) {print $10 \"\\t\" $14}'",
					shell = True
					).rsplit('\n')
				for i in courseRelatedURLPerDay:
					i = i.split("\t")
					if (i[0] != "-") and (i[0] != "") and (i[1] != "-") and (i[1] != ""):
						if (i[0] not in courseRelatedURL[date][timePeriod]):
							courseRelatedURL[date][timePeriod][i[0]] = [1, int(i[1])]
						else:
							courseRelatedURL[date][timePeriod][i[0]][0] += 1
							courseRelatedURL[date][timePeriod][i[0]][1] += int(i[1])
		writeToFile(courseRelatedURL, "./fileInfo/courseRelatedURL.json", "wb+")


	def courseRequests(self):
		courseRequests = {}
		dates = self.__getDateList()
		courses = ["AST209", "ASPH213", "ASPH503"]
		for course in courses:
			courseRequests[course] = {}
			for date in dates:
				regex = course[-3:]
				if regex == '213':
					regex = "[^0+]213[^0]"
				result = int(subprocess.check_output(
					"zcat ./httpRequests/" + date + "/http.*.gz" + " | gawk 'BEGIN {i=0; RS=\"\\\\\\\\n\"; FS=\"\\\\\\\\t\"} ($5~/136.159.55.130/) && ($10~/" + regex + "/) {i++} END {print i}'",
					shell = True
					).rsplit('\n')[0])
				courseRequests[course][date] = result
		writeToFile(courseRequests, './httpInfo/courseRequests.json', 'wb+')


	def courseVolume(self):
		courseVolume = {}
		dates = self.__getDateList()
		courses = ["AST209", "ASPH213", "ASPH503"]
		for course in courses:
			courseVolume[course] = {}
			for date in dates:
				regex = course[-3:]
				if regex == '213':
					regex = "[^0+]213[^0]"
				result = int(subprocess.check_output(
					"zcat ./httpRequests/" + date + "/http.*.gz" + " | gawk 'BEGIN {i=0; RS=\"\\\\\\\\n\"; FS=\"\\\\\\\\t\"} ($5~/136.159.55.130/) && ($10~/" + regex + "/) {i += int($14)} END {print i}'",
					shell = True
					).rsplit('\n')[0])
				courseVolume[course][date] = result
		writeToFile(courseVolume, './httpInfo/courseVolume.json', 'wb+')


	def videoConnDuration(self):
		videoConnDuration = {}
		dates = self.__getDateList()
		for date in dates:
			videoConnDuration[date] = {}
			for files in glob.glob("./httpRequests/" + date + "/http.*.txt.gz"):
				timePeriod = files.split("/")[-1].split(".")[1]
				videoConnDuration[date][timePeriod] = []
				result = subprocess.check_output(
					"zcat " + files + " | gawk 'BEGIN {RS=\"\\\\\\\\n\"; FS=\"\\\\\\\\t\"} ($5~/136.159.55.130/) && (($10~/mp4/) || ($10~/mov/)) {print $14 \"\\t\" $28 \"\\t\" $29 \"\\t\" $30 \"\\t\" $31}'",
					shell = True
					).rsplit('\n')
				for i in result:
					i = i.split("\t")
					if len(i) == 5:
						i = [float(j) for j in i]
						videoConnDuration[date][timePeriod].append(i)
		writeToFile(videoConnDuration, './fileInfo/videoConnDuration.json', 'wb+')


	def videoResponseSize(self):
		videoResponseSize = []
		dates = self.__getDateList()
		for date in dates:
			for files in glob.glob("./httpRequests/" + date + "/http.*.txt.gz"):
				result = subprocess.check_output(
					"zcat " + files + " | gawk 'BEGIN {RS=\"\\\\\\\\n\"; FS=\"\\\\\\\\t\"} ($5~/136.159.55.130/) && (($10~/mp4/) || ($10~/mov/)) {print $14}'",
					shell = True
					).rsplit('\n')
				videoResponseSize += [int(i) for i in result[0: -1]]
		writeToFile(videoResponseSize, './fileInfo/videoResponseSize.json', 'wb')

	
