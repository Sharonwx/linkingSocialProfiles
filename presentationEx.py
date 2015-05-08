from twitter_info import *
import twitter_info
import unicodedata
import string
from datetime import datetime

''' 
Let's stalk Jimmy Fallon!
'''

findJimmy = doAllTheThings('test.txt') #sets findJimmy to a TwitPpl object
print 'Number of twits in twitlist: ' + str(findJimmy.getCount())
print '\nAll the twits in twitlist:'
findJimmy.getAllTwitsFromList() #should print all the Twits from the list: aka only Jimmy

print '-----------------------\n'
jimmeh = findJimmy.getTwitList()
print jimmeh[0]
#print jimmeh[1].getTweetTexts()


