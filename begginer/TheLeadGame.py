# def main():
# 	t = input()
# 	score1 = 0
# 	score2 = 0

# 	while t:
# 		player1, player2 = map(int, raw_input().split())

# 		if player1==player2:
# 			pass

# 		elif player1>player2:
# 			newScore = player1-player2
# 			if newScore>score1:
# 				score1 = newScore
# 		else:
# 			newScore = player2-player1
# 			if newScore > score2:
# 				score2 = newScore
# 		# if score1>score2:
# 		# 	print ("{} {}".format(name1,score1))
# 		# elif score2>score1:
# 		# 	print ("{} {}".format(name2,score2))

# 		t-=1
# 	if score1>score2:
# 		print ("%s %s" %(1,score1))
# 	else:
# 		print ("%s %s" %(2,score2))
# main()
import sys

rounds = int(sys.stdin.readline())

score = [0,0]
leads = [0,0]
while rounds > 0:
    results = map(int, sys.stdin.readline().split())
    score[0] += results[0]
    score[1] += results[1]
    lead = score[0] - score[1]
    if (lead < 0 and leads[1] < -lead): leads[1] = -lead
    if (lead > 0 and leads[0] < lead): leads[0] = lead
    rounds -= 1

if (leads[0] > leads[1]): print 1, leads[0]
else: print 2, leads[1]