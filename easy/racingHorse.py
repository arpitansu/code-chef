for i in range(input()) :
	n = input()
	val = raw_input().split()
	skills = []
	for j in range(n):
		skills.append(int(val[j]))
	skills.sort()
	m = skills[-1]
	for j in range(1,n):
		c = skills[j]-skills[j-1]
		if c < m :
			m = c
	print m  