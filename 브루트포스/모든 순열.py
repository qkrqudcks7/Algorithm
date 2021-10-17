from itertools import permutations
n = int(input())
a = list(range(1,n+1))
for i in permutations(a,n):
    for j in i:
        print(j,end=" ")
    print()