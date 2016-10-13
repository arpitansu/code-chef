# def main():
# 	t  = input()
# 	x = 1000000007

# 	while t:
# 		n = input()
# 		a = input()
# 		b =  2*a
# 		c = 0
# 		d = 2
# 		try:
# 			for i in xrange(n):
# 				a = input()
# 				c*=2
# 				c+=b*a
# 				c=c%x
# 				b+=d*a
# 				b%=x
# 				d*=2
# 				d%=x

# 			return c
# 		except:
# 			return 0

# 		t-=1

# print main()
m = 10**9 + 7	
 
def rgame (a,n):
	s = 2*a[0]
	ans = 0
	p = 1
	for i in range(1,n+1):
		p = (2*p)%m
		ans = (2*ans + s*a[i])%m	
		s = (s + p*a[i])%m
	return ans 
 
 
t = int(raw_input())
 
for i in range(t):
	n = int(raw_input())
	b = raw_input()
	a = map(int,b.split(" "))
	print rgame(a,n)