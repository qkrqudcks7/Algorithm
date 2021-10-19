n, m = map(int, input().split())

graph = [[] for _ in range(n)]
visited = [False] * n


def dfs(count, x):
    if count == 4:
        print(1)
        exit()

    for i in graph[x]:
        if not visited[i]:
            visited[i] = True
            dfs(count + 1, i)
            visited[i] = False


for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n):
    visited[i] = True
    dfs(0, i)
    visited[i] = False

print(0)
