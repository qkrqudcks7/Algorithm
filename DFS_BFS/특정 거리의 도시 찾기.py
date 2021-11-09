import heapq

n, m, k, x = map(int, input().split())
graph = [[] for i in range(n + 1)]
visit = [1e9] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append((1, b))


def dijkstra(start):
    visit[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        cost, node = heapq.heappop(q)

        if cost > visit[node]:
            continue

        for c, nd in graph[node]:
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost + c < visit[nd]:
                visit[nd] = cost + c
                heapq.heappush(q, [cost + c, nd])


dijkstra(x)
flag = False

for i in range(1, n + 1):
    if visit[i] == k:
        flag = True
        print(i)
if not flag:
    print(-1)
