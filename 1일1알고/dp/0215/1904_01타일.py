import sys


N = int(input())
dp = [0]*(N+1)
dp[0] = 1
dp[1] = 2

for i in range(2,N+1):
    #짝수면
    dp[i] = (dp[i-2] + dp[i-1])%15746
print(dp)
print(dp[N])