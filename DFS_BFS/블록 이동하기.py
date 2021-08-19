from collections import deque


def get_next_pos(pos, board):
    next_pos = []
    pos = list(pos)
    px1, py1, px2, py2 = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        px1, py1, px2, py2 = px1 + dx[i], py1 + dy[i], px2 + dx[i], py2 + dy[i]

        if board[px1][py1] == 0 and board[px2][py2] == 0:
            next_pos.append({(px1, py1), (px2, py2)})
    # 로봇이 가로로 놓여져 있으면
    if px1 == px2:
        # 위쪽, 아래쪽으로 회전 가능
        for i in [-1, 1]:
            if board[px1 + i][py1] == 0 and board[px2 + i][py2] == 0:
                next_pos.append({(px1, py1), (px1 + i, py1)})
                next_pos.append({(px2, py2), (px2 + i, py2)})
    # 로봇이 세로로 놓여져 있으면
    elif py1 == py2:
        for i in [-1, 1]:
            if board[px1][py1 + i] == 0 and board[px2][py2 + i] == 0:
                next_pos.append({(px1, py1), (px1, py1 + i)})
                next_pos.append({(px2, py2), (px2, py2 + i)})
    return next_pos


def solution(board):
    n = len(board)
    new_board = [[1] * (n + 2) for i in range(n + 2)]

    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]
    q = deque()
    visited = []
    pos = {(1, 1), (1, 2)}
    q.append((pos, 0))
    visited.append(pos)

    while q:
        pos, cost = q.popleft()
        if (n, n) in pos:
            return cost

        # 현재 위치에서 움직일수 있는지 확인
        for i in get_next_pos(pos, new_board):
            if i not in visited:
                q.append((i, cost + 1))
                visited.append(i)
    return 0
