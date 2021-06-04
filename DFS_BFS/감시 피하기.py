from itertools import combinations

# 복도의 크기
n = int(input())
board = []  # 복도의 정보
teachers = []  # 모든 선생님 위치 정보
spaces = []  # 모든 빈 공간 위치 정보

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        if board[i][j] == "T":
            teachers.append((i, j))
        if board[i][j] == 'X':
            spaces.append((i, j))


def watch(x, y, direction):
    # 왼쪽 방향으로 감시
    if direction == 0:
        while y >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y -= 1
    elif direction == 1:
        while y < n:
            if board[x][y] == "S":
                return True
            elif board[x][y] == "O":
                return False
            y += 1
    elif direction == 2:
        while x >= 0:
            if board[x][y] == "S":
                return True
            elif board[x][y] == "O":
                return False
            x -= 1
    elif direction == 3:
        while x < n:
            if board[x][y] == "S":
                return True
            elif board[x][y] == "O":
                return False
            x += 1
    return False


def process():
    for x, y in teachers:
        for i in range(4):
            if watch(x, y, i):
                return True
    return False


find = False

for i in combinations(spaces, 3):
    for x, y in i:
        board[x][y] = "O"

    if not process():
        find = True
        break
    for x, y in i:
        board[x][y] = "X"

if find:
    print('YES')
else:
    print('NO')
