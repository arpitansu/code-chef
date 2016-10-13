def main():
	t = input()
	l = []

	for i in xrange(t):
			l.append(map(int, raw_input()))
	s = sorted(l)

	for i in xrange(len(s)):
		print (s[i][0])


main()
