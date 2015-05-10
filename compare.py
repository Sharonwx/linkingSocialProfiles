import numpy
from scipy.linalg import norm
from sklearn import cluster
from matplotlib import pyplot

#stores username, cosine similarity for pairs that are compared
redditInstaWordsDict ={}
redditInstaHoursDict = {}
redditInstaMonthsDict = {}
redditInstaYearsDict = {}
instaSummedCosines = {}


redditTwitterWordsDict ={}
redditTwitterHoursDict = {}
redditTwitterMonthsDict = {}
redditTwitterYearsDict = {}
twitterSummedCosines = {}



#collection of instaCosines for users who have posts to compare
instaCosines = []
instaWithoutZero = []


twitterCosines = []
twitterWithoutZero = []

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

#compares reddit users to instagram users
def compareFreqs(userList1,userList2):
	for user in userList1:
		compare = userList2.getInstagramUser(user.getUsername())
		if compare is not None:
			print 'username being compared is ',compare.getUsername()
			if compare.getWordsNorm() is not None:
				#print 'compare.getWordsNorm is ',compare.getWordsNorm()
				print 'comparing words'
				#print 'first dictionary ',user.getWordsNorm()
				userKeys = (user.getWords()).keys()
				#print 'second ',compare.getWordsNorm()
				compareKeys = (compare.getWordsNorm()).keys()
				intersectionKeys = (userKeys and compareKeys)

				cosSim = simple_cosine_sim(user.getWordsNorm(),compare.getWordsNorm())
				print 'cosine similarity is ',cosSim
				redditInstaWordsDict[compare.getUsername()] = cosSim
			else:
				print compare.getUsername()," does not have any posts to compare"
				redditInstaWordsDict[compare.getUsername()] = 0

				if compare.getUsername() not in wordlessInstaList:
					wordlessInstaList.append(compare.getUsername())

			#compare hours
			if compare.getHoursNorm() is not None:
				userKeys = (user.getHoursNorm()).keys()
				compareKeys = (compare.getHoursNorm()).keys()
				intersectionKeys = (userKeys and compareKeys)
				print 'comparing hours'
				#print 'user hours norm ',user.getHoursNorm()
				#print 'compare hours norm ',compare.getHoursNorm()
				cosSim = simple_cosine_sim(user.getHoursNorm(),compare.getHoursNorm())
				print 'cosine similarity is ',cosSim
				redditInstaHoursDict[user.getUsername()] = cosSim

			else:
				print compare.getUsername()," does not have hours to compare"
				redditInstaHoursDict[user.getUsername()] = 0

			#compare months
			if compare.getMonthsNorm() is not None:
				userKeys = (user.getMonthsNorm()).keys()
				compareKeys = (compare.getMonthsNorm()).keys()
				intersectionKeys = (userKeys and compareKeys)
				print 'comparing months'
				cosSim = simple_cosine_sim(user.getMonthsNorm(),compare.getMonthsNorm())
				print 'cosine similarity is ',cosSim
				redditInstaMonthsDict[user.getUsername()] = cosSim

			else:
				print compare.getUsername()," does not have hours to compare"
				redditInstaMonthsDict[user.getUsername()] = 0

			#compare years
			if compare.getYearsNorm() is not None:
				userKeys = (user.getYearsNorm()).keys()
				compareKeys = (compare.getYearsNorm()).keys()
				intersectionKeys = (userKeys and compareKeys)
				print 'comparing years'
				cosSim = simple_cosine_sim(user.getYearsNorm(),compare.getYearsNorm())
				print 'cosine similarity is ',cosSim
				redditTwitterYearsDict[user.getUsername()] = cosSim

			else:
				print compare.getUsername()," does not have hours to compare"
				redditTwitterYearsDict[user.getUsername()] = 0

		else:
			print 'freqs: no twitter exists for ',user.getUsername()


