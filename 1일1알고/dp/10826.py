n = int(input())
# dp = [0]*(n+1)
# dp[1] = 1
# dp[2] = 1
#
# for i in range(3,n+1):
#     dp[i] = dp[i-1] + dp[i-2]


if n<2:
    print(n)
else:
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 1
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    print(dp[n]%1000000)