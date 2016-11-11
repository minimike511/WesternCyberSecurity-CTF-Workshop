import re

#the kek.txt file is a encoded binary file, the students should be able to figure it out after playing around with it. 

#this opens the file
with open('kek.txt', 'r') as myfile:
    data=myfile.read().replace('\n', '')


keks = []
keks = data.split( )
resultlist = []

#this replaces the tops and keks with 1s and 0s
for item in keks:
	if item == "KEK!!!!!":
		item = "00000"
	elif item == "KEK!!!!":
		item = "0000"
	elif item == "KEK!!!":
		item = "000"
	elif item == "KEK!!":
		item = "00"
	elif item == "KEK!":
		item = "0"
	elif item == "TOP!!!!!":
		item = "11111"
	elif item == "TOP!!!!":
		item = "1111"
	elif item == "TOP!!!":
		item = "111"
	elif item == "TOP!!":
		item = "11"
	elif item == "TOP!":
		item = "1"
	resultlist.append(item)

result = ''.join(resultlist)


#this saves the decoded string to a output file
f = open('outbin.txt', 'w')
print >> f, result
f.close()



