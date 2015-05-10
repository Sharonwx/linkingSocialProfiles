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
from datetime import datetime

#setting up authorization to query twitter
CONSUMER_KEY = 'sQ6lPdXZBfoWc1cuUudrE5LCC'
CONSUMER_SECRET = 'lOfAiM7nNNdFud0bYskmKVpHWEZP11xZ1HyFmKZkDXT1JQtpKU'
OAUTH_TOKEN = '1635784340-1F3etXLkk1RmtKAN5SKneMJaZu3G0TkuUE8TDRe'
OAUTH_TOKEN_SECRET = 'jgsDsEShOewtscSifwVsP26yiw8b1VsnJaGh57xLAyuuy'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
twitter_api = twitter.Twitter(auth=auth)

#initialize a list of twitPersons
twitList = TwitPpl()

#twitObjList holds all the Twitter User objects returned by request
#will be used in doAllTheThings so that we save the number of times we make
#GET calls to API, and hopefully are more efficient in terms of working with
#the rate limiting
# this should be a list of TwitterListResponses -- each ListResponse has a dictionary
#where there is really only index 0 bc only one dictionary stored in the list, so...
twitObjList = []

#print twitter_api #this line to just verify that it worked
COUNT = 20 #setting variable for number tweets to pull

#	findMatches takes in a list input and returns a list of twitter users with matching
#Reddit usernames
def findMatches(userlist):
	twitusers = []

	for user in userlist:
		try:
			foundUser = twitter_api.users.lookup(screen_name=user)
			#adds the found string format of username parsed from input
			twitusers.append(user)
			#adds the found user in format of the returned decoded JSON obj
			twitObjList.append(foundUser) 

		except:
			pass
			#notfoundlist = user + 'was not found.' #+ "\n"
			#print notfoundlist

	print '\nMatched: ' + str(len(twitusers)) + ' out of ' + str(len(userlist)) #+ ' Reddit usernames\n'
	
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


# getTweetTimes: given results JSON dictionary from query request, returns a dictionary of dictionaries for
#various time categories -- years, months, hours
def getTweetTimes(statuses):
	timeVals = []
	yearDict = {}
	monthDict = {}
	hourDict = {}
	timeDict = {}

	#statuses = twitter_api.statuses.user_timeline(screen_name=username, count=20)

	for index, tweet in enumerate(statuses):
		#get unicode time obj 'created_at' for each tweet, correct to datetime timestamp format
		timeObj = statuses[index]['created_at']
		correctedTimeObj = datetime.strptime(timeObj, '%a %b %d %H:%M:%S +0000 %Y')

		#this line below would be set to the user object 
		#user.setTweetTimes(timeVals.append(correctedTimeObj))
		try:
			yearDict[correctedTimeObj.strftime('%Y')] = yearDict[correctedTimeObj.strftime('%Y')] + 1
		except: #when first occurence of year to be added to yearDict
			yearDict[correctedTimeObj.strftime('%Y')] = 1

		try:
			monthDict[correctedTimeObj.strftime('%b')] = monthDict[correctedTimeObj.strftime('%b')] + 1
		except: #first occurrence of a month to be added to monthDict
			monthDict[correctedTimeObj.strftime('%b')] = 1

		try:
			hourDict[correctedTimeObj.strftime('%H')] = hourDict[correctedTimeObj.strftime('%H')] + 1
		except: #first occurrence of a specific hour to be added to hourDict
			hourDict[correctedTimeObj.strftime('%H')] = 1

	timeDict = {'hours':hourDict, 'months':monthDict, 'years':yearDict}

	#print timeDict
	return timeDict


#	getTweetWords: given a results JSON dictionary input of statuses from query, returns
#a dictionary of words 
def getTweetWords(results):
	wordDict = {}
	tweets = []
	
	#go through each returned tweet in results and get the unicode text
	for index, tweet in enumerate(results):
		tweetText = results[index]["text"]
		#print tweetText
		tweets.append(tweetText)

	#print tweets

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

#getTweetsInfo takes in a username and GETs the COUNT most recent tweets of that user,
#then passes that dictionary as the parameters to call upon getTweetTimes and getTweetWords
def getTweetsInfo(username):
	tweetInfo = {}
	statuses = twitter_api.statuses.user_timeline(screen_name=username, count=COUNT)
	
	times = getTweetTimes(statuses)
	words = getTweetWords(statuses)

	tweetInfo = {'times':times, 'words': words}
	return tweetInfo

