import sys
sys.stdin = open('3109.txt')
from pprint import pprint
input = sys.stdin.readline

R,C = map(int,input().split())

arr = [list(input().rstrip()) for _ in range(R)]
cnt = 0
#print(arr)

dx = [-1,0,1]
dy = [1,1,1]

def check(nx,ny):
    if 0<=nx<R and 0<=ny<C and arr[nx][ny] == 'x':
        return False
    return True

def dfs(x,y):
    global cnt
    # print(arr)
    # if y==C-1:
    #     cnt += 1
    #     return
    # else:
    # pprint(arr)
    for k in range(3):
        nx = x+dx[k]
        ny = y+dy[k]
        if 0<=nx<R and 0<=ny<C:
            if ny==C-1:
                cnt += 1
                return 1
            else:
                if check(nx,ny):
                    arr[nx][ny] = 'x'  # 방문 표시, 따로 배열을 안만들어주는 이유는 한번 갔던 길은 이미 유망성이 낮기 때문
                    is_arrive = dfs(nx, ny)  # 다음 위치로 이동 #재귀호출 사용
                    if is_arrive:
                        return 1
    return 0

for r in range(R):
    dfs(r,0)
print(cnt)
# pprint(arr)