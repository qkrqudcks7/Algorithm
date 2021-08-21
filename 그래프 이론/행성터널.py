def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
result = 0
parent = [i for i in range(n + 1)]

x = []
y = []
z = []

for i in range(n):
    data = map(int, input().split())
    x.append((data[0],i))
    y.append((data[1],i))
    z.append((data[2],i))
