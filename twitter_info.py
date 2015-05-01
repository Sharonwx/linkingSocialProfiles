#importing twitter wrapper
	#json bc that's what twitter returns things usually in
	#requests to do all the http client-server thingys
	#collections has a Counter object to tally things
	#prettytable to see if it'll print stuff out formatted nicely [:
import twitter
import json
import requests
from collections import Counter
from prettytable import PrettyTable

#setting up authorization to query twitter
CONSUMER_KEY = '2zq826fLWyzsFQFktAl5doane'
CONSUMER_SECRET = 'MajOSCtp2qqt50TCbZ1V996N4px2Xsx0Dcq6tLt2Gg5ncWCDXG'
OAUTH_TOKEN = '1635784340-4TG6WfuuSKd8dgoHIoRIQljBXugH8282FNBlu2G'
OAUTH_TOKEN_SECRET = 'EmsnQNv1SPN6Yw4BpNGj9Pf3yT68B5s9BRqkpfQdMOaKi'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
twitter_api = twitter.Twitter(auth=auth)

#print twitter_api #this line to just verify that it worked

#	findMatches takes in a list input and returns a list of twitter users with matching
#Reddit usernames
def findMatches(userlist):
	twitusers = []

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
	for user in userlist:
		try:
			foundUser = twitter_api.users.lookup(screen_name=user)
			twitusers.append(user)
		except:
			notfoundlist = user + 'was not found.' #+ "\n"
			print notfoundlist

	print '\nMatched: ' + str(len(twitusers)) + ' out of ' + str(len(userlist)) + ' Reddit usernames\n'
	return twitusers



#	findMatchesFromTxt so that we can just take an input of a txtfile and do same comparisons
# ** will need to figure out the rate limiting portion of 100 later **
def findMatchesFromTxt(txtfile):
	infile = open(txtfile, 'r')
	loadinlist = infile.readlines()
	loadinlist = map(lambda s: s.strip(), loadinlist)
	infile.close()

	return findMatches(loadinlist)


def wordFreq(user):
	count = 20
	tweets = []
	tweets = twitter_api.statuses.user_timeline(user_id=user, count=count)

	#statuses = []

	'''	#print json.dumps(tweets, indent=1)
	for tweet in tweets:
		statuses.append(tweet) #[0:19]
	'''

	status_texts = [tweets
		for status in tweets ]

	words = [ w
			for t in status_texts
				for w in t.split()]

	for item in words:
		c = Counter(item)
		#print c.most_common()

	return c



