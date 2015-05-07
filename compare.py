import numpy
from scipy.linalg import norm
from sklearn import cluster
from matplotlib import pyplot

#stores username, cosine similarity for pairs that are compared
redditInstaDictionary ={}

redditInstaHoursDict = {}
redditInstaMonthsDict = {}
redditInstaYearsDict = {}

summedCosines = {}

#collection of cosines for users who have posts to compare
cosines = []

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
				redditInstaDictionary[compare.getUsername()] = cosSim
			else:
				print compare.getUsername()," does not have any posts to compare"
				redditInstaDictionary[compare.getUsername()] = 0

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
			if compare.getHoursNorm() is not None:
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
			if compare.getHoursNorm() is not None:
				userKeys = (user.getYearsNorm()).keys()
				compareKeys = (compare.getYearsNorm()).keys()
				intersectionKeys = (userKeys and compareKeys)
				print 'comparing years'
				cosSim = simple_cosine_sim(user.getYearsNorm(),compare.getYearsNorm())
				print 'cosine similarity is ',cosSim
				redditInstaYearsDict[user.getUsername()] = cosSim

			else:
				print compare.getUsername()," does not have hours to compare"
				redditInstaYearsDict[user.getUsername()] = 0

		else:
			print 'freqs: no instagram exists for ',user.getUsername()





def gatherCosines(userList1):
	writeFile = open('summedCosines.txt','a')
	for user in userList1:
		wordSim = redditInstaDictionary.get(user.getUsername())
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
		summedCosines[user.getUsername()] = (0.5*wordSim)+(0.3*hoursSim)+(0.1*monthsSim)+(0.1*yearsSim)

	for item in summedCosines:
		writeFile.write(str(item))
		writeFile.write(':')
		writeFile.write(str(summedCosines.get(item)))
		cosines.append(summedCosines.get(item))
		writeFile.write(',\n')
		#print 'user is ',item,' cosine sim is: ',item.value()

	return {'cosines':cosines,'summedCosines':summedCosines}

def meanCosines():
	print 'mean is ',numpy.mean(cosines)

def stdDevCosines():
	print 'standard deviation is ',numpy.std(cosines)

def clusterCosines():
	k_means = cluster.KMeans(n_clusters=3,init='k-means++')
	k_means.fit(cosines)

	labels = kmeans.labels
	centroids = kmeans.cluster_centers

	for i in range(0,3):
		ds = data[numpy.where(labels==i)]
		pyplot.plot(ds[:0],ds[:1],'o')
		lines = pyplot.plot(centroids[i,0],centroids[i,1],'kx')
		pyplot.setp(lines,ms=15.0)
		pyplot.setp(lines,mew=2.0)
	pyplot.show()

def getCosineSimilarities():
	return redditInstaDictionary

def getWordlessInstaList():
	return wordlessInstaList

def getWordlessInstaCount():
	return len(wordlessInstaList)



