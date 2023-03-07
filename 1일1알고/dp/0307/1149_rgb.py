
N = int(input())
dp = []
for _ in range(N):
    dp.append(list(map(int,input().split())))
#일단 dp에 다넣고
#두번째 집부터 만약에 이전에 해당색 말고 다른색중 적은 값을 칠한 경우를 반복문으로 돌려줌
for i in range(1,N):
    #해당색 r
    dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + dp[i][0]
    #g
    dp[i][1] = min(dp[i-1][0],dp[i-1][2]) + dp[i][1]
    #b
    dp[i][2] = min(dp[i-1][0],dp[i-1][1]) + dp[i][2]

#다 칠해보고 마지막에 제일 적은 경우를 출력하면됨
print(min(dp[-1]))
