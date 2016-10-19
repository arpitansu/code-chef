# this file has two algo's 
#choose only one and comment out other

# # this is pure logic
for _ in xrange(input()):# testcases
	input() #fooling around
	numList = map(int, raw_input().split()) # list for numbers or arrays
	while min(numList) != max(numList):# checks if the max value in list in equal to min value or not			
		numList.insert(0, numList.pop(numList.index(max(numList))) - min(numList))# maxIs = max(numList)# minIs = min(numList)
	print numList[0]

#this is pure smartness
from fractions import gcd
for _ in xrange(input()):
	input()
	numList = map(int, raw_input().split())
	print reduce(gcd,numList) 