import sys
sys.stdin = open('2565.txt')

N = int(input())
bolt_line = []
for _ in range(N):
    bolt_line.append(list(map(int,input().split())))
# print(bolt_line)

dp = [1]*N
bolt_line.sort(key=lambda x:x[0])
print(bolt_line)
for i in range(N):
    for j in range(i):
        if bolt_line[i][1] > bolt_line[j][1]:
            dp[i] = max(dp[j]+1, dp[i]) #기존에 잇던거랑 이전에 체크한 수의 dp에 1더한거랑 max비교

print(dp)
print(N-max(dp))
