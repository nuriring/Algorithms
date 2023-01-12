import sys
sys.stdin = open('17265.txt')
# def findMax(number):
#     mmax = 0
#     if number>mmax:
#         number = mmax
#     return number
#
# def findMin(number):
#     mmin = 11111111
#     if number<mmin:
#         number = mmin
#     return number
#
#
# def bfs(i,j,N):
#
#     visited = [[0]*N for _ in range(N)]
#     queue = []
#     num = []
#     queue.append((i,j))
#     num.append(int(map[i][j]))
#     visited[i][j] = 1
#     while queue:
#         i, j = queue.pop(0)
#         if (i,j) == (N,N):
#             min_ans = findMin(visited[i][j])
#             max_ans = findMax(visited[i][j])
#             return min_ans, max_ans
#         for di,dj in [[0,1],[1,0]]:
#
#
#
#             ni,nj = i+di, j+dj
#             if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0:
#                 if map[ni][nj] in operator:
#
#                     if map[ni][nj] == '+':
#                         queue.append((ni,nj))
#                         before_num = num.pop()
#                         flag = 0
#
#                     if map[ni][nj] == '-':
#                         queue.append((ni, nj))
#                         before_num = num.pop()
#                         flag = 1
#                     if map[ni][nj] == '*':
#                         queue.append((ni, nj))
#                         before_num = num.pop()
#                         flag = 2
#                 else:
#                     num.append(int(visited[ni][nj]))
#                     queue.append((ni,nj))
#                     if flag == 0:
#                         visited[ni][nj] = before_num + int(visited[ni][nj])
#
#                     if flag == 1:
#                         visited[ni][nj] = before_num - int(visited[ni][nj])
#                     if flag == 2:
#                         visited[ni][nj] = before_num * int(visited[ni][nj])
#
#
# N = int(input())
# map = [list(input().split()) for _ in range(N)]
# print(map)
# operator = ['+','-','*']
# x,y = bfs(0,0,N)
#
# dx = [0,1]
# dy = [1,0]



def dfs(x,y,N,res,op):
    global mmax,mmin,operator
    if (x,y) == (N-1, N-1):
        # - 일떄 대소비교 때문인가..?
        # if res>0:
        if mmax<=res:
            mmax = res

        if res<mmin:
            mmin =res
        # else:
        #     if mmax<0:
        #         if abs(mmax)>=abs(res):
        #             mmax = res
        #     else:
        #         if mmax <= res:
        #             mmax = res
        #     if mmin<0:
        #         if abs(mmin)<abs(res):
        #             mmin = res
        #     else:
        #         if res<mmin:
        #             mmin = res


    else:

        for dx,dy in [[0,1],[1,0]]:
            nx = x+dx
            ny = y+dy
            if 0 <= nx < N and 0 <= ny < N:
                if map[nx][ny] in operator:
                    # print(map[nx][ny])
                    dfs(nx,ny,N,res,map[nx][ny])
                else:
                    if op == '+':
                        dfs(nx,ny,N,res+int(map[nx][ny]),op)
                    if op == '-':
                        dfs(nx, ny, N, res - int(map[nx][ny]), op)
                    if op == '*':
                        dfs(nx,ny,N,res*int(map[nx][ny]),op)




N = int(input())
map = [list(input().split()) for _ in range(N)]
mmax = -111111111
mmin = 1111111111
op=''
operator = ['+','-','*']
dfs(0,0,N,int(map[0][0]),op)
print(mmax,mmin)
