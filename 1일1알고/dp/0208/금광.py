import sys
sys.stdin = open('금광.txt')

input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N,M = map(int,input().split())
    arr = list(map(int,input().split()))
    dp = [[0]*(M+1)]
    for i in range(N):
        dp.append([0]+arr[M*i:M*(i+1)])
    dp.append([0]*(M+1))
    # print(dp)
    for j in range(1,M+1):
        for i in range(1,N+1):
            dp[i][j] = max(dp[i][j], dp[i][j]+dp[i-1][j-1], dp[i][j]+dp[i][j-1], dp[i][j]+dp[i+1][j-1])

    # print(dp)
    ans = 0
    for i in dp:
        # print(i)
        ans = max(ans,i[-1])
    print(ans)


import sys
for tc in range(int(input())):
    n,m = map(int,input().split())
    array = list(map(int,input().split))

    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index+m])
        index +=m

    for j in range(1,m):
        for i in range(n):
            #맨 윗자리 -> 왼쪽 위에서 오는 값 없음
            if i==0 :
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            #맨 아랫자리 -> 왼쪽 아래에서 오는 값 없음
            if i==n-1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]
            left = dp[i][j-1]
            dp[i][j] = dp[i][j] + max(left,left_down,left_up)
    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])
    print(result)