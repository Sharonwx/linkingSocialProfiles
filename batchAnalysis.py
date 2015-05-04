import batchReader
import survey
import operator

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
		total = total + (age*ageDictionary.get(age))
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

def getWhysOneString():
	whys = getWhys()
	stringWhys =""
	for why in whys:
		stringWhys = stringWhys + why
	#for why in stringWhys:

	return stringWhys

