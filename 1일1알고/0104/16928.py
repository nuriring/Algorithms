#
#
#
# import sys
#
# from collections import deque
# from collections import defaultdict
# input = sys.stdin.readline
# graph = defaultdict(int)
#
#
# def bfs(V):
#
#     q = deque()
#     q.append(V)
#     visited[V] = 1
#     next_node = []
#     while q:
#         flag = False
#         cs = q.popleft()
#         if cs == 100:
#             return
#         for i in range(1,7):
#             next_node.append(cs+i)
#         if graph[cs]:
#             next_node.append(graph[cs])
#             flag = True
#
#         for ce in next_node:
#             if 1 <= ce <= 100 and visited[ce] == 0:
#                 q.append(ce)
#                 if flag:
#                     visited[ce] = visited[cs]
#                 if not flag:
#                     visited[ce] = visited[cs] + 1
#
#
#
#
#
# N,M = map(int,input().split())
# #N은 사다리수, M은 뱀의 수
# for _ in range(N):
#     x,y = map(int,input().split())
#     graph[x] = y #단방향
#
# for _ in range(M):
#     u,v = map(int,input().split())
#     graph[u] = v  #단방향
#
# print(graph)
#
# visited = [0]*101
#
# bfs(1)
# print(visited[100]-1)


import sys
sys.stdin = open('16928.txt')

from collections import deque
from collections import defaultdict

input = sys.stdin.readline
graph = defaultdict(int)


def bfs(V):
    q = deque()
    q.append(V)
    visited[V] = 1
    while q:
        cs = q.popleft()
        if cs == 100:
            return
        else:
            for i in range(1, 7):
                ce = cs + i

                if 1 <= ce <= 100 and visited[ce] == 0: #여기서 방문체크는 안해도되네
                    if graph[ce]: #뱀이나 사다리가 있으면
                        ce = graph[ce] #도착점위치를 바로 이동한 값으로 바꾸어준다

                    if visited[ce] == 0: #q에 값을 추가해주는 건 한번만
                        q.append(ce)
                        visited[ce] = visited[cs] + 1





N,M = map(int,input().split())
#N은 사다리수, M은 뱀의 수
for _ in range(N):
    x,y = map(int,input().split())
    graph[x] = y #단방향

for _ in range(M):
    u,v = map(int,input().split())
    graph[u] = v  #단방향

# print(graph)

visited = [0]*101


bfs(1)
print(visited[100]-1) #처음에 주사위 던진 값은 빼줘야함




