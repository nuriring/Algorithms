n = int(input())
score = [0]*301
for i in range(n):
    score[i] = int(input())
# print(score)
d = [0]*301
d[0] = score[0]
d[1] = score[0]+score[1]
d[2] = max(score[0]+score[2], score[1]+score[2])
for i in range(3,n):
    d[i] = max(score[i]+d[i-2], score[i]+score[i-1]+d[i-3])
print(max(d))
