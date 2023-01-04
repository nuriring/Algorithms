


import sys

from collections import deque
from collections import defaultdict
sys.stdin = open('16928.txt')
input = sys.stdin.readline
graph = defaultdict(int)


def bfs(V):

    q = deque()
    q.append(V)
    visited[V] = 1
    next_node = []
    while q:
        flag = False
        cs = q.popleft()
        if cs == 100:
            return
        for i in range(1,7):
            next_node.append(cs+i)
        if graph[cs]:
            next_node.append(graph[cs])
            flag = True

        for ce in next_node:
            if 1 <= ce <= 100 and visited[ce] == 0:
                q.append(ce)
                if flag:
                    visited[ce] = visited[cs]
                if not flag:
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
print(visited[100]-1)


