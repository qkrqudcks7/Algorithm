from itertools import permutations

N, M = map(int, input().split())
L = list(map(int, input().split()))

L.sort()
# visited = [False] * N
# out = []
#
# def solve(depth, N, M):
#     if depth == M:
#         print(' '.join(map(str, out)))
#         return
#     for i in range(N):
#         if not visited[i]:
#             visited[i] = True
#             out.append(L[i])
#             solve(depth+1, N, M)
#             out.pop()
#             visited[i] = False
#
# solve(0, N, M)
for i in permutations(L, M):
    for j in i:
        print(j, end=" ")
    print()
