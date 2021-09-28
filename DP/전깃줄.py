# 가장 긴 증가하는 수열이라고 보면 됨
n = int(input())
line = []
for i in range(n):
    a, b = map(int, input().split())
    line.append((a, b))

line.sort()
a_to_b = list(map(lambda x: x[1], line))
print(a_to_b)
max_length = [1] * n

for i in range(1, n):
    for j in range(i):
        if a_to_b[i] > a_to_b[j]:
            max_length[i] = max(max_length[i], max_length[j] + 1)

print(n - max(max_length))
