import numpy

def getMSE(first,second):
	mse = ((first-second) ** 2).mean(axis=None)
	return mse



def compareAllWordFreqs(userList):
	for user in userList:
		#need to write code that compares the users list in reddit
		#to the users list in twitter
		#to the users list in Insta



def compareWordFreqs(firstDict,secondDict):

	inFirstNotSecond = set(firstDict.keys()) - set(secondDict.keys())
	#print 'in first not second',inFirstNotSecond
	print 'number in first not in second',len(inFirstNotSecond)
	inSecondNotFirst = set(secondDict.keys()) - set(firstDict.keys())
	#print 'in second not first',inSecondNotFirst
	print 'number in second not in first',len(inSecondNotFirst)
	inBoth = set(firstDict.keys()) and set(secondDict.keys())
	#print 'in both', inBoth
	print 'number in both',len(inBoth)

		