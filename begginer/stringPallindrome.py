def pallindrome(a,b):
	foo = 0
	for i in range(0, len(b)):
		if b[i] in a[:]:
			foo = 1

	return foo




def main():
	t = input()
	# t = int(t)

	while t:
		a = raw_input()
		b = raw_input()
		try:
			check = pallindrome(a,b)
			if check:
				print('Yes')
			else:
				print('No')
		except:
			return 0
		t-=1

# if __name__=='__main__':
main()