from twitter_info import *
import twitter_info
import pprint
import json
import re
import unicodedata
import string
from datetime import datetime
#from prettytable import PrettyTable


test = doAllTheThings('test.txt')

print 'Number of twits in twitlist: ' + str(test.getCount())
print 'All the twits in twitlist:'
test.getAllTwitsFromList()

listofppl = test.getTwitList()

print listofppl[0].getTweetTexts()
print listofppl[0].getNormWords()


'''
NOTE: By using normalizeTimeFreqs, we directly manipulate the original dictionary
inputs. If we want to keep them, we should create new dictionaries to store the 
changed values, like in normalizeWordFreqs. Explains why getTweetTimes returns the 
same normalized values instead of the original ones.
'''
print listofppl[0].getTweetTimes()
print listofppl[0].getNormYears()
print listofppl[0].getNormMonths()


#statuses = twitter_api.statuses.user_timeline(screen_name='jimmyfallon', count=20)

#test = twitter_info.getTweetTimes('jimmyfallon')

#print test['hours']


#testTime = statuses[0]['text']
#test = statuses[1]['created_at']
#print testTime

#d = datetime.strptime(testTime,'%a %b %d %H:%M:%S +0000 %Y')
#print d

#print test

#print d.strftime('%Y')
#print d.strftime('%b')
#print d.strftime('%H')

#for piece in pieces:
#	stringVer = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore')
#


'''
for index, tweet in enumerate(statuses):
	timeObj = statuses[index]['created_at']
	timeVals.append(timeObj)
'''
#print timeVals
#test = twitter_info.wordFreq('kayseax3')
#print test



#mew = twitter_api.statuses.user_timeline(screen_name='kayseax3',count=20)
'''
mew = twitter_api.statuses.user_timeline(screen_name='jimmyfallon',count=20)

mer = []
wordDict = {}

for index, thing in enumerate(mew):
	tweetText = mew[index]["text"]
	#print '\n' + 'Type of tweetText: ' + str(type(tweetText)) + '\n'

	#tweetText = re.sub('[?!@#$%&*)(\/",.:;-]', '', tweetText)
	#tweetText.encode('ascii', 'ignore')
	mer.append(tweetText)

for tweet in mer:
	words = tweet.split()
	table = string.maketrans("","")

	for word in words:
		stringVer = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore')
		correctedWord = stringVer.lower().translate(table, string.punctuation)
		try:
			wordDict[correctedWord] = wordDict[correctedWord] + 1
		except:
			wordDict[correctedWord] = 1 

#print str(mew) + '\n'

print 'Length of mer: ' + str(len(mer))
print mer 
print '\n'
print wordDict
#print json.dumps(mer, indent=1)

'''

#print '\n' + 'More testing: twitter_info wordFreq method'
#test = twitter_info.wordFreq('jimmyfallon')
#print test

'''
matches = twitter_info.findMatchesFromTxt('usernames.txt')
print matches




testuser = matches[5]
testuser2 = matches[10]
testuser3 = matches[8]

#mew = testuser2['screen_name']

print testuser2
print getUserTimelineStats(testuser2)

#print wordFreq(testuser3)


#print testuser + ' ' + wordFreq(testuser) + '\n//////////////////////////'
#print testuser2 + ' ' +  wordFreq(testuser2)+ '\n//////////////////////////'
#print testuser3 + ' ' + wordFreq(testuser3)+ '\n//////////////////////////'

'''

''' randomly trying something that didn't work out haha
for eachuser in (enumerate(matches)):
    label = 'Found usernames'
    pt = PrettyTable(field_names=[label])
    #c = Counter(data)
    [ pt.add_row(kv) for kv in eachuser ]
    pt.align[label] = 'l' #, 'r' # Set column alignment
    print pt
 '''