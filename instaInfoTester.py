import instaInfo

matches = instaInfo.getMatchesFromFile('usernames.txt')
print "username: " + matches[2].username
print instaInfo.countWords(matches[2])
# instaInfo.printAllUserCounts(matches)
  
