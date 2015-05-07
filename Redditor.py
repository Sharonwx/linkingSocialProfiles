import datetime

class Redditor (object):

	def __init__(self, redditor,username,timeCreated,submissions,timesOfSubmissions,submittedSubs,submittedSubsKarma,
	comments, timesOfComments, commentedSubs,commentedSubsKarma):
		self.redditor = redditor
		self.username = username
		self.timeCreated = timeCreated
		self.submissions = submissions
		self.timesOfSubmissions = timesOfSubmissions
		self.submittedSubs = submittedSubs
		self.submittedSubsKarma = submittedSubsKarma
		self.comments = comments
		self.timesOfComments = timesOfComments
		self.commentedSubs = commentedSubs
		self.commentedSubsKarma = commentedSubsKarma
		self.words = {}
		self.wordsNorm = {}
		self.hoursNorm = {}
		self.monthsNorm = {}
		self.yearsNorm = {}


	def getRedditor(self):
		return self.redditor

	def getUsername(self):
		return self.username

	def getTimeCreated(self):
		return self.timeCreated

	def getTimeString(self):
		return datetime.datetime.fromtimestamp(float(self.timeCreated)).strftime("%Y-%m-%d %H:%M")

	def getSubmissions(self):
		return self.submissions

	def getSubmissionTimes(self):
		return self.timesOfSubmissions

	def getSubmittedSubs(self):
		return self.submittedSubs

	def getSubmittedSubsKarma(self):
		return self.submittedSubsKarma

	def getComments(self):
		return self.comments

	def getCommentTimes(self):
		return self.timesOfComments

	def getCommentedSubs(self):
		return self.commentedSubs

	def getCommentedSubsKarma(self):
		return self.commentedSubsKarma

	def setWords(self,words):
		self.words = words

	def getWords(self):
		return self.words

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

	def getMonthsNorm(self):
		return self.monthsNorm

	def setYearsNorm(self,yearsNorm):
		self.yearsNorm = yearsNorm

	def getYearsNorm(self):
		return self.yearsNorm


class Redditors (object):

	def __init__(self):
		self.count = 0
		self.list = []

	def increaseRedditorCount(self):
		self.count = self.count + 1

	def addRedditor(self,redditor):
		self.list.append(redditor)

	def getCount(self):
		return self.count

	def getList(self):
		return self.list

	def getListItems(self):
		for item in self.list:
			print item.getUsername()

	def getRedditor(self,username):
		for redditor in self.list:
			if redditor.getUsername() == username:
				return redditor