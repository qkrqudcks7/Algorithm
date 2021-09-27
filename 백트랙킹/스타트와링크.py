from itertools import combinations

n = int(input())
board = [list(map(int, input().split())) for i in range(n)]

candidate = list(range(0, n))

result = 1e9
for comb in combinations(candidate, n // 2):
    start = set(comb)
    link = set(candidate) - start

    start = list(start)
    link = list(link)
    print(start)
    print(link)
    score = 0

    for i in range(1, n//2):
        for j in range(i):
            score += board[start[i]][start[j]] + board[start[j]][start[i]]
            score -= board[link[i]][link[j]] + board[link[j]][link[i]]
    result = min(abs(score), result)
print(result)
