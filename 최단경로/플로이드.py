n = int(input())
m = int(input())

graph = [[1e9] * (n + 1) for i in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for i in range(m):
    a, b, c = map(int, input().split())
    if c<graph[a][b]:
        graph[a][b] = c

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == 1e9:
            print("0", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()
