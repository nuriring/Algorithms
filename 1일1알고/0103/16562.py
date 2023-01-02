import sys
sys.stdin = open('16562.txt')

input = sys.stdin.readline

from collections import defaultdict
from collections import deque



def bfs(V):
    q = deque()
    q.append(V)
    visited[V] = 1
    min_cost = cost[V]
    while q:
        cs = q.popleft()
        if min_cost>cost[cs]:
            min_cost=cost[cs]
        for ce in graph[cs]:
            if visited[ce] == 0:
                q.append(ce)
                visited[ce] = 1
    return min_cost



N,M,k = map(int,input().split()) #N은 학생 수, M은 친구 관계 수, k는 가지고 있는 돈
cost = [0] + list(map(int,input().split()))
graph = defaultdict(list)
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
# print(graph)
visited = [0]*(N+1)

aws = 0 #친구비
for i in range(1,N+1):
    if visited[i] == 0:
        aws += bfs(i)

if aws>k:
    print("Oh no")
else:
    print(aws)

