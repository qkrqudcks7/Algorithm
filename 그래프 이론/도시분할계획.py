def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [0] * (v + 1)

# 모든 간선을 담을 리스트
edges = []
# 최종 비용을 담을 변수
result = 0

for i in range(1, v + 1):
    parent[i] = i

for i in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()
# 최소 산장 트리에 포함되는 간성 중 가장 비용이 큰 간선
# 크루스칼로 모두 이어져 있으니 이걸 빼면 두개로 나뉘어짐
last = 0

for i in edges:
    cost, a, b = i
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        # 비용순으로 했으니 for문 맨 마지막이 cost
        last = cost
print(result - last)