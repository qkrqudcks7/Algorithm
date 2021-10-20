from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]
check = [[[0] * 2 for _ in range(m)] for _ in range(n)]


def dfs():
    q = deque()
    q.append((0, 0, 0))
    check[0][0][0] = 1

    while q:
        x, y, wall = q.popleft()

        if x == n - 1 and y == m - 1:
            return check[x][y][wall]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and check[nx][ny][wall] == 0:
                if board[nx][ny] == 0:
                    q.append((nx, ny, wall))
                    check[nx][ny][wall] = check[x][y][wall] + 1

                if board[nx][ny] == 1 and wall == 0:
                    q.append((nx, ny, 1))
                    check[nx][ny][1] = check[x][y][wall] + 1
    return -1


print(dfs())
