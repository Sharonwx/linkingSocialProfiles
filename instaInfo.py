from instagram.client import InstagramAPI

api = InstagramAPI(client_id='56511a3cf82d4525befd4e7c669a7ab2', client_secret='50e62e2b2a674b0a920af8bed61ab756')

# return a list of matching Instagram users from a list of Reddit usernames 
def getMatches(loadedlist):
  userlist = []
  
  for user in loadedlist:
    try:
      userlist.append(api.user_search(user)[0])
    except:
      username_error = user + " was not found"
    
  print "There are " + str(len(userlist)) + " Instagram username matches out of the original " + str(len(loadedlist)) + " Reddit usernames."
  return userlist


# get matching users from a txtfile of Reddit usernames
def getMatchesFromFile(txtfile):
  #parse the file for usernames
  myfile = open(txtfile, 'r')
  loadedlist = myfile.readlines()
  loadedlist = map(lambda s: s.strip(), loadedlist) #remove newline char
  myfile.close()
  
  return getMatches(loadedlist)


# return a dictionary of word counts for a specific user
def countWords(user):
  try:
    recentmedia = api.user_recent_media(user_id=user.id,count=20)
    
    allcaptions = []
    wordDict = {}
    
    # when retrieving captions, remove special characters and convert to lowercase
    for media in recentmedia[0]:
      try:
        allcaptions.append(media.caption.text.translate(None, '.,@#!$').lower().split())
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
    
    return wordDict
  except:
    print "This user is private."
  

# return a dictionary of posting counts (by hour) for a specific user
def countTimes(user):
  try:
    recentmedia = api.user_recent_media(user_id=user.id,count=20)
    timeDict = {}
    
    for media in recentmedia[0]:
      hour = media.created_time.hour
      try: 
        timeDict[hour] = timeDict[hour] + 1
      except: 
        timeDict[hour] = 1 #first occurence of this hour
    
    return timeDict
  except:
    print "This user is private."

#print word counts and posting time counts for a list of Instagram users
def printAllUserCounts(userlist):
  for user in userlist:
    print "username: " + user.username
    print "\nWord Counts:"
    print countWords(user)
    print "\nPosting Time Counts:"
    print countTimes(user)
    print "\n\n"


