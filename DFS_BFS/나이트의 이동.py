from collections import deque

dx = [1, 1, 2, 2, -1, -1, -2, -2]
dy = [2, -2, 1, -1, 2, -2, 1, -1]


def bfs(x, y, x_end, y_end):
    q = deque()
    q.append((x, y))
    board[x][y] = 0
    while q:
        x, y = q.popleft()
        if x == x_end and y == y_end:
            return board[x][y]

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < l and board[nx][ny] == 0:
                q.append((nx, ny))
                board[nx][ny] = board[x][y] + 1


for _ in range(int(input())):
    l = int(input())
    board = [[0] * l for i in range(l)]
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())

    print(bfs(x1,y1,x2,y2))
