t = input()
for i in xrange(t):
	n = 0
	k = 0
	# ar = raw_input().split(" ")
	# ar = [int(x) for x in ar]
	# a, b, c, d = ar[0], ar[1], ar[2], ar[3]
	a, b, c, d = map(int, raw_input().split())
	if c <= a:
		c = a + 1
	if d <= b:
		b = d - 1
	if c <= b:
		n = b + 1 - c
		k = c - a
		c = b + 1
	if b < a or d < c or d < a:
		print 0
	# else:
	print (d - c + 1) * (b - a + 1) + (n * (2 * k + n - 1) /2) 