import getUsernames
import Redditor
import frequencies
import createHistograms
import compare
import instaInfo
import time
import numpy

tic = time.clock()
#reddit

summedCosines = {}

#collection of cosines for users who have posts to compare
cosines = []

#files = ['one.csv','two.csv','three.csv','four.csv','five.csv','six.csv','seven.csv','eight.csv','nine.csv','ten.csv','eleven.csv','twelve.csv']

files = ['one.csv']
for f in files:
	getUsernames.getUsernamesFromList(f)
	getUsernames.doEverything()
	userList = getUsernames.getLists()
	createHistograms.createHistsAndNorms(userList)

	#instagram, already normalizes
	instaUserList = instaInfo.doEverything('one.csv')
	#print 'user list is',instaUserList

	#returns: {'summedCosines':summedCosines,'cosines':cosines}
	dic = compare.compareFreqs(userList,instaUserList)
	sC = dic.get('summedCosines')
	for entry in sC:
		summedCosines[entry] = sC.get(entry)
		cosines.append(sC.get(entry))

	compare.gatherCosines(userList)
	compare.meanCosines()
	compare.stdDevCosines()

#try later?
#compare.clusterCosines()

toc = time.clock()
print 'time is ',toc-tic