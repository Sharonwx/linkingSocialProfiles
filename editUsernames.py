
f = open('usernames.csv')


#try with first 300
content = f.readlines()
for lines in content[0:49]:
	f2 = open('one.csv','a')
	f2.write(lines)

for lines in content[50:99]:
	f3 = open('two.csv','a')
	f3.write(lines)

for lines in content[100:149]:
	f3 = open('three.csv','a')
	f3.write(lines)

for lines in content[150:199]:
	f3 = open('four.csv','a')
	f3.write(lines)

for lines in content[200:249]:
	f3 = open('five.csv','a')
	f3.write(lines)

for lines in content[250:299]:
	f3 = open('six.csv','a')
	f3.write(lines)
