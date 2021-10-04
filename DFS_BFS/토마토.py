from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for i in range(n)]

q = deque()
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            q.append((i, j))


def bfs():
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
                board[nx][ny] = board[a][b] + 1
                q.append((nx, ny))

bfs()
isTrue = False
result = -2

for i in board:
    for j in i:
        if j==0:
            isTrue = True
        result = max(result,j)
if isTrue == True:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result-1)