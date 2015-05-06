import numpy
from scipy.linalg import norm

#stores username, cosine similarity for pairs that are compared
redditInstaDictionary ={}
#list of instas who can't be compared because no words
wordlessInstaList = []


def simple_cosine_sim(a, b):
    if len(b) < len(a):
        a, b = b, a

    res = 0
    for key, a_value in a.iteritems():
        res += a_value * b.get(key, 0)
    if res == 0:
        return 0

    try:
        res = res / norm(a.values()) / norm(b.values())
    except ZeroDivisionError:
        res = 0
    return res 

def compareAllWordFreqs(userList1,userList2):
	for user in userList1:
	#need to write code that compares the users list in reddit
	#to the users list in twitter
	#to the users list in Insta
		compare = userList2.getInstagramUser(user.getUsername())
		if compare is not None:
			if compare.getWordsNorm() is not None:
				#print 'compare.getWordsNorm is ',compare.getWordsNorm()
				print 'username being compared is ',compare.getUsername()
				#print 'first dictionary ',user.getWordsNorm()
				userKeys = (user.getWords()).keys()
				#print 'second ',compare.getWordsNorm()
				compareKeys = (compare.getWordsNorm()).keys()
				intersectionKeys = (userKeys and compareKeys)

				cosSim = simple_cosine_sim(user.getWordsNorm(),compare.getWordsNorm())
				print 'cosine similarity is ',cosSim
				redditInstaDictionary[compare.getUsername()] = cosSim
			else:
				print compare.getUsername()," does not have any posts to compare"
				if compare.getUsername() not in wordlessInstaList:
					wordlessInstaList.append(compare.getUsername())
		else:
			print 'no instagram exists for ',user.getUsername()

'''
def compareAllTimeFreqs(userList1,userList2):
	#compare hours
	for user in userList1:
		compare = userList2.getInstagramUser(user.getUsername())
		if compare.get
	#compare months


	#compare years
'''
def getCosineSimilarities():
	return redditInstaDictionary

def getWordlessInstaList():
	return wordlessInstaList

def getWordlessInstaCount():
	return len(wordlessInstaList)



def compareWordFreqs(firstDict,secondDict):

	inFirstNotSecond = set(firstDict.keys()) - set(secondDict.keys())
	#print 'in first not second',inFirstNotSecond
	#print 'number in first not in second',len(inFirstNotSecond)
	inSecondNotFirst = set(secondDict.keys()) - set(firstDict.keys())
	#print 'in second not first',inSecondNotFirst
	#print 'number in second not in first',len(inSecondNotFirst)
	inBoth = set(firstDict.keys()) and set(secondDict.keys())
	#print 'in both', inBoth
	#print 'number in both',len(inBoth)

'''
def compareAllTimeFreqs(userList):
	for user in userList:
		for compare in userList:
			if user != compare:
				#compareHoursFreqs(user.getHoursNorm(),compare.getHoursNorm())

				'''



'''
# rewriting code to normalize within union 
userDictionary = user.getWords()
userSet = set(userDictionary)
compareDictionary = compare.getWords()
compareSet = set(compareDictionary)
unionSet = (userSet and compareSet)
setSize = len(unionSet)

nUserDictionary = {}
for word in unionSet:
	nUserDictionary[word] = float(userDictionary.get(word,0))/setSize
print nUserDictionary
print "\n\n\n\n"

nCompareDictionary = {}
for word in unionSet:
	nCompareDictionary[word] = float(compareDictionary.get(word,0))/setSize
print nCompareDictionary
print "\n\n\n\n"

#compare renormalized words
print simple_cosine_sim(nUserDictionary,nCompareDictionary)
print "\n\n\n\n"
'''

#checking that the function is working -- it is
'''
dictionaryA = {'neighboring':.10,'November':.20,'hourly':.10,'privacy':.15,'lights':.15,'smoke':.10,'talks':.20}
dictionary = {'neighboring':.10,'November':.20,'hourly':.10,'privacy':.15,'human':.15,'popular':.20,'tech':.10}
print simple_cosine_sim(dictionaryA,dictionary)
'''