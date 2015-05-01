from twitter_info import *
import twitter_info
#from prettytable import PrettyTable

matches = twitter_info.findMatchesFromTxt('usernames.txt')
print matches

testuser = matches[0]

print wordFreq(testuser)


''' randomly trying something that didn't work out haha
for eachuser in (enumerate(matches)):
    label = 'Found usernames'
    pt = PrettyTable(field_names=[label])
    #c = Counter(data)
    [ pt.add_row(kv) for kv in eachuser ]
    pt.align[label] = 'l' #, 'r' # Set column alignment
    print pt
 '''
