n = int(input())
x, y = 1, 1
plan = input().split()
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
types = ['L', 'R', 'U', 'D']

for i in plan:
    for j in range(len(types)):
        if i == types[j]:
            nx = x + dx[j]
            ny = y + dy[j]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x, y = nx, ny
print(x, y)
