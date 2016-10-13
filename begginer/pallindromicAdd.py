def main():
	t = input()

	while t:
		s = 0
		start, end = map(int, raw_input().split())
		for number in range(start, end+1):
			if ifPallindrome(number):
				s = s+number


		print s

		t-=1


def ifPallindrome(number):
	i = False
	if str(number) == (str(number))[::-1]:
		i = True
	return i 

main()
