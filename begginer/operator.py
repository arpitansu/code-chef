def main():
	t = input()

	while t:
		s = 0
		first, second = map(int, raw_input().split())
		operator = findOperator(first, second)
		print operator

		t-=1

def findOperator(first, second):
	if first > second:
		return '>'
	elif second > first:
		return '<'
	else:
		return '='

main()
