from collections import defaultdict

t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a_sum = defaultdict(int)

answer = 0

for i in range(n):
    for j in range(i, n):
        a_sum[sum(a[i:j + 1])] += 1

for i in range(m):
    for j in range(i,m):
        answer += a_sum[t-sum(b[i:j+1])]

print(answer)