import datetime

class InstagramUser (object):

	def __init__(self,instagramUser):
		self.instagramUser = instagramUser
		self.username = username
		self.submissions = submissions
		self.timesOfSubmissions = timesOfSubmissions
		self.wordsNorm = {}
		self.hoursNorm = {}
		self.monthsNorm = {}
		self.yearsNorm = {}

	def getInstagramUser(self):
		return self.instagramUser

	def getUsername(self):
		return self.username

	def getTimeString(self):
		return datetime.datetime.fromtimestamp(float(self.timeCreated)).strftime("%Y-%m-%d %H:%M")

# 	def getSubmissions(self):
# 		return self.submissions

# 	def getSubmissionTimes(self):
# 		return self.timesOfSubmissions

	def setWordsNorm(self,wordsNorm):
		self.wordsNorm = wordsNorm

	def getWordsNorm(self):
		return self.wordsNorm

	def setHoursNorm(self,hoursNorm):
		self.hoursNorm = hoursNorm

	def getHoursNorm(self):
		return self.hoursNorm

	def setMonthsNorm(self,monthsNorm):
		self.monthsNorm = monthsNorm

	def getMonthssNorm(self):
		return self.monthsNorm

	def setYearsNorm(self,yearsNorm):
		self.yearsNorm = yearsNorm

	def getYearsNorm(self):
		return self.yearsNorm


class InstagramUsers (object):

	def __init__(self):
		self.count = 0
		self.list = []

	def increaseInstagramUserCount(self):
		self.count = self.count + 1

	def addInstagramUser(self,instagramUser):
		self.list.append(instagramUser)

	def getCount(self):
		return self.count

	def getList(self):
		return self.list

	def getListItems(self):
		for item in self.list:
			print item.getUsername()

	def getInstagramUser(self,username):
		for instagramUser in self.list:
			if instagramUser.getUsername() == username:
				return instagramUser