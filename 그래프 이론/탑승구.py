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


G = int(input())
P = int(input())

parent = [i for i in range(G + 1)]

result = 0
for i in range(P):
    # 현재 비행기의 탑승구의 루트 확인
    data = find_parent(parent, int(input()))
    # 현재 루트가 0이면, 종료
    if data == 0:
        break
    # 그렇지 않다면 바로 왼쪽의 집합과 합치기
    union_parent(parent, data, data - 1)
    result += 1

print(result)
