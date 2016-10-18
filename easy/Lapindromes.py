from collections import Counter

for _ in xrange(input()):# testcases
	s = raw_input() #words input
	a = list(s) # converting words to list
	if len(a)%2 is not 0: # looping through list a
		a.pop(len(a)/2) # poping the middle char if length of words not even is not even
	part1 = a[0:len(a)/2] # dividing part 1 and 2 to half of the list a 
	part2 = a[len(a)/2:]

	if Counter(part1) == Counter(part2): #counting occurance of words Frequency and checkingin both if they are equal
		print ('YES')
	else:
		print ('NO')
