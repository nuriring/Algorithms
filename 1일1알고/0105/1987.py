import sys
sys.stdin = open('1987.txt')
from collections import deque
from collections import defaultdict
input = sys.stdin.readline


def bfs(i,j,check):

    q = set([(i,j,check)]) #중복 알파벳을 제거해주기위해 set 활용
    answer = 1


    while q:
        i,j,check = q.pop()

        answer = max(answer, len(check)) #가장 길이가 긴 경로를 찾아야하므로

        for di,dj in [(0,1),(1,0),(0,-1),(-1,0)]:
            ni,nj = i+di, j+dj
            if 0<=ni<R and 0<=nj<C and arr[ni][nj] not in check: #범위를 안 벗어나고 이때까지 걸어온길과 중복되지 않으면
                q.add((ni,nj,check+arr[ni][nj])) #큐자체에 걸어온길을 넣어주는게 핵심 해결법

    return answer #더이상 갈곳이 없으면 answer를 반환


R,C = map(int,input().split())
arr = list(input().rstrip() for _ in range(R))


print(bfs(0,0,arr[0][0]))


