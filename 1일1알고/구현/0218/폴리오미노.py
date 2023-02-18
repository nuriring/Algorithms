import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

for _ in range(5):
    board = list(input().rstrip())
    # print(board)
    cnt = 0
    idx = 0
    while True:
        if idx==len(board):
            break
        if board[idx] == 'X':
            cnt += 1
        else:
            cnt = 0

        if cnt!=0 and cnt %2 == 0:
            for i in range(idx-1,idx+1):
                board[i] = 'B'
        if cnt!=0 and cnt % 4 == 0:
            for j in range(idx-3, idx+1):
                board[j] = 'A'

        idx+=1
    if 'X' not in board:
        for i in board:
            print(i,end='')
    else:
        print(-1)
