from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
board = [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]
N = len(board)
visited = []


def can_go(left, right):
    # 범위 내에 있고, 벽이 아니면 갈수 있다
    if 0 <= left[0] < N and 0 <= left[1] < N and 0 <= right[0] < N and 0 <= right[1] < N:
        return True
    return False


def spin(left, right):
    # 좌축 위아래 회전
    cleft = (left[0] + 1, left[1])
    cright = (right[0] + 1, right[1])
    if can_go(cleft, cright) and board[cleft[0]][cleft[1]] == 0 and board[cright[0]][cright[1]] == 0:
        return left, (right[0] + 1, right[1] - 1)


def get_next_position(left, right):
    next_pos = []
    (x1, y1) = (left[0], left[1])
    (x2, y2) = (right[0], right[1])
    # 상하좌우
    for k in range(4):
        nleft = (x1 + dx[k], y1 + dy[k])
        nright = (x2 + dx[k], y2 + dy[k])
        if can_go(nleft, nright) and board[nleft[0]][nleft[1]] == 0 and board[nright[0]][nright[1]] == 0:
            next_pos.append((nleft, nright))
    # 세로에서 가로 회전
    if y1 == y2:
        for i in [-1, 1]:
            n1 = ((x1, y1), (x1, y1 + i))
            n2 = ((x2, y2), (x2, y2 + i))
            if can_go(n1[0], n1[1]) or can_go(n2[0], n2[1]) and board[x1][y1 + i] == 0 and board[x2][y2 + i] == 0:
                next_pos.append(n1)
                next_pos.append(n2)
    # 가로에서 세로 회전
    if x1 == x2:
        for i in [-1, 1]:
            n1 = ((x1, y1), (x1 + i, y1))
            n2 = ((x2, y2), (x2 + i, y2))
            if can_go(n1[0], n1[1]) or can_go(n2[0], n2[1]) and board[x1 + i][y1] == 0 and board[x2 + i][y2] == 0:
                next_pos.append(n1)
                next_pos.append(n2)

    return next_pos


def bfs(left, right, cost):
    q = deque()
    q.append((left, right, cost))
    visited.append((left, right))

    while q:
        left, right, cost = q.popleft()
        if left == (N, N) or right == (N, N):  # 한칸이라도 도착지점에 도착하면 끝
            return cost
        for next_pos in get_next_position(left, right):
            if next_pos not in visited:
                q.append((next_pos[0], next_pos[1], cost + 1))
                visited.append(next_pos)

        # for k in range(4):
        #     nleft = (left[0] + dx[k], left[1] + dy[k])
        #     nright = (right[0] + dx[k], right[1] + dy[k])
        #     if can_go(nleft,nright) and visited[left[0]][left[1]] == 0 and visited[right[0]][right[1]] == 0:
        #         q.append(nleft,nright)
        #         visited[nleft[0]][nleft[1]] = 1
        #         visited[nright[0]][nright[1]] = 1
        #     else:
        #         nleft,nright = spin(nleft,nright)


print(bfs((0, 0), (0, 1), 0))
