from itertools import combinations

n, s = map(int, input().split())
arr = list(map(int, input().split()))
count = 0

for i in range(1, n + 1):
    temp = combinations(arr, i)
    for j in temp:
        if sum(j) == s:
            count += 1

print(count)
