import urllib2
import os
import math
import json
import copy


def readFromDict(fileName):
	with open(fileName) as myFile:
		return json.load(myFile, object_hook = decodeDict)


def readFromList(fileName):
	with open(fileName) as myFile:
		return json.load(myFile, object_hook = decodeList)


def writeToFile(data, fileName, mode):
		"""This function writes the data (usually a dictionary) into a file.
		"""
		with open(fileName, mode) as myFile:
			json.dump(data, myFile)


def getLogValue(l):
	l1 = copy.deepcopy(l)
	for i in range(0, len(l1)):
		if l1[i] > 0:
			l1[i] = math.log(l1[i], 2)
	return l1


def decodeList(data):
	rv = []
	for item in data:
		if isinstance(item, unicode):
			item = item.encode('utf-8')
		elif isinstance(item, list):
			item = decodeList(item)
		elif isinstance(item, dict):
			item = decodeDict(item)
		rv.append(item)
	return rv


def decodeDict(data):
	rv = {}
	for key, value in data.iteritems():
		if isinstance(key, unicode):
			key = key.encode('utf-8')
		if isinstance(value, unicode):
			value = value.encode('utf-8')
		elif isinstance(value, list):
			value = decodeList(value)
		elif isinstance(value, dict):
			value = decodeDict(value)
		rv[key] = value
	return rv


def showTopKResults(dic, k):
	# results = {}
	sortedDic = sorted(dic.items(), key = lambda x: x[1], reverse = True)
	sortedDic = sortedDic[0: k]
	# for i in sortedDic:
	# 	results[i[0]] = i[1]
	# return results
	return sortedDic


def writeToTxt(data, fileName, mode):
	with open(fileName, mode) as myFile:
		myFile.write(data)