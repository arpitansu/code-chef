def gcd(a,b): 
	if b==0: return a 
	else: return gcd(b,a%b)
for _ in xrange(input()):
	a,b = map(int, raw_input().split())
	print (gcd(a,b))