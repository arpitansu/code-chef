for _ in xrange(input()):
	notes, costOfSweet = map(int, raw_input().split())
	notesValue = map(int, raw_input().split())
	# print notesValue
	if len(notesValue) > notes:
		print -1

	else:
		s = 0
		for i in notesValue:
			s+=i
		throwAwaySum = s-min(notesValue)
		# print throwAwaySum
		if throwAwaySum/costOfSweet == s/costOfSweet:
			print -1
		else:
			print s/costOfSweet



# java solution
# -------------------------------
# import java.util.Arrays;
# import java.util.Scanner;
# public class Main {
#     public static void main(String[] args){
#         Scanner in = new Scanner(System.in);
#         int t = in.nextInt();
#          while (t !=0){
#             int noteCount = in.nextInt();
#             int cost = in.nextInt();
#             int[] notes = new int[noteCount];
#             int total = 0;
#             for (int i = 0 ; i < noteCount; ++i){
#                 notes[i] = in.nextInt();
#                 total+= notes[i];
#             }
#             Arrays.sort(notes); 
#              int ans = total/cost;
#              if((total-notes[0])/cost == ans)
#                  System.out.println(-1);
#              else
#                  System.out.println(ans);
#             t--;
#         }
#     }
# } 