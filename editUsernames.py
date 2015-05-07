
f = open('usernames.csv')


#try with first 300
content = f.readlines()
for lines in content[0:24]:
	f2 = open('one.csv','a')
	f2.write(lines)

for lines in content[25:49]:
	f3 = open('two.csv','a')
	f3.write(lines)

for lines in content[50:74]:
	f3 = open('three.csv','a')
	f3.write(lines)

for lines in content[75:99]:
	f3 = open('four.csv','a')
	f3.write(lines)

for lines in content[100:124]:
	f3 = open('five.csv','a')
	f3.write(lines)

for lines in content[125:149]:
	f3 = open('six.csv','a')
	f3.write(lines)

for lines in content[150:174]:
	f3 = open('seven.csv','a')
	f3.write(lines)

for lines in content[175:199]:
	f3 = open('eight.csv','a')
	f3.write(lines)

for lines in content[200:224]:
	f3 = open('nine.csv','a')
	f3.write(lines)

for lines in content[225:249]:
	f3 = open('ten.csv','a')
	f3.write(lines)

for lines in content[250:274]:
	f3 = open('eleven.csv','a')
	f3.write(lines)

for lines in content[275:299]:
	f3 = open('twelve.csv','a')
	f3.write(lines)

