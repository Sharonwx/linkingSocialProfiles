import getUsernames
import Redditor
import frequencies
import createHistograms
import compare
import instaInfo
import time
import numpy

import twitter_info


instaSummedCosines = {}
instaCosines = []

#files = ['one.csv','two.csv','three.csv','four.csv','five.csv','six.csv','seven.csv','eight.csv','nine.csv','ten.csv','eleven.csv','twelve.csv']

#files = ['1.csv','2.csv','3.csv','4.csv','5.csv','6.csv','7.csv','8.csv','9.csv','10.csv']

files = ['30.csv']
def compareInstagram():
	tic = time.clock()
	for f in files:
		print 'currently in file ',f
		print 'time so far: ',(time.clock()-tic) 
		getUsernames.getUsernamesFromList(f)
		getUsernames.doEverything()
		userList = getUsernames.getLists()
		createHistograms.createHistsAndNorms(userList)

		#instagram, already normalizes
		instaUserList = instaInfo.doEverything(f)
		#print 'user list is',instaUserList

		#returns: {'instaSummedCosines':instaSummedCosines,'cosines':cosines}
		compare.compareFreqs(userList,instaUserList)

		dictionary = compare.gatherinstaCosines(userList)
		cosinesTemp = dictionary.get('instaCosines')
		for cos in cosinesTemp:
			instaCosines.append(cos)
		instaSummedCosinesTemp = dictionary.get('instaSummedCosines')
		for item in instaSummedCosinesTemp:
			instaSummedCosines[item] = instaSummedCosinesTemp.get(item)
		compare.meanInstaCosines()
		compare.stdDevInstaCosines()
	toc = time.clock()
	print 'time is ',toc-tic

def compareTwitter():
	tic = time.clock()
	for f in files:
		print 'currently in file ',f
		print 'time so far: ',(time.clock()-tic)
		getUsernames.getUsernamesFromList(f)
		getUsernames.doEverything()
		userList = getUsernames.getLists()
		print userList
		createHistograms.createHistsAndNorms(userList)

		twitterUserList = twitter_info.doAllTheThings(f)


		compare.compareTwitterFreqs(userList,twitterUserList)
		dictionary = compare.gatherTwitterCosines(userList)
		print dictionary.get('twitterCosines')
		print dictionary.get('twitterSummedCosines')








