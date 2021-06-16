import heapq

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for test in range(int(input())):
    n = int(input())
    graph = []

    for i in range(n):
        graph.append(list(map(int, input().split())))
    distance = [[1e9] * n for i in range(n)]

    x, y = 0, 0
    #  시작 노드로 가기 위한 비용은 (0,0) 위치의 값으로 설정하여, 큐에 삽입
    q = [(graph[x][y], x, y)]
    distance[x][y] = graph[x][y]

    while q:
        dist, x, y = heapq.heappop(q)
        if distance[x][y] == dist:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                cost = dist + graph[nx][ny]
                # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))
    print(distance[n-1][n-1])
