from itertools import combinations

a, b = map(int, input().split())

arr = list(map(str, input().split()))
arr.sort()
answer = []
for i in combinations(arr, a):
    answer.append(i)

for i in answer:
    mC = 0
    jC = 0
    for j in i:
        if j in ['a', 'e', 'i', 'o', 'u']:
            mC += 1
        else:
            jC += 1
    if mC < 1 or jC < 2:
        pass
    else:
        print("".join(i))
    mC = 0
    jC = 0
