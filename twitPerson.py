import datetime

#TwitPerson object has many characteristics pertaining to a Twitter User
#sidenote: I may have found some humor in naming the class a twitperson :x
class TwitPerson (object): 
	def __init__(self, twitPerson, screenname, userid, realname, timeCreated, location, description):
		self.twitPerson = twitPerson #this would be the returned JSON obj version of a User I believe?
		#I included the above after checking to make sure I covered bases for everything needed and am
		#a bit confused over includion 
		self.screenname = screenname
		self.userid = userid
		self.realname = realname
		self.timeCreated = timeCreated
		self.location = location
		self.description = description


		self.hashtags = {} #keeping for now but not necessarily implemented yet since not necessary...
		
		#changing to empty dictionaries so that we don't need as a parameter when creating TwitPerson obj
		#self.tweetTimes = tweetTimes
		self.tweetTimes = {}
		#self.tweetTexts = tweetTexts
		self.tweetTexts = {}

		#
		self.normYears = {}
		self.normMonths = {}
		self.normHours = {}
		self.normWords = {}

	#------------------ Getter methods for the class characteristics
	def getTwitPerson(self): 
		return self.twitperson

	def getScreenName(self):
		return self.screenname

	def getUserId(self):
		return self.userid

	def getRealName(self):
		return self.realname

	def getTimeCreated(self):
		return self.timeCreated

	def getLocation(self):
		return self.location

	def getDescription(self):
		return self.description

	def getHashtags(self):
		return self.hashtags

	def getTweetTimes(self):
		return self.tweetTimes

	def getTweetTexts(self):
		return self.tweetTexts

	def getNormYears(self):
		return self.normYears

	def getNormMonths(self):
		return self.normMonths

	def getNormHours(self):
		return self.normHours

	def getNormWords(self):
		return self.normWords

	#-------------------Setter methods for characteristics
	def setTweetTexts(self, tweetTexts):
		self.tweetTexts = tweetTexts

	def setTweetTimes(self, tweetTimes):
		self.tweetTimes = tweetTimes

	def setNormYears(self, normYears):
		self.normYears = normYears

	def setNormMonths(self, normMonths):
		self.normMonths = normMonths

	def setNormHours(self, normHours):
		self.normHours = normHours

	def setNormWords(self, normWords):
		self.normWords = normWords

#TwitPpl object has list and count characteristic; basically a list of TwitPersons and the number of them
class TwitPpl(object):

	def __init__(self):
		self.list = []
		self.count = 0

	#-----------------------Getter methods for characteristics
	def getTwitList(self): #hehe
		return self.list

	def getCount(self):
		return self.count

	#-----------------------Methods to use for TwitPpl
	def addTwitPerson(self, twitPerson): 
		self.list.append(twitPerson)

	def addTwitCount(self): #ahaha I swear I'm not doing it on purpose... maybe
		self.count = self.count+1

	def getAllTwitsFromList(self): 
		for item in self.list:
			print item.getScreenName()

	def getTwitFromList(self, screename):
		for twitPerson in self.list:
			return twitPerson.getScreenName() == screename


