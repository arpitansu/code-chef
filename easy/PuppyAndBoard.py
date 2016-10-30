g = [
[1,0,0],
[0,1,0],
[0,0,1],
[0,0,0]
]
for _ in xrange(input()):
	n , m = map(int, raw_input().split())
	if (g[(n-1)%4][(m-1)%3] is 0):
		print ('Tuzik')
	else:
		print ("Vanya")