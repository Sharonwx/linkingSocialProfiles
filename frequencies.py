import praw
import string
import unicodedata
import pprint
import getUsernames
import Redditor

import datetime 

frequencies ={}



#ideas: put comments and submission into different dictionaries? or same?
def wordFrequencies(comments,submissions):

	for comment in comments:
		#print 'hi'
		#print comment
		words = comment.split()
		table = string.maketrans("","")

		for word in words:
			if word[:4] == 'http':
				frequencies[word] = (frequencies.get(word,0)+1)
			else:
				# next line translates unicode to string so we can use .translate
				sword = unicodedata.normalize('NFKD', word).encode('ascii','ignore')
				lowercase = sword.lower()
				correctWord = lowercase.translate(table,string.punctuation)
				#count the number of times a user uses a given word
				frequencies[correctWord] = (int(frequencies.get(correctWord,0))+1)

	for submission in submissions:
		subs = submission.split()
		table = string.maketrans("","")

		for s in subs:
			if s[:4] =='http':
				frequencies[s] = (frequencies.get(s,0)+1)
			else:
				sword = unicodedata.normalize('NFKD', s).encode('ascii','ignore')
				#lowercase = sword.lowercase() #this doesn't work y?
				correctWord = sword.translate(table,string.punctuation)
				frequencies[correctWord] = (int(frequencies.get(correctWord,0))+1)

	return frequencies
	# something weird happening with links ex: xhereshttpswwwyoutubecomwatchvr5z8o7p1ms

#ideas: create a dictionary for times posted
#hour of the day: times
#month: times?
#year: times?
#so different breakdowns of times and counts
def timeFrequencies(cTimes,sTimes):

	hours = {}
	months = {}
	years = {}

	for tm in cTimes:
		years[tm.year] = (years.get(tm.year,0)+1)
		months[tm.strftime("%B")] = (months.get(tm.strftime("%B"),0)+1)
		hours[tm.strftime("%H")] = (hours.get(tm.strftime("%H"),0)+1)

	for tm in sTimes:
		years[tm.year] = (years.get(tm.year,0)+1)
		months[tm.strftime("%B")] = (months.get(tm.strftime("%B"),0)+1)
		hours[tm.strftime("%H")] = (hours.get(tm.strftime("%H"),0)+1)

	times = {'hours':hours,'months':months,'years':years}
	return times



def getTopics(subsComms,subsSubs):

	topics = []
	for item in subsComms:
		topics.append(item)
	for item in subsSubs:
		if item not in topics:
			topics.append(item)
	print topics



