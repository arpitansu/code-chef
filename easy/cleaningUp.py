

# def assingment(numberOfJobs, numberOfjobList, jobsCompleted,jobsDone):
# 	for jobs in xrange(numberOfJobs): numberOfjobList+=str(jobs+1)
# 	for i in xrange(jobsDone): numberOfjobList.remove(jobsCompleted[i])
# 	return numberOfjobList

# def main():
# 	testcases = int(raw_input())
# 	for _ in  xrange(testcases):
# 		jobsCompleted = [] # list for job completed
# 		numberOfjobList = [] #create list of total jobs
# 		numberOfJobs, jobsDone = map(int, raw_input().split()) #n, m = 6, 3
# 		jobsCompleted = map(str, raw_input().split()) # m = 2,4,1
# 		numberOfjobList = assingment(numberOfJobs, numberOfjobList, jobsCompleted,jobsDone)
# 		for chefjob in range(0, len(numberOfjobList), 2): print (numberOfjobList[chefjob])
# 		print ('\n')
# 		for assistant in range(1, len(numberOfjobList), 2): print (numberOfjobList[assistant])
# main()
# from __future__ import print_function

# for _ in  xrange(input()):
# 	jobsCompleted = [] # list for job completed
# 	numberOfjobList = [] #create list of total jobs
# 	c = ''
# 	a = ''
# 	numberOfJobs, jobsDone = map(int, raw_input().split()) #n, m = 6, 3
# 	jobsCompleted = map(int, raw_input().split()) # m = 2,4,1

# 	for i in xrange(1,numberOfJobs+1):
# 		if (i) not in jobsCompleted:
# 			numberOfjobList+=str(i)
# 	numberOfjobList.sort()	

# 	for chefjob in range(0, len(numberOfjobList), 2): 
# 		c += (numberOfjobList[chefjob])+' '
# 	for assistant in range(1, len(numberOfjobList), 2): 
# 		a += (numberOfjobList[assistant])+' '
# 	print c
# 	print a

for _ in xrange(input()):
    a = map(int,raw_input().split())
    m = map(int,raw_input().split())
    b = list(range(1,a[0]+1))
    print a
    print m
    print b
    for i in range(a[1]):
        p=b.index(m[i])
        b.pop(p)
    b.sort()    
    C=""
    A=""
    for i in range(len(b)):
        if i%2==0:
            C += str(b[i])+" "
        else:
            A += str(b[i])+" "
    print C
    print A