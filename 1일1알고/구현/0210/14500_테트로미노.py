import sys
sys.stdin = open('14500.txt')

#회전 대칭 가능
#
dx = [0,1,0,-1]
dy = [1,0,-1,0]

history = []
# 산 모양 외 최대값
def dfs(x,y,ssum, cnt):
    global mmax
    if cnt==4:
        mmax = max(mmax,ssum)

        return
    for k in range(4):
        nx = x+dx[k]
        ny = y+dy[k]
        if 0<=nx<N and 0<=ny<M and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            dfs(nx,ny,ssum+arr[nx][ny], cnt+1)
            visited[nx][ny] = 0



# 산 모양 최대값
di = [0,0,-1]
dj = [1,-1,0]
def mount(x,y):



N,M = map(int,input().split()) #N이 세로 #M이가로
arr = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
print(arr)

mmax = 0
dfs(0,0,arr[0][0],1)
print(mmax)
print(visited)
