from itertools import combinations

n = int(input())

board = [list(map(int, input().split())) for i in range(n)]

temp = list(range(0, n))
result = 1e9

for i in combinations(temp, n // 2):
    start = set(i)
    link = set(temp) - start

    start = list(start)
    link = list(link)
    score = 0

    for a in range(1, n // 2):
        for b in range(a):
            score += board[start[a]][start[b]] + board[start[b]][start[a]]
            score -= board[link[a]][link[b]] + board[link[b]][link[a]]
    result = min(abs(score), result)

print(result)
