from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m = map(int, input().split())
board = [list(map(int, input())) for i in range(n)]


def bfs(board, x, y):
    q = deque()
    q.append((x, y))

    while q:
        a, b = q.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 1:
                    board[nx][ny] = board[a][b] + 1
                    q.append((nx, ny))


bfs(board, 0, 0)

print(board[-1][-1])
