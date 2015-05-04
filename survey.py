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

	def getRespondent(self,wid):
		for respondent in self.list:
			if respondent.getWid() == wid:
				return respondent
