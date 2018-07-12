#!/usr/local/bin/python3

numone = input("Please enter number one ")
op = input("Please enter an operator ")
numtwo = input("Please enter number two ")


numone = int(numone)
numtwo = int(numtwo)

if op == "+":
	result = numone + numtwo
	print(result)
elif op == "*":
	result = numone * numtwo
	print(result)
elif op == "/":
	result = numone / numtwo
	print(result)
elif op == "-":
	result = numone - numtwo
	print(result)
else: 
	print("Not an operator")

#print(result)
