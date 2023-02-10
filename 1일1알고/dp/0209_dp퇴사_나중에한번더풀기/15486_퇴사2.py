import sys
sys.stdin = open('15486.txt')
input = sys.stdin.readline

N = int(input())
arr = []
dp = [0] * (N+1)
for _ in range(N):
    cost, profit = map(int,input().split())
    arr.append((cost,profit))
print(arr)
# for i in range(N-1,-1,-1): #역순으로 진행
#     if i+arr[i][0] <= N: #i번째 일을 할 수 있다는 의미 퇴사전에
#         dp[i] = max(arr[i][1] + dp[i+arr[i][0]], dp[i+1])
#         #i번째 일을 할 수 있다면
#         # dp[i+arr[i][0]] : 해당 날에서 걸린 시간더한 날 만큼 지나치고 할수 있었던 최대값 dp에
#         # arr[i][1] i번째날 일할 수 있어서 얻을수 있는 이익을 더한 값과
#         # i번째날 일을  하지 않았을때 값인 i+1번째 dp값이랑 비교해서 더 큰 값
#     else:
#         dp[i] = dp[i+1]
#         #i번째에서 날짜를 초과한다고 해서 아무것도 안하는게 아니라 i+1번째 값을 복사해야함
# print(dp[0])

#본래순대로 푸는법
#이 문제는 각 날짜에서의 최대 수익을 dp배열을 생성하여
#dp[종료일] = max(이전까지의 수익+현재 수익, dp[종료일])을 계산함
for i in range(1,N+1):
    dp[i] = max(dp[i-1], dp[i]) #이전날짜와 비교해서 더큰 수익으로 갱신
    if i+arr[i-1][0] <= N+1: #7일째까지 일할수 있음
        #상담종료일의 최댓값도 갱신
        dp[i+arr[i-1][0]-1] = max(dp[i-1]+arr[i-1][1], dp[i+arr[i-1][0]-1])
print(dp)