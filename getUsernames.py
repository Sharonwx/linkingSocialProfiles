import praw
import csv
import pprint
import Redditor
import datetime

r = praw.Reddit(user_agent='mac:personal_research:v1.0 (by"empteeh20bttl")')

#f2 = open('usernames.csv','a')
redditors = Redditor.Redditors()

list = []


def getUsernamesFromFrontPage():
	content = r.get_front_page()
	for c in content:
		name = c.author.name
		list.append(name)

def doEverything():

	for item in list:
		user = r.get_redditor(item)
		timeCreated = datetime.datetime.fromtimestamp(float(user.created_utc))
	
		submissions = [] 
		generator = user.get_submitted(time='all')
		timesOfSubmissions = []
		submittedSubs = []
		submittedSubsKarma = {}
		for thing in generator:
			submissions.append(thing.selftext)
			tm = datetime.datetime.fromtimestamp(float(thing.created_utc))
			timesOfSubmissions.append(tm)
			subreddit = thing.subreddit.display_name
			if subreddit not in submittedSubs:
				submittedSubs.append(subreddit)
			submittedSubsKarma[subreddit] = (submittedSubsKarma.get(subreddit,0)+thing.score)

		comments = []
		generator = user.get_comments(limit=None)
		timesOfComments = []
		commentedSubs = []
		commentedSubsKarma = {}
		for comment in generator:
			comments.append(comment.body)
			tm = datetime.datetime.fromtimestamp(float(comment.created_utc))
			timesOfComments.append(tm)
			subreddit = comment.subreddit.display_name
			if subreddit not in commentedSubs:
				commentedSubs.append(subreddit)
			commentedSubsKarma[subreddit] = (commentedSubsKarma.get(subreddit,0)+comment.score)

		redditUser = Redditor.Redditor(user,item,timeCreated,submissions,timesOfSubmissions,submittedSubs,submittedSubsKarma,comments,timesOfComments,commentedSubs,commentedSubsKarma)
		redditors.increaseRedditorCount()
		redditors.addRedditor(redditUser)

	print "total count is",redditors.getCount()
	print "final list is",redditors.getList()

def getRedditor(username):
	print redditors.getRedditor(username)
	return redditors.getRedditor(username)

def getLists():
	#print redditors.getList()
	#redditors.getListItems()
	return redditors.getList()
	

