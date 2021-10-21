from collections import deque

dx = [1, -1, 0, 0, -1, 1, 1, -1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]

w, h = map(int, input().split())

board = [list(map(int, input().split())) for i in range(h)]
count = 0
q = deque()

for i in range(h):
    for j in range(w):
        if board[i][j] == 1:
            q.append((i, j))
            board[i][j] = 0

            while q:
                x, y = q.popleft()
                for k in range(8):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if 0 <= nx < h and 0 <= ny < w and board[nx][ny] == 1:
                        q.append((nx, ny))
                        board[nx][ny] = 0
            count += 1

print(count)
