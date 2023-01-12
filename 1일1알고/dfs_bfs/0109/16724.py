import sys
from pprint import pprint

sys.stdin = open("16724.txt")

input = sys.stdin.readline

# N, M = map(int, input().split())
# # arr = [input().rstrip() for _ in range(N)]
# table = []
# for _ in range(N):
#     table.append([x for x in input().rstrip()])
# visited = [[0] * M for _ in range(N)]
# print(table)
#
#
# direction = ['L','R','U','D']
# dx = [0,0,-1,1]
# dy = [-1,1,0,0]
#
#
# def dfs(i, j, idx):
#     global answer
#     if visited[i][j] != 0:
#         if visited[i][j] == idx: #cycle
#             answer += 1
#         return
#     visited[i][j] = idx
#     number = direction.index(table[i][j])
#     print(number)
#     dfs(i+dx[number], j+dy[number], idx)
#
#
#
#
# idx = 0
# cnt = 0
# for i in range(N):
#     for j in range(M):
#         dfs(i,j,idx)
#         idx += 1
#
#
#             # cnt += 1
# print(answer)
# # print(visited)
x_lim, y_lim = map(int,input().split())
table = []
for _ in range(x_lim):
    table.append([x for x in input()])
print(table)
visited = [[-1] * y_lim for _ in range(x_lim)]
print(visited)
direction = ['L','R','U','D']
dx = [0,0,-1,1]
dy = [-1,1,0,0]
def move(x,y,idx):
    global answer
    if visited[x][y] != -1: #깊이 탐색을 하다가 방문한적이 있다면
        if visited[x][y] == idx: #방문한적이 있고 새로운 사이클이라면 #그니까 idx값이 유지된채로 재방문해야 사이클로 보는거구나
            answer +=1
        return #재방문했을 때 함수종료해주고 idx값 변경
    visited[x][y] = idx #사용할 idx를 가지고 방문표시
    i = direction.index(table[x][y])
    print(i)
    move(x+dx[i], y+dy[i], idx)

idx = 0
answer = 0
for i in range(x_lim):
    for j in range(y_lim):
        move(i,j,idx)
        idx+=1 #계속 idx값을 변경해줘야 새로운 사이클 생성시 지표가됨
print(answer)