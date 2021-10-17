from itertools import combinations

l, c = map(int, input().split())

arr = list(map(str, input().split()))
arr.sort()
answer = []
for i in combinations(arr, l):
    answer.append(i)


for i in answer:
    mC = 0
    cC = 0
    for j in i:
        if j in ['a', 'e', 'i', 'o', 'u']:
            mC += 1
        else:
            cC += 1
    if mC < 1 or cC < 2:
        pass
    else:
        print("".join(i))
    mC = 0
    cC = 0
