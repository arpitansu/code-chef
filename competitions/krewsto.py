# r1 = [2,1,2,6] #x1 = r1[0] ,y1 = r1[1] , x2 = r1[3], y2 = r1[4]
# r2 = [1,3,5,3] #x1 = r2[0] ,y1 = r2[1] , x2 = r2[3], y2 = r2[4]
# r3 = [4,1,4,4] #x1 = r3[0] ,y1 = r3[1] , x2 = r3[3], y2 = r3[4]
# r4 = [1,5,5,5] #x1 = r4[0] ,y1 = r4[1] , x2 = r4[3], y2 = r4[4]
n = input()
# whileN = n
inputs = []
# n = 4 #number of roads 

# inputs = [[2,1,2,6],[1,3,5,3],[4,1,4,4],[1,5,5,5]] #inputs[0][1] = x1
for _ in xrange (n):
	# whileN-=1
	inputs.append(map(int, raw_input().split()))
# print inputs
lenInputs = len(inputs)
m = 0 
for i in xrange(lenInputs):
	if max(inputs[i]) > m:
		m = max(inputs[i])

# print m

Matrix = [[0 for x in xrange(m)] for y in xrange(m)] #populated list with 0s m x m 

for pos1 in xrange(lenInputs):#0,1,2,3

	if (inputs[pos1][0] == inputs[pos1][2]): #X1 == X2, populate in x direction 
		x = inputs[pos1][0]
		v1 = max(inputs[pos1][3],inputs[pos1][1])
		v2 = min(inputs[pos1][3],inputs[pos1][1])
		for pos2 in xrange(v1-v2+1):
			if Matrix[x][pos2] >0:
				value = str(Matrix[x][pos2])+str(pos1+1)
				Matrix[x][pos2] = (value)
			else:
				Matrix[x][pos2] = str(pos1+1)

	elif (inputs[pos1][1] == inputs[pos1][3]): #y1 == y2, populate in y diection
		y = inputs[pos1][1]
		v1 = max(inputs[pos1][2],inputs[pos1][0])
		v2 = min(inputs[pos1][2],inputs[pos1][0])
		for pos2 in xrange(v1-v2+1):
			if Matrix[pos2][y] >0:
				value = str(Matrix[pos2][y])+str(pos1+1)
				Matrix[pos2][y] = (value)
			else:
				Matrix[pos2][y] = str(pos1+1)
# for i in Matrix:
# 	print i
lenMatrix = len(Matrix)
sets = 0
for i in xrange(lenMatrix):
	for j in xrange(lenMatrix):
		if int(Matrix[i][j])>10:
			sets+=1


fl = []

for val in xrange(1,m+1):
	sets2 = 0
	for i in xrange(lenMatrix):
		for j in xrange(lenMatrix):
			if int(Matrix[i][j])>10:
				# print (Matrix[i][j])
				if str(val) in (Matrix[i][j]):
					# print 'y'
					sets2+=1
					# l.append(sets2)# = sets2
	# m = max(l)
	fl.append(sets2)
	# print l
				


print sets
setsval = ''

for i in xrange(n):
	setsval+=str(fl[i])+" "
print setsval