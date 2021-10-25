# 투 포인터 문제입니다. 암기하세요!

n, m = map(int, input().split())
board = list(map(int, input().split()))

count = 0
start = 0
end = 1
temp = board[start]

while start < n:
    if temp == m:
        count += 1
        temp -= board[start]
        start += 1

    if end == n and temp < m:
        break

    elif temp < m:
        temp += board[end]
        end += 1

    elif temp > m:
        temp -= board[start]
        start += 1

print(count)
