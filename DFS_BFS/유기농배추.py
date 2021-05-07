def dfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if ground[nx][ny] == 1:
                ground[nx][ny] = -1
                dfs(nx, ny)


m, n, k = map(int, input().split())

ground = [[0] * m for i in range(n)]
result = 0
for i in range(k):
    a, b = map(int, input().split())
    ground[b][a] = 1
for j in range(n):
    for k in range(m):
        if ground[j][k] > 0:
            dfs(j, k)
            result += 1

print(result)
