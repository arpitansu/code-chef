# long maxLR = 0;
# long maxR = 0;
# int ans = 0;
# for (int i = 1; i <= L.length; i++) {
#     if (L[i] * (long) R[i] > maxLR) {
#         maxLR = L[i] * (long) R[i];
#         maxR = R[i];
#         ans = i;
#     } else if (L[i] * (long) R[i] == maxLR) {
#         if (R[i] > maxR) {
#             maxR = R[i];
#             ans = i;
#         }
#     }

for rounds in range(input()):
    n= input()
    
    l= map(int, raw_input().split())

    r= map(int, raw_input().split())

    maxlr= 0
    index= 0
    
    for i in range(n):
        if l[i] * r[i] > maxlr :
            maxlr = l[i] * r[i]
            index = i
        
        elif l[i] * r[i] == maxlr :
            if r[i] > r[index]:
                index = i
                
    print index+1 