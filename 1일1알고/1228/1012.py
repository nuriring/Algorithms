import sys
sys.stdin = open('1012.txt')


from collections import deque

def bfs(i,j):
    q = deque()
    q.append((i,j))
    visited[i][j] = 1

    while q:
        i,j = q.popleft()
        for di,dj in [(0,1),(1,0),(0,-1),(-1,0)]:
            ni = i+di
            nj = j+dj
            if 0<=ni<x and 0<=nj<y and visited[ni][nj] == 0 and arr[ni][nj] == 1:
                q.append((ni,nj))
                visited[ni][nj] = 1






T = int(input())
for tc in range(T):
    x,y,baechoos = map(int,input().split())
    arr = [[0]*y for _ in range(x)]
    visited = [[0]*y for _ in range(x)]
    # print(arr)
    for baechoo in range(baechoos): #배추심기
        i,j = map(int,input().split())
        arr[i][j] = 1

    cnt = 0
    for i in range(x):
        for j in range(y):
            if arr[i][j] == 1 and visited[i][j] == 0: #여기서 방문배열체크이 필요한가? 안전영역이랑 똑같음 다른 배추 영역 검사할때 이전 영역 검사 막음
                bfs(i,j)
                cnt +=1
    print(cnt)



