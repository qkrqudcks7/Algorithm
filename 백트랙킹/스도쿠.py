import sys

board = [list(map(int, input().split())) for i in range(9)]
# 0인 좌표
zeros = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]


def get_possible(r, c):
    possibles = set(range(1, 10))
    possibles -= set(board[r])
    test = set()
    for i in range(9):
        test.add(board[i][c])
    possibles -= test

    test = set()
    for i in range(r // 3 * 3, r // 3 * 3 + 3):
        for j in range(c // 3 * 3, c // 3 * 3 + 3):
            test.add(board[i][j])
    possibles -= test
    return tuple(possibles)


def solve(i):
    if i == len(zeros):
        [print(*row) for row in board]
        sys.exit()
    r, c = zeros[i]
    possible = get_possible(r, c)

    for num in possible:
        board[r][c] = num
        solve(i + 1)
        board[r][c] = 0


solve(0)
