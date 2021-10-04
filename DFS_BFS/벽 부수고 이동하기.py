from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input())) for i in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():
    # (0,0) 출발, 벽 안 부숨
    q = deque([(0, 0, 0)])
    visited[0][0][0] = 1

    while q:
        a, b, wall = q.popleft()
        if a == n - 1 and b == m - 1:
            return visited[a][b][wall]

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            # 범위 안이고, 한번도 방문 안했으면
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny][wall] == 0:
                # 벽이 아니라면 이동하고, 이전경로 + 1 visited 배열에 저장
                if board[nx][ny] == 0:
                    q.append((nx, ny, wall))
                    visited[nx][ny][wall] = visited[a][b][wall] + 1

                # 벽 1번도 안 부쉈고, 다음 이동할 곳이 벽이라면
                if wall == 0 and board[nx][ny] == 1:
                    # 벽을 부순 상태를 1로 표현
                    q.append((nx, ny, 1))
                    visited[nx][ny][1] = visited[a][b][wall] + 1
    return -1


print(bfs())
