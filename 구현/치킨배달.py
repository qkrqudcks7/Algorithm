from itertools import combinations

n, m = map(int, input().split())
board = [list(map(int, input().split())) for i in range(n)]

house = []
chicken = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            house.append((i, j))
        elif board[i][j] == 2:
            chicken.append((i, j))

candidates = list(combinations(chicken, m))
print(candidates)

def get_sum(i):
    result = 0
    for hx, hy in house:
        temp = 1e9
        for cx, cy in i:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))

        result += temp
    return result


result = 1e9
for i in candidates:
    print(i)
    result = min(result, get_sum(i))

print(result)
