import getUsernames
import Redditor
import frequencies
import createHistograms
import instaInfo
import compare

instagramUsers = instaInfo.doEverything()

single = instaInfo.getSingleUser('instagram')
print single.getUsername()
print single.getWordsNorm()
print single.getHoursNorm()
print single.getSubmissions()
