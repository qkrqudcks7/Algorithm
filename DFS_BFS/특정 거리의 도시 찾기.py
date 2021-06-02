import heapq

n, m, k, x = map(int, input().split())

arr = [[] for i in range(n + 1)]
visit = [1e9] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    arr[a].append((b, 1))


def dijkstra(start):
    visit[start] = 0
    q = []
    #  시작 노드로 가기 위한 최단 경로는 0으로 설정하며, 큐에 삽입
    heapq.heappush(q, (0, start))

    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if dist > visit[now]:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in arr[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < visit[i[0]]:
                visit[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(x)
flag = False

for i in range(1, n + 1):
    if visit[i] == k:
        flag = True
        print(i)

if not flag:
    print(-1)
