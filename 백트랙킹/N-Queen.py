n = int(input())
count = 0
board = [-1 for i in range(n)]


def is_possible(i, j):
    for x in range(i):
        if j == board[x] or (abs(i - x) == abs(j - board[x])):
            return False
    return True


def backtracking(row):
    global count
    if row == n:
        count += 1
    else:
        for col in range(n):
            if is_possible(row, col):
                board[row] = col
                backtracking(row + 1)
                board[row] = -1


backtracking(0)
print(count)
