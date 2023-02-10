import sys
sys.stdin = open('1103.txt')
input = sys.stdin.readline
N,M = map(int,input().split()) #N은 세로크기 M은 가로크기
arr = [list(input().rstrip()) for _ in range(N)]


dp = [[0]*(M) for _ in range(N)]
visited = [[0]*(M) for _ in range(N)]


dx = [-1,1,0,0]
dy = [0,0,-1,1]




def dfs(x, y, cnt):
    # print(visited)
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


ans = 0
flag = False
dfs(0,0,1)
# print(dp)
# print(ans)
print(dp)

if flag:
    print(-1)
else:
    print(ans)