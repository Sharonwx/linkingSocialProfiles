import instaInfo

#get list of Instagram matches
matches = instaInfo.getMatchesFromFile('usernames.txt')

#getting info on a single user
singleuser = matches[2]
print "username: " + singleuser.username
print instaInfo.countWords(singleuser)
print instaInfo.countTimes(singleuser)

#get info on all the users
#instaInfo.printAllUserCounts(matches)