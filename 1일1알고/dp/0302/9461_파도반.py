import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    dp = [0]*101
    N = int(input())
    for i in range(3):
        dp[i] = 1
    dp[3],dp[4] = 2,2
    dp[5] = 3
    for i in range(6,N+1):
        dp[i] = dp[i-5] + dp[i-1]
    print(dp[N-1])
