dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4
for a in range(4,11):
    dp[a] = dp[a - 1] + dp[a - 2] + dp[a - 3]
for _ in range(int(input())):
    a = int(input())
    print(dp[a])
