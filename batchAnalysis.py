import batchReader
import survey
import operator
import string
import csv


#have a list of respondents 
results = batchReader.readBatch()
respondents = results.get('respondents')
resList = results.get('list')

print 'total respondents is ',respondents.getCount()


#returns the mode of any dictionary
def getMode(dictionary):
	return max(dictionary.iteritems(),key=operator.itemgetter(1))[0]


#AGE SECTION
def getAges():
	ageDictionary = {}
	for respondent in resList:
		age = respondent.getAge()
		ageDictionary[age] = (int(ageDictionary.get(age,0))+1)
	return ageDictionary

def getNormalizedAges():
	total = 0
	ageDictionary = getAges()
	for age in ageDictionary:
		current = (int(ageDictionary.get(age)))
		percent = (float(current)/respondents.getCount())*100
		ageDictionary[age] = percent
		total = total + percent
	print 'total is ',total
	return ageDictionary

#returns normalized age list in sorted order increasing age
def getAgeList():
	ageDictionary = getAges()
	ageList = []
	for age in ageDictionary:
		ageList.append((age,ageDictionary.get(age)))
	ageList.sort()
	return ageList

def getAgeMean():
	ageDictionary = getAges()
	total = 0
	for age in ageDictionary:
		total = total + (int(age)*int(ageDictionary.get(age)))
	average = total/respondents.getCount()
	print average


#GENDER SECTION
def getGenders():
	genderDictionary = {}
	for respondent in resList:
		gender = respondent.getGender()
		genderDictionary[gender] = (int(genderDictionary.get(gender,0))+1)
	return genderDictionary

def getNormalizedGenders():
	total = 0
	genderDictionary = getGenders()
	for gender in genderDictionary:
		current = (int(genderDictionary.get(gender)))
		percent = (float(current)/respondents.getCount())*100
		genderDictionary[gender] = percent
		total = total + percent
	print 'total is ',total
	return genderDictionary



# LENGTH SECTION
def getLengths():
	lengthDictionary = {}
	for respondent in resList:
		length = respondent.getLength()
		lengthDictionary[length] = (int(lengthDictionary.get(length,0))+1)
	return lengthDictionary

def getNormalizedLength():
	total = 0
	lengthDictionary = getLengths()
	for length in lengthDictionary:
		current = (int(lengthDictionary.get(length)))
		percent = (float(current)/respondents.getCount())*100
		lengthDictionary[length] = percent
		total = total + percent
	print 'total is ',total
	return lengthDictionary



# EDUCATION SECTION
def getEducations():
	educationDictionary = {}
	for respondent in resList:
		education = respondent.getEducation()
		educationDictionary[education] = (int(educationDictionary.get(education,0))+1)
	return educationDictionary

def getNormalizedEducations():
	total = 0
	educationDictionary = getEducations()
	for education in educationDictionary:
		current = (int(educationDictionary.get(education)))
		percent = (float(current)/respondents.getCount())*100
		educationDictionary[education] = percent
		total = total + percent
	print 'total is ',total
	return educationDictionary


# OTHER SITES SECTION
def getOtherSites():
	sitesDictionary = {}
	for respondent in resList:
		sites = respondent.getOtherSites()
		sitesString = sites.split("|")
		for site in sitesString:
			sitesDictionary[site] = (int(sitesDictionary.get(site,0))+1)
	return sitesDictionary

def getNormalizedOtherSites():
	total = 0
	sitesDictionary = getOtherSites()
	for sites in sitesDictionary:
		current = (int(sitesDictionary.get(sites)))
		percent = (float(current)/respondents.getCount())*100
		sitesDictionary[sites] = percent
	print 'total is ',total
	return sitesDictionary



# SAME USERNAMES SECTION
def getSameUsernames():
	total = 0
	usernamesDictionary = {}
	for respondent in resList:
		usernames = respondent.getSameUsername()
		usernamesString = usernames.split("|")
		for username in usernamesString:
			total = total + 1
			usernamesDictionary[username] = (int(usernamesDictionary.get(username,0))+1)
	print 'total number of same usernames is ',total
	return usernamesDictionary

def getNormalizedSameUsernames():
	total = 0
	usernamesDictionary = getSameUsernames()
	for usernames in usernamesDictionary:
		current = (int(usernamesDictionary.get(usernames)))
		percent = (float(current)/respondents.getCount())*100
		usernamesDictionary[usernames] = percent
	print 'total is ',total
	return usernamesDictionary



