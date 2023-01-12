import sys
sys.stdin = open('3109.txt')
from pprint import pprint
input = sys.stdin.readline

# R,C = map(int,input().split())
#
# arr = [list(input().rstrip()) for _ in range(R)]
# cnt = 0
#
# dx = [-1,0,1]
# dy = [1,1,1]
#
# def check(nx,ny):
#     if 0<=nx<R and 0<=ny<C and arr[nx][ny] == 'x':
#         return False
#     return True
#
# def dfs(x,y):
#     global cnt
#
#     for k in range(3):
#         nx = x+dx[k]
#         ny = y+dy[k]
#         if 0<=nx<R and 0<=ny<C:
#             if ny==C-1:
#                 cnt += 1
#                 return 1 #도착했다는 사실을 알려주는 지표
#             else:
#                 if check(nx,ny):
#                     arr[nx][ny] = 'x'  # 방문 표시, 못가는 건물로 만들기
#                     is_arrive = dfs(nx, ny)  # 다음 위치로 이동 #재귀호출 사용
#                     if is_arrive:
#                         return 1 #이게 있어야 반복문이 더 돌지 않고 스택이 종료되고 다음 행에서 함수를 시행함
#
#
# for r in range(R):
#     dfs(r,0)
# print(cnt)

R, C = map(int, input().split())
data = [list(input()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]
dx = [1, 0, -1]
dy = [1, 1, 1]
ans = 0


def dfs(x, y):
    global ans
    stack = [(x, y)]
    while stack:
        x, y = stack.pop()
        visited[x][y] = 1
        if y == C - 1:
            ans += 1
            return
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and data[nx][ny] == '.' and visited[nx][ny] == 0:
                stack.append((nx, ny))


for i in range(R):
    dfs(i, 0)
print(ans)