N = int(input())  # 6
arr = [0]+list(map(int, input().split()))
dp = [0] * (N + 1)
for i in range(1, N + 1):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[j] + 1, dp[i])
        # else:
        #     dp[j] = dp[j-1]
print(max(dp))
