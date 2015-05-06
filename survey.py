
class Respondent (object):
	def __init__(self,wid,age,education,gender,length,otherSites,sameUsername,accounts,why):
		self.wid = wid
		self.age = age
		self.education = education
		self.gender = gender
		self.length = length
		self.otherSites = otherSites
		self.sameUsername = sameUsername
		self.accounts = accounts
		self.why = why

	def getWid(self):
		return self.wid

	def getAge(self):
		return self.age

	def getEducation(self):
		return self.education

	def getGender(self):
		return self.gender

	def getLength(self):
		return self.length

	def getOtherSites(self):
		return self.otherSites

	def getSameUsername(self):
		return self.sameUsername

	def getAccounts(self):
		return self.accounts

	def getWhy(self):
		return self.why



class Respondents (object):
	def __init__(self):
		self.count = 0
		self.list = []

	def increaseRespondentsCount(self):
		self.count = self.count + 1

	def getCount(self):
		return self.count

	def addRespondent(self,respondent):
		self.list.append(respondent)

	def getList(self):
		#print self.list
		return self.list

	def getListItems(self):
		for item in self.list:
			print item.getWid

	def females(self):
		females = []
		for respondent in self.list:
			if respondent.getGender() == 'Female':
				females.append(respondent)
		return females

	def males(self):
		males = []
		for respondent in self.list:
			if respondent.getGender() == 'Male':
				males.append(respondent)
		return males

	#returns ages in range given lower and upper
	def age(self,lower,upper):
		age = []
		ageList = range(lower,upper)
		for respondent in self.list:
			if int(respondent.getAge()) in ageList:
				age.append(respondent)
		return age

	#returns group given education level
	def education(self,level):
		education = []
		for respondent in self.list:
			if respondent.getEducation() == level:
				education.append(respondent)
		return education

	#returns group given num accounts
	def account(self,num):
		accounts = []
		for respondent in self.list:
			if respondent.getAccounts() == num:
				accounts.append(respondent)
		return accounts

	def getRespondent(self,wid):
		for respondent in self.list:
			if respondent.getWid() == wid:
				return respondent
