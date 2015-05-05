#Author: Tiffany Ang
#Class: CS349 (Wellesley College) - Data Privacy
#functionality: gets an Instagram User account and collects it's word and time counts using the Instagram API

from instagram.client import InstagramAPI
import createHistograms
import InstagramUser
import csv

api = InstagramAPI(client_id='56511a3cf82d4525befd4e7c669a7ab2', client_secret='50e62e2b2a674b0a920af8bed61ab756')

instagramUsers = InstagramUser.InstagramUsers()


def doEverything():
# 	matches = getMatchesFromCSV('usernames.csv')
  matches = getMatchesFromFile('usernames.txt')
  for user in matches:
	  instagramUser = InstagramUser.InstagramUser(user)
	  instagramUsers.increaseInstagramUserCount()
	  instagramUsers.addInstagramUser(instagramUser)
  for user in instagramUsers.getList():
    setAllNorms(user)
  return instagramUsers

#returns a matching Instagram user from a username
def getMatch(user):
  print api.user_search(user)[0]
  return api.user_search(user)[0]
  
  
#sets all normalized dictionaries for a instagramUser
def setAllNorms(user):
  # print 'setting norms'
  try:
    user.setWordsNorm(countNormWords(user))
    times = countNormTimes(user)
    user.setHoursNorm(times['hours'])
    user.setMonthsNorm(times['months'])
    user.setYearsNorm(times['years'])
  except:
    print 'This user has no available posts.'


#returns a single user from a username
def getSingleUser(username):
  user = getMatch(username)
  instagramUser = InstagramUser.InstagramUser(user)
  setAllNorms(instagramUser)
  return instagramUser
  

# return a list of matching Instagram users from a list of usernames 
def getMatches(userlist):
  instalist = []
  
  for user in userlist:
    try:
      instalist.append(getMatch(user))
    except:
      username_error = user + " was not found"
    
  print "There are " + str(len(instalist)) + " Instagram username matches out of the original " + str(len(userlist)) + " Reddit usernames.\n"
  return instalist


# get matching users from a txtfile of Reddit usernames
def getMatchesFromFile(txtfile):
  #parse the file for usernames
  myfile = open(txtfile, 'r')
  loadedlist = myfile.readlines()
  loadedlist = map(lambda s: s.strip(), loadedlist) #remove newline char
  myfile.close()
  
  return getMatches(loadedlist)

# get matching users from a csv of Reddit usernames
def getMatchesFromCSV(filename):
  #parse the csv file for usernames
  loadedlist = []
  f = open(filename)
  reader = csv.reader(f)
  for name in reader:
    for thing in name:
    #user = "".join(name)
      loadedlist.append(thing)

  return getMatches(loadedlist)


# return a dictionary of word counts for a specific user
def countWords(user):
  try:
    recentmedia = api.user_recent_media(user_id=user.getID(),count=20)
    
    allcaptions = []
    wordDict = {}
    
    # when retrieving captions, remove special characters and convert to lowercase
    for media in recentmedia[0]:
      try:
        allcaptions.append(media.caption.text.translate(None, '.,@#!$').lower().split())
        # print 'appending'
      except:
        media_error = "media not found"
      
    # count occurences of words in all the captions
    for caption in allcaptions:
      for word in caption:
        try:
          wordDict[word] = wordDict[word] + 1
        except: 
          # first occurence of this word
          wordDict[word] = 1
    
    user.setSubmissions(allcaptions)
    # print wordDict
    return wordDict
  except:
    print "countwords: This user is private."
    
# return a normalized dictionary of word counts for a specific user
def countNormWords(user):
  try:
    wordDict = countWords(user)
    return createHistograms.normalizeWordFreqs(wordDict) 
  except:
    print "countnormwords: This user has no available posts."


# return a normalized dictionary of posting counts (by hour, month, year) for a specific user
def countTimes(user):
  try:
    recentmedia = api.user_recent_media(user_id=user.getID(),count=20)
    hourDict = {}
    monthDict = {}
    yearDict = {}
    allTimes = []
    
    for media in recentmedia[0]:
      item = media.created_time
      # print item
      
      allTimes.append(item)

      try: 
        hourDict[item.hour] = timeDict[item.hour] + 1
      except: 
        hourDict[item.hour] = 1 #first occurence of this hour

      try:
        monthDict[item.month] = monthDict[item.month] + 1
      except:
        monthDict[item.month] = 1 #first occurence of this month

      try:
        yearDict[item.year] = yearDict[item.year] + 1
      except:
        yearDict[item.year] = 1 #first occurence of this year

    user.setSubmissionTimes(allTimes)
    
    time = {'hours':hourDict,'months':monthDict,'years':yearDict}
    # print time
    return time
    
  except:
    print "counttimes: This user is private."
    
    
def countNormTimes(user):
  try:
    timeDict = countTimes(user)
    return createHistograms.normalizeTimeFreqs(timeDict['hours'], timeDict['months'], timeDict['years'])

  except:
    print "countnormtimes: This user has no available posts."
    

#print word counts and posting time counts for a list of Instagram users
def printAllUserCounts(userlist):
  for user in userlist:
    print "username: " + user.username
    
    #unnormalized
    print "\nWord Counts:"
    print countWords(user)
    print "\nPosting Time Counts:"
    print countTimes(user)

#print normalized word counts and posting time counts for a list of Instagram users
def printAllUserCounts(userlist):
  for user in userlist:
    print "username: " + user.username
    
    #normalized  
    print "\nNormalized Word Counts:"
    print countNormWords(user)
    print "\nNormalized Posting Time Counts:"
    print countNormTimes(user)
    print "\n\n"


