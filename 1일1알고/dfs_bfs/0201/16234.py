import sys
from collections import deque
sys.stdin = open('16234.txt')
input = sys.stdin.readline
N,L,R = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

dx = [0,1,0,-1] #우하좌상 검사
dy = [1,0,-1,0]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    union = [(x,y)]
    count = arr[x][y]
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]

            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==0 and L <= abs(arr[x][y] - arr[nx][ny]) <= R:
                union.append((nx,ny))
                visited[nx][ny] = 1
                q.append((nx, ny))
                count += arr[nx][ny]
    #이 큐가 끝나면 해당bfs에서 이어진 연합국만 계산됨
    for x,y in union:
        arr[x][y] = count//len(union)
    # print(len(union))
    return len(union)


day = 0
while True:
    visited = [[0]*N for _ in range(N)]
    flag = False#인구이동을 계속할지 flag
    for i in range(N):
        for j in range(N):
            if visited[i][j]==0:
                if bfs(i,j)>1: #연합국이 2개이상이면,
                    flag = True

    if not flag:
        break
    day+=1


print(day)
