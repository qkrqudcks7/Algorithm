# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
# 한 열에 하나의 퀸
# 한 행에 하나의 퀸
# 한 대각선에 하나의 퀸만 존재해야 된다.
# i번째 행에 j라는 요소를 넣어 1차원 배열로 표현

n = int(input())
count = 0
board = [-1 for i in range(n)]

# i행에 j번째에 퀸을 배치할 수 있는가
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
