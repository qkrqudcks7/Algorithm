import heapq

n, m = map(int, input().split())
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]
# 최단거리 테이블을 모두 무한으로 초기화
distance = [1e9] * (n + 1)

for i in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미.
    graph[a].append((c, b))


def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0 으로 설정하며 , 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        value, destination = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[destination] < value:
            continue
        # v=비용 d=노드, 현재 노드와 연결된 다른 인접한 노드들을 확인
        for v, d in graph[destination]:
            cost = value + v
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[d]:
                distance[d] = cost
                heapq.heappush(q, (cost, d))

dijkstra(start)

for i in range(1,n+1):
    if distance[i] == 1e9:
        print("무한")
    else:
        print(distance[i])
