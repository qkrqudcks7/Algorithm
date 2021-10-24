n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(input()))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

count = 1


def bfs(i, j):
    global count
    q = {(0, 0, board[0][0])}

    while q:
        x, y, visited = q.pop()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] not in visited:
                q.add((nx, ny, visited + board[nx][ny]))
                count = max(count, len(visited) + 1)


bfs(0, 0)
print(count)
