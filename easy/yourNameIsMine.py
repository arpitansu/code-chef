#choose only 1

#sol 1
# returns TRUE if matching char's present
for _ in xrange(input()):
	name1, name2 = raw_input().split()
	name1 = list(name1)
	name2 = list(name2)
	l1 = len(name1)
	l2 = len(name2)
	if l1 <= l2 :
		for x in xrange(l1):
			if name1[x] in name2:
				name1[x] = 'YES'
	elif l2 <= l1 :
		for x in xrange(l2):
			if name2[x] in name1:
				name2[x] = 'YES'
	name1 = list(set(name1))
	name2 = list(set(name2))
	if len(name1)==1 or len(name2)==1:
		print('YES')
	else:
		print('NO')
#-------------------------------------------------------------------
#sol 2
#returns true acc to ques
def isSubset(m, f):
	if len(m) >= len(f):
		fmale = 0
		for i in range(len(m)):
			if m[i] == f[fmale]:
				fmale+=1
			if fmale == len(f): return True
		return False
	return False
 
for _ in range(input()):
	m, f = map(str, raw_input().split())
	if isSubset(m, f) or isSubset(f, m):
		print 'YES'
	else:
		print 'NO' 

