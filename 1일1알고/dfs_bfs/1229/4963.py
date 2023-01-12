import sys
sys.stdin = open('4963.txt')
from collections import deque

#배추에서 검사범위를 대각선도 해주면됨

def bfs(i,j):
    q = deque()
    q.append((i,j))
    visited[i][j] = 1
    while q:
        i,j = q.popleft()
        for di,dj in [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]:
            ni,nj = i+di, j+dj
            if 0<=ni<h and 0<=nj<w and visited[ni][nj] == 0 and arr[ni][nj] == 1:
                q.append((ni,nj))
                visited[ni][nj] = 1


while True:
    w,h = map(int,input().split()) #지도의 너비와 높이
    # [list(map(int, input().split())) for _ in range(N)]
    arr = [list(map(int,input().split())) for _ in range(h)]
    visited = [[0]*w for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1 and visited[i][j] == 0:
                bfs(i,j)
                cnt+=1
    if (w,h) == (0,0):
        break
    print(cnt)


