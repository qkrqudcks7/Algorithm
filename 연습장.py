n, m = map(int, input().split())
a = list(map(int, input().split()))

dp=[10001]*(m+1)

dp[0]=0
for i in range(n):
    for j in range(a[i],m+1):
        dp[j]=min(dp[j],dp[j-a[i]+1])


