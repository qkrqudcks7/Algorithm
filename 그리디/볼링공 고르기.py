n, m = map(int, input().split())
a = list(map(int, input().split()))
count = 0
ball = [0] * 11
for i in a:
    ball[i] += 1

for i in range(1, m + 1):
    n -= ball[i]
    count += ball[i] * n
print(count)
