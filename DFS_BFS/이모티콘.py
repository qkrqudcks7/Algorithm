from collections import deque

n = int(input())
# board[화면 이모티콘 수][클립보드 이모티콘 수]
board = [[-1] * (n + 1) for i in range(n + 1)]

q = deque()
q.append((1, 0))
board[1][0] = 0

while q:
    s, c = q.popleft()
    # 클립보드 복사
    if board[s][s] == -1:  # 방문 안 했으면
        board[s][s] = board[s][c] + 1
        q.append((s, s))

    # 클립보드에 있는 모든 이모티콘 화면에 복붙
    if s + c <= n and board[s + c][c] == -1:
        board[s + c][c] = board[s][c] + 1
        q.append((s + c, c))

    if s - 1 >= 0 and board[s - 1][c] == -1:
        board[s - 1][c] = board[s][c] + 1
        q.append((s - 1, c))

answer = 1e9
for i in range(n + 1):
    if board[n][i] != -1:
        if answer > board[n][i]:
            answer = board[n][i]
print(answer)
