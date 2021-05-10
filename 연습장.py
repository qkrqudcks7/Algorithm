m, n, k = map(int, input().split())

ground = [[0] * m for i in range(n)]

for i in range(k):
    a, b = map(int, input().split())
    ground[b][a] = 1


def dfs(x, y):
    if (0 <= x < n) and (0 <= y < m):
        if ground[x][y] == 1:
            ground[x][y] == -1

            dfs(x - 1, y)
            dfs(x, y - 1)
            dfs(x + 1, y)
            dfs(x, y + 1)

            return True
    return False


cnt = 0
for i in range(n):
    for j in range(m):
        if ground[i][j]:
            cnt += 1
print(cnt)
