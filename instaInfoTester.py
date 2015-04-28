import instaInfo

#get list of Instagram matches
matches = instaInfo.getMatchesFromFile('usernames.txt')

#getting info on a single user
singleuser = matches[2]
print "username: " + singleuser.username
print instaInfo.countWords(singleuser)
print instaInfo.countNormWords(singleuser)
print instaInfo.countTimes(singleuser)
print instaInfo.countNormTimes(singleuser)

#get info on all the users
instaInfo.printAllUserCounts(matches)