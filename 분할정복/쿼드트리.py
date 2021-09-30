n = int(input())
board = [list(map(int, input())) for i in range(n)]
result = []


def qd(x, y, n):
    global result
    color = board[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != board[i][j]:
                result.append("(")
                qd(x, y, n // 2)
                qd(x, y + n // 2, n // 2)
                qd(x + n // 2, y, n // 2)
                qd(x + n // 2, y + n // 2, n // 2)
                result.append(")")
                return
    result.append(color)


qd(0, 0, n)
print("".join(map(str, result)))
