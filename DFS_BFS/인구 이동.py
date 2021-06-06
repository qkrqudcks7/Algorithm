from collections import deque

n, L, R = map(int, input().split())

maps = [list(map(int, input().split())) for i in range(n)]
visit = [[False] * n for i in range(n)]

q = deque()

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

count=0

while True:
    check=False
    for i in range(n):
        for j in range(n):
            if visit[i][j]==False:
                q.append((i,j))
                visit[i][j]=True
                
