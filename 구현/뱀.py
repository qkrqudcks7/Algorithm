n = int(input())
k = int(input())

# 맵정보
data = [[0] * (n + 1) for i in range(n + 1)]
# 방향 회전 정보
info = []

for i in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

l = int(input())
for i in range(l):
    x, c = input().split()
    info.append((int(x), c))

# 처음에 오른쪽을 보고 있으므로(동,남,서,북) 오른쪽으로 회전
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction


def simulate():
    x, y = 1, 1  # 뱀의 머리
    data[x][y] = 2  # 뱀이 존재하는 위치는 2로 표시
    direction = 0  # 처음에 동쪽을 보고 있음
    time = 0  # 시작한 뒤에 지난 '초' 시간
    index = 0  # 다음에 회전할 정보
    q = [(x, y)]  # 뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽)

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면
        if 1 <= nx <= n and 1 <= ny <= n and data[nx][ny] != 2:
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                data[px][py] = 0
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx, ny))
        #  벽이나 뱀의 몸통과 부딪혔다면
        else:
            time += 1
            break
        x, y = nx, ny
        time += 1
        if index < l and time == info[index][0]:
            direction = turn(direction, info[index][1])
            index += 1
    return time


print(simulate())
