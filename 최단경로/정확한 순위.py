n, m = map(int, input().split())

graph = [[1e9] * (n + 1) for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

for i in range(m):
    a, b = map(int, input().split())
    # 비용은 다 1로
    graph[a][b] = 1

for i in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])

result = 0
# 각 학생을 번호에 따라 한 명씩 확인하며 도달 가능한지 확인
for i in range(1, n + 1):
    count = 0
    for j in range(1, n + 1):
        if graph[i][j] != 1e9 or graph[j][i] != 1e9:
            count += 1
    if count == n:
        result += 1
print(result)
