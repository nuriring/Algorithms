import sys
sys.stdin = open('1932.txt')

input = sys.stdin.readline

N = int(input())
#0 패딩
arr=[[0,0]]+[[0]+list(map(int,input().split()))+[0] for _ in range(N)]
# print(arr)
# dp = []
# for k in range(2,N+3):
#     dp.append([0]*k)
# print(dp)

for i in range(1,N+1):
    for j in range(1,i+1):
        arr[i][j] = max(arr[i-1][j-1]+arr[i][j],arr[i-1][j]+arr[i][j])
# print(arr)
print(max(arr[-1]))