# THIS METHOD GIVES THE PERCENT OF USERS WHO USE THE SAME USERNAME ON A SITE
def getPercentOtherSitesSameUsernames():
	otherSites = getOtherSites()
	sameUsernames = getSameUsernames()
	percents = {}
	for site in sameUsernames:
		print 'site is ',site
		numOnSite = otherSites.get(site)
		print 'num on site is ',numOnSite
		sameUsername = sameUsernames.get(site)
		print 'same usernames is ',sameUsername
		percents[site] = (float(sameUsername)/numOnSite)*100
	print percents


# ACCOUNTS SECTION
def getAccounts():
	accountsDictionary = {}
	for respondent in resList:
		accounts = respondent.getAccounts()
		accountsDictionary[accounts] = (int(accountsDictionary.get(accounts,0))+1)
	return accountsDictionary

def getNormalizedAccounts():
	total = 0
	accountsDictionary = getAccounts()
	for accounts in accountsDictionary:
		current = (int(accountsDictionary.get(accounts)))
		percent = (float(current)/respondents.getCount())*100
		accountsDictionary[accounts] = percent
		total = total + percent
	print 'total is ',total
	return accountsDictionary

# WHY SECTION
def getWhys():
	whys = []
	for respondent in resList:
		ans = str(respondent.getWhy())
		if (ans != "{}"):
			whys.append(ans)
			whys.append(" ")
	return whys


# in order to make the word cloud
def getWhysOneString():
	whys = getWhys()
	table = string.maketrans("","")


	whyDictionary = {}
	for why in whys:
		split = why.split(" ")
		for part in split:
			lowercase = part.lower()
			correctWord = lowercase.translate(table,string.punctuation)


			whyDictionary[correctWord] = int(whyDictionary.get(correctWord,0)+1)

	for word in whyDictionary:
		print (word, whyDictionary.get(word))

		'''
	stringWhys =""
	for why in whys:
		stringWhys = stringWhys + why
	#for why in stringWhys:

	return stringWhys
	'''


# in order to make the word cloud
def readWhysFromFile(filename):
	f = open(filename,'r')

	f2 = open('created.txt','a')

	table = string.maketrans("","")
	for line in f:
		correctWord = line.translate(table,string.punctuation)
		stringy = correctWord.split(" ")
		word = stringy[0]
		number = stringy[1]
		print number
		for x in range(0,int(number)):
			f2.write(word+",")

def getFemales():
	return respondents.females()

def getMales():
	return respondents.males()

def get18To24():
	return respondents.age(18,24)

def get25To34():
	return respondents.age(25,34)

def get35To44():
	return respondents.age(35,44)

#we didn't get any ages over 80
def get45Up():
	return respondents.age(45,80)

def getHighSchool():
	return respondents.education('Some High School')

def getSomeCollege():
	return respondents.education('Some college, no degree')

def getAssociates():
	return respondents.education('Associates degree')

def getBachelors():
	return respondents.education('Bachelors degree')

def getGrads():
	return respondents.education('Graduate degree (Masters, Doctorate, etc.)')

def oneAccount():
	return respondents.account('1 account')

def twoAccounts():
	return respondents.account('2-5 accounts')

def fiveAccounts():
	return respondents.account('6-10 accounts')

def elevenAccounts():
	return respondents.account('11+ accounts')
	
	
	
#gives username/why info given demographic (list of users)
def givenDemographicUsernameInfo(userList):
	otherSites = {}
	totalSites = 0
	sameUsername = {}
	totalUsernames = 0
	for person in userList:
		sites = person.getOtherSites()
		sitesString = sites.split("|")
		for site in sitesString:
			totalSites = totalSites +1
			otherSites[site] = (int(otherSites.get(site,0))+1)
		usernames = person.getSameUsername()
		usernamesString = usernames.split("|")
		for username in usernamesString:
			totalUsernames = totalUsernames + 1
			sameUsername[username] = (int(sameUsername.get(username,0))+1)
	print 'other sites ',otherSites
	for site in otherSites:
		otherSites[site] = (float(otherSites[site])/totalSites)*100
	print 'normalized sites ',otherSites

	print 'same usernames ',sameUsername
	for username in sameUsername:
		sameUsername[username] = (float(sameUsername[username])/totalUsernames)*100
	print 'normalized usernames ',sameUsername

#gives number accounts given demographic
def givenDemographicAccountInfo(userList):
	accounts = {}
	accountsNorm = {}
	total = 0
	for user in userList:
		num = user.getAccounts()
		accounts[num] = (int(accounts.get(num,0))+1)
	for entry in accounts:
		accountsNorm[entry] = (float(accounts[entry])/len(userList))*100

	print 'num accounts ',accounts
	print 'norm accounts ',accountsNorm


