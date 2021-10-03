from collections import deque

n, m, v = map(int, input().split())

graph = [[0] * (n + 1) for i in range(n + 1)]

for i in range(m):
    m1, m2 = map(int, input().split())

    graph[m1][m2] = graph[m2][m1] = 1
visit = [0] * (n + 1)


def dfs(v):
    visit[v] = 1
    print(v, end=" ")
    for i in range(1, n + 1):
        if visit[i] == 0 and graph[v][i] == 1:
            dfs(i)


def bfs(v):
    q = [v]
    visit[v] = 0

    while q:
        x = q.pop(0)
        print(x, end=" ")
        for i in range(1, n + 1):
            if visit[i] == 1 and graph[x][i] == 1:
                q.append(i)
                visit[i] = 0


dfs(v)
print()
bfs(v)