# normAll sets all the normalized dictionaries of a TwitPerson
#aka do all the normalizing things; in this case user is a TwitPerson
#object and username is the text string to pass for the other functions;
#in all the other function calls, user is a string input of the the username
def normAll(user):
	'''
	In order to use this with just string username input from the list 
	that is returned from the findMatches function, 
	'''
	#try:
	username = user.getScreenName()
	tweetInfo = getTweetsInfo(username)

	#print '***********' 
	#print tweetInfo['times']

	#meow = tweetInfo['times']
	user.setTweetTimes(tweetInfo['times'])
	
	
	
	times = normTimes(tweetInfo['times']) #normTimes(username)
	
	#print '***********'
	#print tweetInfo['times']

	#do I need to say user.TwitPerson.set..... bc its from TwitPerson?
	user.setNormYears(times['years'])
	user.setNormMonths(times['months'])
	user.setNormHours(times['hours'])

	user.setTweetTexts(tweetInfo['words'])

	user.setNormWords(normWords(tweetInfo['words']))

	#except: 
		#print 'Error found in normAll'

# normWords takes in a dictionary of tweet words and then normalizes that list according to
#the function in createHistograms
def normWords(wordsDict):
	#tweetTextDict = getTweetWords(username)
	return createHistograms.normalizeWordFreqs(wordsDict)


def normTimes(timesDict):
	#tweetTimesDict = getTweetTimes(username)
	return createHistograms.normalizeTimeFreqs(timesDict['hours'], timesDict['months'], timesDict['years'])


#doAllTheThings takes your input file of reddit usernames and finds the matches;
#creates a TwitPerson and keeps a running list of each TwitPerson created;
#returns the TwitPeople object, list of TwitPersons
def doAllTheThings(inputFile):
	#1) find all the matches from inputfile -- choose which one you want to load from
	twitusers = findMatchesFromTxt(inputFile)
	#twitusers = findMatchesFromCsv(inputFile)

	print 'Found the following usernames:'
	print twitusers
	'''
	findMatches returns a list of the usernames that were found in twitter.
	However, it does not return of a list of Twitter user objects; the good
	part is that while it went through and matched the users, we also appended
	the actual Twitter JSON decoded User object to the separate list called
	twitObjList. 
	'''

	#this loops goes through the now updated twitObjList of Twitter's user objects
	#and should create OUR VER of a TwitPerson from the user data
	for index, twit in enumerate(twitObjList):
		
		#user is Twitter JSON decoded obj
		user = twitObjList[index]
		#print str(type(user))
		#print user

		username = user[0]['screen_name']
		#print str(type(username))

		print 'Inside loop, creating TwitPerson for ' + username

		userid = user[0]['id_str']
		realname = user[0]['name']
		#print '*********' + realname
		timeCreated = user[0]['created_at']
		location = user[0]['location']
		description = user[0]['description']
		#print '**********' + description

		#create TwitPerson from gathered info, add to twitList, increase count
		twitPerson = TwitPerson(twit, username, userid, realname, timeCreated, location, description)
		
		#print twitPerson.getScreenName()

		twitList.addTwitPerson(twitPerson)
		twitList.addTwitCount()
		#tweetInfo = getTweetsInfo(username)
	
	#2) for every twit(ie TwitPerson) in twitList, set the normalized dictionaries! (&prenormal ones)
	for twit in twitList.getTwitList():
		#username = twit.TwitPerson.getScreenname()
		normAll(twit) #set all the normalized dictionaries of twit
		#twit.setTweetTexts(pass)
		#twit.setTweetTimes(getTweetTimes)

	#return the final list TwitPpl with the TwitPersons all set with dictionaries to pull
	return twitList



''' *** RENAMED METHOD TO 'getTweetWords', Kept following for reference ***
***************************************************************************
#	wordFreq takes a user input and gets the 20 most recent tweets (if possible) of the user
#from their timeline. Then it counts each aggregates all the text and 
def wordFreq(results):
	wordDict = {}
	tweets = []

	#API call doesn't throw errors if there aren't enough tweets to reach COUNT
	#results = twitter_api.statuses.user_timeline(screen_name=username, count=COUNT)
	
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

	****COMMENTS originally from doAllTheThings, removed bc no longer applies but
	*********kept for reference [:
	#2) for every username that matched, create a TwitPerson and add to the overarching
	#global var twitList... so take the Twitter JSON User objects in twitObjList
	for twit in twitusers:
		#line below isn't functioning completely, just saves the username but it should
		#still be fine; just won't return your actual twitter user object yet
		twitPerson = TwitPerson.twitPerson(twit)
		twitPerson.setScreenname(twit)
		twitList.addTwitPerson(twitPerson)
		twitList.addTwitCount()

	'''
