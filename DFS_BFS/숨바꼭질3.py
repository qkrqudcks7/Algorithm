from collections import deque

n, k = map(int, input().split())
MAX = 100001
board = [0] * MAX


def bfs():
    q = deque()
    q.append(n)

    while q:
        x = q.popleft()
        if x == k:
            return board[x]

        for i in (x - 1, x + 1, 2 * x):
            if 0 <= i < MAX and not board[i]:
                if i == 2 * x and x != 0:
                    board[i] = board[x]
                    q.append(i)
                else:
                    board[i] = board[x] + 1
                    q.append(i)


print(bfs())
