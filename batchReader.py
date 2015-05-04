import csv
import survey

respondents = survey.Respondents()


def readBatch():
	f = open('batch.csv')
	reader = csv.reader(f)

	for row in reader:

		wid = row[15]
		#print 'wid is ',wid
		age = row[27]
		#print 'age is',age
		education = row[28]
		educationBool = (education != 'select one')
		#print 'education is',education
		gender = row[29]
		genderBool = (gender != 'Answer.Gender')
		#print 'gender is',gender
		length = row[30]
		lengthBool = (length != 'select one') and (length != 'Answer.Length')
		#print 'length is',length
		otherSites = row[31]
		#print 'other sites is ',otherSites
		sameUsername = row[32]
		#print 'same username is ',sameUsername
		accounts = row[33]
		accountsBool = (accounts != 'select one')
		#print 'num accounts is ',accounts
		why = row[34]
		#print 'why is ',why
		#print row

		# makes sure all answers being used are complete
		if (genderBool and lengthBool and educationBool and accountsBool):
			respondent = survey.Respondent(wid,age,education,gender,length,otherSites,
				sameUsername,accounts,why)

			respondents.addRespondent(respondent)
			respondents.increaseRespondentsCount()

	#print respondents.getCount()
	#respondents.getListItems()
	return {'respondents':respondents,'list':respondents.getList()}

