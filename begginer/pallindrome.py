def pallindrome(number):
	original = str(number)

	originalToInt = int(number)

	rev = ''

	for i in range(0, len(original)):
		rev+= str(number%10)
		number = int(number/10)
	return int(rev)

# print pallindrome(2345)
def check(number):
	original = str(number)
	try:
		if original[0] is '0':
			print ('losses')
		else:
			toPallindrome = pallindrome(number)
			if toPallindrome == number:
				print("wins")
			else:
				print('losses')
	except:
		return 0

# check(666)
def main():
	t = raw_input()
	t = int(t)

	while t:
		test = raw_input()
		test = int(test)
		check(test)
		t-=1

if __name__=='__main__':
	main()