for _ in xrange(input()):
	n , k = map(int, raw_input().split())
   	if k is 0:
   		print 0, n
	elif n%k==0:
		print n/k, 0
	else:
		m = n%k
		n = n-n%k
		print n/k, m