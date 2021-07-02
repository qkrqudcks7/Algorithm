import heapq

n, m = map(int, input().split())

start = 1

graph = [[] for i in range(n + 1)]
distance = [1e9] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append((1, b))
    graph[b].append((1, a))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 1

    while q:
        cost, node = heapq.heappop(q)

        if cost > distance[node]:
            continue

        for c, nd in graph[node]:
            if cost + c < distance[nd]:
                graph[nd] = cost + c
                heapq.heappush(q, [cost + c, nd])


dijkstra(start)

max_node = 0
max_distance = 0
result = []

for i in range(1, n + 1):
    if max_distance < distance[i]:
        max_node = i
        max_distance = distance[i]
        result = [max_node]
    elif max_distance == distance[i]:
        result.append(i)

print(max_node, max_distance, len(result))
