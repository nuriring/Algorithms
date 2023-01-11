import sys

sys.stdin = open('1103.txt')
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [list(input().rstrip()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dp = [[0] * M for _ in range(N)]
flag = 0
ans = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


## 이게 왜 답이 안나오지 이건 진짜 모르겠다
# def dfs(x, y, cnt):
#     global ans
#     stack = [(x, y, cnt)]
#     while stack:
#         x, y, cnt = stack.pop()
#         visited[x][y] = 1
#
#         if ans < cnt:
#             ans = cnt
#         for k in range(4):
#             nx = x + dx[k] * int(arr[x][y])
#             ny = y + dy[k] * int(arr[x][y])
#             if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] != 'H' and cnt + 1 > dp[nx][ny]:
#                 if visited[nx][ny]:
#                     ans = -1
#                     return
#                 else:
#                     stack.append((nx, ny, cnt + 1))
#                     dp[nx][ny] = cnt + 1
# dfs(0,0,1)
# print(ans)
####################

###########
# def dfs(x, y, cnt):
#     global ans, flag
#
#     if ans < cnt:
#         ans = cnt
#
#     for k in range(4):
#         nx = x + dx[k] * int(arr[x][y])
#         ny = y + dy[k] * int(arr[x][y])
#         if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] != 'H' and cnt + 1 > dp[nx][ny]:
#             if visited[nx][ny]:
#                 flag = 1
#                 return
#
#             else:
#                 dp[nx][ny] = cnt + 1
#                 visited[nx][ny] = 1
#                 dfs(nx, ny, cnt + 1)
#                 visited[nx][ny] = 0
#
#     if flag:
#         return -1
#     else:
#         return ans
#
#
# print(dfs(0, 0, 1))
# print(dp)
###############

########### 정말 다양한 방식으로 나타낼수 있음
def dfs(x, y, cnt):
    global ans, flag

    if ans < cnt:
        ans = cnt

    for k in range(4):
        nx = x + dx[k] * int(arr[x][y])
        ny = y + dy[k] * int(arr[x][y])
        if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] != 'H' and cnt + 1 > dp[nx][ny]: #여기서 이 마지막이 중요한거임 더 큰 경우일 때만 검사함으로써 시간을 절약할수 있음
            if visited[nx][ny]: #무한루프발생
                flag = 1
                return

            else:
                dp[nx][ny] = cnt + 1
                visited[nx][ny] = 1
                dfs(nx, ny, cnt + 1)
                visited[nx][ny] = 0

dfs(0,0,1)
if flag: print(-1)
else:
    mmax = 0
    for i in range(N):
        mmax = max(mmax, max(dp[i]))
    print(mmax)
############