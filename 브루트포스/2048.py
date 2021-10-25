import copy
from copy import deepcopy

def move(dir):
    if dir == 0:
        for j in range(n):
            idx = 0
            for i in range(1,n):
                if a


def dfs(count):
    global board,ans
    if count == 5:
        for i in range(n):
            for j in range(n):
                ans = max(ans,board[i][j])
        return

    temp = deepcopy(board)
    for i in range(4):
        move(i)
        dfs(count+1)
        board = deepcopy(temp)

n = int(input())
board = [list(map(int, input().split())) for i in range(n)]
ans = 0
dfs(0)
print(ans)