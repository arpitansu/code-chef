def findZeros(number):
	s = 0
	power = 1
	if number==0:
		return 0
	else:
		while number>0:
			s +=number/(5)
			number = number/(5)
			power+=1
	return s


t = input()

for i in xrange(t):
	number = input()

	s = findZeros(number)

	print s

