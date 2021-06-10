n = int(input())
t = []
p = []
dp = [0] * (n + 1)
maxV = 0

for i in range(n):
    x, y = map(int, input().split())

    t.append(x)
    p.append(y)

for i in range(n - 1, -1, -1):
    time = t[i] + i

    if time <= n:
        dp[i] = max(p[i] + dp[time], maxV)
        maxV = dp[i]
    else:
        dp[i] = maxV
print(maxV)
