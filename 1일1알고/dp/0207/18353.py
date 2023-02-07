
N = int(input())
arr = list(map(int,input().split()))
dp = [1]*N
#가장 긴 감소하는 부분수열
for i in range(N):
    for j in range(i):
        if arr[j]>arr[i]:
            dp[i] = max(dp[j]+1, dp[i])
# print(dp)
print(N-max(dp))