#importing twitter wrapper
	#json bc that's what twitter returns things usually in
	#requests to do all the http client-server thingys as needed
	#collections has a Counter object to tally things, so let's hope it works
	#prettytable to see if it'll print stuff out formatted nicely [:
import twitter
import json
import requests
#from prettytable import PrettyTable

import twitPerson
from twitPerson import *
import createHistograms
import csv

import string
import unicodedata

#setting up authorization to query twitter
CONSUMER_KEY = '2zq826fLWyzsFQFktAl5doane'
CONSUMER_SECRET = 'MajOSCtp2qqt50TCbZ1V996N4px2Xsx0Dcq6tLt2Gg5ncWCDXG'
OAUTH_TOKEN = '1635784340-4TG6WfuuSKd8dgoHIoRIQljBXugH8282FNBlu2G'
OAUTH_TOKEN_SECRET = 'EmsnQNv1SPN6Yw4BpNGj9Pf3yT68B5s9BRqkpfQdMOaKi'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
twitter_api = twitter.Twitter(auth=auth)

#initialize a list of twitPersons
twitList = TwitPpl()

#print twitter_api #this line to just verify that it worked

COUNT = 20 #set

#	findMatches takes in a list input and returns a list of twitter users with matching
#Reddit usernames
def findMatches(userlist):
	twitusers = []

	for user in userlist:
		try:
			foundUser = twitter_api.users.lookup(screen_name=user)
			twitusers.append(user)
		except:
			notfoundlist = user + 'was not found.' #+ "\n"
			print notfoundlist

	print '\nMatched: ' + str(len(twitusers)) + ' out of ' + str(len(userlist)) + ' Reddit usernames\n'
	return twitusers

	'''
	What it should do: 
	for each user/item/thing in the userlist 
		//our_screen_name = user/thing
		try:
			query twitter api http link ending with &screen_name=and concat screen_name
			foundUser = twitter_api.users.lookup(screen_name= + user)
			twitusers.append(user)
			** there is a better way to just command it to look through 100 usernames
			** will need to adjust code for when we choose to use such a thing

		except: 
			Exception, e: >>the exception would be user not found?.. exception is 'errors'
			notfoundlist = user/item/thing + 'was not found.'
			print notfoundlist
			#will figure out a better way to do this part.. maybe save to list and print that out
	print "Matched :" + str(len(twitusers)) + " out of " + str(len(userlist)) + " Reddit usernames"
	return twitusers 
	'''


#	findMatchesFromTxt so that we can just take an input of a txtfile and do same comparisons
# ** will need to figure out the rate limiting portion of 100 later **
def findMatchesFromTxt(txtfile):
	infile = open(txtfile, 'r')
	loadinlist = infile.readlines()
	loadinlist = map(lambda s: s.strip(), loadinlist)
	infile.close()

	return findMatches(loadinlist)

#	findMatchesFromCsv to support CSV file parsing of usernames and comparisons
def findMatchesFromCsv(csvFile):
	loadinlist = []
	f = open(csvFile)
	reader = csv.reader(f)

	for item in reader:
		for username in item:
			loadinlist.append(username)

	return findMatches(loadinlist)


#	wordFreq takes a user input and gets the 20 most recent tweets (if possible) of the user
#from their timeline. Then it counts each aggregates all the text and 
def wordFreq(user):
	wordDict = {}
	tweets = []

	#API call doesn't throw errors if there aren't enough tweets to reach COUNT
	results = twitter_api.statuses.user_timeline(screen_name=user, count=COUNT)
	
	#go through each returned tweet in results and get the unicode text
	for index, tweet in enumerate(results):
		tweetText = results[index]["text"]
		#print tweetText
		tweets.append(tweetText)

	#transform list of unicode tweets into string words and create a dictionary
	for tweet in tweets:
		words = tweet.split()
		table = string.maketrans("","")

		#converting from unicode to string, remove punctuation
		for word in words:
			stringVer = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore')
			correctedWord = stringVer.lower().translate(table, string.punctuation)

			#add corrected word into dictionary, update count
			try:
				wordDict[correctedWord] = wordDict[correctedWord] + 1
			except:
				wordDict[correctedWord] = 1 

	#user.setTweetTexts(wordDict) #not used here but should be called later
	return wordDict

#
def getTweetTimes(user):
	timeVals = []
	yearDict = {}
	monthDict = {}
	hourDict = {}

	statuses = twitter_api.statuses.user_timeline(screen_name=user, count=20)

	for index, tweet in statuses:
		timeObj = statuses[index]['created_at']
		timeVals.append(timeObj)


def getTweetWords(user):
	pass


# normAll sets all the normalized dictionaries of a TwitPerson
def normAll(user):
	times = countNormTimes(user)
	
	user.setNormYears()
	user.setNormMonths(times[yearDict])
	user.setNormHours()

	user.setNormWords(normWords(user))

def normWords(user):
	pass

def normTimes(user):
	timeVals = []
	yearDict = {}
	monthDict = {}
	hourDict = {}






#doAllTheThings takes your input file of reddit usernames and finds the matches;
#creates a TwitPerson and keeps a running list of each TwitPerson created;
#returns the TwitPeople object, list of TwitPersons
def doAllTheThings(inputFile):
	twitusers = findMatchesFromTxt(inputFile)
	for twit in twitusers:
		twitPerson = TwitPerson.twitPerson(twit)
		twitList.addTwitPerson(twitPerson)
		twitList.addTwitCount()
	
	for twit in twitList.getTwitList():
		normAll(twit)

	return twitList






