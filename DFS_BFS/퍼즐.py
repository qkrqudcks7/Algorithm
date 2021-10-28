from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

board = [list(map(int, input().split())) for i in range(3)]

def bfs():
    q = deque()
    q.append(board)