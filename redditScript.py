import getUsernames
import Redditor
import frequencies
import createHistograms
import compare



# the below line will pull usernames off the front page
getUsernames.getUsernamesFromList('usernames.csv')
getUsernames.doEverything()

userList = getUsernames.getLists()


createHistograms.createHistsAndNorms(userList)

compare.compareAllWordFreqs(userList)



