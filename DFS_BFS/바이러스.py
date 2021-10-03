def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
m = int(input())

parent = [i for i in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    union(parent, a, b)

answer = 0

for i in range(1, n + 1):
    if find_parent(parent, i) == 1:
        answer += 1

print(answer - 1)
