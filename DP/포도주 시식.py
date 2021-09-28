n = int(input())

s = [0] * 10000
for i in range(n):
    s[i] = int(input())

dp = [0] * 10000
dp[0] = s[0]
dp[1] = s[0] + s[1]
# 현재 포도주 + 이전 포도주, 전전 포도주는 x
# 현재 포도주 + 전전 포도주 , 이전 포도주 x
# 현재 포도주 x
dp[2] = max(s[2] + s[0], s[2] + s[1], dp[1])

for i in range(3, n):
    dp[i] = max(s[i] + dp[i - 2], s[i] + s[i - 1] + dp[i - 3], dp[i - 1])
print(max(dp))
