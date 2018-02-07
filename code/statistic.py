import subprocess
import os
import json
import glob


class Statistic:
	rootDir = "/data4/"

	def __init__(self):
		os.chdir(self.rootDir)


	def httpInfo(self):
		"""This function extracts all the records containing "aurora.phys" in everyday's http logs.
		The extracted data are written into Aurora/httpRequests folder.
		Field seperator is "\t", record seperator is "\n".
		"""
		currentDir = subprocess.check_output("ls", shell = True)
		currentDir = currentDir.rsplit()
		for folder in currentDir:
			if os.path.isdir(folder) and folder[:2] == "20" and folder[:10] >= "2015-04-26" and folder[:10] <= "2015-04-30":
				if not os.path.exists("/home/sourish/D2Lnew/httpRequests/" + folder):
					os.makedirs("/home/sourish/D2Lnew/httpRequests/" + folder)
				for files in glob.glob(folder + "/http.*.log.gz"):
					#httpRequestsPerHour = subprocess.check_output("zcat ./" + files + " | gawk '/d2l\.ucalgary/ {print $0}'", shell = True)
					httpRequestsPerHour = subprocess.check_output("zcat ./" + files + " | gawk '/d2l/ {print $0}'", shell = True)
					writeToFile(httpRequestsPerHour, "/home/sourish/D2Lnew/httpRequests/" + files[0:33] + ".txt", "wb+")
					subprocess.call("gzip -q /home/sourish/D2Lnew/httpRequests/" + files[0:33] + ".txt", shell = True)


	def httpRequestTotalPerDay(self):
		"""This function returns a dictionary containing the total number of requests per hour per day.
		E.g. {'2014-12-01': {'http.00...-01...': '1000\n', 'http.01...-02...': '23423\n'} ...}
		Also the dictionary is written to Aurora/httpRequestTotalPerDay.txt file.
		"""
		httpRequestTotalPerDay = {}
		currentDir = subprocess.check_output("ls", shell = True)
		currentDir = currentDir.rsplit()
		for folder in currentDir:
			if os.path.isdir(folder) and folder[:2] == "20":
				# print subprocess.check_output("ls " + folder, shell = True)
				# print "zcat ./" + folder + "/http.*.log.gz | gawk 'BEGIN {i=0} /Aurora\.phys/ {i++} END {print i}'"
				httpRequestTotalPerDay[folder] = {}
				for files in glob.glob(folder + "/http.*.log.gz"):
					#httpRequestTotalPerDay[folder][files] = subprocess.check_output("zcat ./" + files + " | gawk 'BEGIN {i=0} /d2l\.ucalgary/ {i++} END {print i}'", shell = True)
					httpRequestTotalPerDay[folder][files] = subprocess.check_output("zcat ./" + files + " | gawk 'BEGIN {i=0} /d2l/ {i++} END {print i}'", shell = True)

				writeToFile(httpRequestTotalPerDay[folder], "/home/sourish/D2Lnew/httpRequestsTotalPerDay2.txt", "a+")
		writeToFile(httpRequestTotalPerDay, "/home/sourish/D2Lnew/httpRequestsTotalPerDay3.txt", "a+")
		return httpRequestTotalPerDay


	def httpClientsIPDictionary(self):
		ipDictionary = {}
		currentDir = subprocess.check_output("ls", shell = True)
		currentDir = currentDir.rsplit()
		for folder in currentDir:
			if os.path.isdir(folder) and folder[:2] == "20":
				#ipAddress = subprocess.check_output("zcat ./" + folder + "/http.*.log.gz | gawk '/d2l\.ucalgary/ {print $3}'")
				ipAddress = subprocess.check_output("zcat ./" + folder + "/http.*.log.gz | gawk '/d2l/ {print $3}'")
				ipAddress = ipAddress.rsplit()
				ipDictionary[folder] = {}
				for i in ipAddress:
					if i not in ipDictionary[folder].keys():
						ipDictionary[folder][i] += 1
					else:
						ipDictionary[folder][i] = 1
				writeToFile(ipDictionary[folder], "/home/sourish/D2Lnew/httpClientsIPDictionary.txt", "a+")
		return ipDictionary


	def connInfo(self):
		currentDir = subprocess.check_output("ls", shell = True)
		currentDir = currentDir.rsplit()
		for folder in currentDir:
			if os.path.isdir(folder) and folder[:2] == "20":
				if not os.path.exists("/home/sourish/D2Lnew/connInfo/" + folder):
					os.makedirs("/home/sourish/D2Lnew/connInfo/" + folder)
				for files in glob.glob(folder + "/conn.*.log.gz"):
					connPerHour = subprocess.check_output("zcat ./" + files + " | gawk -F'\\t' '/199.30.181.42/ {$1=strftime(\"%Y-%m-%dD%aT%H:%M:%S\", $1); print $0;}'", shell = True)
					writeToFile(connPerHour, "/home/sourish/D2Lnew/connInfo/" + files[0:33] + ".txt", "wb+")
					subprocess.call("gzip -q /home/sourish/D2Lnew/connInfo/" + files[0:33] + ".txt", shell = True)



def writeToFile(data, fileName, mode):
	"""This function writes the data (usually a dictionary) into a file.
	"""
	with open(fileName, mode) as myFile:
		json.dump(data, myFile)


stat = Statistic()
# stat.connInfo()
# httpRequestTotalPerDay = stat.httpRequestTotalPerDay()
# print httpRequestTotalPerDay
stat.httpInfo()
