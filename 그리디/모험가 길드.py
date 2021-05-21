n = int(input())

a = list(map(int, input().split()))
result = 0
count = 0
a.sort()

for i in a:
    count += 1
    if count >= a[i]:
        result += 1
        count = 0

print(result)
