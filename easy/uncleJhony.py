for _ in xrange(input()): #testacases
	numOfSongs = input() #this line here is just to make online judge a fool
	songsUnsorted = map(int, raw_input().split())# takes input of songs
	uncleJhonyPosInSongsUnsorted = input()# position of UJ song in the playlist
	uJinUnsorted = songsUnsorted[uncleJhonyPosInSongsUnsorted-1]# finds pos of UJ in unsorted list
	songsUnsorted.sort()# sorted the list
	print ((songsUnsorted.index(uJinUnsorted))+1)# prints out the new pos of UJ song
