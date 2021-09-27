from itertools import combinations

n,m = map(int,input().split())

a = list(map(int,input().split()))
temp = []
for i in combinations(a,3):
    if sum(i) <= m:
        temp.append(sum(i))

print(max(temp))