import getUsernames
import Redditor
import frequencies
import createHistograms
import compare
import instaInfo


#reddit
'''
getUsernames.getUsernamesFromList('usernames.txt')
getUsernames.doEverything()
userList = getUsernames.getLists()
createHistograms.createHistsAndNorms(userList)
'''
#instagram, already normalizes
instaUserList = instaInfo.doEverything()
print 'user list is',instaUserList

for user in instaUserList.getList():
  print user.getUsername()
  print user.getWordsNorm()

# TODO: write code...

#compare.compareAllWordFreqs(userList,instaUserList)




