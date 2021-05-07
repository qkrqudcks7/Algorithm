n, m, k = map(int, input().split())
a = list(map(int, input().split()))
sum = 0
check = 1
a.sort(reverse=True)
print(a)
for i in range(m):
    if check <= k:
        sum += a[0]
        check += 1
    else:
        sum += a[1]
        check = 0
print(sum)
