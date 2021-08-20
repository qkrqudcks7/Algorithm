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
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        # v=비용 d=노드, 현재 노드와 연결된 다른 인접한 노드들을 확인
        for v, d in graph[now]:
            cost = dist + v
            if cost < distance[d]:
                distance[d] = cost
                heapq.heappush(q, (cost, d))


dijkstra(start)

# 최단 거리가 가장 먼 노드 번호
max_node = 0
# 도달할 수 있는 노드 중에서 최단 거리가 가장 먼 노드와의 최단거리
max_distance = 0
# 최단 거리가 가장 먼 노드와의 최단거리와 동일한 최단 거리를 가지는 노드들의 리스트
result = []

for i in range(1, n + 1):
    if max_distance < distance[i]:
        max_node = i
        max_distance = distance[i]
        result = [max_node]

    elif max_distance == distance[i]:
        result.append(i)

print(max_node, max_distance, len(result))
