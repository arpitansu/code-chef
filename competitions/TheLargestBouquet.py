for _ in xrange(input()):
	Maple = map(int, raw_input().split()) #Mg,My,Mr
	Oak = map(int, raw_input().split())#Og,Oy,Or
	Poplar = map(int, raw_input().split()) #Pg,Py,Pr
	# print Maple,Oak,Poplar
	greenLeaves = [Maple[0],Oak[0],Poplar[0]]
	yellowLeaves = [Maple[1],Oak[1],Poplar[1]]
	redLeaves = [Maple[2],Oak[2],Poplar[2]]
	maxSum = 0
	for i in Maple:
		maxSum += i

	oakSum = 0
	for i in Oak:
		oakSum+=i
	if maxSum>oakSum:
		pass
	else:
		maxSum = oakSum

	PoplarSum = 0
	for i in Poplar:
		PoplarSum+=i
	if maxSum>PoplarSum:
		pass
	else:
		maxSum = PoplarSum
	
	greenSum = 0
	for i in greenLeaves:
		greenSum+=i
	if maxSum>greenSum:
		pass
	else:
		maxSum = greenSum

	yellowSum = 0
	for i in yellowLeaves:	
		yellowSum+=i
	if maxSum>yellowSum:
		pass
	else:
		maxSum = yellowSum

	redSum = 0
	for i in redLeaves:	
		redSum+=i
	if maxSum>redSum:
		pass
	else:
		maxSum = redSum

	if maxSum==0:
		print 0
	elif maxSum>0 and maxSum%2==0:
	 	print maxSum-1
	else:
		print maxSum

