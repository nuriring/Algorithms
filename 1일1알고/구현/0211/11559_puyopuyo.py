import sys
sys.stdin = open('11559.txt')
from collections import deque
arr = [list(input()) for _ in range(12)]

# print(arr)

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(x,y,z):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    pang = [(x,y)]
    cnt = 1
    flag = 0
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x+ dx[k]
            ny = y+ dy[k]
            if 0<=nx<12 and 0<=ny<6 and arr[nx][ny] == z and visited[nx][ny] == 0:
                pang.append((nx,ny))
                visited[nx][ny] = 1
                q.append((nx,ny))
                cnt += 1
    if cnt>=4:
        flag = 1
        while pang:
            x,y = pang.pop()
            arr[x][y] = '.'
    return flag


def gravity():
    for j in range(6):
        q = deque()
        for i in range(11,-1,-1):
            if arr[i][j] != '.':
                q.append(arr[i][j])
        for k in range(11,-1,-1):
            if q:
                tmp = q.popleft()
                arr[k][j] = tmp
            else:
                arr[k][j] = '.'

result = 0
while True:
    check = 0
    for i in range(11,-1,-1):
        for j in range(6):
            if arr[i][j] != '.':
                visited = [[0] * 6 for _ in range(12)]
                check += bfs(i,j, arr[i][j])


    if check == 0: # 더이상 터뜨릴 뿌요 없다
        print(result)
        break
    else:
        result += 1
    gravity() #while문 안에서 반복문을 수행해줘야 제대로 연쇄횟수 카운트 가능 bfs뒤에 바로넣어버리면 최종 형태는 구할 수 있겠지만 바로 터져서 연쇄횟수 세기 어려움
