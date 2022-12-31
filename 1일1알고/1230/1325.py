import sys
sys.stdin = open('1325.txt')

input = sys.stdin.readline

from collections import deque
from collections import defaultdict


#V는 탐색을 시작할 정점의 번호
def bfs(V):
    q = deque()
    q.append(V)
    visited[V] = True #방문표시
    cnt = 0
    while q:
        cs = q.popleft() #시작점빼기
        cnt +=1
        for ce in graph[cs]:

            #if graph[cs] and visited[ce] == 0:#한번더 검사할 필요가 없음
            if not visited[ce]:
                q.append(ce)
                visited[ce] = True

    return cnt


N,M = map(int,input().split())
graph = dict()

for _ in range(M):
    a, b = map(int,input().split())
    graph[b].append(a)

print(graph)
mmax = 0
lst = []
for num in range(1,N+1):
    if num in graph.keys():
        visited = [False] * (N + 1)
        sol = bfs(num)
        # print("난sol",sol)
        if mmax==sol:
            mmax = sol

            lst.append(num)
        if mmax<sol:
            mmax = sol
            lst = []
            lst.append(num)


print(*lst)
print(graph)
for key in graph.keys():
    print("key",key)

