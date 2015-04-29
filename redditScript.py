import getUsernames
import Redditor
import frequencies
import createHistograms

# the below line will pull usernames off the front page
getUsernames.getUsernamesFromFrontPage()
getUsernames.doEverything()

userList = getUsernames.getLists()

for user in userList:
	print user.getUsername()

	ct = user.getCommentTimes()
	st = user.getSubmissionTimes()
	coms = user.getComments()
	subs = user.getSubmissions()
	s1 = user.getSubmittedSubs()
	s2 = user.getCommentedSubs()

	frequencies.getTopics(s1,s2)
	freqs = frequencies.wordFrequencies(coms,subs)
	timeFreqs = frequencies.timeFrequencies(ct,st)

	createHistograms.normalizeWordFreqs(freqs)
	createHistograms.normalizeTimeFreqs(timeFreqs.get('hours'),
		timeFreqs.get('months'),timeFreqs.get('years'))