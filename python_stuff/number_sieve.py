#!/usr/local/bin/python3

numone = int(input("Enter number one "))
numtwo = int(input("Enter number two "))
fourset = set() 
sevenset = set() 
testset = set()
foursevenset = set() 
numdict = {}

while numtwo <  numone:
	print("{1} is not larger than {0}.".format(numone, numtwo))
	numtwo = input("Please enter a larger number ")

for i in range(numone, numtwo):
	print(i)
	if i % 4 == 0 and i % 7 != 0:
		fourset.add(i)
	elif i % 4 != 0 and i % 7 == 0:
		sevenset.add(i)
	elif i % 4 == 0 and i % 7 == 0:
		foursevenset.add(i)
	else:
		testset.add(i)
print("fourset is: {0}".format(fourset))
print("sevenset is: {0}".format(sevenset))
print("foursevenset is: {0}".format(foursevenset))

numdict['four'] = fourset
numdict['seven'] = sevenset
numdict['fourseven'] = foursevenset
print(numdict)