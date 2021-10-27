from collections import deque

n, k = map(int, input().split())
MAX = 100001
visited = [0] * MAX
path = [0] * MAX


def bfs():
    q = deque()
    q.append(n)

    while q:
        v = q.popleft()
        if v == k:
            print(visited[v])
            ans = []
            while v != n:
                ans.append(v)
                v = path[v]
            ans.append(n)
            ans.reverse()
            print(' '.join(map(str, ans)))
            return

        for i in (v - 1, v + 1, v * 2):
            if 0 <= i < MAX and not visited[i]:
                visited[i] = visited[v] + 1
                q.append(i)
                path[i] = v
bfs()
