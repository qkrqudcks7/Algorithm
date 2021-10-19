from collections import deque

n = int(input())
board = [list(map(int, input())) for i in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(board, i, j):
    q = deque()
    q.append((i, j))
    board[i][j] = 0
    c = 1

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == 1:
                    board[nx][ny] = 0
                    q.append((nx, ny))
                    c += 1
    return c


count = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            count.append(bfs(board, i, j))

count.sort()
print(count)
print(len(count))
for i in range(len(count)):
    print(count[i])
