n = int(input())
board = [list(map(int, input().split())) for i in range(n)]
list = []


def check(x, y, n):
    number = board[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if number != board[i][j]:
                check(x, y, n // 3)
                check(x, y + n // 3, n // 3)
                check(x, y + (2 * n // 3), n // 3)
                check(x + n // 3, y, n // 3)
                check(x + (2 * n // 3), y, n // 3)
                check(x + n // 3, y + n // 3, n // 3)
                check(x + n // 3, y + (2 * n // 3), n // 3)
                check(x + (2 * n // 3), y + n // 3, n // 3)
                check(x + (2 * n // 3), y + (2 * n // 3), n // 3)
                return
    if number == 0:
        list.append(0)
    elif number == 1:
        list.append(1)
    elif number == -1:
        list.append(-1)


check(0, 0, n)
print(list.count(-1))
print(list.count(0))
print(list.count(1))
