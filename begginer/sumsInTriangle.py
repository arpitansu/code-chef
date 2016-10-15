import sys
'''this ques has two types of solution
to find minimum sum use function minimum and for max use maximum'''
def minmumTotal(triangle):
    for i in range(len(triangle)-2,-1,-1):
        for j in range(0,i+1):
            triangle[i][j] += min(triangle[i+1][j],triangle[i+1][j+1])
    return triangle[0][0]

def maximumTotal(triangle):
    results = []
    results.append(triangle[0][0])
    l = len(triangle)
    i = 1
    while i<l:
        results.append(triangle[i][i]+results[i-1])
        j = i-1
        while j>0:
            results[j] = max(results[j],results[j-1])+triangle[i][j]
            j-=1
        results[0] = results[0]+triangle[i][0]
        i+=1
    return max(results)

rounds = int(sys.stdin.readline())
listOfLines = []
length = 0
largestSum = 0

for _ in xrange(rounds):
	lengthOfList = int(sys.stdin.readline())
	length = lengthOfList

	for inp in xrange(length):
		listOfLines.append(map(int, sys.stdin.readline().split()))

	largestSum = maximumTotal(listOfLines)

print (largestSum)
	# findMaxInlastlist = max(listOfLines[length-1])
	# if findMaxInlastlist is listOfLines[length-1][0]:
	# 	largestSum = addAtPos0(findMaxInlastlist, 0, length, largestSum, listOfLines)


	# elif findMaxInlastlist is listOfLines[length-1][len(listOfLines[length-1])-1]:
	# 	largestSum = addAtPoslast(findMaxInlastlist, 0, length, largestSum, listOfLines)


	# else:
	# 	for s in xrange(length):
	# 		belowlargest = max(listOfLines[length-(1+s)])
	# 		if listOfLines[length-(2+s)][listOfLines[length-(1+s)].index(belowlargest)]:
	# 			if listOfLines[length-(2+s)][listOfLines[length-(1+s)].index(belowlargest)] > listOfLines[length-(2+s)][listOfLines.index(belowlargest)-1]:
	# 				largestSum+=listOfLines[length-(2+s)][listOfLines[length-(1+s)].index(belowlargest)]
	# 			else:
	# 				largestSum+=listOfLines[length-(2+s)][listOfLines.index(belowlargest)-1]



# belowlargest = max(listOfLines[length-(1)])


# print listOfLines[length-(1)].index(belowlargest)
# print listOfLines[length-1][len(listOfLines[length-1])-1]

# def addAtPos0(findMaxInlastlist, rangeStart, length, largestSum, listOfLines):
# 	for s in xrange(rangeStart, length):
# 		largestSum += listOfLines[length-(1+s)][0]
# 	return largestSum

# def addAtPoslast(findMaxInlastlist, rangeStart, length, largestSum, listOfLines):
# 	for s in xrange(rangeStart, length):
# 		largestSum += listOfLines[length-(1+s)][len(listOfLines[length-(1+s)])-1]
# 	return largestSum