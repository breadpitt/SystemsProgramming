#!/usr/local/bin/python3

numone = int(input("Enter number one "))
numtwo = int(input("Enter number two "))

def addMe(inone, intwo):
	output = inone + intwo 
	return output

retval = addMe(numone, numtwo)
print("The sum is {0}".format(retval))

def find_max(inone, intwo):
	if inone == intwo:
		return 0
	elif inone > intwo:
		return inone 
	elif intwo > inone: 
		return intwo

retval = find_max(numone, numtwo)
print("The max is {0}".format(retval))



