from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(board, x, y):
    q = deque()
    board[x][y] = 0
    q.append((x, y))

    while q:
        i, j = q.popleft()
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 1:
                    board[nx][ny] = 0
                    q.append((nx, ny))


for i in range(int(input())):
    n, m, k = map(int, input().split())
    board = [[0] * m for _ in range(n)]

    for _ in range(k):
        a, b = map(int, input().split())
        board[a][b] = 1

    count = 0
    for x in range(n):
        for y in range(m):
            if board[x][y] == 1:
                bfs(board, x, y)
                count += 1
    print(count)
