# A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z
holesDic = {
	'A':1,
	'B':2,
	'C':0,
	'D':1,
	'E':0,
	'F':0,
	'G':0,
	'H':0,
	'I':0,
	'J':0,
	'K':0,
	'L':0,
	'M':0,
	'N':0,
	'O':1,
	'P':1,
	'Q':1,
	'R':1,
	'S':0,
	'T':0,
	'U':0,
	'V':0,
	'W':0,
	'X':0,
	'Y':0,
	'Z':0,
}
a='arpit'
# print a[1]
# print type(holesDic.get('A'))
# a = 'A'
# for k,v in holesDic.iteritems():
# 	if k==a:
# 		print 'yes'

for _ in xrange(input()):
	holes = 0
	inputString = raw_input().upper()
	for char in xrange(len(inputString)):
		w = inputString[char]
		holes+=int(holesDic.get(w))
	print holes




