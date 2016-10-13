n , k = map(int, raw_input().split())
howManyAreDivisibleByK = 0
for i in xrange(n):
	data = input()
	if data%k == 0:
		howManyAreDivisibleByK+=1
print howManyAreDivisibleByK