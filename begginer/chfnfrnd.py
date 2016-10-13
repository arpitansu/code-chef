def main():
	t = input()

	while t:
		noOfFrnds, pairs = map(int,raw_input().split())

		listOfPairs = []

		for i in range(0,pairs):
			listOfPairs.append(raw_input().split())

		print listOfPairs


		t-=1
main()