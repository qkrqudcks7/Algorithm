from collections import deque

n, k = map(int, input().split())
MAX = 10 ** 5
board = [0] * (MAX + 1)


def bfs():
    q = deque()
    q.append(n)

    while q:
        x = q.popleft()
        if x == k:
            print(board[x])
            break
        for i in (x - 1, x + 1, 2 * x):
            if 0 <= i <= MAX and not board[i]:
                board[i] = board[x] + 1
                q.append(i)


bfs()
