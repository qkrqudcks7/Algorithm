n = int(input())
a = list(map(int, input().split()))

add, sub, mul, div = map(int, input().split())

minV = 1e9
maxV = -1e9


def dfs(i, now):
    global minV, maxV, add, sub, mul, div

    if i == n:
        minV = min(minV, now)
        maxV = max(maxV, now)

    else:
        if add > 0:
            add -= 1
            dfs(i + 1, now + a[i])
            add += 1
        elif sub > 0:
            sub -= 1
            dfs(i + 1, now - a[i])
            sub += 1
        elif mul > 0:
            mul -= 1
            dfs(i + 1, now * a[i])
            mul += 1
        elif div > 0:
            div -= 1
            dfs(i + 1, int(now / a[i]))
            div += 1


dfs(1, a[0])

print(maxV)
print(minV)
