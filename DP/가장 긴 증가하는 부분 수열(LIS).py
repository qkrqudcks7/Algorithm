n = int(input())

s = list(map(int, input().split()))

dp = [1] * n
for i in range(n):
    for j in range(i):
        # 길이를 찾으려는 숫자가 비교할 숫자보다 크면, 그 숫자가 가지고 있는 길이+1과 자신이 길이를 비교해서 큰 값으로 최신화 한다.
        if s[i] > s[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
