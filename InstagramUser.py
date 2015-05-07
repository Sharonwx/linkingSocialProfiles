# Author: Tiffany Ang 
# Class: CS349 (Wellesley College) - Data Privacy
# functionality: defines InstagramUser objects and InstagramUsers objects
# - InstagramUser contains submissions, timesOfSubmissions, and normalized dictionaries for word counts
#   and posting time counts in addition to normal profile info (username, id, Instagram user profile)
# - InstagramUsers stores a list of InstagramUser objects inside it 

import datetime

class InstagramUser (object):

	def __init__(self,instagramUser):
		self.instagramUser = instagramUser
		self.username = instagramUser.username
		self.id = instagramUser.id
		self.submissions = []
		self.timesOfSubmissions = []
		self.wordsNorm = {}
		self.hoursNorm = {}
		self.monthsNorm = {}
		self.yearsNorm = {}

	def getInstagramUser(self):
		return self.instagramUser

	def getUsername(self):
		return self.username
		
	def getID(self):
	  return self.id

	def getTimeString(self):
		return datetime.datetime.fromtimestamp(float(self.timeCreated)).strftime("%Y-%m-%d %H:%M")

	def setSubmissions(self, submissions):
		 self.submissions = submissions

	def getSubmissions(self):
		return self.submissions

	def setSubmissionTimes(self,timesOfSubmissions):
		self.timesOfSubmissions = timesOfSubmissions
		
	def getSubmissionTimes(self):
	  return self.timesOfSubmissions
	
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