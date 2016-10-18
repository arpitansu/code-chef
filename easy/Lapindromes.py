from collections import Counter

for _ in xrange(input()):
	s = raw_input()
	a = list(s)
	if len(a)%2 is not 0:
		a.pop(len(a)/2)
	part1 = a[0:len(a)/2]
	part2 = a[len(a)/2:]

	if Counter(part1) == Counter(part2):
		print ('YES')
	else:
		print ('NO')
