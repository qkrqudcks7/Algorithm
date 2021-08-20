n, m = map(int,input().split())
parent = [0] * (n+1)

for i in range(n):
    data = list(map(int,input().split()))
    for j in range(n):
        if data[j] == 1:
