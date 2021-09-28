# 배낭문제
n, k = map(int, input().split())

stuff = [[0,0]]
for i in range(n):
    w, v = map(int, input().split())
    stuff.append([w, v])

bag = [[0 for i in range(k + 1)] for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        w = stuff[i][0]
        v = stuff[i][1]

        if j < w:
            # weight보다 작으면 위의 값을 그대로 가져온다
            bag[i][j] = bag[i - 1][j]
        else:
            #  max(현재 물건 가치 + knapsack[이전 물건][현재 가방 무게 - 현재 물건 무게], knapsack[이전 물건][현재 가방 무게])
            bag[i][j] = max(v + bag[i - 1][j - w], bag[i - 1][j])

print(bag[n][k])
