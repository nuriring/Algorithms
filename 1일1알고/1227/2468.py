import sys
sys.stdin = open('2468.txt')

from collections import deque


# def findMax(N):
#     global mmax
#     for i in range(N):
#         for j in range(N):
#             if map[i][j]>=mmax:
#                 mmax=map[i][j]
#     return mmax
#
#
#
# def bfs(i,j,height,visited):
#     global cnt
#     queue = deque()
#     queue.append((i,j))
#
#     visited[i][j] = 1
#
#     while queue:
#         i,j = queue.popleft()
#         for di,dj in [[0,1],[1,0],[0,-1],[-1,0]]:
#             ni,nj = i+di, j+dj
#             if 0<=ni<N and 0<=nj<N and map[ni][nj] > height and visited[ni][nj] == 0:
#                 visited[ni][nj] = 1
#                 queue.append((ni,nj))
#
#
#
#
#
#
# N = int(input())
# map = [list(map(int,input().split())) for _ in range(N)]
# mmax = 0
# maxHeight = findMax(N)
# # print(maxHeight)
#
# #maxHieght까지 안전영역을 찾으면서 반복문으로 하나씩 높이면서 찾으면서
# #최대갯수를 갱신
#
# #반복문 안에서
# #높이마다 안전영역 세팅
# max_ans = 0
#
# for height in range(1,maxHeight+1):
#     visited = [[0]* N for i in range(N)]
#
#     cnt = 0
#     for i in range(N):
#         for j in range(N):
#             if map[i][j] > height and visited[i][j] == 0: #더 높은 위치고 방문안했으면 안전영역이면
#                 bfs(i,j,height, visited)
#                 cnt += 1
#
#
#     if max_ans<=cnt:
#         max_ans=cnt
#
# print(max_ans)




def findMax(N):
    x = 0 #전역변수를 쓸 이유가 전혀없지요
    for i in range(N):
        for j in range(N):
            if arr[i][j]>x:
                x=arr[i][j]
    return x



def bfs(i,j):
    queue = deque()
    queue.append((i,j))

    visited[i][j] = 1

    while queue:
        i,j = queue.popleft()
        for di,dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni,nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] > height and visited[ni][nj] == 0: #안전영역이고 방문한적 없으면 #하나의 안전영역 안에서 중복검사 방지
                visited[ni][nj] = 1
                queue.append((ni,nj))






N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
maxHeight = findMax(N)
# print(maxHeight)

#maxHieght까지 안전영역을 찾으면서 반복문으로 하나씩 높이면서 찾으면서
#최대갯수를 갱신

#반복문 안에서
#높이마다 안전영역 세팅
max_ans = 0

for height in range(maxHeight+1):
    visited = [[0]* N for i in range(N)]

    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > height and visited[i][j] == 0: #더 높은 위치고 방문안했으면 안전영역이면 #안전영역 갯수 늘어날때마다 이미 검사한 안전영역 못하게
                bfs(i,j)
                cnt += 1


    if max_ans<=cnt:
        max_ans=cnt

print(max_ans)