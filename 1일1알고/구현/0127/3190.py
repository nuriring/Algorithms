import sys
sys.stdin = open('3190.txt')
input = sys.stdin.readline
from collections import defaultdict
from collections import deque

from collections import Counter
test = [1,2,3,2]
counter = Counter(test)
print(counter) #Counter({2: 2, 1: 1, 3: 1})
print(counter[2]) #2


def turn_right(now_d):
    if now_d == 3:
        return 0
    else:
        return now_d+1

def turn_left(now_d):
    if now_d == 0:
        return 3
    else:
        return now_d-1



spin_info = defaultdict(str)
N = int(input()) #N*N크기의 보드
apple = int(input())
arr = [[0]*N for _ in range(N)]
for _ in range(apple):
    apple_x, apple_y = map(int,input().split())
    arr[apple_x-1][apple_y-1] = 1 #1은 사과
L = int(input()) #방향 회전 정보 갯수
for _ in range(L):
    sec, d = input().split()
    spin_info[int(sec)] = d #spin정보를 딕트에 담음
print(spin_info)
dx = [0,1,0,-1] #우하좌상
dy = [1,0,-1,0]
# print(arr)
cnt = 0

#꼬리를어떻게 찾지?
#큐가 왜있겠니
#큐에 제일 처음 넣어준게 꼬리 역할을 하는 것이다

def game(x,y):
    q = deque()
    global cnt
    direction = 0
    arr[x][y] = 2
    q.append((x,y))
    # tmp_x, tmp_y = x, y
    # tmp_direction = direction
    while True:
        cnt += 1 #한번 반복할때마다 1초씩 흐름
        nx = x+dx[direction]
        ny = y+dy[direction]
        if nx<0 or nx>N-1 or ny<0 or ny>N-1 or arr[nx][ny] == 2: #벽이거나 뱀몸(2)이면
            #게임끝
            return
        else:
            if arr[nx][ny] == 1: #사과면
                q.append((nx, ny))
                arr[nx][ny] = 2 #뱀몸으로 바꿈
                x,y = nx,ny

            else:

                # arr[tmp_x][tmp_y] = 0 #초기화 #처음으로 사과가 아닐때 꼬리를 기억했다가 줄여야함
                # tmp_x = tmp_x+dx[direction]
                # tmp_y = tmp_y+dy[direction]
                tmp_x,tmp_y = q.popleft()
                arr[tmp_x][tmp_y] = 0 #꼬리초기화
                q.append((nx,ny))
                arr[nx][ny] = 2 #뱀몸으로 바꿈
                x,y = nx,ny

        if cnt in spin_info.keys():
            if spin_info[cnt] == 'D':
                direction = turn_right(direction)
            else:
                direction = turn_left(direction)

game(0,0)
print(cnt)