def compareTwitterFreqs(userList1,userList2):
	print 'HERE'
	for user in userList1:
		compare = userList2.getTwitFromList(user.getUsername())
		print compare
		if compare is not None:
			print 'username being compared is ',compare.getScreenName()
			#compare words
			if compare.getNormWords() is not None:
				print 'comparing words'
				userKeys = (user.getWords()).keys()
				compareKeys = (compare.getNormWords()).keys()
				intersectionKeys = (userKeys and compareKeys)

				cosSim = simple_cosine_sim(user.getWordsNorm(),compare.getNormWords())
				print 'cosine similarity is ',cosSim
				redditTwitterWordsDict[compare.getScreenName()] = cosSim
			else:
				print compare.getScreenName()," does not have any posts to compare"
				redditTwitterWordsDict[compare.getScreenName()] = 0

			#compare hours
			if compare.getNormHours() is not None:
				userKeys = (user.getHoursNorm()).keys()
				compareKeys = (compare.getNormHours()).keys()
				intersectionKeys = (userKeys and compareKeys)
				print 'comparing hours'
				cosSim = simple_cosine_sim(user.getHoursNorm(),compare.getNormHours())
				print 'cosine similarity is ',cosSim
				redditTwitterHoursDict[user.getUsername()] = cosSim
			else:
				print compare.getScreenName()," does not have hours to compare"
				redditTwitterHoursDict[user.getUsername()] = 0

			#compare months
			if compare.getNormMonths() is not None:
				userKeys = (user.getMonthsNorm()).keys()
				compareKeys = (compare.getNormMonths()).keys()
				intersectionKeys = (userKeys and compareKeys)
				print 'comparing months'
				cosSim = simple_cosine_sim(user.getMonthsNorm(),compare.getNormMonths())
				print 'cosine similarity is ',cosSim
				redditTwitterMonthsDict[user.getUsername()] = cosSim
			else:
				print compare.getScreenName()," does not have hours to compare"
				redditTwitterMonthsDict[user.getUsername()] = 0

			#compare years
			if compare.getNormYears() is not None:
				userKeys = (user.getYearsNorm()).keys()
				compareKeys = (compare.getNormYears()).keys()
				intersectionKeys = (userKeys and compareKeys)
				print 'comparing years'
				cosSim = simple_cosine_sim(user.getYearsNorm(),compare.getNormYears())
				print 'cosine similarity is ',cosSim
				redditInstaYearsDict[user.getUsername()] = cosSim
			else:
				print compare.getScreenName()," does not have hours to compare"
				redditInstaYearsDict[user.getUsername()] = 0




def gatherinstaCosines(userList1):
	writeFile = open('instaSummedCosines.txt','a')
	for user in userList1:
		wordSim = redditInstaWordsDict.get(user.getUsername())
		if wordSim is None:
			wordSim = 0
		#print 'wordSim is ',wordSim
		hoursSim = redditInstaHoursDict.get(user.getUsername())
		if hoursSim is None:
			hoursSim = 0
		#print 'hoursSim is ',hoursSim
		monthsSim = redditInstaMonthsDict.get(user.getUsername())
		if monthsSim is None:
			monthsSim = 0
		#print 'monthsSim is ',monthsSim
		yearsSim = redditInstaYearsDict.get(user.getUsername())
		if yearsSim is None:
			yearsSim = 0
		#print 'yearsSim is ',yearsSim

		#this is where we have to decide how to weight it
		#now it's:
		#words: .5
		#hours: .3
		#months: .1
		#years: .1
		instaSummedCosines[user.getUsername()] = (0.5*wordSim)+(0.3*hoursSim)+(0.1*monthsSim)+(0.1*yearsSim)

	for item in instaSummedCosines:
		writeFile.write(str(item))
		writeFile.write(':')
		writeFile.write(str(instaSummedCosines.get(item)))
		instaCosines.append(instaSummedCosines.get(item))
		writeFile.write(',\n')
		#print 'user is ',item,' cosine sim is: ',item.value()

	return {'instaCosines':instaCosines,'instaSummedCosines':instaSummedCosines}



def gatherTwitterCosines(userList1):
	writeFile = open('twitterSummedCosines.txt','a')
	for user in userList1:
		wordSim = redditTwitterWordsDict.get(user.getUsername())
		if wordSim is None:
			wordSim = 0
		#print 'wordSim is ',wordSim
		hoursSim = redditTwitterHourssDict.get(user.getUsername())
		if hoursSim is None:
			hoursSim = 0
		#print 'hoursSim is ',hoursSim
		monthsSim = redditTwitterMonthsDict.get(user.getUsername())
		if monthsSim is None:
			monthsSim = 0
		#print 'monthsSim is ',monthsSim
		yearsSim = redditTwitterYearsDict.get(user.getUsername())
		if yearsSim is None:
			yearsSim = 0
		#print 'yearsSim is ',yearsSim

		#this is where we have to decide how to weight it
		#now it's:
		#words: .5
		#hours: .3
		#months: .1
		#years: .1
		twitterSummedCosines[user.getUsername()] = (0.5*wordSim)+(0.3*hoursSim)+(0.1*monthsSim)+(0.1*yearsSim)

	for item in twitterSummedCosines:
		writeFile.write(str(item))
		writeFile.write(':')
		writeFile.write(str(twitterSummedCosines.get(item)))
		twitterCosines.append(twitterSummedCosines.get(item))
		writeFile.write(',\n')
		#print 'user is ',item,' cosine sim is: ',item.value()

	return {'twitterCosines':twitterCosines,'twitterSummedCosines':twitterSummedCosines}

def meanInstaCosines():
	for cos in instaCosines:
		if cos != 0:
			instaWithoutZero.append(cos)

	print 'mean is ',numpy.mean(instaWithoutZero)

def stdDevInstaCosines():
	print 'standard deviation is ',numpy.std(instaWithoutZero)


def getinstaCosinesimilarities():
	return redditInstaWordsDict

def getWordlessInstaList():
	return wordlessInstaList

def getWordlessInstaCount():
	return len(wordlessInstaList)



