import sys
sys.stdin = open('2583.txt')
from pprint import pprint
from collections import deque

def bfs(i,j):
    q = deque()
    q.append((i,j))
    visited[i][j] = 1
    area = 1 #한칸이라도 있으면 1이니까
    while q:
        i,j = q.popleft()
        for di,dj in [(0,1),(1,0),(0,-1),(-1,0)]:
            ni,nj = i+di, j+dj
            if 0<=ni<M and 0<=nj<N and visited[ni][nj] == 0 and arr[ni][nj] == 0:
                q.append((ni,nj))
                area +=1
                visited[ni][nj] = 1

    return area


M,N,K = map(int,input().split()) #M은 높이, N은 너비, K는 직사각형 갯수
arr = [[0]*N for _ in range(M)]
visited = [[0]*N for _ in range(M)]
for _ in range(K):
    lx,ly,rx,ry = map(int,input().split())
    for i in range(ly,ry):
        for j in range(lx,rx):
            arr[i][j] = 1
cnt = 0
res = []
for x in range(M):
    for y in range(N):
        if arr[x][y] == 0 and visited[x][y] == 0:
            res.append(bfs(x,y))
            cnt +=1

print(cnt)
print(*sorted(res))

