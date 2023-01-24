import sys
sys.stdin = open('18405.txt')
from collections import deque

di = [-1,1,0,0]
dj = [0,0,-1,1]

def bfs(i,j,virus):
    q = deque()
    q.append((i,j,virus))

    # visited[i][j] = virus
    while q:
        i,j,virus = q.popleft()
        for k in range(4):
            ni = i+di[k]
            nj = j+dj[k]
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 0: #바이러스가 없을때
                arr[ni][nj] = virus
                q.append((ni,nj,virus))

        return
            # elif 0<=ni<N and 0<=nj<N and virus>arr[ni][nj]:
            #     visited[ni][nj] = virus



#처음에방문표시
#바이러스 한번 퍼뜨림 근데 상하좌우로한번만 1초에 낮은순서대로 차례대로
#그 뒤 반복인데
#근데 더 안퍼뜨리고 상하좌우 한번...



N,K = map(int,input().split()) #1~K번 바이러스
arr = [list(map(int,input().split())) for _ in range(N)]
S,X,Y = map(int,input().split())

visited = [[0]*N for _ in range(N)]
print(arr)

def check(N):
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and arr[i][j] != 0: #바이러스가 있다면 증식
                visited[i][j] = 1
                virus_list.append((i,j,arr[i][j]))


    virus_list.sort(key=lambda x:x[2]) #낮은번호순으로 증식

# print(virus_list)
# cnt = 0
# for i in virus_list:
#     bfs(i[0],i[1],i[2])

second = 0
while second<S:
    virus_list = []
    check(N)
    for i in virus_list:
        bfs(i[0],i[1],i[2])
    second += 1

print(visited)
print(arr)
print(arr[X-1][Y-1])