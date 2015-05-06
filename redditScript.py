import getUsernames
import Redditor
import frequencies
import createHistograms
import compare
import instaInfo


#reddit

getUsernames.getUsernamesFromList('usernames.csv')
getUsernames.doEverything()
userList = getUsernames.getLists()
createHistograms.createHistsAndNorms(userList)

#instagram, already normalizes
instaUserList = instaInfo.doEverything()
#print 'user list is',instaUserList


#compare.compareAllWordFreqs(userList,instaUserList)




