import getUsernames
import Redditor
import frequencies
import createHistograms
#import compare



# the below line will pull usernames off the front page
getUsernames.getUsernamesFromList('usernames.csv')
getUsernames.doEverything()
userList = getUsernames.getLists()

print userList

print instaInfo.getMatches('usernames.csv')




createHistograms.createHistsAndNorms(userList)

one = userList[0]
#print one
#print one.getUsername()
wordsOne = one.getWordsNorm()
#print 'words one is',wordsOne
two = userList[1]
wordsTwo = two.getWordsNorm()

# compare.compareWordFreqs(wordsOne,wordsTwo)


