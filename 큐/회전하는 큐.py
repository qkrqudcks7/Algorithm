from collections import deque

n, m = map(int, input().split())
s = list(map(int, input().split()))

d = deque([i + 1 for i in range(n)])
count = 0
for i in s:
    while True:
        if d.index(i) == 0:
            d.popleft()
            break
        if d.index(i) <= len(d) - d.index(i):
            d.append(d.popleft())
            count += 1
        else:
            d.appendleft(d.pop())
            count += 1
print(count)
