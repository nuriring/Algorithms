import sys
sys.stdin = open('12865.txt')
input = sys.stdin.readline

N,K = map(int,input().split())
#[배낭무게, 배낭가치]
arr = [[0,0]] + [list(map(int,input().split())) for _ in range(N)]
#print(arr)
dp = [[0]*(1+K) for _ in range(1+N)]
#print(dp)

#i는 arr를 순회
for i in range(1,N+1):
    # j는 최대 무게 K를 순회
    for j in range(1,K+1):
        # 현재 arr 물건을 실을 수 있을 때
        if j>=arr[i][0]: #담을 수 있는 무게라면
            #dp[i-1][j] : 실을 수 있는 무게 가치의 최대값(한 행 전)
            #dp[i-1][j-arr[i][0]] : 현재 물건에서 실으려고하는 무게를 빼줬을 때 최대가치
            #arr[i][1] : 현재 물건 가치
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-arr[i][0]] + arr[i][1])
        #실을 수 없을 때 한 행 위 값을 넣음( 실을 수 있는 무게 가치의 최대값)
        else:
            dp[i][j] = dp[i-1][j]
# 가장 끝에 있는 값이 최대 실을 수 있는 무게의 가치 최대 값
print(dp[N][K])
