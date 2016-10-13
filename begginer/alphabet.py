def main():
	words = raw_input()
	toSet = ()
	for letter in range(0,len(words)):
		toSet += letter
	t = input()
	while t:
		newWord = raw_input()
		try:
			check = toCheck(words,toSet)
			if check:
				print('Yes')
			else:
				print('No')
		except:
			return 0 		
		t-=1

def toCheck(words,toSet):
	foo = 0
	for i in range(0,len(words)):
		if words[i] in toSet:
			foo = 1
			break
	return foo
		
main()