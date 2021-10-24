board = [list(map(int, input().split())) for i in range(9)]
zero = [(i, j) for j in range(9) for i in range(9) if board[i][j] == 0]


def solve(i):
    if i == len(zero):
        [print(*row) for row in board]

    r, c = zero[i]

    # 행
    possible = set(range(1, 10))
    possible -= set(board[r])

    # 열
    test = set()
    for i in range(9):
        test.add(board[i][c])
    possible -= test

    test = set()
    for i in range(r // 3 * 3, r // 3 * 3 + 3):
        for j in range(c // 3 * 3, c // 3 * 3 + 3):
            test.add(board[i][j])
    possible -= test

    for i in tuple(possible):
        board[r][c] = i
        solve(i + 1)
        board[r][c] = 0


solve(0)
