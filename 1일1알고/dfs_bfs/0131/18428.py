import sys
import copy
sys.stdin = open('18428.txt')
input = sys.stdin.readline
from itertools import combinations
N = int(input())
arr = [list(input().split()) for _ in range(N)]
# print(arr)
arr_for_comb = []

dx = [0,1,0,-1]
dy = [1,0,-1,0]

#학생 다 살아남는지 check
# def check(x,y,arr):
#     tmp_x=x
#     tmp_y=y
#     global possible
#     #네방향검사시작
#     for k in range(4):
#         flag = False #장애물 여부
#         x,y = tmp_x,tmp_y
#         while 0<=x<N and 0<=y<N: #범위를 벗어나지 않으면 반복 한방향 계속확인
#             x = x + dx[k]
#             y = y + dy[k]
#             if 0<=x<N and 0<=y<N and arr[x][y] == 'O':
#                 flag = True
#             if 0<=x<N and 0<=y<N and arr[x][y] == 'S' and not flag: #한번이라도 장애물 없이 학생이 보이면
#                 possible = False
#                 return


def check(x,y,arr):
    global possible
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 직선 방향으로 확인
        while 0<= nx < N and 0<= ny < N and arr[nx][ny] !='O':
            if arr[nx][ny] == 'S':
                possible = False
                return
            else:
                # T 나 X으면 계속 탐색
                nx += dx[i]
                ny += dy[i]

def check(x,y,arr):
    global possible
    #네방향검사시작
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        flag = False #장애물 여부
        while 0<=nx<N and 0<=ny<N: #범위를 벗어나지 않으면 반복 한방향 계속확인

            if arr[nx][ny] == 'O':
                flag = True
            if arr[nx][ny] == 'S' and not flag: #한번이라도 장애물 없이 학생이 보이면
                possible = False
                return
            nx += dx[k] #한방향으로 계속이동
            ny += dy[k]



#장애물 놓을 수 있는 자리 찾기
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'X':
            arr_for_comb.append((i,j))
res = 'No'
for comb in combinations(arr_for_comb,3):
    # print(comb) #((4, 1), (4, 3), (4, 4))
    #comb마다 검사
    #arr초기화
    copy_arr = copy.deepcopy(arr) #얕은복사를 하면 배열을 변화시킬 때 원본에 영향을 미침
    copy_arr[comb[0][0]][comb[0][1]] = 'O'
    copy_arr[comb[1][0]][comb[1][1]] = 'O'
    copy_arr[comb[2][0]][comb[2][1]] = 'O'
    #장애물 세개를 놓을 수 있는 케이스마다 검사를 할거야
    possible = True
    #모든 선생에 대해 다 검사해
    for i in range(N):
        for j in range(N):
            if copy_arr[i][j] == 'T':
                check(i,j,copy_arr)
    #모든 선생에 대해 다 검사가 끝났어
    if possible:
        res = 'Yes'
        break

print(res)