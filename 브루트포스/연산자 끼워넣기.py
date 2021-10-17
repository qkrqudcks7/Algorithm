n = int(input())
arr = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

minV = 1e9
maxV = -1e9


def dfs(i, now):
    global minV, maxV, plus, minus, mul, div

    if i == n:
        minV = min(minV, now)
        maxV = max(maxV, now)
    else:
        if plus > 0:
            plus -= 1
            dfs(i + 1, now + arr[i])
            plus += 1

        if minus > 0:
            minus -= 1
            dfs(i + 1, now - arr[i])
            minus += 1

        if mul > 0:
            mul -= 1
            dfs(i + 1, now * arr[i])
            mul += 1

        if div > 0:
            div -= 1
            dfs(i + 1, int(now / arr[i]))
            div += 1


dfs(1, arr[0])
print(maxV)
print(minV)
