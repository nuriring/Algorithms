import sys
sys.stdin = open('1697.txt')

input = sys.stdin.readline

from collections import deque


def bfs(V):
    q = deque()
    q.append(V)
    visited[V] = 1

    while q:
        cs = q.popleft()
        if cs == M:
            return visited[cs]
        for ce in [cs-1, cs+1, cs*2]:
            if 0<=ce<=100000 and visited[ce] == 0:
                q.append(ce)
                visited[ce] = visited[cs] + 1


N,M = map(int,input().split()) #N은 수빈이의 위치, M은 동생의 위치
visited = [0]*100000

print(bfs(N))
