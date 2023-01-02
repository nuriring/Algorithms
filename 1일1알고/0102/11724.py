
import sys
sys.stdin = open('11724.txt')

input = sys.stdin.readline

from collections import defaultdict
from collections import deque


def bfs(V):
    q = deque()
    q.append(V)
    visited[V] = 1
    while q:
        cs = q.popleft()
        for ce in graph[cs]:
            if visited[ce] == 0:
                q.append(ce)
                visited[ce] = 1

N,M = map(int,input().split())
graph = defaultdict(list)
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
# print(graph)

cnt = 0
visited = [0]*(N+1)
for i in range(1,N+1):
    if visited[i] == 0:
        bfs(i)
        cnt +=1
print(cnt)