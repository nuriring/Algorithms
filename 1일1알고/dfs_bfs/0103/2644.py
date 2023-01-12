import sys
sys.stdin = open('2644.txt')
input = sys.stdin.readline

from collections import defaultdict
from collections import deque

def bfs(V):
    q = deque()
    q.append(V)
    visited[V] = 0
    while q:
        cs = q.popleft()
        if cs == M:
            return
        for ce in graph[cs]:
            if visited[ce] == -1 :
                q.append(ce)
                visited[ce] = visited[cs] + 1





people = int(input()) #사람수
N,M = map(int,input().split()) #촌수를 구해야하는 관계
relation = int(input()) #관계를 나타내는 갯수
graph = defaultdict(list)
visited = [-1]*(people+1)

for _ in range(relation):
    a,b = map(int,input().split())
    graph[a].append(b) #양방향? 단방향?
    graph[b].append(a)
bfs(N)
print(visited[M])



